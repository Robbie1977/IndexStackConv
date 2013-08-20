import numpy as np
import os
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!' 
    print 'e.g. python Index2domain.py DomainPrefix indexfile1.nrrd indexfileN.nrrd ...'
else:
     
    print 'Adding to domains', str(sys.argv[1]), '....'
    for x in xrange(2,(len(sys.argv))):
        print 'adding data from file', sys.argv[x]
        readdata, options = nrrd.read(str(sys.argv[x]))
        for i in xrange(1,255):
            if i in readdata: 
                print 'appending index', str(i)
                domfile = str(sys.argv[1]) + str(i).zfill(4) + '.nrrd'
                if os.path.exists(domfile):
                    domain, options = nrrd.read(domfile)
                else:
                    domain = np.zeros(readdata.shape,np.uint8)
                domain[readdata==i]=255
                nrrd.write(domfile, domain)
    
    
    
    
print 'Done.'