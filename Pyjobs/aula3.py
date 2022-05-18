a = int(input('Primeiro bimestre:'))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre:'))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('terceiro bimestre:'))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre:'))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Média: {}'.format(media))
else:
    print('Foi informado alguma nota errada')




# a = int(input('Entre com o primeiro valor:'))
# b = int(input('Entre com o segundo valor:'))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')

#  a = int(input('entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número é par')
# else:
#     print('Número é impar')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor'))
# if a > b and a > c:
#      print('O maior número é {}'.format(a))
# elif b > a and b > c:
#      print('O maior número é: {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('final do programa')