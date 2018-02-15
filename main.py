# -*- coding: utf-8 -*-
"""
Created on Feb 15 2018 3:53 PM
@author: andrevaETH
"""

import os
from PIL import Image


class ImageReader:

    def __init__(self):
        """
        Constructor
        """
        # - Parameters -
        self.file_path = "/Users/andrevanoncini/Desktop/Papi_Lokis"
        self.new_file_path = "/Users/andrevanoncini/Desktop/Papi_Lokis/adjusted"

        # - These are the required actions -
        list_paths = self.collect_all_image_files(self.file_path)
        self.process_all_images(list_paths)


    def collect_all_image_files(self, file_path):
        """
        Method to collect all files and store them in list
        """
        all_possible_files = os.listdir(file_path)
        all_jpg_images = []

        for el in all_possible_files:
            file_ext = el.split('.')[-1]

            if file_ext == 'JPG':
                all_jpg_images.append(el)

        all_jpg_images.sort()

        return list(all_jpg_images)


    def process_all_images(self, image_files):
        """
        Method to load the images into RAM and then process them
        """
        if type(image_files) == list:
            for el in image_files:
                image_path = os.path.join(self.file_path, el)
                self.process_image(image_path, el)
        else:
            image_path = os.path.join(self.file_path, image_files)
            self.process_image(image_path, image_files)


    def process_image(self, image_path, image_path_short):
        """
        Method to load the image into RAM and then process them
        """
        im_path = Image.open(image_path)
        curr_img = im_path.load()

        # - Store dimensions of image -
        im_width = im_path.size[0]
        im_height = im_path.size[1]

        # - Replace all completely white pixels with black -
        for x in range(im_width):
            for y in range(im_height):
                pix_val = curr_img[x,y]

                if sum(pix_val) > 700:
                    curr_img[x, y] = (0, 0, 0)

        # - Save in new location -
        new_path = os.path.join(self.new_file_path, image_path_short)
        im_path.save(new_path)
        im_path.close()



def main():
    # - Make object -
    img_reader = ImageReader()


if __name__ == '__main__':
    main()
