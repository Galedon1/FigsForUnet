# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 08:11:03 2024

@author: User

Invertuje barevnou škálu černobílého obrázku (převede na černobílý, pokud je barevný)

"""

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


path_in = "C:/Users/Vilem Nedela/Desktop/AI Segmentace/GIT/FigsForUnet/Input/"

path_out = "C:/Users/Vilem Nedela/Desktop/AI Segmentace/GIT/FigsForUnet/Output/"

# seznam koncovek souborů k přetvoření - soubory s jinou koncovkou budou ignorovány
koncovky = (
    ".tif",
    ".tiff",
    ".png",
    ".jpg"
    )


# seznam souborů pro přetvoření - pokud je list prázdný, tedy jen [], vezmou se všechny soubory
flist = [
    # "Častice 10x  laser place H.tif"    
    ]
# %%

def invertColors(im_arr):
    return im_arr.max() - im_arr
    

# %%


if len(flist) == 0:
    flist = os.listdir(path_in)

plt.ioff()
for file in flist: 
    if not file.endswith(koncovky):
        continue
    im = Image.open(path_in + file)
    im_arr = np.array(im)
    im_arr = invertColors(im_arr)
        
    fig, ax = plt.subplots()
    ax.imshow(im_arr, cmap = "Grays")
    ax.set_axis_off()
    
    fig.tight_layout(pad = 0)
    fig.savefig(path_out + file, 
                bbox_inches='tight',
                pad_inches = 0
                )
plt.ion()

