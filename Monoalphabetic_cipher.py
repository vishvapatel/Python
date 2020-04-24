#Encrypting Method
def Encrypt_text(keyword_pattern,plain_t):
    cipher_t = list()
    for char in plain_t:
        
        if char in keyword_pattern:
            cipher_t.append(keyword_pattern[char])

        else:
            print("pattern cannot be encrypted as no vlaue for the character:{}".format(char))

    print("The cipher text for plain text",plain_t,"is {}".format("".join(cipher_t)))
                    
    return cipher_t



#Decrypting Method

def Decrypt_text(keyword_pattern,cipher_t):
    plain_t=list()
    for char in cipher_t:
        for kei in keyword_pattern.keys():
            
            if keyword_pattern[kei] == char:
                plain_t.append(kei)

                
    print("The plain text for ciphre text {}".format("".join(cipher_t)),"is {}".format("".join(plain_t)))

    return None
    



#Main Method
          
def main():
    number = int(input("Enter the number for the inputs:"))
    keyword_pattern = dict()
    for i in range(number):
        kei = input("input the key character :")
        vlues = input("input the value for the corresponding key :")
        keyword_pattern[kei] = vlues
    #for kei,vlue in keyword_pattern.items():
        #print(kei, vlue)
    plain_t = input("Enter plain text") 
    cipher_t = Encrypt_text(keyword_pattern, plain_t)
    Decrypt_text(keyword_pattern,cipher_t)

    
#Calling Main_Method
if __name__ == "__main__":
                  main()
