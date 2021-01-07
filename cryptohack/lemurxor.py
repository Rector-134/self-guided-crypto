#!/usr/bin/env python3

import cv2
import numpy as np

lemur_encoded = cv2.imread('/home/bones/.cryptohack/lemur_encoded.png')
flag = cv2.imread('/home/bones/.cryptohack/flag.png')

lemur = cv2.bitwise_xor(lemur_encoded, flag, mask = None)

filename = 'lemur.png'

cv2.imwrite(filename, lemur)
