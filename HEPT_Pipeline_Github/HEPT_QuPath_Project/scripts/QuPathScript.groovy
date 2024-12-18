setImageType('BRIGHTFIELD_H_E');
setColorDeconvolutionStains('{"Name" : "H&E default", "Stain 1" : "Hematoxylin", "Values 1" : "0.65111 0.70119 0.29049 ", "Stain 2" : "Eosin", "Values 2" : "0.2159 0.8012 0.5581 ", "Background" : " 255 255 255 "}');
classifyDetectionsByCentroid("Preprocessing_model")

name = getProjectEntry().getImageName();

writePredictionImage("Preprocessing_model", "[Insert your output folder's path for the 1st model here]/${name}.ome.tif")

setImageType('BRIGHTFIELD_H_E');
setColorDeconvolutionStains('{"Name" : "H&E default", "Stain 1" : "Hematoxylin", "Values 1" : "0.65111 0.70119 0.29049 ", "Stain 2" : "Eosin", "Values 2" : "0.2159 0.8012 0.5581 ", "Background" : " 255 255 255 "}');
classifyDetectionsByCentroid("Strict_model")

name = getProjectEntry().getImageName();

writePredictionImage("Strict_model", "[Insert your output folder's path for the 2nd model here]/${name}.ome.tif")
