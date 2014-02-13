import numpy as np
import os
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!' 
    print 'e.g. python domain2index.py indexoutput.nrrd domainprefix(000#)'
else:
     
    print 'Adding to index', str(sys.argv[1]), '....'
    for x in range(2,(len(sys.argv))):
        for i in range(1,255):
            fn = str(sys.argv[x]) + str(i).zfill(4) + '.nrrd'
            if os.path.exists(fn):
                print 'adding data from file', fn
                readdata, option = nrrd.read(fn)
                readdata[readdata>0] = np.uint8(i) 
                print 'appending index', str(i)
                indfile = str(sys.argv[1])
                if os.path.exists(indfile):
                    domain, option = nrrd.read(indfile)
                else:
                    domain = np.zeros(readdata.shape,np.uint8)
                domain[readdata==np.uint8(i)]=np.uint8(i)
                nrrd.write(indfile, domain, options=option)
    
    
    
    
print 'Done.'