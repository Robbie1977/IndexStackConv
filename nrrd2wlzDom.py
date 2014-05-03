import glob, subprocess, sys

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

subprocess.call('%sWlzSetVoxelSize -x%s -y%s -z%s %s >%s_E' % (wlzdir, Vsize, Vsize, Zsize, Tfile, Tfile), shell=True)

#subprocess.call('find %s0*_dom.wlz -size -2b | xargs rm -f'% (Fpre), shell=True) 

subprocess.call('cat %s_E %s0*_dom.wlz | %sWlzCompound >out.wlz'% (Tfile, Fpre, wlzdir), shell=True)

print 'Result saved to out.wlz'
