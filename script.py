from glob import glob                                                           
import cv2 
import label_image
path = glob('Payh/to/images/*.jpg')

for i in path:

	label_image.getFoto(i)	


