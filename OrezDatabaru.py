# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:55:14 2024

@author: User
"""

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


path_in = "D:/projekty/FigsForUnet/input/"

path_out = "D:/projekty/FigsForUnet/output/"

pixels_to_cut = 80

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

def CutDatabar(fig_arr, pixels = 80):
    return fig_arr[:-pixels, :]





# %%


if len(flist) == 0:
    flist = os.listdir(path_in)

plt.ioff()
for file in flist: 
    if not file.endswith(koncovky):
        continue
    im = Image.open(path_in + file)
    im_arr = np.array(im)
    im_arr = CutDatabar(im_arr, pixels_to_cut)
    
    fig, ax = plt.subplots()
    ax.imshow(im_arr, cmap = "Grays")
    ax.set_axis_off()
    
    fig.tight_layout(pad = 0)
    fig.savefig(path_out + file, 
                bbox_inches='tight',
                pad_inches = 0
                )
    
plt.ion()


