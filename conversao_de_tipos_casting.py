"""
Aula: Conversão de tipos (casting)

"""

# ================================
# PROBLEMA SEM CASTING
# ================================

valor1 = input("Digite um número: ")
valor2 = input("Digite outro número: ")

print("Resultado sem casting:", valor1 + valor2)

print("\n---\n")

# ================================
# CASTING PARA INTEIRO
# ================================

numero_texto = input("Digite um número inteiro: ")
numero = int(numero_texto)

print("Valor convertido:", numero)
print("Tipo:", type(numero))

print("\n---\n")

# ================================
# CASTING PARA FLOAT
# ================================

valor_texto = input("Digite um valor decimal: ")
valor_decimal = float(valor_texto)

print("Valor convertido:", valor_decimal)
print("Tipo:", type(valor_decimal))

print("\n---\n")

# ================================
# CASTING PARA STRING
# ================================

total = 150
mensagem = "Valor total: " + str(total)

print(mensagem)

print("\n---\n")

# ================================
# CASTING COM OPERAÇÃO
# ================================

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = a + b
print(f"Resultado da soma: {soma}")

print("\nFim do script")
