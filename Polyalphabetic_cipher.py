#   This program is based oln the concept of POLYALPHABETIC CIPHER TECHNIQUE of INFORMATION SECURITY
#   Author @vishvaPatel
#   IDE Pycharm
#   platform Python 3.7
#   GITHUB vishvapatel/Information_Security

char_map = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
            'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26
            }

#   Method Encryption i/p: Keyword and Original Txt  o/p: Encrypted text


def encryption(keyword, plain_t):

    cipher_t = list()
    i = 0
    for char in range (len(plain_t)):

        if i == len(keyword):
            i = 0
            key_char = char_map[keyword[i]]

            plain_char = char_map[plain_t[char]]

            cipher_char = (key_char + plain_char) % 26
            i += 1
            for kei in char_map.keys():
                if char_map[kei] == cipher_char:
                    cipher_t.append(kei)
        else:
            key_char = char_map[keyword[i]]

            plain_char = char_map[plain_t[char]]

            cipher_char = (key_char + plain_char) % 26
            i += 1
            for kei in char_map.keys():
                if char_map[kei] == cipher_char:
                    cipher_t.append(kei)

    print("\nTHE CIPHER TEXT FOR PLAIN TEXT {} IS {}".format(plain_t, "".join(cipher_t)))
    decryption(cipher_t, keyword)

#   Decryption i/p: cipher_t and keyword o/p: Original Text


def decryption(cipher_t, keyword):

    original_t = list()
    i = 0

    for char in cipher_t:
        if i == len(keyword):
            i = 0
            key_char = keyword[i]
            original_char = char_map[char] - char_map[key_char]
            if original_char < 0:
                original_char += 26
            i += 1
            for kei in char_map.keys():
                if char_map[kei] == original_char:
                    original_t.append(kei)
        else:
            key_char = keyword[i]
            original_char = char_map[char] - char_map[key_char]
            if original_char < 0:
                original_char += 26
            i += 1
            for kei in char_map.keys():
                if char_map[kei] == original_char:
                    original_t.append(kei)

    print("\nTHE Original TEXT FOR cipher TEXT {} IS {}".format("".join(cipher_t), "".join(original_t)))


def main():
    keyword = input("Enter the keyword:")
    plain_t = input("Enter the plain text:")
    encryption(keyword, plain_t)


if __name__ == '__main__':
    main()

#   cipher_t = encrypted text
#   plain_t = original text
