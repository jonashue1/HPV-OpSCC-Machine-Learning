#@ DatasetIOService io
#@ CommandService command

""" This example runs stardist on all tif files in a folder
Full list of Parameters: 
res = command.run(StarDist2D, False,
			 "input", imp, "modelChoice", "Versatile (fluorescent nuclei)",
			 "modelFile","/path/to/TF_SavedModel.zip",
			 "normalizeInput",True, "percentileBottom",1, "percentileTop",99.8,
			 "probThresh",0.5, "nmsThresh", 0.3, "outputType","Label Image",
			 "nTiles",1, "excludeB	oundary",2, "verbose",1, "showCsbdeepProgress",1, "showProbAndDist",0).get();			
"""

from de.csbdresden.stardist import StarDist2D 
from glob import glob
import os

# run stardist on all tiff files in <indir> and save the label image to <outdir>
indir   = os.path.expanduser("[Insert your input directory here.]")
outdir  = os.path.expanduser("[Insert your output directory here.]")

for f in sorted(glob(os.path.join(indir,"*.tif"))):
	print "processing ", f
  
	imp = io.open(f)
  
	res = command.run(StarDist2D, False,
			"input", imp,
			"modelChoice", "Versatile (H&E nuclei)",
            "normalizeInput",True,
            "percentileBottom",1,
            "percentileTop",99.8,
            "probThresh",0.479071,
            "nmsThresh", 0.3,
            "outputType","Label Image",
            "nTiles",1,
            "excludeBoundary",2,
            "verbose",False,
			).get()
	label = res.getOutput("label")
  
	io.save(label, os.path.join(outdir, "Stardist_"+os.path.basename(f)))