 
import os.path
from skimage.io import imread
from skimage import data_dir
img = imread(os.path.join(data_dir, 'checker_bilevel.png'))
 
 
''' Image stored as numpy object (2D Matrix) '''
print(type(img))        # <class 'numpy.ndarray'>
''' Number of image dimensions '''
print(img.ndim)         # 2
''' Shape of the image (rows, columns) '''
print(img.shape)        # (10, 10)
''' Number of total elements in the image '''
print(img.size)         # 100 
''' Size of per element (in bytes) '''
print(img.itemsize)     # 1
''' Size of complete image (in bytes) '''
print(img.nbytes)       # 100
 
 
 
''' assuming you have read the image in variable img '''
# Transpose
img_t = img.T
# Reshape
img_reshape = img.reshape(5, 20)
# Sort
img_srt = img.copy()
img_srt.sort(axis = 0) 
# Compression
img_cmp = img.copy()
img_cmp = img_cmp.compress([True,False,True,0,1,1,1,0,0,1],axis = 0)
print(img_cmp.shape)
 
 
import matplotlib.pyplot as plt
plt.imshow(img, cmap = 'Greys') # Pass above used image names in place of 'img' to visualize
 
