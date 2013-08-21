import numpy as np
import sys
import nrrd

if (len(sys.argv) < 4):
    print 'Error: missing arguments!'
    print 'e.g. ConvertLabels.py [1,2,3,4,5] [5,4,3,2,1] imagefile.nrrd'
    print 'e.g. ConvertLabels.py [1,2,3,4,5] [255,254,253,252,251] imagefile.nrrd optionaloutputfile.nrrd'
else:
     
    print 'Changing label', str(sys.argv[1]), 'to', str(sys.argv[2]), 'for file', str(sys.argv[3]) 
    readdata, options = nrrd.read(str(sys.argv[3]))
    
    old_list = sys.argv[1].replace('[','').replace(']','').split(',')
    new_list = sys.argv[2].replace('[','').replace(']','').split(',')
    
    tempdata=readdata
    for i in xrange(0,len(new_list)):
        dc = readdata==int(old_list[i])
        tempdata[dc] = int(new_list[i])
        print old_list[i], '->', new_list[i]
    
    
    if (len(sys.argv) < 5):
        print 'saving result to', str(sys.argv[3]) 
    
        nrrd.write(str(sys.argv[3]), tempdata)
    else:
        print 'saving result to', str(sys.argv[4]) 
    
        nrrd.write(str(sys.argv[4]), tempdata)
    
print 'Done.'
