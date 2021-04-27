# EnComp
## A hybrid algorithm that comprises of 
  * Elliptic Curve Cryptography encryption algorithm
  * Canonical Huffman Encoding compression algorithm
  
The general flow of the algorithm

__Sender side__
  * Original Textfile ---> ECC Encryption ---> Cannonical Huffman Encoding compression
  
__Receiver Side__
  * Cannonical Huffman Encoding decompression ---> ECC Decryption ---> Original textfile
  
---
The crux of this algorithm is to secure textfiles and transmit them even on low bandwidth communication channel.

---
![Console Output]![encomp_output](https://user-images.githubusercontent.com/48949772/116284477-bf423c00-a7aa-11eb-943a-5db29ad2cca3.JPG)


