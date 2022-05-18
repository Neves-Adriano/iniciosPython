class Calculadora:

    def soma (self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self,valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
valor_a = int(input('Entre com o primeiro valor: '))
valor_b = int(input('Entre com o segundo valor: '))
print(calculadora.soma(valor_a, valor_b))
print(calculadora.subtracao(valor_a, valor_b))
print(calculadora.multiplicacao(valor_a, valor_b))
print(calculadora.divisao(valor_a, valor_b))
