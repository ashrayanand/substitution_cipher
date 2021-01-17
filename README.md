# substitution_cipher

encr.py should take as inputs two files named Key.txt and Plain.txt.

Key.txt have an arbitrary permutation of 26 alphabets (in capital) such as
PNIYUHZGMKVAQCETXOFRSDLJWB


The file named plain.txt contains a english language text – over 5000 words taken from some book.

In either case, it (i) removes all characters other than 26 alphabets, replaces tab and newline character by “space” and retains the “space” character as it is, then (ii) converts all characters to uppercase, and (iii) encodes each character using the permutation given in the file Key.txt and the coded text is written to a file named Cipher.txt.

Also, the file decr.py have code that takes as input the files Key.txt and Cipher.txt and produces a file called Message.txt.

Of course, if the same permutation is used to encrypt and decrypt then Message.txt should be same as Plain.txt (minus the extra characters).
