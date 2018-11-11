# -*- coding: utf-8 -*-
"""
Created on Feb 15 2018 3:53 PM
@author: andrevaETH
"""

import os
import skimage
import skimage.io
import skimage.filters
import skimage.color
import skimage.feature
import numpy as np
from PIL import Image


class ImageReader:

    def __init__(self):
        """
        Constructor
        """
        # - Parameters -
        self.file_path = "/Users/andrevanoncini/Desktop/Papi_Lokis"
        self.new_file_path = "/Users/andrevanoncini/Desktop/Papi_Lokis/adjusted"
        self.aspect_ratio = 3

        # - These are the required actions -
        list_paths = self.collect_all_image_files(self.file_path)
        self.process_all_images(list_paths)

    def pil_2_numpy(self, pil_image):
        """
        Converts a PIL object to a numpy array
        """
        return np.array(pil_image)

    def numpy_2_pil(self, numpy_array):
        """
        Converts a numpy array back to a PIL object
        """
        pass

    def collect_all_image_files(self, file_path):
        """
        Method to collect all files and store them in list
        :param file_path:
        :return:
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
        :param image_files:
        :return:
        """
        if type(image_files) == list:
            for el in image_files:
                image_path = os.path.join(self.file_path, el)
                self.process_image(image_path, el)
        else:
            image_path = os.path.join(self.file_path, image_files)
            self.process_image(image_path, image_files)

    def process_skimage(self, image_path, image_path_short):
        """
        Method to load an image into RAM and then process it with the skimage set
        :param image_path:
        :param image_path_short:
        :return:
        """
        im_path = skimage.io.imread(image_path)
        gray_im = skimage.color.rgb2gray(im_path)

        filter_img = skimage.filters.sobel(gray_im)
        view_img = skimage.viewer.ImageViewer(filter_img)
        view_img.show()

    def filter_stack(self, pil_image):
        """
        All operations which are done on the image
        """
        np_image = self.pil_2_numpy(pil_image)

        gray_im = skimage.color.rgb2gray(np_image)
        sobel_im = skimage.filters.sobel(gray_im)
        
    def process_image(self, image_path, image_path_short):
        """
        Method to load an image into RAM and then process it
        ==> not returning desirable results
        :param image_path:
        :param image_path_short:
        :return:
        """
        im_path = Image.open(image_path)

        # - Store dimensions of image and crop -
        im_path = self.resize_image(im_path)
        im_width = im_path.size[0]
        im_height = im_path.size[1]
        new_im_height = im_height
        curr_img = im_path

        #new_im_height = im_height / self.aspect_ratio
        #crop_height_zero = (im_height - new_im_height) / 2

        #im_path = im_path.crop((0, crop_height_zero, im_width, crop_height_zero + new_im_height))
        #curr_img = im_path.load()

        # - Replace all completely white pixels with black -
        for x in range(im_width):
            for y in range(new_im_height):
                pix_val = curr_img[x, y]

                if sum(pix_val) > 700:
                    curr_img[x, y] = (0, 0, 0)

        # - Save in new location -
        new_path = os.path.join(self.new_file_path, image_path_short)
        im_path.save(new_path)
        im_path.close()

    def apply_filter(self, pixel_image, filter_kernel):
        """
        This method applies a filter to an image
        :param pixel_image:
        :param filter_kernel:
        :return:
        """
        np_image = self.pil_2_numpy(pixel_image)

        [width, height] = np_image.shape
        [filter_width, filter_height] = filter_kernel.shape
        np_row = np_col = 0
        while np_row < height:
            np_col = 0
            for np_col in range(0, width):
                if(np_col - filter_width < 0 or np_col + filter_width > width):
                    # - Case if we are at the border of the image -
                    pass

    def resize_image(self, pixel_image):
        """
        Resizes the image to the required dimensions
        :param pixel_image:
        :return:
        """

        small_image = pixel_image.resize((150, 50), Image.LANCZOS)

        return small_image




def main():
    # - Make object -
    img_reader = ImageReader()


if __name__ == '__main__':
    main()
