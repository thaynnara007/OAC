import math

def XOR(bit1, bit2):

    if bit1 == bit2 : 
        return "0"
    else: 
        return "1"

def XORconsecutivos(posicoes, bit):

    global byteRecebido

    bit1 = byteRecebido[posicoes[0] - 1]
    bit2 = byteRecebido[bit - 1]

    result = XOR(bit1,bit2)

    for i in xrange(1,len(posicoes)):

        bit = byteRecebido[posicoes[i] - 1]
        result = XOR(result, bit)

    return result

def findRelacao(tamanho):

    global bitsParidade

    for i in xrange(1,tamanho + 1):

        if math.log(i,2) % 1 == 0:

            bitsParidade[i] = []
        
        else:

            byte = bin(i)[2:]
            size = len(byte)
            for j in xrange(size -1, -1, -1):

                if byte[j] == "1":

                    index = math.fabs(size - (j+1))
                    bit = 2 ** index
                    bitsParidade[bit].append(i)

def findParidade():

    global bitsParidade
    result = {}
    
    for bit in bitsParidade.keys():

       if bitsParidade[bit] != []:
            result[bit] = XORconsecutivos(bitsParidade[bit], bit)
    
    return result

def findErro():

    global bitsParidade
    global byteRecebido
    global tamanho
    global paridade

    findRelacao(tamanho)
    paridade = findParidade()
    erro = False
    saida = ''

    for bit in paridade.keys():

        if paridade[bit] != "0":
            
            saida += ' bit %d' %bit
            erro = True
    
    if erro:

        saida = "Houve erro. Inconsistencia encontrada no(s) bit(s):" + saida
    
    else:

        saida = "Nao houve erro."
    
    print saida
    return erro

def findBitErrado():

    global paridade

    bits = paridade.keys()
    bits.sort()
    bits.reverse()
    bitErrado = ""

    for bit in bits:

        bitErrado += paridade[bit]
    
    return bitErrado

def corrigeErro():

    global tamanho
    global byteRecebido

    bitErrado = findBitErrado()
    print bitErrado
    posicao = int(bitErrado, 2) -1
    print posicao
    byteCorrigido = ""

    for i in xrange(tamanho):

        if i == posicao:
            print "here"
            byteCorrigido += XOR(byteRecebido[i], "1")
        
        else:

            byteCorrigido += byteRecebido[i]
    
    return byteCorrigido
    

bitsParidade = {}
paridade = {}
repetir = True

while repetir:

    byteRecebido = raw_input('informe o byte recebido:')

    print "============= RELATORIO ================"
    tamanho = len(byteRecebido)
    print tamanho
    erro = findErro()
    if erro:

        print "Fazendo correcao de erro:"

        byte = corrigeErro()

        print "byte corrigido para: %s" %byte 
    
    print "\ntecle 1 para continuar, ou qualquer outra tecla para sair do programa"
    tecla = raw_input()

    if tecla != "1": repetir = False




