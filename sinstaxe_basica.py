"""
Aula 04 - Sintaxe Básica em Python
"""

# ============================
# O que é sintaxe
# ============================

# Sintaxe são as regras que definem como o código deve ser escrito
# Se a sintaxe estiver errada, o Python não consegue executar o código

print("Exemplo de código com sintaxe correta")


# ============================
# Indentação em Python
# ============================

# Python usa indentação para definir blocos de código
# O padrão é usar 4 espaços

if True:
    print("Esta linha está corretamente indentada")

# Exemplo INCORRETO de indentação
# DESCOMENTE para ver o erro

# if True:
# print("Erro de indentação")

# Esse código gera:
# IndentationError: expected an indented block

# ============================
# Fim de linha e comandos
# ============================

# Cada linha é uma instrução
# Não é necessário usar ponto e vírgula (;)

print("Linha 1")
print("Linha 2")


# ============================
# Case sensitive
# ============================

# Python diferencia letras maiúsculas de minúsculas

print("Ok")    # correto

# Exemplo INCORRETO
# DESCOMENTE para ver o erro

# Print("Erro")

# Esse código gera:
# NameError: name 'Print' is not defined


# ============================
# Comentários no código
# ============================

# Comentários não são executados
# Servem para explicar decisões e facilitar leitura

print("Código executado")  # Comentário ao final da linha


# ============================
# Strings em Python
# ============================

# Strings são textos
# Podem ser declaradas com aspas simples ou duplas

print("Python para QAs")
print('Curso básico')


# ============================
# Erros comuns de sintaxe
# ============================

# 1. Esquecer os dois pontos (:)
# DESCOMENTE para ver o erro

# if True
#     print("Erro")

# Gera:
# SyntaxError: expected ':'


# 2. Aspas não fechadas
# DESCOMENTE para ver o erro

# print("Erro)

# Gera:
# SyntaxError: unterminated string literal


# 3. Indentação incorreta
# Misturar TAB e espaços pode gerar erro
# O PyCharm ajuda a evitar esse problema automaticamente


# ============================
# Boas práticas iniciais
# ============================

# Código limpo é melhor que código curto
# Organização visual ajuda na leitura

a = 10
b = 5
soma = a + b

print("Resultado da soma:", soma)
