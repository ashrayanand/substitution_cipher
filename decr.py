# Submitted By:
# ASHRAY ANAND
# CMI roll number: MDS201905  
# Current batch: MSC DS II

import os
import sys
alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    f = open(os.path.join(sys.path[0], "Cipher.txt"), "r")
    cipher_text = f.read()
    f = open(os.path.join(sys.path[0], "Key.txt"), "r")
    key = f.read()
    table2 = str.maketrans(key , alphabets)
    message_text = cipher_text.translate(table2)
    #print("message_text: \n", message_text)

    text_file = open(os.path.join(sys.path[0], "Message.txt"), "w")
    text_file.write(message_text)
    text_file.close()

    # To check if the original Plain_after_non-alphabets_removal and decrypted message_text file are same.

    #f = open(os.path.join(sys.path[0], "Plain_after_non-alphabets_removal.txt"), "r")
    #plain_text = f.read()
    #f = open(os.path.join(sys.path[0], "Message.txt"), "r")
    #message_text = f.read()
    #if (plain_text == message_text) :  
    #    print("Yes") 
    #else :  
    #     print("No")

if __name__ == '__main__':
   main()