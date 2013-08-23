import numpy as np
import sys
import nrrd

if (len(sys.argv) < 3):
    print 'Error: missing arguments!'
    print 'e.g. python CompareIndex.py newIndex.nrrd oldIndex.nrrd'
else:

    print 'Checking index for ', str(sys.argv[1]), ' against the index in (', str(sys.argv[2]), ')...'
  
    readdata, options = nrrd.read(str(sys.argv[2]))
    
    im1 = readdata
    
    readdata, options = nrrd.read(str(sys.argv[1])) 
    im2 = readdata
      
    if (im1.size <> im2.size):
        print '\n\nError: Images must be the same size!!'
    else:
    
       
        
        r=np.zeros([255,253])
        for j in range(1,255):
            print 'Checking index %s...'% str(j)
            i = np.where(im1 == j)
            d=np.zeros(np.size(i[0],0))
            for c in range(0, np.size(i[0],0)):
                d[c] = im2[i[0][c]][i[1][c]][i[2][c]] 
            r[j]=np.histogram(d, bins=range(0,255))[0][1:]
        
        st1='['  
        st2='['  
        dv = '' 
        for c in range(1,255):
            if (r[c].argmax() > 1):
                print '%s -> %s' % (str(c), str((r[c].argmax())+1))
                st1 = st1 + dv + str(c)
                st2 = st2 + dv + str((r[c].argmax())+1)
                dv= ','
            else:
                print '%s -> %s' % (str(c), str(r[c].argmax()))
                
        st1 = st1 + ']'
        st2 = st2 + ']'
        
        print st1
        print st2

    
        #print 'The alignment has a RMS Diff value of:', r1, ' (0=perfect)'
        #
        #print 'Outputing results to ', str(sys.argv[3])
        #
        #with open(str(sys.argv[3]), "a") as myfile: 
        #    myfile.write(str(r1) + ', RMS Diff, ' + str(sys.argv[1]) + ', ' + str(sys.argv[2]) + '\n')
        
        print 'Done.'
        
  

