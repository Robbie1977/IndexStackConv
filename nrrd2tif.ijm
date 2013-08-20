// ImageJ macro lsm2nrrdPP.ijm
// Designed to open and PreProcess 1 channel tif image stacks and output 1 NRRD file
// Written by Robert Court - r.court@ed.ac.uk 


name = getArgument;
if (name=="") exit ("No argument!");
setBatchMode(true);

outfile = replace(name, ".nrrd", ".tif");

run("Nrrd ...", "load=[" + name + "]");
saveAs("Tiff", outfile);


run("Quit");

