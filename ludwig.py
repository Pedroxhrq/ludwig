# # # # # # # # # # # # #
# # #               # # #
# # #  L U D W I G  # # #
# # #               # # #
# # # # # # # # # # # # #

# -*- coding: utf-8 -*-

import cv2
import imutils
import pytesseract
import unicodedata
from pytesseract import Output
from PIL import Image

img_orig = cv2.imread('di.jpg', 1)

for angle in xrange(0, 360, 90):
	img_rot = imutils.rotate_bound(img_orig, angle=angle)

height, width = img_rot.shape[:2]
star_row, star_col = int(height*.69), int(width*.15)
end_row, end_col = int(height*.80), int(width*.77)
img_crop = img_rot[star_row:end_row, star_col:end_col]

cv2.imshow('Imagem de Entrada', img_crop)

SC = cv2.imread('SC.jpg', 1)
RS = cv2.imread('RS.jpg', 1)
SP = cv2.imread('SP.jpg', 1)
PR = cv2.imread('PR.jpg', 1)

img = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

img = imutils.resize(img, height=803)

# img = cv2.GaussianBlur(img, (5, 5), 5)

# img = cv2.bilateralFilter(img,9,75,75)

# img = cv2.medianBlur(img,5)

# img = imutils.auto_canny(img)

# img = cv2.Laplacian(img,cv2.CV_64F)
# img = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=1)
# img = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=1)

# img = cv2.blur(img(5,5))

# kernel = np.ones((3,3), np.float32)/9
# img = cv2.filter2D(img, -1, kernel)

# img = cv2.bilateralFilter(img, 9, 75, 75)

text = pytesseract.image_to_string(img, lang='por')
text = unicodedata.normalize("NFD", text).encode('WINDOWS-1252', 'ignore')

if (text.find('SANTA CATARINA') != -1):
    print (u'SSPSC - Secret. de Seg. Pública de Santa Catarina\nIGP-SC - Inst. Geral de Perícias de Santa Catarina\nSSP - Secretaria de Seg. Pública\nIISC - Inst. de Identificação de Santa Catarina')
    cv2.imshow('Imagem de Referência para Comparação - Perfuração Mecânica de Santa Catarina', SC)
    cv2.waitKey(0)
elif (text.find('SAO PAULO') != -1):
    print (u'IIRGD - Inst. de Ident. Ricardo Gumbleton Daunt')
    cv2.imshow('Imagem de Referência para Comparação - Perfuração Mecânica de São Paulo', SP)
    cv2.waitKey(0)
elif (text.find('PARANA') != -1):
    print (u'SESP - Secret. de Estado da Seg. Pública do Paraná\nIIPR - Inst. de Identificação de Paraná')
    cv2.imshow('Imagem de Referência para Comparação - Perfuração Mecânica do Paraná', PR)
    cv2.waitKey(0)
elif (text.find('RIO GRANDE DO SUL') != -1):
    print (u'IIRS - Instituto de Ident. do Rio Grande do Sul\nDIRS - Dep. de Identificação. do Rio Grande do Sul')
    cv2.imshow('Imagem de Referência para Comparação - Perfuração Mecânica do Rio Grande do Sul', SC)
    cv2.waitKey(0)
else:
    print ('ERROR 404 NOT FOUND')

# print (text)

# # # # # # # # #