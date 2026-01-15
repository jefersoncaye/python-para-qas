"""
Aula 05 - Comentários e Boas Práticas Iniciais

"""

# ==================================
# Comentários no contexto do aprendizado
# ==================================

# No início, comentários ajudam a organizar o raciocínio
# Eles funcionam como um "guia" para quem está aprendendo

# Entrada de dados
valor = 10

# Processamento
resultado = valor * 2

# Saída
print(resultado)


# ==================================
# Comentários como apoio ao aprendizado
# ==================================

# Durante o aprendizado, é comum comentar o que estamos tentando fazer
# Isso ajuda a pensar antes de escrever o código

# Aqui quero validar se o valor é maior que 10
if valor > 10:
    print("Valor válido")

# Com o tempo, esse tipo de comentário vai sendo reduzido naturalmente


# ==================================
# Código é lido mais vezes do que escrito
# ==================================

# Clareza é mais importante que velocidade
# Código simples é melhor que código "esperto"
# Quem lê o código pode não ser quem escreveu


# ==================================
# Boas práticas iniciais
# ==================================

# 1. Espaçamento ajuda na leitura

# Exemplo ruim (difícil de ler)
print("Resultado:",10+5)

# Exemplo melhor (mais legível)
print("Resultado:", 10 + 5)


# ==================================
# 2. Quebre o código em partes claras
# ==================================

# Exemplo ruim (difícil de entender)
a=10;b=5;
print(a+b)

# Esse código funciona, mas é difícil de ler e manter

# Exemplo melhor (mais claro)
a = 10
b = 5
soma = a + b
print(soma)


# ==================================
# 3. Organização visual importa
# ==================================

# Usar linhas em branco ajuda a separar blocos lógicos

valor = 10

resultado = valor * 2

print(resultado)


# ==================================
# 4. Código deve explicar a si mesmo
# ==================================

# Exemplo ruim: comentários explicando algo óbvio
# Soma a com b
# Depois imprime
# Resultado final
print(a + b)

# Exemplo melhor: código claro, com menos comentários
resultado = a + b
print(resultado)


# ==================================
# O que evitar desde o início
# ==================================

# - Código confuso "que funciona"
# - Comentários para esconder erros
# - Falta de organização
# - Copiar código sem entender


# ==================================
# Ligação com QA
# ==================================

# Para QA, essas boas práticas são fundamentais porque:
# - Testes precisam ser claros
# - Scripts são mantidos por times
# - Debug depende de leitura rápida
# - Evidências precisam ser confiáveis
