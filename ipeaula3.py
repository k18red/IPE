
# a = "Sabádo"
# b = "Amanhã é domigo"

# print (len(a))
# print (a[3])

# C = a * 3 + b * 2

# print (C)

# idade = str(input("Digite sua idade"))
# print("João tem %d idade " % idade )

# valor = 45
# real = 32321.683
# print("%0d" % valor)
# print("%5d" % valor)
# print("%05d" % valor)
# print("%-5d" % valor)
# print("%05f" % valor)
# print("%2.2f" % valor)

# frase = "Hoje é sabádo"
# i = 0
# for i in frase:
#     print(i)
 
import string
palavra = input("Digite uma palvra ")

for i in string.punctuation + " ":
    palavra = palavra.replace(i,"")
    
palavra = palavra.lower()

if palavra == palavra[::-1]:
    print("A palavra é um palindromo")  
else:
    print("Não é um palindromo")
    
    