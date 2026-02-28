"""
Aula: Estruturas Condicionais (if, elif, else)
"""

# ================================
# IF BÁSICO
# ================================

idade = 18

# Verifica se idade é maior ou igual a 18
if idade >= 18:
    print("Você é maior de idade")

print("\n---\n")


# ================================
# IF + ELSE
# ================================

idade = 16

if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

print("\n---\n")


# ================================
# IF + ELIF + ELSE
# ================================

nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")
else:
    print("Precisa melhorar")

print("\n---\n")


# ================================
# ORDEM DAS CONDIÇÕES
# ================================

nota = 9

# Exemplo com ordem incorreta
if nota >= 7:
    print("Bom")
elif nota >= 9:
    print("Excelente")

print("\nCorrigindo a ordem:\n")

# Ordem correta
if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bom")

print("\n---\n")


# ================================
# CONDIÇÃO EXPLÍCITA
# ================================

idade = 20

if idade > 18:
    print("Maior que 18 (condição explícita)")

print("\nExemplo que funciona, mas não é recomendado:\n")

if idade:
    print("Isso funciona, mas não deixa clara a regra")

print("\n---\n")


# ================================
# ERRO COMUM 1 — FALTA DOS DOIS PONTOS
# ================================

print("Exemplo comentado para não quebrar o script:")

# if idade >= 18
#     print("Erro")

print("Erro: SyntaxError: expected ':'")

print("\n---\n")


# ================================
# ERRO COMUM 2 — INDENTAÇÃO
# ================================

print("Exemplo comentado para não quebrar o script:")

# if idade >= 18:
# print("Erro de indentação")

print("Erro: IndentationError: expected an indented block")

print("\n---\n")


# ================================
# ERRO COMUM 3 — = EM VEZ DE ==
# ================================

print("Exemplo comentado para não quebrar o script:")

# if idade = 18:
#     print("Erro")

print("Erro: SyntaxError: cannot assign to expression")

print("\nExemplo correto:")

if idade == 20:
    print("Comparação correta usando ==")

print("\n---\n")


# ================================
# ERRO COMUM 4 — TIPOS INCOMPATÍVEIS
# ================================

idade = "18"  # string

print("Tipo atual da variável idade:", type(idade))

print("\nExemplo que geraria erro (comentado):")

# if idade >= 18:
#     print("Erro de tipo")

print("Erro: TypeError: '>=' not supported between instances of 'str' and 'int'")

print("\nExplicação:")
print('"18" é string')
print("18 é inteiro")
print("Não é possível comparar string com inteiro diretamente")

print("\n---\n")
