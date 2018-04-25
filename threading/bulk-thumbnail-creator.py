'''
Bulk Thumbnail Creator
Picture processing can take a bit of time for some transformations. Especially if the image is large. Create an image program which can take hundreds of images and converts them to a specified size in the background thread while you do other things. For added complexity, have one thread handling re-sizing, have another bulk renaming of thumbnails etc.
'''
import multiprocessing
import os, time
from PIL import Image


def resize(img_list, path_img, path_thumb, size):
    print(multiprocessing.current_process())

    for img in img_list:
        #image thumb
        infile = path_img + img
        #thumbnail puth
        outfile = path_thumb + img

        try:
            im = Image.open(infile)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save(outfile, "JPEG")

        except IOError:
            print("Cannot create thumbnail for image {}".format(img))


def rename(img_list, path_thumb):
    print(multiprocessing.current_process())

    for img in img_list:
        old_file = os.path.join(path_thumb, img)
        new_file = os.path.join(path_thumb, "thumb-" + img)
        os.rename(old_file, new_file)


img_list = [str(x) for x in range(1,34)]
size = 250, 250
path_img = "images/"
path_thumb = "images/thumbnail/"

p1 = multiprocessing.Process(target = resize, args = [img_list, path_img, path_thumb,size,])
p2 = multiprocessing.Process(target = rename, args = [img_list, path_thumb,])

p1.start()
time.sleep(2)
p2.start()

p1.join()
p2.join()
