import numpy as np
import os
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!' 
    print 'e.g. python mergeIndexFiles.py indexfile.nrrd indexfile1.nrrd indexfileN.nrrd ...'
else:
     
    print 'Adding to index', str(sys.argv[1]), '....'
    for x in range(2,(len(sys.argv))):
        print 'adding data from file', sys.argv[x]
        readdata, options = nrrd.read(str(sys.argv[x]))
        for i in np.unique(readdata[readdata>0]):
            if np.uint8(i) in readdata: 
                print 'appending index', str(i)
                indfile = str(sys.argv[1])
                if os.path.exists(indfile):
                    domain, options = nrrd.read(indfile)
                else:
                    domain = np.zeros(readdata.shape,np.uint8)
                domain[readdata==i]=np.uint8(i)
                nrrd.write(indfile, domain)
    
    
    
    
print 'Done.'