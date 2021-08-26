from random import randint
from time import sleep



while True:
    print '+='*10
    print '''1 - GERAR CPF
2 - CRIAR CPF
3 - VALIDAR CPF
4 - SAIR''' 
    try:
        resp = int(raw_input('>'))
    except:
        print 'Tente de Novo' 
        continue
    soma = 0

    if resp == 3:
        var = 0
        while var == 0:
            try:
                print 'Validar CPF'
                soma =  raw_input('CPF:')
                var += 1
            except:
                continue

    elif resp == 1:
        print 'GERANDO' 
        sleep(2)
        a = str(randint(100,1000))
        b = str(randint(100,1000))
        c = str(randint(100,1000))

        soma = a + '.' + b + '.' + c


    elif resp == 2:
        var = 0
    
        while var <= 5:
            if var <= 5:
                try:
                    print '''Criar CPF
                    Ex: 111.222.333'''
                    soma = raw_input('CPF: ')
                    var += 1
            
                except:
                    continue
            
        
                
    elif resp == 4:
        print 'SAINDO...'
        sleep(2)
        exit()

    def digito1():

        global soma
        result1 = 0

        pri = int(soma[0])*10
        seg = int(soma[1])*9
        ter = int(soma[2])*8
        qua = int(soma[4])*7
        qui = int(soma[5])*6
        sex = int(soma[6])*5
        set = int(soma[8])*4
        oct = int(soma[9])*3
        non = int(soma[10])*2

        junt = pri+seg+ter+qua+qui+sex+set+oct+non
        rest = junt%11
        if rest == 0 or rest == 1:
            return result1
        else:
            result1 = (rest - 11)*-1
            return result1


    second = digito1()

    def digito2():

        global soma
        global second
        result2 = 0
        pri = int(soma[0])*11
        seg = int(soma[1])*10
        ter = int(soma[2])*9
        qua = int(soma[4])*8
        qui = int(soma[5])*7
        sex = int(soma[6])*6
        set = int(soma[8])*5
        oct = int(soma[9])*4
        non = int(soma[10])*3
        dec = int(second)*2
        junt = pri+seg+ter+qua+qui+sex+set+oct+non+dec
        rest = junt%11
        if rest == 0 or rest == 1:
            return result2
        else:
            result2 = (rest - 11) * -1
            return result2

    if resp == 1 or resp == 2:
        print '---->'+soma+'-'+str(digito1())+str(digito2())

    elif resp == 3:
        if soma[12] == str(digito1()) and soma[13] == str(digito2()):
            sleep(2)
            print 'VALIDO'
        else:
            sleep(2)
            print 'INVALIDO' 

