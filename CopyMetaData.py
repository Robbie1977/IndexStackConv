import numpy as np
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!'
    print 'e.g. python CopyMetaData.py template.nrrd DataToBeCorrected.nrrd'
else:

    print 'Checking index for ', str(sys.argv[1]), ' against the index in (', str(sys.argv[2]), ')...'
  
    readdata, op1 = nrrd.read(str(sys.argv[2]))
    
    im1 = readdata
    
    readdata, op2 = nrrd.read(str(sys.argv[1])) 
    im2 = readdata
      
    if (im1.size <> im2.size):
        print '\n\nError: Images must be the same size!!'
    else:
        
        print 'Changing the meta data for %s to match that of %s' %(str(sys.argv[2]),str(sys.argv[1]))
        nrrd.write(str(sys.argv[2]), im1, options=op2)
        
        print 'Done.'
        
  

