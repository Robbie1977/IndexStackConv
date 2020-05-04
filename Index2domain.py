import numpy as np
import os
import sys
import nrrd

if (len(sys.argv) < 3):
    print('Error: missing arguments!')
    print('e.g. python Index2domain.py DomainPrefix indexfile1.nrrd indexfileN.nrrd ...')
else:
     
    print('Adding to domains', str(sys.argv[1]), '....')
    for x in range(2,(len(sys.argv))):
        print('adding data from file', sys.argv[x])
        readdata, option = nrrd.read(str(sys.argv[x]))
        for i in np.unique(readdata[readdata>0]):
            if np.uint8(i) in readdata: 
                print('appending index', str(i))
                domfile = str(sys.argv[1]) + str(i).zfill(4) + '.nrrd'
                if os.path.exists(domfile):
                    domain, option = nrrd.read(domfile)
                else:
                    domain = np.zeros(readdata.shape,np.uint8)
                domain[readdata==i]=np.uint8(255)
                nrrd.write(domfile, domain, header=option)
    
    
    
    
print('Done.')