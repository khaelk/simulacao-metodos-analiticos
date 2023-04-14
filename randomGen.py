#import matplotlib.pyplot as plt

#funcao de calculo do numero aleatorio utilizando metodo congruencia linear
def metodoCongruenciaLinear (a, m, c, x0, randomNums, numDeRandomNums):
    randomNums[0] = x0

    for i in range(1, numDeRandomNums):
        #Xi = Xi-1 * a + c mod M
        randomNums[i] = ((randomNums[i-1]*a)+c) % m

#funcao de debug
def printNums (randomNums):
    for i in randomNums:
        print(i, end=' ')

#normalizacao dos numeros aleatorios
def normalizeNums (max, randomNums):
    for i in range(len(randomNums)):
        randomNums[i] = round((randomNums[i])/(max),4)
    return randomNums

#caso queira gerar o grafico demonstrando os numeros aleatorios
def generateGraph(x,y):
    plt.scatter(x, y)
    plt.title('Pseudo-random generated numbers')
    plt.xlabel('Generated number index')
    plt.ylabel('Generated number')

    plt.show()

#caso queira escrever os numeros aleatorios num txt
def writeNumsTxt(fileName, content):
    with open(fileName, 'w') as f:
        for i in content:
            f.write(str(i)+ '\n')

#classe com numeros gerados
class GeneratedNums:
    def __init__(self, quantity, seed):
        x0 = seed
        a = 214013
        m = 4294967296
        c = 2531011
        self.quantity = quantity+1
        randomNums = [0] * self.quantity
        metodoCongruenciaLinear (a, m, c, x0, randomNums, self.quantity)
        maxNum = max(randomNums[1:])
        self.nums = normalizeNums(maxNum, randomNums[1:])
    
    def getNums(self):
        return self.nums

    def writeTxt(self):
        writeNumsTxt("numerosGerados.txt", self.nums)


if __name__ == '__main__':
    #seed
    x0 = 346
    #*
    a = 214013
    #modulo
    m = 4294967296
    #+
    c = 2531011

    #qtd de num considerando que indice 0 do array seja a seed
    numDeRandomNums = 1001

    #vetor 'vazio'
    randomNums = [0] * numDeRandomNums
    metodoCongruenciaLinear (a, m, c, x0, randomNums, numDeRandomNums)
    maxNum = max(randomNums[1:])
    normalizedNums = normalizeNums(maxNum, randomNums[1:])
    printNums(normalizedNums)
    arrX=[0]*(numDeRandomNums-1)
    for i in range(numDeRandomNums-1):
        arrX[i]=i
    y = normalizedNums
    x = arrX
    #writeNumsTxt("numerosGerados.txt", normalizedNums)
    #generateGraph(x,y)