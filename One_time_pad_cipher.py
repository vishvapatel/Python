#This program is an implementation of one time pad cipher in an Information Security domain.
#programming language Python 3
#@Author vishva patel
#IDE Jetbrains-pycharm
# Github vishvapatel/Information_Security

import random

char_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26
            }


def main():
            
    plain_t = input("Enter the palin text:")
    key_list = list()
    for i in range(len(plain_t)):
        keyword = random.randint(1, 26)
        key_list.append(keyword)
    encryption(plain_t, key_list)



def encryption(plain_t, key_list):
            
    cipher_t = list()
    for i in range(len(plain_t)):
        cipher_char = char_map[plain_t[i]] + key_list[i]
        cipher_mod = cipher_char % 26
        for kei in char_map.keys():
            if cipher_mod == char_map[kei]:
                cipher_t.append(kei)
    print("The cipher text for the plain text {} is {}".format(plain_t, "".join(cipher_t)))
    print("The key for encryption is {}".format(key_list))
            
    decryption(cipher_t, key_list)




def decryption(cipher_t, key_list):
            
    original_t = list()
    for i in range(len(cipher_t)):
        original_char = char_map[cipher_t[i]] - key_list[i]
        if original_char < 0:
            original_char = 26 + original_char
            original_mod = original_char % 26
        else:
            original_mod = original_char % 26
        for kei in char_map.keys():
            if original_mod ==  char_map[kei]:
                original_t.append(kei)
    print("The original text for the cipher text {} is {} ".format("".join(cipher_t), "".join(original_t)))



if __name__ == "__main__":
    main()


# -----------------------------------------------------------OUTPUT---------------------------------------------------------------------
Enter the palin text:vishvapatel
            
The cipher text for the plain text vishvapatel is vdcragouchp
            
The key for encryption is [26, 21, 10, 10, 5, 6, 25, 20, 9, 3, 4]

The original text for the cipher text vdcragouchp is vishvapatel 
