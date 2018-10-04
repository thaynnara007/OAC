def XOR(bit1, bit2):

    if bit1 == bit2 : 
        return "0"
    else: 
        return "1"

def divide(byte1, byte2, tamanho):

    result = ""

    for i in xrange(1,tamanho):

        result += XOR(byte1[i], byte2[i])

    return result

def getGrau(polinomio):

    if polinomio[0] == '1':

        return 0
    
    else:

        return int(polinomio[2])

def polinomioToBinario(polinomio):

    fatores = polinomio.split('+')
    size = len(fatores)

    binario = '1'
   
    if len(fatores[0]) > 2:
        ultimoExpoente = fatores[0][2]
        
    elif(fatores[0] != ''):
        ultimoExpoente = 0
        
    else:
        ultimoExpoente = 0
        binario = ""

    for i in xrange(1,size):
        
        fator = fatores[i]

        if len(fator) > 1:
            expoente = fator[2]
        else:
            expoente = 0

        espaco = int(ultimoExpoente) - int(expoente)
        binario += ('0' * (espaco - 1)) + "1"

        ultimoExpoente = expoente

    if ultimoExpoente != 0:

        binario += "0"

    return binario

def verificaErro(plonimonio, mensagem):
    
    tamanho = getGrau(polinomio) + 1
    byteGerador = polinomioToBinario(polinomio)
    size = len(mensagem)

    i = tamanho
    byte = mensagem[:i]
    nulo = '0' * tamanho

    while i <= size:
        
        if byte[0] != "0":

            byte = divide(byte, byteGerador, tamanho)

        else:

            byte = divide(byte, nulo, tamanho)

        i += 1

        if i <= size:

            byte += mensagem[i -1]
        

    if byte == ("0" * (tamanho - 1)):

        print "Nao houve erro."

    else:
        
        print "Houve erro."

repetir = True

while repetir:

    polinomio = raw_input('polinomio:')
    mensagem = raw_input('mensagem:')
    
    print "========= RELATORIO ==========="
    verificaErro(polinomio,mensagem)

    print "\nTecle 1 para continuar, ou qualquer outra tecla para sair do programa"
    tecla = raw_input()

    if tecla != "1": repetir = False

