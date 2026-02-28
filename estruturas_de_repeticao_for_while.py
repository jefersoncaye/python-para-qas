"""
Aula: Estruturas de Repetição (for, while, break, continue)
"""

# ================================
# O QUE É UM LOOP
# ================================

print("Exemplo sem loop:")
print("Teste")
print("Teste")
print("Teste")

print("\nAgora usando loop:\n")

for numero in range(3):
    print("Teste")

print("\n---\n")


# ================================
# ESTRUTURA FOR
# ================================

print("Exemplo 1 — Repetindo 5 vezes")

for numero in range(5):
    print("Executando...")

print("\n---\n")

print("Exemplo 2 — Mostrando os números")

for numero in range(5):
    print(numero)

print("\n---\n")

print("Exemplo 3 — Começando de outro número")

for numero in range(1, 6):
    print(numero)

print("\n---\n")

print("Exemplo 4 — Definindo passo")

for numero in range(0, 10, 2):
    print(numero)

print("\n---\n")


# ================================
# ESTRUTURA WHILE
# ================================

print("Exemplo — Contador simples com while")

contador = 0

while contador < 5:
    print(contador)
    contador += 1

print("\n---\n")


# ================================
# LOOP INFINITO (EXEMPLO COMENTADO)
# ================================

print("Exemplo que geraria loop infinito (comentado):")

# contador = 0
# while contador < 5:
#     print(contador)
# (contador nunca é atualizado)

print("Se não atualizar a variável, o loop nunca termina.")

print("\n---\n")


# ================================
# DIFERENÇA ENTRE FOR E WHILE
# ================================

print("Use FOR quando sabe a quantidade de repetições.")
print("Use WHILE quando depende de uma condição.")

print("\n---\n")


# ================================
# EXEMPLO PRÁTICO PARA QA
# ================================

print("Simulando tentativas de login:")

tentativas = 0

while tentativas < 3:
    print("Tentando login...")
    tentativas += 1

print("\n---\n")


# ================================
# BREAK — INTERROMPENDO O LOOP
# ================================

print("Exemplo com while usando break")

contador = 0

while contador < 10:
    print(contador)

    if contador == 5:
        break

    contador += 1

print("\n---\n")

print("Exemplo com for usando break")

for numero in range(10):
    if numero == 3:
        break

    print(numero)

print("\n---\n")


# ================================
# CONTINUE — PULANDO ITERAÇÃO
# ================================

print("Exemplo com for usando continue")

for numero in range(6):
    if numero == 3:
        continue

    print(numero)

print("\n---\n")

print("Exemplo com while usando continue")

contador = 0

while contador < 6:
    contador += 1

    if contador == 3:
        continue

    print(contador)

print("\n---\n")


# ================================
# EXEMPLO PRÁTICO QA — BREAK
# ================================

status_codes = [200, 200, 500, 200]

print("Buscando erro 500:")

for status in status_codes:
    if status == 500:
        print("Erro encontrado!")
        break

print("\n---\n")


# ================================
# EXEMPLO PRÁTICO QA — CONTINUE
# ================================

print("Ignorando status 200:")

for status in status_codes:
    if status == 200:
        continue

    print("Status diferente de 200:", status)

print("\n---\n")