#corresponde ao ex 9, pq eu achei os ex anteriores muito fraquinhos

num = int(input("Digite um número para ver sua tabuada: "))

def funcao():
    print("-"*15)
    for i in range(11):
        if i > 0:
            print ("{} x {:2} = {}". format(num, i, num*i))
            i+= 1
    print("-"*15)

funcao()