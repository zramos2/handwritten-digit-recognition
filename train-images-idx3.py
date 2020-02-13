import struct as st
import numpy as np

filename = {'images' : 'train-images.idx3-ubyte' ,'labels' : 'train-labels.idx1-ubyte'}
train_imagesfile = open(filename['images'],'rb')

train_imagesfile.seek(0)
magic = st.unpack('>4B',train_imagesfile.read(4))

Img = st.unpack('>I',train_imagesfile.read(4))[0] #num of images
nR = st.unpack('>I',train_imagesfile.read(4))[0] #num of rows
nC = st.unpack('>I',train_imagesfile.read(4))[0] #num of column

images_array = np.zeros((nImg,nR,nC))


#‘B’ is used since it is of ‘unsigned char’ C type and ‘integer’
#Python type and has standard size 1 as mentioned in the official documentation of struct.

#‘>’ is used since the data is in MSB first (high endian) format
#used by most non-Intel processors, as mentioned in their original website.
nBytesTotal = nImg*nR*nC*1 #since each pixel data is 1 byte
images_array = 255 - np.asarray(st.unpack('>'+'B'*nBytesTotal,imagesfile.read(nBytesTotal))).reshape((nImg,nR,nC))
