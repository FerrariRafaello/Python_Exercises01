print('Imprimindo numeros de 0 a 9')
for x in range(10): # utilização do (10) pq os numeros se inicam em (0)    
    print(x, end=' ') # imprime os numeros na horizontal
#se fosse utlizado apenas -print=(x)-, seria imprimido na vertical

print('\nImprimindo os numeros de 1 a 10')
#utilização do (\n) para n sobresair na linha de cima                                            
for x in range(1,11): #uso do 1 para começar em 1 e 11 para ir até 10
    print(x, end=' ')

print('\nImprimindo os numeros impares de 1 a 10')
for x in range(1,11,2):
#utilização novamente do 1 para sinalizar o inicio da repetição e o (2)
#para que seja pulado de 2 em 2! [x-começa,x1-termina,x2-pula]
    print(x,end=' ')

print('\nImprimindo numeros pares')
for x in range(0,11,2): #(0)inicia, (11) termina, (2) pula
    print(x, end = ' ')

print('\nImprimindo numeros de 10 a 0')
for x in range(10,-1,-1):
#(a) sendo 10, satisfaz condição maior que )b) -> -1, fazendo (-s)-> -1
    print(x, end=' ')

print('\nImprimindo numeros de 0 ate 10')
for x in range (0,11,+1):
#o representando o começo, 11 a variação de 0 a 10 e +1(crescente)
    print(x, end=' ')
    
