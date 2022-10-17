from tkinter import image_names
from skimage import io, color, img_as_ubyte, img_as_float
from skimage.filters import threshold_multiotsu
from skimage.segmentation import chan_vese
import matplotlib.pyplot as plt
import numpy as np
from skimage import data
from skimage import filters
import skimage.segmentation.morphsnakes

class Menu:
    def __init__(self,image_source):
        self.image_source  = image_source
        self.image = io.imread(fname=self.image_source)
        
    def get_source(self):
        return self.image

    def save_output(self, output):
        
        io.imsave(self.image_source, output)
    
    def save_as_output(self,output,file_source):
        io.imsave(file_source+"."+self.image_source.split(".")[-1], img_as_ubyte(output))
    
    def export_as_source(self):
        pass
    
    def export_as_output(self, output_image):
        pass
    
    def rgb_to_gray(self):
        gray_image = color.rgb2gray(self.get_source())
  
        filename = "proccesed_images/rgb_to_gray.jpg"
        io.imsave(filename,gray_image)
        return filename

    def rgb_to_hsv(self):
        hsv_image = color.rgb2hsv(self.get_source())
        filename = "proccesed_images/rgb_to_hsv.jpg"
        io.imsave(filename,hsv_image)
        return filename
    
    def multi_otsu_thresholding(self):

        thresholds = threshold_multiotsu(self.image)
        regions = np.digitize(self.image, bins=thresholds)
        #print(regions.shape)
        #print(regions.dtype)
        #io.imshow(regions)
        #plt.show()
        filename = "proccesed_images/multi_otsu_thresholding.jpg"
        io.imsave(filename,regions)
        return filename

    
    def chan_vese_segmentation(self):
        image = img_as_float(self.get_source())
        # Feel free to play around with the parameters to see how they impact the result
        cv = chan_vese(image, mu=0.25, lambda1=1, lambda2=1, tol=1e-3,
               max_num_iter=200, dt=0.5, init_level_set="checkerboard",
               extended_output=True)

        filename = "proccesed_images/chan_vese_segmentation.jpg"
        io.imsave(filename,(cv[0]))
        return filename
    
    def morphological_snakes(self):
        pass
    
    
    def sobel_edge_detection(self):
        image = img_as_float(self.get_source())
        filename = "proccesed_images/sobel_edge_detection.jpg"
        io.imsave(filename,filters.sobel(image))
        return filename
    
    def roberts_edge_detection(self):
        #image = data.horse()
        #  The parameter `image` must be a 2-dimensional array
        image = img_as_float(self.get_source())
        filename = "proccesed_images/roberts_edge_detection.jpg"
        io.imsave(filename,filters.roberts(image))
        return filename

    def scharr_edge_detection(self):
        image = img_as_float(self.get_source())
        filename = "proccesed_images/scharr_edge_detection.jpg"
        io.imsave(filename,filters.scharr(image))
        return filename
    
    def prewitt_edge_detection(self):
        image = img_as_float(self.get_source()) 
        filename = "proccesed_images/prewitt_edge_detection.jpg"
        io.imsave(filename,filters.prewitt(image))
        return filename

#aa  = Menu("image.png")
#x = aa.prewitt_edge_detection()
#io.imshow(x)
#plt.show()
