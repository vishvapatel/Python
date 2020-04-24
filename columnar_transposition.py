import math
plain_t = input("Enter the plain text:")
plain_tmatrix = list()
size = int(math.sqrt(len(plain_t)))
k = 0

for i in range(size):
    plain_tmatrix.insert(i, '0')
    plain_tmatrix[i] = list()
    for j in range(size):
        plain_tmatrix[i].insert(j, plain_t[k])
        k += 1
        if k == len(plain_t):
            break

    if k == len(plain_t):
        i = 0
        j = 0
        break

k = 0
cipher_t = list()
for i in range(size):
    for j in range(size):
            cipher_t.append(plain_tmatrix[j][i])


print("The cipher_t for plain text {} is {}".format(plain_t, "".join(cipher_t)))


