#Name: Gopika Raghavendran
#StudentID: 105189824
#Course: ELEC8900-4-R-2020F Information Transmission Systems
#Submitted to: Dr. Kemal Tepe

import sys
from struct import*
filename="plain.txt"
fileHandle=open(filename,"r")
message=fileHandle.read()

if (len(sys.argv)>1):
        message=str(sys.argv[1])

def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary.get(w,45))
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    debug_str=""
    from io import StringIO
    
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))

    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        debug_str += "Adding: ["+str(dict_size)+"]\t"+dictionary[dict_size]+"\n"
        dict_size += 1
        w = entry
    return result.getvalue(),debug_str

 
# How to use:
print("Input: ", message)
compressed = compress(message)
print("\nCompressed Data:\n", compressed)

##Compressed file extracted
output_file = open("Encoded.txt", "w")
for data in compressed:
    data = str(data)
    data = data+","
    output_file.write(data)
output_file.close()

decompressed, debug_str = decompress(compressed)
print("\nDecompressed Data:\n", (decompressed))

##De-Compressed file extracted
decodedfile = open("Decoded.txt", "w")
for data in decompressed:
    data = str(data)
    decodedfile.write(data)
decodedfile.close()

print("\n\nDebug")
print(debug_str)
