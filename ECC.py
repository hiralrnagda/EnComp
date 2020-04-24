import random
import curve


class ECC:
    def __init__(self):
        self.h = 1
        self.k = random.getrandbits(256)

    def encAscii(self, character):
        #print("char_______>>>",character)
        return ord(character) << 2

    def decAscii(self, asciiVal):
        return int(asciiVal) >> 2

    def encode(self, msg):
        #print("msg----->",msg)
        encodedString = ''
        for i in msg:
            #print("i----------->>>>",i)
            encodedString += str(self.encAscii(i))
        return encodedString

    def decode(self, encAscii_string):
        pack = ''
        i = 0
        decodedString = ''
        #print("encAscii_string",encAscii_string)
        while (i < len(str(encAscii_string))):
            pack = encAscii_string[i:i+3]
            #print("Pack---->",pack)
            decodedString += chr(self.decAscii(pack))
            #print("decodedstr--->",decodedString)
            i = i+3
        return decodedString

    # formulae referred on https://hackernoon.com/elliptic-curve-crypto-addition-42f6cb9916d7

    def modInverse(self, a, n = curve.P):
        lowM = 1
        highM = 0
        low = a % n
        high = n
        while low > 1:
            r = high//low
            nm = highM-lowM*r
            new = high-low*r
            lowM, low, highM, high = nm, new, lowM, low
        return lowM % n

    def eccAddition(self, a, b):
        LamAdd = ((b[1]-a[1]) * self.modInverse(b[0]-a[0], curve.P)) % curve.P
        x = (LamAdd*LamAdd-a[0]-b[0]) % curve.P
        y = (LamAdd*(a[0]-x)-a[1]) % curve.P
        return(x, y)

    def ecTwoFold(self, a):
        Lam = ((3*a[0]*a[0]+curve.A) * self.modInverse((2*a[1]), curve.P)) % curve.P
        x = (Lam*Lam-2*a[0]) % curve.P
        y = (Lam*(a[0]-x)-a[1]) % curve.P
        return(x, y)

    def eccDot(self, generatedPoint, constK):  # Double & add. Not true multiplication
        constKBin = str(bin(constK))[2:]
        Q = generatedPoint

        # this is a optimised implementaion for faster multiplication
        for i in range(1, len(constKBin)):  # EC multiplication.
            Q = self.ecTwoFold(Q)
            if constKBin[i] == "1":
                Q = self.eccAddition(Q, generatedPoint)
        return (Q)

    def gen_pubKey(self, privKey):
        #print("******* Public Key Generation *********")
        PublicKey = self.eccDot(curve.GP, privKey)
        return PublicKey

    def encryption(self, Public_Key, msg):
        msg = self.encode(msg)
        C1 = self.eccDot(curve.GP, self.k)
        C2 = self.eccDot(Public_Key, self.k)[0]+int(msg)
        return (C1, C2)

    def decryption(self, C1, C2, private_Key):
        solution = C2 - self.eccDot(C1, private_Key)[0]
        return self.decode(str(solution))
