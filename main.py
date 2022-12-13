from Calculadora import *

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

escolha = int(input('Escolha sua operação:\n'
                    '1-Soma\n'
                    '2-Subtração\n'
                    '3-Multiplicação\n'
                    '4-Divisão\n'))

res = Calculadora(n1, n2)

match escolha:
    case 1:
        print(f'A soma entre {n1} e {n2} resulta em: {res.getsoma()}')
    case 2:
        print(f'A diferença entre {n1} e {n2} resulta em: {res.getsub()}')
    case 3:
        print(f'A multiplicação entre {n1} e {n2} resulta em: {res.getmult()}')
    case 4:
        print(f'A divisão entre {n1} e {n2} resulta em: {res.getdiv()}')
    case _:
        pass
