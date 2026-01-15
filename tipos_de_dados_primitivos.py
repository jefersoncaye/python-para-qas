"""
Aula 06 - Tipos de Dados Primitivos em Python
"""

# --------------------------------------------
# O que é um tipo de dado?
# --------------------------------------------
# Um tipo de dado informa ao Python:
# - Como o valor será armazenado
# - Como ele será exibido
# - Como ele poderá ser usado futuramente

# Exemplo simples:
status_code = 200
print(status_code)  # O Python entende que 200 é um número inteiro (int)

print("-" * 40)

# --------------------------------------------
# 1. Inteiro (int)
# --------------------------------------------
# Representa números inteiros, sem casas decimais

status_code = 200
quantidade_usuarios = 15
tentativas = 3

print(status_code)
print(quantidade_usuarios)
print(tentativas)

print("-" * 40)

# --------------------------------------------
# 2. Ponto flutuante (float)
# --------------------------------------------
# Representa números decimais

tempo_resposta = 1.42
valor_total = 199.90

print(tempo_resposta)
print(valor_total)

print("-" * 40)

# --------------------------------------------
# 3. Texto (str)
# --------------------------------------------
# Representa textos
# Strings sempre ficam entre aspas simples ou duplas

mensagem = "Usuário criado com sucesso"
endpoint = "/api/login"
nome_usuario = "admin"

print(mensagem)
print(endpoint)
print(nome_usuario)

print("-" * 40)

# --------------------------------------------
# 4. Booleano (bool)
# --------------------------------------------
# Representa valores lógicos:
# True  -> verdadeiro
# False -> falso
#
# Por enquanto, apenas exibimos esses valores.
# O uso em decisões será visto mais adiante.

login_valido = True
usuario_ativo = False

print(login_valido)
print(usuario_ativo)

print("-" * 40)

# --------------------------------------------
# 5. Valor nulo (None)
# --------------------------------------------
# Representa ausência de valor
# None NÃO é texto e NÃO é número

token = None
print(token)

print("-" * 40)

# --------------------------------------------
# Tipagem dinâmica
# --------------------------------------------
# Python é uma linguagem de tipagem dinâmica.
# Isso significa que não declaramos o tipo da variável.
# O Python identifica o tipo automaticamente.

resultado = 10
print(resultado)

resultado = "Erro na execução"
print(resultado)

print("-" * 40)

# --------------------------------------------
# Descobrindo o tipo de uma variável
# --------------------------------------------
# Usamos a função type() para verificar
# qual tipo o Python atribuiu ao valor

tempo = 1.5
print(type(tempo))

mensagem = "OK"
print(type(mensagem))

print("-" * 40)

# --------------------------------------------
# Cuidados iniciais com tipos
# --------------------------------------------
# Mesmo que os valores pareçam iguais,
# tipos diferentes NÃO são a mesma coisa.

codigo = 200          # inteiro
codigo_texto = "200"  # texto

print(codigo)
print(codigo_texto)

# Esses dois valores parecem iguais visualmente,
# mas possuem tipos diferentes.
# Isso será muito importante quando começarmos validações.

print(type(codigo))
print(type(codigo_texto))

# --------------------------------------------
# Fim do script
# --------------------------------------------
