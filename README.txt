Student Name: Gopika Raghavendran
Programming language: Python 3.8.2
Compiler:	MSC v.1927 64 bit (AMD64)
Algorithm: LZW
Files: Gopika_Raghavendran_105189824.py, Decoded.txt, Encoded.txt and Plain.txt

This program requires user input as a python file name through command line. Save the message in the plain.txt.

Encoding and Decoding:
The input data is encoded using the encoder code, the dictionary of size 256 is built and initialized, using the python dictionary data structure in the dictionary, key are characters and values are the ascii values the lzw compression algorithm is applied and we get the compressed data, the program outputs the compressed data and stores it to an output file named encoded.txt. The compressed data is of 4,546 bytes.

The compressed data is decompressed using the decoder code the dictionary of size 256 is built and initialized, using the python dictionary data structure in the dictionary, key are characters and values are the ascii values the lzw decompression algorithm is applied and we get the decompressed data, the program outputs the decompressed data and stores it to an  output file named Decoded.txt. The decompressed data is of 2,559 bytes.

How to run the file:
1. Open the command window.
2. Set the current directory to the location where the file is present.
3. To Encode and Decode, type: 
	python Gopika_Raghavendran_105189824.py

The compressed file will be stored as Encoded.txt and the output file will be stored as Decoded.txt

The program works well with the example provided on canvas, for other data the efficiency depends on the the repeating data values and the size of data.