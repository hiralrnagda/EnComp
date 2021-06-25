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

The crux of this algorithm is to secure textfiles and transmit them even on low bandwidth communication channel by compressing them.

Through EnComp, the filesize of textfile _after encrypting and compressing_ was brought down to 25% of the _original textfile_ which is now __secure__ and __lightweight__ 

---
![encomp_output](https://user-images.githubusercontent.com/48949772/116284477-bf423c00-a7aa-11eb-943a-5db29ad2cca3.JPG)

---
![demo](https://user-images.githubusercontent.com/48949772/123384694-56aceb00-d5b2-11eb-8a10-ab44f55311c3.mp4)


