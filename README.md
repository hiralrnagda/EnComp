# EnComp
##A hybrid algorithm that comprises of 
  - Elliptic Curve Cryptography encryption algorithm
  - Canonical Huffman Encoding compression algorithm
  
The general flow of the algorithm
*** Sender side ***
  - Original Textfile ---> ECC Encryption ---> Cannonical Huffman Encoding compression
  
*** Receiver Side ***
  - Cannonical Huffman Encoding decompression ---> ECC Decryption ---> Original textfile
  
===
The crux of this algorithm is to secure textfiles and transmit them even on low bandwidth communication channel.

