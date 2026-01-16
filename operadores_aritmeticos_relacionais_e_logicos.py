"""
Aula: Operadores aritméticos, relacionais e lógicos
"""

# ================================
# OPERADORES ARITMÉTICOS
# ================================

# Valores base
a = 10
b = 3

# Soma
soma = a + b
print("Soma (10 + 3):", soma)

# Subtração
subtracao = a - b
print("Subtração (10 - 3):", subtracao)

# Multiplicação
multiplicacao = a * b
print("Multiplicação (10 * 3):", multiplicacao)

# Divisão (sempre retorna float)
divisao = a / b
print("Divisão (10 / 3):", divisao)

# Divisão inteira (descarta casas decimais)
divisao_inteira = a // b
print("Divisão inteira (10 // 3):", divisao_inteira)

# Resto da divisão
resto = a % b
print("Resto da divisão (10 % 3):", resto)

# Potenciação
potencia = a ** b
print("Potência (10 ** 3):", potencia)

print("\n---\n")

# ================================
# OPERADORES RELACIONAIS
# ================================
# Operadores relacionais comparam valores
# e retornam True ou False

x = 5
y = 10

print("x =", x)
print("y =", y)

# Igualdade
print("x == y:", x == y)

# Diferença
print("x != y:", x != y)

# Maior que
print("x > y:", x > y)

# Menor que
print("x < y:", x < y)

# Maior ou igual
print("x >= y:", x >= y)

# Menor ou igual
print("x <= y:", x <= y)

print("\n---\n")

# ================================
# OPERADORES LÓGICOS
# ================================
# Operadores lógicos trabalham com valores booleanos

usuario_logado = True
usuario_admin = False

print("Usuário logado:", usuario_logado)
print("Usuário admin:", usuario_admin)

# AND (ambos precisam ser True)
resultado_and = usuario_logado and usuario_admin
print("Logado AND Admin:", resultado_and)

# OR (pelo menos um True)
resultado_or = usuario_logado or usuario_admin
print("Logado OR Admin:", resultado_or)

# NOT (inverte o valor)
resultado_not = not usuario_logado
print("NOT Logado:", resultado_not)

print("\n---\n")

# ================================
# COMBINAÇÃO SIMPLES
# ================================

idade = 20
idade_minima = 18

# Comparação simples
maior_de_idade = idade >= idade_minima
print("Idade:", idade)
print("É maior de idade?", maior_de_idade)

# Operadores lógicos combinados
acesso_permitido = usuario_logado and maior_de_idade
print("Acesso permitido?", acesso_permitido)

# Fim do script
