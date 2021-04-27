import os
import sys
import random
import time
import ECC
import huffman as huffman
import io

def ECC_tester():
    filename = "f1.txt"
    original_size = os.path.getsize("InputFiles/" + filename)
    print("\n"+filename+ " Size ---> "+ str(original_size) + " bits\n")
    
    ##########################    ENCRYPTION    ##########################
    
    start_time = time.time()
    input_file = open("InputFiles/" + filename,"r")
    message=input_file.read()
    privKey = random.getrandbits(256)
    ecc = ECC.ECC()
    public_key = ecc.gen_pubKey(privKey)
    (C1,C2) = ecc.encryption(public_key, message)

    eoutput_file = open("EncryptedFiles/" + filename.split(".")[0] + ".txt", "w")
    eoutput_file.write("%d,%d$%d" % (C1[0], C1[1], C2))
    eoutput_file.close()
    
    encrypted_size = os.path.getsize("EncryptedFiles/" + filename.split(".")[0] + ".txt")
    print("Encrypted Size ---> "+ str(encrypted_size) + " bits\n")
    encrypted_time = (time.time() - start_time)
    print("Encrypted time in secs " + str(encrypted_time) + "\n")
    
    ################       COMPRESSION & DECOMPRESSION      ######################
    
    huffman.conduct_test(filename)
    
    ######################          DECRYPTION         ###########################
    
    start_time = time.time()
    f = open("DecompressedFiles/" + filename.split(".")[0] + ".txt",'r')
    message = f.read()
    c = message.index(',')
    m = message.index('$')
    x= (int(message[:c]))
    y=(int(message[(c+1):m]))
    C1=(x,y)
    C2 = int(message[(m+1):])
    dataD = ecc.decryption(C1, C2, privKey)
    
    
    doutput_file = open("DecryptedFiles/" + filename.split(".")[0] + ".txt", "w", encoding="utf-8")
    doutput_file.write("%s" % dataD)
    doutput_file.close()
    
    decrypted_size = os.path.getsize("DecryptedFiles/" + filename.split(".")[0] + ".txt")
    print("Decrypted_size ---> "+ str(decrypted_size) + " bits\n")
    print("Decryption Time : %s seconds\n" % (time.time() - start_time))
   
h=ECC_tester()


