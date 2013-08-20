import glob, subprocess

wlzdir = '/disk/data/VFBTools/Woolz2013Full/bin/'
Tfile = 'flyVNCtemplate20xDaS_th.wlz'

for i in xrange(1,250):
    outfile = 'TAGdomain' + str(i).zfill(4) + '_dom.wlz'
    print 'Creating blank %s...'% outfile
    subprocess.call('%sWlzMakeEmpty >%s'% (wlzdir, outfile), shell=True)
    

for infile in glob.glob("TAGdomain0*.tif"):
    outfile = infile.replace('.tif','_dom.wlz')
    print 'Converting %s to %s...' % (infile, outfile)
    subprocess.call('%sWlzExtFFConvert -ftif -Fwlz %s | %sWlzThreshold -v1 |%sWlzDomain >%s' % (wlzdir, infile, wlzdir, wlzdir, outfile), shell=True)
    comfile = infile.replace('.tif','.txt')
    print 'Calculating centre for %s and saving to %s...' % (outfile, comfile)
    subprocess.call('%sWlzCentreOfMass -o %s %s' % (wlzdir, comfile, outfile), shell=True)
    
    #print '%sWlzExtFFConvert -ftif -Fwlz %s | %sWlzDomain >%s' % (wlzdir, infile, wlzdir, outfile)


print 'Compiling...'

subprocess.call('cat %s TAGdomain0*_dom.wlz | %sWlzCompound >out.wlz'% (Tfile, wlzdir), shell=True)

print 'Result saved to out.wlz'