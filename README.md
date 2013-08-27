IndexStackConv
==============

Convert Index stack into individual domain images then Woolz files

Convert the Index image stack into an NRRD file in ImageJ/Fiji.

Then to correct any index labels run Convertlabels 
ConvertLabels.py [1,2,3,4,5] [5,4,3,2,1] imagefile.nrrd
ConvertLabels.py [1,2,3,4,5] [255,254,253,252,251] imagefile.nrrd optionaloutputfile.nrrd
e.g.
python ConvertLabels.py [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75] [141,78,15,109,23,102,133,11,94,149,66,35,117,39,27,82,82,82,62,74,7,51,70,3,105,113,98,47,86,121,43,90,54,82,129,125,58,31,19,137,145,141,78,109,102,133,94,149,66,35,117,39,27,82,82,82,62,74,51,70,105,113,98,47,86,121,43,90,54,82,129,125,58,31,145] ../JFRCtempate2010.mask130819.nrrd ../JFRCtempate2010.mask130819-CorIndex.nrrd 

Then split apart into individual domians using:

python Index2domain.py DomainPrefix indexfile1.nrrd indexfileN.nrrd ...

e.g.

python Index2domain.py ../domains/BrainTemplate ../JFRCtempate2010.mask130819-CorIndex.nrrd

Then Combine a greyscale with the domains to make a compound woolz object:

python nrrd2wlzDom.py DomainPrefix GreyScale.wlz /path/to/WoolzCommands/ /path/to/fijiexec

e.g.

python nrrd2wlzDom.py ../domains/BrainTemplate ../oldTemplate/oldTemplate000000.wlz /disk/data/VFBTools/Woolz2013Full/bin/ /disk/data/VFBTools/Fiji.145/fiji-linux64

The compound object is saved as out.wlz in current working dir.

VFB only notes:

Get label index changes by running (assuming template image is the same):

python CompareIndex.py JFRCtempate2010.mask130819.nrrd oldIndex.nrrd

Use the Index number change arrays printed in the next stage.

for complete run changing JFRCtemplate2010.mask130819 to the new filename on karenin:

cd /disk/data/VFB/IMAGE_DATA/JFRCtemplate2010/scripts

python ConvertLabels.py [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75] [141,78,15,109,23,102,133,11,94,149,66,35,117,39,27,82,82,82,62,74,7,51,70,3,105,113,98,47,86,121,43,90,54,82,129,125,58,31,19,137,145,141,78,109,102,133,94,149,66,35,117,39,27,82,82,82,62,74,51,70,105,113,98,47,86,121,43,90,54,82,129,125,58,31,145] ../JFRCtempate2010.mask130819.nrrd ../JFRCtempate2010.mask130819-CorIndex.nrrd 

python Index2domain.py ../domains/BrainTemplate ../JFRCtempate2010.mask130819-CorIndex.nrrd

python nrrd2wlzDom.py ../domains/BrainTemplate ../oldTemplate/oldTemplate000000.wlz /disk/data/VFBTools/Woolz2013Full/bin/ /disk/data/VFBTools/Fiji.145/fiji-linux64

