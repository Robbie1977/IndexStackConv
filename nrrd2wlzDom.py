import glob, subprocess, sys

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is one of "yes" or "no".
    """
    valid = {"yes":False,   "y":False,  "ye":False,
             "no":True,     "n":True}
    if default == None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "\
                             "(or 'y' or 'n').\n")


if (len(sys.argv) < 4):
    print 'e.g. python nrrd2wlzDom.py DomainPrefix templateFile WoolzDir FijiExec Zsize XYsize'
    print 'Error: missing arguments - using defaults:'
    print 'e.g. python nrrd2wlzDom.py TAGdomain flyVNCtemplate20xDaS_th.wlz /disk/data/VFBTools/Woolz2013Full/bin/ /disk/data/VFBTools/Fiji.145/fiji-linux64'
    wlzdir = '/disk/data/VFBTools/Woolz2013Full/bin/'
    Tfile = 'flyVNCtemplate20xDaS_th.wlz'
    Fpre = 'TAGdomain'
    Lfiji = '/disk/data/VFBTools/Fiji.145/fiji-linux64'
    Zsize = str(1)
    Vsize = str(1)
    if query_yes_no('Do you want to run with the defaults?', default='no'): sys.exit(0)
else:
    Lfiji = str(sys.argv[4])
    wlzdir = str(sys.argv[3])
    Tfile = str(sys.argv[2])
    Fpre = str(sys.argv[1])
    Zsize = str(sys.argv[5])
    Vsize = str(sys.argv[6])

for infile in glob.glob(Fpre + "0*.nrrd"):
    print 'Converting %s to %s...' % (infile, infile.replace('.nrrd','.tif'))
    subprocess.call('nice xvfb-run %s -macro nrrd2tif.ijm %s -batch' % (Lfiji, infile), shell=True)

for i in xrange(1,250):
    outfile = Fpre + str(i).zfill(4) + '_dom.wlz'
    print 'Creating blank %s...'% outfile
    subprocess.call('nice %sWlzMakeEmpty -o%s'% (wlzdir, outfile), shell=True)


for infile in glob.glob(Fpre + "0*.tif"):
    outfile = infile.replace('.tif','_dom.wlz')
    print 'Converting %s to %s...' % (infile, outfile)
    subprocess.call('nice %sWlzExtFFConvert -ftif -Fwlz %s | %sWlzThreshold -v1 |%sWlzDomain |%sWlzSetVoxelSize -x%s -y%s -z%s >%s' % (wlzdir, infile, wlzdir, wlzdir, wlzdir, Vsize, Vsize, Zsize, outfile), shell=True)
    comfile = infile.replace('.tif','.txt')
    print 'Calculating centre for %s and saving to %s...' % (outfile, comfile)
    subprocess.call('nice %sWlzCentreOfMass -o %s %s' % (wlzdir, comfile, outfile), shell=True)

    #print '%sWlzExtFFConvert -ftif -Fwlz %s | %sWlzDomain >%s' % (wlzdir, infile, wlzdir, outfile)


print 'Compiling...'

subprocess.call('%sWlzSetVoxelSize -x%s -y%s -z%s %s >%s' % (wlzdir, Vsize, Vsize, Zsize, Tfile, Tfile.replace('.wlz','_E.wlz')), shell=True)

#subprocess.call('find %s0*_dom.wlz -size -2b | xargs rm -f'% (Fpre), shell=True)

subprocess.call('cat %s %s0*_dom.wlz | %sWlzCompound >out.wlz'% (Tfile.replace('.wlz','_E.wlz'), Fpre, wlzdir), shell=True)

print 'Result saved to out.wlz'
