"""
Aula: Laços Aninhados (Loops dentro de Loops)
"""

# ================================
# O QUE SÃO LAÇOS ANINHADOS
# ================================

print("Laços aninhados são loops dentro de outros loops.")
print("O loop interno executa completamente para cada execução do loop externo.")

print("\nEstrutura geral:\n")

print("""
for x in algo:
    for y in algo:
        bloco_de_codigo
""")

print("\n---\n")


# ================================
# EXEMPLO BÁSICO COM FOR
# ================================

print("Exemplo básico com for:\n")

for i in range(3):
    for j in range(2):
        print("i =", i, "| j =", j)

print("\nExplicação:")
print("Loop externo roda 3 vezes.")
print("Loop interno roda 2 vezes para cada repetição do externo.")
print("Total de execuções: 3 x 2 = 6")

print("\n---\n")


# ================================
# ENTENDENDO A EXECUÇÃO PASSO A PASSO
# ================================

print("Fluxo simplificado:")
print("1. i = 0 → j = 0, j = 1")
print("2. i = 1 → j = 0, j = 1")
print("3. i = 2 → j = 0, j = 1")
print("O loop interno sempre termina antes do externo continuar.")

print("\n---\n")


# ================================
# EXEMPLO VISUAL — TABELA
# ================================

print("Criando uma tabela 3x3:\n")

for linha in range(3):
    for coluna in range(3):
        print("*", end=" ")
    print()

print("\nExplicação:")
print("Loop interno imprime os elementos da linha.")
print("Loop externo controla quantas linhas existem.")

print("\n---\n")


# ================================
# LAÇOS ANINHADOS COM WHILE
# ================================

print("Exemplo com while aninhado:\n")

i = 0

while i < 3:
    j = 0

    while j < 2:
        print("i =", i, "| j =", j)
        j += 1

    i += 1

print("\nExplicação:")
print("Cada loop possui sua própria variável de controle.")
print("Cada loop controla sua própria condição.")

print("\n---\n")


# ================================
# APLICAÇÃO PRÁTICA PARA QA
# ================================

print("Simulando múltiplos usuários com múltiplas tentativas:\n")

usuarios = ["Ana", "Carlos"]

for usuario in usuarios:
    for tentativa in range(2):
        print("Testando login de", usuario, "- tentativa", tentativa)

print("\nExplicação:")
print("Para cada usuário, executamos múltiplas tentativas.")
print("Esse padrão é comum em automação de testes.")

print("\n---\n")


# ================================
# ERRO COMUM — EXCESSO DE NÍVEIS
# ================================

print("Exemplo com três níveis de laço:\n")

for a in range(3):
    for b in range(3):
        for c in range(3):
            print(a, b, c)

print("\nExplicação:")
print("Funciona, mas muitos níveis dificultam leitura e manutenção.")
print("Mais níveis = maior complexidade.")

print("\n---\n")


# ================================
# COMPLEXIDADE
# ================================

print("Entendendo crescimento de execuções:")
print("Loop externo 10 vezes + loop interno 10 vezes = 100 execuções")
print("10 x 10 = 100")
print("100 x 100 = 10.000")
print("1.000 x 1.000 = 1.000.000")
print("Laços aninhados aumentam rapidamente o custo computacional.")

print("\n---\n")
