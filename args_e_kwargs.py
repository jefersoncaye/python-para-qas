"""Aula: *args e **kwargs em Python"""

print("=== 1. O PROBLEMA: QUANTIDADE VARIAVEL DE ARGUMENTOS ===")


# Imagine que voce precisa criar uma funcao que loga informacoes de teste
# Mas cada teste pode ter uma quantidade diferente de detalhes

# Sem *args, voce teria que definir um numero fixo de parametros:
def logar_resultado_limitado(teste, detalhe1, detalhe2):
    print(f"[LOG] {teste}: {detalhe1}, {detalhe2}")


logar_resultado_limitado("Login", "status: 200", "tempo: 1.2s")

# E se um teste tiver 5 detalhes? Ou apenas 1?
# Precisariamos criar funcoes diferentes para cada caso...
# E eh exatamente isso que *args resolve!

print("\n---\n")

print("=== 2. *ARGS: ARGUMENTOS POSICIONAIS VARIAVEIS ===")


# O * antes do nome do parametro empacota todos os argumentos extras em uma tupla
def logar_resultado(teste, *detalhes):
    print(f"[LOG] Teste: {teste}")
    for detalhe in detalhes:
        print(f"  - {detalhe}")


# Podemos passar quantos argumentos quisermos
print("Teste com 2 detalhes:")
logar_resultado("Login", "status: 200", "tempo: 1.2s")

print()
print("Teste com 4 detalhes:")
logar_resultado(
    "Cadastro",
    "status: 201",
    "tempo: 0.8s",
    "usuario criado: user_42",
    "email enviado: True"
)

print()
print("Teste com 0 detalhes:")
logar_resultado("Health Check")

print()


# O que eh *detalhes por dentro? Uma tupla!
def mostrar_tipo_args(*args):
    print(f"Tipo: {type(args)}")
    print(f"Conteudo: {args}")


mostrar_tipo_args("dev", "hml", "prod")

print("\n---\n")

print("=== 3. EXEMPLO QA: VALIDAR MULTIPLOS STATUS CODES ===")


def todos_sucesso(*status_codes):
    """Verifica se todos os status codes indicam sucesso (2xx)"""
    for code in status_codes:
        if not (200 <= code < 300):
            print(f"  FALHA: status {code} nao eh sucesso")
            return False
    print(f"  OK: todos os {len(status_codes)} status sao sucesso")
    return True


print("Cenario 1 - Todos OK:")
resultado = todos_sucesso(200, 201, 204)
print(f"  Resultado: {resultado}")

print()
print("Cenario 2 - Um falhou:")
resultado = todos_sucesso(200, 404, 201)
print(f"  Resultado: {resultado}")

print()
print("Cenario 3 - Chamada sem argumentos:")
resultado = todos_sucesso()
print(f"  Resultado: {resultado}")

print("\n---\n")

print("=== 4. **KWARGS: ARGUMENTOS NOMEADOS VARIAVEIS ===")


# ** empacota argumentos nomeados extras em um dicionario
def configurar_requisicao(url, **opcoes):
    print(f"URL: {url}")
    for chave, valor in opcoes.items():
        print(f"  {chave}: {valor}")


print("Requisicao simples:")
configurar_requisicao("https://api.exemplo.com/users")

print()
print("Requisicao com opcoes:")
configurar_requisicao(
    "https://api.exemplo.com/users",
    metodo="GET",
    timeout=30,
    headers={"Authorization": "Bearer token123"},
    verificar_ssl=True
)

print()


# O que eh **opcoes por dentro? Um dicionario!
def mostrar_tipo_kwargs(**kwargs):
    print(f"Tipo: {type(kwargs)}")
    print(f"Conteudo: {kwargs}")


mostrar_tipo_kwargs(ambiente="dev", versao="2.1", debug=True)

print("\n---\n")

print("=== 5. EXEMPLO QA: GERAR MASSA DE TESTE DINAMICA ===")


def gerar_usuario_teste(**campos):
    """Gera um dicionario de usuario com campos personalizaveis"""
    # Valores padrao
    usuario = {
        "nome": "Usuario Teste",
        "email": "teste@qa.com",
        "ativo": True
    }
    # Sobrescreve/adiciona com os campos recebidos
    usuario.update(campos)
    return usuario


print("Usuario padrao:")
u1 = gerar_usuario_teste()
for chave, valor in u1.items():
    print(f"  {chave}: {valor}")

print()
print("Usuario customizado:")
u2 = gerar_usuario_teste(
    nome="Maria Silva",
    email="maria@empresa.com",
    perfil="admin",
    departamento="Engenharia"
)
for chave, valor in u2.items():
    print(f"  {chave}: {valor}")

print("\n---\n")

print("=== 6. COMBINANDO *ARGS E **KWARGS ===")


# A ordem OBRIGATORIA dos parametros eh:
# 1. Parametros normais
# 2. *args
# 3. **kwargs

def executar_teste(nome_teste, *passos, **config):
    print(f"Teste: {nome_teste}")

    print("Passos:")
    for i, passo in enumerate(passos, 1):
        print(f"  {i}. {passo}")

    if config:
        print("Configuracoes:")
        for chave, valor in config.items():
            print(f"  {chave}: {valor}")
    print()


executar_teste(
    "Fluxo de Compra",  # nome_teste (normal)
    "Acessar catalogo",  # *passos
    "Adicionar item ao carrinho",  # *passos
    "Finalizar pedido",  # *passos
    ambiente="producao",  # **config
    navegador="Chrome",  # **config
    timeout=60  # **config
)

executar_teste(
    "Smoke Test",  # nome_teste (normal)
    "Verificar health check",  # *passos
    "Checar versao da API",  # *passos
    ambiente="dev"  # **config
)

print("\n---\n")

print("=== 7. DESEMPACOTAMENTO: PASSANDO LISTAS E DICTS COMO ARGUMENTOS ===")

# Alem de receber argumentos variaveis, podemos ENVIAR usando * e **

# * desempacota uma lista/tupla em argumentos posicionais
status_codes = [200, 201, 204, 200]
print("Desempacotando lista com *:")
print(f"  todos_sucesso(*{status_codes})")
resultado = todos_sucesso(*status_codes)
print(f"  Resultado: {resultado}")

print()

# ** desempacota um dicionario em argumentos nomeados
config_padrao = {
    "metodo": "POST",
    "timeout": 15,
    "verificar_ssl": True
}
print("Desempacotando dicionario com **:")
print(f"  config: {config_padrao}")
configurar_requisicao("https://api.exemplo.com/login", **config_padrao)

print()

# Isso eh muito util para reutilizar configuracoes
print("Combinando dict fixo + argumentos extras:")
configurar_requisicao(
    "https://api.exemplo.com/admin",
    **config_padrao,
    headers={"X-Admin": "true"}
)

print("\n---\n")

print("=== 8. APLICACAO PRATICA QA: FUNCAO DE LOG FLEXIVEL ===")

from datetime import datetime


def registrar_evento(nivel, mensagem, *tags, **contexto):
    """Sistema de log flexivel para automacao de testes"""
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Formata a linha principal
    linha = f"[{timestamp}] [{nivel.upper()}] {mensagem}"

    # Adiciona tags se existirem
    if tags:
        linha += f" | tags: {', '.join(tags)}"

    print(linha)

    # Adiciona contexto detalhado
    for chave, valor in contexto.items():
        print(f"    {chave}: {valor}")


# Uso 1: Log simples
registrar_evento("info", "Teste iniciado")

print()

# Uso 2: Log com tags
registrar_evento("warn", "Resposta lenta detectada", "performance", "api", "critico")

print()

# Uso 3: Log com contexto
registrar_evento(
    "error",
    "Falha na autenticacao",
    "auth", "login",
    endpoint="/api/login",
    status_code=401,
    usuario="admin@teste.com",
    tentativa=3
)

print()

# Uso 4: Reutilizando contexto base
contexto_ci = {
    "pipeline": "CI-1234",
    "branch": "main",
    "runner": "ubuntu-latest"
}
registrar_evento("info", "Deploy realizado", "deploy", **contexto_ci)

print("\n---\n")

print("=== FIM DA AULA ===")