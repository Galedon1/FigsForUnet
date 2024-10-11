# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:52:07 2024

@author: User
"""

import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


path_in = "D:/projekty/FigsForUnet/input/"

path_out = "D:/projekty/FigsForUnet/output/"

koncovky = (
    ".tif",
    ".tiff",
    ".png",
    ".jpg"
    )

# %%

diakritika_map = {'À': 'A',
     'Á': 'A',
     'Â': 'A',
     'Ã': 'A',
     'Ä': 'A',
     'Å': 'A',
     'Ç': 'C',
     'È': 'E',
     'É': 'E',
     'Ê': 'E',
     'Ë': 'E',
     'Ì': 'I',
     'Í': 'I',
     'Î': 'I',
     'Ï': 'I',
     'Ñ': 'N',
     'Ò': 'O',
     'Ó': 'O',
     'Ô': 'O',
     'Õ': 'O',
     'Ö': 'O',
     'Ù': 'U',
     'Ú': 'U',
     'Û': 'U',
     'Ü': 'U',
     'Ý': 'Y',
     'ß': 's',
     'à': 'a',
     'á': 'a',
     'â': 'a',
     'ã': 'a',
     'ä': 'a',
     'å': 'a',
     'ç': 'c',
     'è': 'e',
     'é': 'e',
     'ê': 'e',
     'ë': 'e',
     'ì': 'i',
     'í': 'i',
     'î': 'i',
     'ï': 'i',
     'ñ': 'n',
     'ò': 'o',
     'ó': 'o',
     'ô': 'o',
     'õ': 'o',
     'ö': 'o',
     'ù': 'u',
     'ú': 'u',
     'û': 'u',
     'ü': 'u',
     'ý': 'y',
     'ÿ': 'y',
     'Ā': 'A',
     'ā': 'a',
     'Ă': 'A',
     'ă': 'a',
     'Ą': 'A',
     'ą': 'a',
     'Ć': 'C',
     'ć': 'c',
     'Ĉ': 'C',
     'ĉ': 'c',
     'Ċ': 'C',
     'ċ': 'c',
     'Č': 'C',
     'č': 'c',
     'Ď': 'D',
     'ď': 'd',
     'Đ': 'D',
     'đ': 'd',
     'Ē': 'E',
     'ē': 'e',
     'Ĕ': 'E',
     'ĕ': 'e',
     'Ė': 'E',
     'ė': 'e',
     'Ę': 'E',
     'ę': 'e',
     'Ě': 'E',
     'ě': 'e',
     'Ĝ': 'G',
     'ĝ': 'g',
     'Ğ': 'G',
     'ğ': 'g',
     'Ġ': 'G',
     'ġ': 'g',
     'Ģ': 'G',
     'ģ': 'g',
     'Ĥ': 'H',
     'ĥ': 'h',
     'Ħ': 'H',
     'ħ': 'h',
     'Ĩ': 'I',
     'ĩ': 'i',
     'Ī': 'I',
     'ī': 'i',
     'Ĭ': 'I',
     'ĭ': 'i',
     'Į': 'I',
     'į': 'i',
     'İ': 'I',
     'ı': 'i',
     'Ĳ': 'I',
     'ĳ': 'J',
     'Ĵ': 'i',
     'ĵ': 'j',
     'Ķ': 'J',
     'ķ': 'j',
     'ĸ': 'K',
     'Ĺ': 'k',
     'ĺ': 'k',
     'Ļ': 'L',
     'ļ': 'l',
     'Ľ': 'L',
     'ľ': 'l',
     'Ŀ': 'L',
     'ŀ': 'l',
     'Ł': 'L',
     'ł': 'l',
     'Ń': 'L',
     'ń': 'l',
     'Ņ': 'N',
     'ņ': 'n',
     'Ň': 'N',
     'ň': 'n',
     'ŉ': 'N',
     'Ŋ': 'n',
     'ŋ': 'N',
     'Ō': 'n',
     'ō': 'N',
     'Ŏ': 'O',
     'ŏ': 'o',
     'Ő': 'O',
     'ő': 'o',
     'Œ': 'O',
     'œ': 'o',
     'Ŕ': 'O',
     'ŕ': 'E',
     'Ŗ': 'o',
     'ŗ': 'e',
     'Ř': 'R',
     'ř': 'r',
     'Ś': 'R',
     'ś': 'r',
     'Ŝ': 'R',
     'ŝ': 'r',
     'Ş': 'S',
     'ş': 's',
     'Š': 'S',
     'š': 's',
     'Ţ': 'S',
     'ţ': 's',
     'Ť': 'S',
     'ť': 's',
     'Ŧ': 'T',
     'ŧ': 't',
     'Ũ': 'T',
     'ũ': 't',
     'Ū': 'T',
     'ū': 't',
     'Ŭ': 'U',
     'ŭ': 'u',
     'Ů': 'U',
     'ů': 'u',
     'Ű': 'U',
     'ű': 'u',
     'Ų': 'U',
     'ų': 'u',
     'Ŵ': 'U',
     'ŵ': 'u',
     'Ŷ': 'U',
     'ŷ': 'u',
     'Ÿ': 'W',
     'Ź': 'w',
     'ź': 'Y',
     'Ż': 'y',
     'ż': 'Y',
     'Ž': 'Z',
     'ž': 'z',
     'ſ': 'Z',
     '€': 'z',
     '£': 'Z'}

# %%
def RewriteFname(fname):
    fname = fname.replace(" ", "_")
    
    fname = ".".join(
        fname.split(".")[:-1] + ["tif"]
        )
    for char_dia, char_nodia in diakritika_map.items(): 
        fname = fname.replace(char_dia, char_nodia)
        
    return fname



flist = os.listdir(path_in)
plt.ioff()
for file in flist: 
    if not file.endswith(koncovky):
        continue
    im = Image.open(path_in + file)
    im_arr = np.array(im)
    
    fig, ax = plt.subplots(
        # figsize =np.array(
        #     im_arr.shape[:-1][::-1])/100
        )
    ax.imshow(im_arr, cmap = "Grays")
    ax.set_axis_off()
    # ax.margins(0,0)
    # ax.xaxis.set_major_locator(plt.NullLocator())
    # ax.yaxis.set_major_locator(plt.NullLocator())
    
    fig.tight_layout(pad = 0)
    fig.savefig(path_out + RewriteFname(file), 
                bbox_inches='tight',
                pad_inches = 0
                )
    
plt.ion()
    













