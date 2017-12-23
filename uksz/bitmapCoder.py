import binascii as converter
from PIL import Image
from sys import argv


def isEven(val):

    if  not type(val) == type(1): val = ord(val)
    if val % 2 == 0:
        return True
    else:
        return False


def changeParity(val):
    if val == 255:
        val = val - 1
    else:
        val = val + 1
    return val


def coder(string, img):
    im = Image.open(img)
    binaryStringMap = map(bin, bytearray(string, 'ASCII'))
    listOfImageData = list(im.getdata())
    
    if len(listOfImageData)/7 < len(string):
        raise Exception('Error. Too much data to code.')
    counter = 0
    for i in range(0,len(string)+1):
        if i==len(string):
            bits = list('0000000')
        else:
            bits = list(bin(ord(string[i])))
            while len(bits)>7: bits.pop(0)
  
        
        
        for b in bits:
            if isEven(b):
                if not isEven(listOfImageData[counter]):
                    listOfImageData[counter] = changeParity(listOfImageData[counter])
            else:
                if isEven(listOfImageData[counter]):
                    listOfImageData[counter] = changeParity(listOfImageData[counter])
            counter = counter + 1

    
    codedIMG = im.putdata(listOfImageData)
    im.save('codedIMG.bmp')
    print('done.')
    

def decoder(img):
    dim = Image.open(img)
    dataList = list(dim.getdata())
    #print dataList
    word = ''
    counter = 0
    binword = '0b'
    for element in dataList:

        if element % 2 == 0:
           binword = binword + '0'
        else:
            binword = binword + '1'
        counter = counter + 1
        if counter > 6:         
            letter = str(chr(int(binword, 2)))
            if binword == '0b0000000':
                break
            word = word + letter
            
            binword = '0b'
            counter = 0

    print (word)
        

if __name__ == '__main__':

    if len(argv) == 4:
        if argv[1] == '-c':
            coder(argv[3], argv[2])
    elif len(argv) == 3:
        if argv[1] == '-d':
            decoder(argv[2])
    else:
        print ('Bad parameters.')
