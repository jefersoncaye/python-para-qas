"""
Aula: Tuplas em Python
"""

print("=== 1. CRIANDO TUPLAS ===")

# Ambientes de teste (dados fixos)
ambientes = ("desenvolvimento", "homologacao", "producao")
print("Ambientes:", ambientes)

# Códigos HTTP de sucesso
codigos_sucesso = (200, 201, 204)
print("Códigos de sucesso:", codigos_sucesso)

# Tupla com tipos mistos
dados_mistos = ("QA", 3, True)
print("Dados mistos:", dados_mistos)

print("\n---\n")

print("=== 2. ACESSANDO ELEMENTOS ===")

print("Primeiro ambiente:", ambientes[0])
print("Segundo ambiente:", ambientes[1])
print("Último ambiente:", ambientes[-1])

print("\n---\n")

print("=== 3. IMUTABILIDADE ===")

ambientes = ("desenvolvimento", "homologacao", "producao")

# Tentativa de alteração (vai gerar erro)
# ambientes[1] = "staging"

print("Tuplas não podem ser alteradas após criação")
print("Tentativa de alteração resultaria em TypeError")

# Comparação com lista (comportamento diferente)
urls_lista = ["https://dev.api.com", "https://hml.api.com", "https://api.com"]
urls_lista[2] = "http://api.com"  # permitido

print("Lista alterada:", urls_lista)

urls_tupla = ("https://dev.api.com", "https://hml.api.com", "https://api.com")

# urls_tupla[2] = "http://api.com"  # erro

print("Tupla protegida contra alteração:", urls_tupla)

print("\n---\n")

print("=== 4. TUPLA COM UM ELEMENTO ===")

# Forma correta
ambiente = ("producao",)
print("Tupla com 1 elemento:", ambiente)
print("Tipo:", type(ambiente))

# Forma incorreta (vira string)
ambiente_errado = ("producao")
print("Não é tupla:", ambiente_errado)
print("Tipo:", type(ambiente_errado))

print("\n---\n")

print("=== 5. TAMANHO E LOOP ===")

codigos_sucesso = (200, 201, 204)

print("Quantidade de códigos:", len(codigos_sucesso))

for codigo in codigos_sucesso:
    print("Validando código:", codigo)

print("\n---\n")

print("=== 6. ENUMERATE ===")

for indice, ambiente in enumerate(ambientes):
    print(f"{indice + 1}. {ambiente}")

print("\n---\n")

print("=== 7. APLICACAO PRATICA QA ===")

# Configuração fixa de banco
CONFIG_BANCO = ("localhost", 5432, "qa_database")

host = CONFIG_BANCO[0]
porta = CONFIG_BANCO[1]
banco = CONFIG_BANCO[2]

print("Host:", host)
print("Porta:", porta)
print("Banco:", banco)

print("\n---\n")

print("=== 8. VALIDACAO DE STATUS ===")

STATUS_SUCESSO = (200, 201, 204)
STATUS_ERRO_CLIENTE = (400, 401, 403, 404)
STATUS_ERRO_SERVIDOR = (500, 502, 503)

codigo_retornado = 201

if codigo_retornado in STATUS_SUCESSO:
    print("Requisição bem-sucedida")
elif codigo_retornado in STATUS_ERRO_CLIENTE:
    print("Erro do cliente")
elif codigo_retornado in STATUS_ERRO_SERVIDOR:
    print("Erro do servidor")
else:
    print("Código desconhecido")

print("\n---\n")

print("=== 9. RETORNO DE FUNCAO COM TUPLA ===")

def obter_credenciais_teste():
    return ("usuario_teste", "senha123")

usuario, senha = obter_credenciais_teste()

print("Usuário:", usuario)
print("Senha:", senha)

print("\n---\n")
