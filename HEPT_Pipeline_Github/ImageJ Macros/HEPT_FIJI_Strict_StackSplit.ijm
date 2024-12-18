// For the macro to run without the bioformats dialogue box popping up with each image go to: 
// Plugins > Bio-formats > Bio-formats plugins configuration > Formats > Select OME-TIFF and check the "Windowless" box.
input_path = [Insert your input path here. Eg."C:/..."]
output_path = [Insert your output path here.]
dir1 = getDirectory(input_path);
dir2 = getDirectory(output_path);
list = getFileList(dir1);
setBatchMode(true);
for (i=0; i<list.length; i++) {
showProgress(i+1, list.length);
open(dir1+list[i]);
title = getTitle();
selectWindow(title);
//Eg. this renames "ID15_Img1.tif.tif.ome.tif" to "ID15_Img1_"
newtitle = replace(title, "\\.tif\\.ome\\.tif", "_");
run("Stack to Images");

//ImmC = Immune Cells
saveAs("Tiff", output_path+"/"+newtitle+"Others.tif");
close();
saveAs("Tiff", output_path+"/"+newtitle+"ImmC.tif");
close();
call("java.lang.System.gc");
}
