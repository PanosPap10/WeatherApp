# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 18:07:52 2023

@author: papap
"""

from PIL import Image

# Load the original image
original_image = Image.open("icon_search.png")

# Resize the image to 20x20 using ANTIALIAS method
resized_logo = original_image.resize((40, 40), Image.ANTIALIAS)

# Save the resized image to a file
resized_logo.save("resized_search_icon.png")
