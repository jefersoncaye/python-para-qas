"""Aula: Strings — Operações e Métodos em Python"""

print("=== 1. O QUE É UMA STRING ===")

# Strings são sequências de caracteres — texto entre aspas simples ou duplas
endpoint = "https://api.exemplo.com/v1/usuarios"
status_message = 'Not Found'
corpo_resposta = """{"id": 1, "nome": "João", "ativo": true}"""

print(f"Endpoint: {endpoint}")
print(f"Status: {status_message}")
print(f"Corpo: {corpo_resposta}")

# Strings são imutáveis — cada operação gera uma nova string
email = "QA@EMPRESA.COM"
email_normalizado = email.lower()
print(f"\nOriginal:    {email}")
print(f"Normalizado: {email_normalizado}")

print("\n---\n")

print("=== 2. ACESSO POR ÍNDICE E FATIAMENTO ===")

# Índices em Python começam no 0
#  H   T   T   P   /   1   .   1
#  0   1   2   3   4   5   6   7
# -8  -7  -6  -5  -4  -3  -2  -1

protocolo = "HTTP/1.1"
print(f"Protocolo completo: {protocolo}")
print(f"Primeiro caractere [0]:  {protocolo[0]}")
print(f"Último caractere [-1]:   {protocolo[-1]}")
print(f"Versão [5:]:             {protocolo[5:]}")
print(f"Protocolo até barra [:4]: {protocolo[:4]}")

# Fatiamento em respostas de API — QA usa muito para validar prefixos/sufixos
token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
tipo_auth = token[:6]
print(f"\nToken recebido: {token[:30]}...")
print(f"Tipo de autenticação: {tipo_auth}")

print("\n---\n")

print("=== 3. OPERAÇÕES COM STRINGS ===")

# Concatenação com +
metodo = "GET"
rota = "/usuarios"
versao = "/v1"
url_completa = metodo + " " + versao + rota
print(f"Requisição montada: {url_completa}")

# Repetição com *
separador = "-" * 40
print(separador)

# Verificação de conteúdo com 'in'
corpo = '{"status": "error", "message": "Token expirado"}'
print(f"\nCorpo da resposta: {corpo}")
print(f"Contém 'error':         {'error' in corpo}")
print(f"Contém 'Token expirado': {'Token expirado' in corpo}")
print(f"Contém 'success':       {'success' in corpo}")

# len() — comprimento da string
senha_teste = "abc123"
print(f"\nSenha testada: '{senha_teste}'")
print(f"Comprimento:   {len(senha_teste)} caracteres")
print(f"Senha válida (mín. 8): {len(senha_teste) >= 8}")

print("\n---\n")

print("=== 4. MÉTODOS DE BUSCA E VERIFICAÇÃO ===")

log_erro = "  ERROR 2024-01-15 | NullPointerException na linha 42  "

# startswith / endswith — verificar prefixo e sufixo
linha_log = "ERROR: falha na autenticação do usuário"
print(f"Log: '{linha_log}'")
print(f"Começa com ERROR:    {linha_log.startswith('ERROR')}")
print(f"Começa com WARNING:  {linha_log.startswith('WARNING')}")
print(f"Termina com 'usuário': {linha_log.endswith('usuário')}")

# find() e count() — localizar e contar ocorrências
resposta_api = "user_id=42&status=active&role=admin&status=pending"
print(f"\nQuery string: {resposta_api}")
print(f"Posição de 'status':        {resposta_api.find('status')}")
print(f"Ocorrências de 'status':    {resposta_api.count('status')}")
print(f"Ocorrências de 'role':      {resposta_api.count('role')}")

# find() retorna -1 quando não encontra — útil em asserts
campo = "email"
print(f"\n'email' presente na resposta: {resposta_api.find(campo) != -1}")

print("\n---\n")

print("=== 5. MÉTODOS DE TRANSFORMAÇÃO ===")

# strip() — remover espaços e caracteres indesejados
email_digitado = "  usuario@teste.com  "
print(f"Email bruto:     '{email_digitado}'")
print(f"Após strip():    '{email_digitado.strip()}'")
print(f"Após lstrip():   '{email_digitado.lstrip()}'")
print(f"Após rstrip():   '{email_digitado.rstrip()}'")

# upper / lower / title — normalização de dados
ambiente = "PRODUCAO"
nome_usuario = "maria silva"
print(f"\nAmbiente recebido:  '{ambiente}'")
print(f"Normalizado lower:  '{ambiente.lower()}'")
print(f"\nNome recebido:  '{nome_usuario}'")
print(f"Capitalizado:   '{nome_usuario.title()}'")

# replace() — substituição de valores
url_template = "https://api.exemplo.com/v1/{recurso}/{id}"
url_usuarios = url_template.replace("{recurso}", "usuarios").replace("{id}", "99")
print(f"\nTemplate: {url_template}")
print(f"URL real:  {url_usuarios}")

print("\n---\n")

print("=== 6. SPLIT E JOIN ===")

# split() — dividir string em lista
# Muito usado para processar CSV, query strings, logs, headers
csv_linha = "id,nome,email,perfil,status"
campos = csv_linha.split(",")
print(f"Linha CSV:  {csv_linha}")
print(f"Campos:     {campos}")
print(f"Total de campos: {len(campos)}")

# Validar header de resposta CSV
cabecalhos_esperados = ["id", "nome", "email", "perfil", "status"]
print(f"Cabeçalhos corretos: {campos == cabecalhos_esperados}")

# split() com query string
query = "env=hml&versao=2&debug=true"
params = {}
for par in query.split("&"):
    chave, valor = par.split("=")
    params[chave] = valor
print(f"\nQuery string:    {query}")
print(f"Parâmetros:      {params}")

# join() — unir lista em string
ambientes = ["dev", "hml", "prod"]
print(f"\nAmbientes:              {ambientes}")
print(f"Formatado com vírgula:  {', '.join(ambientes)}")
print(f"Formatado com barra:    {' | '.join(ambientes)}")

# Reconstruir URL a partir de segmentos
segmentos = ["https://api.exemplo.com", "v2", "pedidos", "status"]
url = "/".join(segmentos)
print(f"\nSegmentos: {segmentos}")
print(f"URL montada: {url}")

print("\n---\n")

print("=== 7. APLICAÇÃO PRÁTICA — VALIDAÇÕES DE QA ===")

# Cenário 1: Validar Content-Type de uma resposta HTTP
def validar_content_type(header_value, esperado="application/json"):
    return esperado in header_value.lower()

header = "application/json; charset=utf-8"
print(f"Content-Type recebido: {header}")
print(f"É JSON: {validar_content_type(header)}")

# Cenário 2: Extrair e validar código de status de um log
linha_log = "2024-01-15 14:32:01 | POST /login | 401 | 120ms"
partes = linha_log.split(" | ")
status_code = partes[2].strip()
print(f"\nLog de requisição: {linha_log}")
print(f"Status extraído:   {status_code}")
print(f"É falha de auth:   {status_code == '401'}")

# Cenário 3: Normalizar e validar email antes de enviar ao endpoint
def normalizar_email(email_bruto):
    return email_bruto.strip().lower()

emails_teste = ["  Admin@Empresa.COM  ", "usuario@teste.com", "  QA@CORP.BR"]
print(f"\nEmails normalizados:")
for e in emails_teste:
    normalizado = normalizar_email(e)
    tem_arroba = "@" in normalizado
    tem_dominio = "." in normalizado.split("@")[-1] if tem_arroba else False
    print(f"  '{e.strip()}' -> '{normalizado}' | válido: {tem_arroba and tem_dominio}")

print("\n---\n")

print("=== RESUMO DOS MÉTODOS VISTOS ===")

resumo = {
    "Acesso":         ["[index]", "[-index]", "[start:end]"],
    "Operações":      ["+ (concatenar)", "* (repetir)", "in (verificar)"],
    "Busca":          ["startswith()", "endswith()", "find()", "count()"],
    "Transformação":  ["strip()", "lower()", "upper()", "title()", "replace()"],
    "Divisão/União":  ["split()", "join()"],
}

for categoria, metodos in resumo.items():
    print(f"  {categoria}: {', '.join(metodos)}")

print("\n=== FIM DA AULA ===")