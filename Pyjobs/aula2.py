# a = 10
# b = 5
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('soma: {}. \nsubtracao: {}. '
      '\nmultiplicao: {}. \ndivisao: {}. '
      '\nresto: {}.'.format(soma,
                            subtracao,
                            multiplicacao,
                            divisao,resto))
print(resultado)

# print('soma: ' + str(soma))
# print('subtracao: ' + str(subtracao))
# print(multiplicacao)
# print(int(divisao))
# print(resto)
# x = '1'
# soma2 = int(x) + 1
# print(soma2)
