"""Aula: Valores Padrão e Argumentos Nomeados em Python"""

print("=== 1. PARAMETRO VS ARGUMENTO ===")

# Parâmetro: variável definida na CRIAÇÃO da função
# Argumento: valor passado na CHAMADA da função

def verificar_status(codigo):  # "codigo" é o PARÂMETRO
    return 200 <= codigo < 300

# 200 é o ARGUMENTO passado para o parâmetro "codigo"
resultado = verificar_status(200)
print(f"verificar_status(200) = {resultado}")

# Na prática, os termos são usados como sinônimos
# Mas saber a diferença ajuda a ler documentações

print(f"\nResumo:")
print(f"  Parâmetro = variável na definição (def func(parametro):)")
print(f"  Argumento = valor na chamada (func(argumento))")

print("\n---\n")

print("=== 2. VALORES PADRAO ===")

# Valores padrão tornam parâmetros opcionais
# Se o argumento não for passado, usa o valor padrão

def gerar_url_teste(endpoint, ambiente="dev"):
    bases = {
        "dev": "https://dev.api.com",
        "hml": "https://hml.api.com",
        "prod": "https://api.com"
    }
    base = bases.get(ambiente, "https://dev.api.com")
    return f"{base}/{endpoint}"

# Sem passar ambiente: usa "dev" (valor padrão)
print(f"Sem ambiente: {gerar_url_teste('users')}")

# Passando ambiente explicitamente: sobrescreve o padrão
print(f"Com hml:     {gerar_url_teste('users', 'hml')}")
print(f"Com prod:    {gerar_url_teste('users', 'prod')}")

print()

# Exemplo com múltiplos valores padrão
def criar_usuario_teste(nome, perfil="viewer", ativo=True):
    return {
        "nome": nome,
        "perfil": perfil,
        "ativo": ativo
    }

# Usando todos os padrões
print(f"Padrões:     {criar_usuario_teste('Ana QA')}")
# Sobrescrevendo apenas o perfil
print(f"Admin:       {criar_usuario_teste('Carlos', 'admin')}")
# Sobrescrevendo perfil e ativo
print(f"Inativo:     {criar_usuario_teste('Bot', 'api', False)}")

print("\n---\n")

print("=== 3. REGRA DE POSICAO DOS VALORES PADRAO ===")

# Parâmetros COM valor padrão devem vir DEPOIS dos sem padrão
# Correto: def func(obrigatorio, opcional="valor")
# Errado:  def func(opcional="valor", obrigatorio)  -> SyntaxError

def configurar_teste(nome_teste, timeout=30, retries=3, verbose=False):
    config = {
        "nome": nome_teste,
        "timeout": timeout,
        "retries": retries,
        "verbose": verbose
    }
    return config

# "nome_teste" é obrigatório, o resto tem padrão
print(f"Config mínima: {configurar_teste('login_test')}")
print(f"Com timeout:   {configurar_teste('login_test', 60)}")

print()
print("# Se inverter a ordem, Python dá erro:")
print("# def func(opcional='x', obrigatorio):  -> SyntaxError")
print("# Motivo: Python não saberia qual argumento vai pra qual parâmetro")

print("\n---\n")

print("=== 4. ARGUMENTOS NOMEADOS (KEYWORD ARGUMENTS) ===")

# Até agora, passamos argumentos pela POSIÇÃO
# Argumentos nomeados permitem especificar QUAL parâmetro recebe QUAL valor

def gerar_relatorio(suite, total, passou, falhou, ambiente="dev"):
    taxa = (passou / total * 100) if total > 0 else 0
    return f"[{ambiente.upper()}] {suite}: {passou}/{total} ({taxa:.0f}%) | Falhas: {falhou}"

# Argumentos posicionais (pela ordem)
print("Posicional:")
print(f"  {gerar_relatorio('Login', 10, 8, 2)}")

# Argumentos nomeados (pela chave)
print("\nNomeado:")
print(f"  {gerar_relatorio(suite='Login', total=10, passou=8, falhou=2)}")

# Grande vantagem: PULAR parâmetros com valor padrão
print("\nPulando parâmetros:")
print(f"  {gerar_relatorio('Login', 10, 8, 2, ambiente='prod')}")

print()

# Outra vantagem: MUDAR A ORDEM dos argumentos
print("Ordem diferente (mesmo resultado):")
print(f"  {gerar_relatorio(falhou=2, suite='Login', passou=8, total=10)}")

print("\n---\n")

print("=== 5. COMBINANDO POSICIONAIS E NOMEADOS ===")

# Regra: posicionais SEMPRE antes dos nomeados
# Correto: func(valor1, valor2, nome="x")
# Errado:  func(nome="x", valor1, valor2)  -> SyntaxError

def executar_request(metodo, endpoint, timeout=30, headers=None, auth=False):
    config = {
        "metodo": metodo,
        "endpoint": endpoint,
        "timeout": timeout,
        "headers": headers or {},
        "auth": auth
    }
    return config

# Posicionais para os obrigatórios, nomeados para os opcionais
print("GET simples:")
req1 = executar_request("GET", "/api/users")
print(f"  {req1}")

print("\nPOST com opcionais específicos:")
req2 = executar_request("POST", "/api/users", auth=True, timeout=60)
print(f"  {req2}")

print("\nGET com headers:")
req3 = executar_request("GET", "/api/admin", headers={"X-Role": "admin"}, auth=True)
print(f"  {req3}")

print()
print("# Repare: pulamos direto para 'auth' e 'headers'")
print("# sem precisar passar 'timeout' no meio")

print("\n---\n")

print("=== 6. CUIDADO COM VALORES PADRAO MUTAVEIS ===")

# ARMADILHA: usar lista ou dicionário como valor padrão

# ERRADO: a lista é compartilhada entre todas as chamadas
def adicionar_log_errado(mensagem, logs=[]):
    logs.append(mensagem)
    return logs

resultado1 = adicionar_log_errado("Erro 404")
resultado2 = adicionar_log_errado("Erro 500")
print(f"ERRADO (logs compartilhados):")
print(f"  Chamada 1: {resultado1}")
print(f"  Chamada 2: {resultado2}")  # Tem os dois! A lista é a mesma

print()

# CORRETO: usar None e criar a lista dentro da função
def adicionar_log_correto(mensagem, logs=None):
    if logs is None:
        logs = []
    logs.append(mensagem)
    return logs

resultado3 = adicionar_log_correto("Erro 404")
resultado4 = adicionar_log_correto("Erro 500")
print(f"CORRETO (logs independentes):")
print(f"  Chamada 1: {resultado3}")
print(f"  Chamada 2: {resultado4}")  # Cada chamada tem sua própria lista

print()
print("# Regra: nunca use lista, dicionário ou set como valor padrão")
print("# Use None e crie o objeto dentro da função")

print("\n---\n")

print("=== 7. APLICACAO PRATICA: FUNCAO DE VALIDACAO FLEXIVEL ===")

# Cenário real: função que valida resposta de API com configurações flexíveis

def validar_resposta_api(
    status_code,
    corpo,
    status_esperado=200,
    campos_obrigatorios=None,
    tempo_resposta=None,
    max_tempo=5.0
):
    if campos_obrigatorios is None:
        campos_obrigatorios = []

    erros = []

    # Validar status code
    if status_code != status_esperado:
        erros.append(f"Status: esperado {status_esperado}, recebeu {status_code}")

    # Validar campos obrigatórios no corpo
    for campo in campos_obrigatorios:
        if campo not in corpo:
            erros.append(f"Campo ausente: '{campo}'")

    # Validar tempo de resposta (se informado)
    if tempo_resposta is not None and tempo_resposta > max_tempo:
        erros.append(f"Tempo: {tempo_resposta}s excede limite de {max_tempo}s")

    if erros:
        return {"valido": False, "erros": erros}
    return {"valido": True, "erros": []}


# Teste 1: validação mínima (só status code)
print("Teste 1 - Validação mínima:")
r1 = validar_resposta_api(200, {"id": 1, "nome": "Ana"})
print(f"  {r1}")

# Teste 2: com campos obrigatórios
print("\nTeste 2 - Com campos obrigatórios:")
r2 = validar_resposta_api(
    200,
    {"id": 1},
    campos_obrigatorios=["id", "nome", "email"]
)
print(f"  {r2}")

# Teste 3: validação completa
print("\nTeste 3 - Validação completa:")
r3 = validar_resposta_api(
    status_code=201,
    corpo={"id": 1, "nome": "Ana"},
    status_esperado=200,
    campos_obrigatorios=["id", "nome"],
    tempo_resposta=6.2,
    max_tempo=5.0
)
print(f"  {r3}")

# Teste 4: endpoint com status diferente
print("\nTeste 4 - Status 201 (criação):")
r4 = validar_resposta_api(
    201,
    {"id": 99, "nome": "Novo User"},
    status_esperado=201,
    campos_obrigatorios=["id", "nome"]
)
print(f"  {r4}")

print("\n---\n")

print("=== FIM DA AULA ===")