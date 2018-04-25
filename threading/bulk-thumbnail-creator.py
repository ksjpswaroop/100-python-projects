'''
Bulk Thumbnail Creator
Picture processing can take a bit of time for some transformations. Especially if the image is large. Create an image program which can take hundreds of images and converts them to a specified size in the background thread while you do other things. For added complexity, have one thread handling re-sizing, have another bulk renaming of thumbnails etc.
'''
import multiprocessing
import os, sys
from PIL import Image


def resize(img_list):
    size = 250, 250

    for img in img_list:
        #path of images
        infile = "images/" + img
        #path of thumbnails
        outfile = "images/thumbnail/" + img
        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")
        except IOError:
            print("cannot create thumbnail for image {}".format(img))


def rename(img_list):
    for img in img_list:
        path = "images/thumbnail/"
        old_file = os.path.join(path, img)
        new_file = os.path.join(path, "thumb-" + img)
        os.rename(old_file, new_file)


img_list = [str(x) for x in range(1,34)]

#resize(img_list)
#rename(img_list)
