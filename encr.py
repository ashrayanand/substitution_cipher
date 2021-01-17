# Submitted By:
# ASHRAY ANAND
# CMI roll number: MDS201905  
# Current batch: MSC DS II

import re
import os
import sys
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
    f =  open(os.path.join(sys.path[0], "Plain.txt"),  encoding="utf8")  #open("Plain.txt", "r")
    plain_text = f.read()
    f = open(os.path.join(sys.path[0], "Key.txt"), 'r')
    key = f.read()

    regex = re.compile('[^a-zA-Z]')
    plain_text = regex.sub(' ', plain_text)
    plain_text = plain_text.replace("\n", " ")
    plain_text =  plain_text.replace("\t", " ")
    plain_text = plain_text.upper()

    text_file = open(os.path.join(sys.path[0], "Plain_after_non-alphabets_removal.txt"), "w")
    text_file.write(plain_text)
    text_file.close()

    table = str.maketrans(alphabets, key)
    cipher_text = plain_text.translate(table)
    #print("cipher_text: \n",cipher_text)

    text_file = open(os.path.join(sys.path[0], "Cipher.txt"), "w")
    text_file.write(cipher_text)
    text_file.close()

if __name__ == '__main__':
   main()