"""
Jadoo, the Space Alien has befriended Koba upon landing on Earth. Since then, he wishes Koba to be more like him.
In order to do so he decides to slowly transcribe Koba's DNA into RNA.
But he has to write a very short code in order to do the transcription so as not to make Koba aware of the change.
The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
G --> C
C --> G
T --> A
A --> U
Input: The input will always be a string of characters.
Output: The output should always be a string of characters. In the case of invalid input, you should output Invalid Input as a string.
Rules: Your code should not consist of any numerical characters(0, 1, 2, 3, 4, 5, 6, 7, 8, 9) and the length of your code should be
<= 103.
 @Solved by vishva patel
 Github Link vishvapatel/python
"""
DNA_SEQUENCE = input()
RNA_SEQUENCE =[]
flag = "m"
for nucleiotides in DNA_SEQUENCE:
    if nucleiotides == "C":
        RNA_NUCLEIOTIDE = "G"
        RNA_SEQUENCE.append(RNA_NUCLEIOTIDE)
    elif nucleiotides == "G":
        RNA_NUCLEIOTIDE = "C"
        RNA_SEQUENCE.append(RNA_NUCLEIOTIDE)
    elif nucleiotides == "T":
        RNA_NUCLEIOTIDE = "A"
        RNA_SEQUENCE.append(RNA_NUCLEIOTIDE)
    elif nucleiotides == "A":
        RNA_NUCLEIOTIDE = "U"
        RNA_SEQUENCE.append(RNA_NUCLEIOTIDE)
    else:
        flag = "n"
if flag == "n":
    print("Invalid Input")
if flag == "m":
    print("".join(RNA_SEQUENCE))