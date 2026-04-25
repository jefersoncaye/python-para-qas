"""Aula: Criação e Uso de Funções em Python"""

print("=== 1. O QUE É UMA FUNÇÃO ===")

# Uma função é um bloco de código reutilizável que executa uma tarefa específica
# Em QA, funções evitam repetição de código nos testes

# Sintaxe básica: def nome_da_funcao():
def exibir_separador():
    print("-" * 40)

# Chamando a função
exibir_separador()
print("Relatório de Testes")
exibir_separador()

print("\n---\n")

print("=== 2. FUNÇÕES COM PARÂMETROS ===")

# Parâmetros permitem que a função receba dados externos
def exibir_status_teste(nome_teste, status):
    print(f"Teste: {nome_teste} | Status: {status}")

exibir_status_teste("Login com credenciais válidas", "PASSOU")
exibir_status_teste("Login com senha incorreta", "PASSOU")
exibir_status_teste("Login sem preencher email", "FALHOU")

print()

# Função com parâmetro usado em lógica interna
def classificar_status_code(codigo):
    if 200 <= codigo < 300:
        print(f"Status {codigo}: Sucesso")
    elif 400 <= codigo < 500:
        print(f"Status {codigo}: Erro do cliente")
    elif 500 <= codigo < 600:
        print(f"Status {codigo}: Erro do servidor")
    else:
        print(f"Status {codigo}: Código não classificado")

classificar_status_code(200)
classificar_status_code(404)
classificar_status_code(500)

print("\n---\n")

print("=== 3. FUNÇÕES COM RETORNO ===")

# Funções podem retornar valores com a palavra-chave return
def calcular_taxa_sucesso(total, aprovados):
    if total == 0:
        return 0
    taxa = (aprovados / total) * 100
    return taxa

# O valor retornado pode ser armazenado em uma variável
taxa_login = calcular_taxa_sucesso(10, 8)
taxa_cadastro = calcular_taxa_sucesso(5, 5)
taxa_checkout = calcular_taxa_sucesso(8, 3)

print(f"Taxa de sucesso - Login: {taxa_login}%")
print(f"Taxa de sucesso - Cadastro: {taxa_cadastro}%")
print(f"Taxa de sucesso - Checkout: {taxa_checkout}%")

print()

# Função que retorna um dado processado
def gerar_email_teste(nome, dominio="qatest.com"):
    email = f"{nome.lower().replace(' ', '.')}@{dominio}"
    return email

email1 = gerar_email_teste("João Silva")
email2 = gerar_email_teste("Maria Souza")
email3 = gerar_email_teste("Ana Costa", "empresa.com.br")

print(f"Email gerado: {email1}")
print(f"Email gerado: {email2}")
print(f"Email gerado: {email3}")

print("\n---\n")

print("=== 4. FUNÇÕES SEM RETORNO (NONE) ===")

# Quando uma função não tem return, ela retorna None automaticamente
def logar_acao(acao):
    print(f"[LOG] Ação executada: {acao}")

resultado = logar_acao("Clicou no botão Salvar")
print(f"Retorno da função logar_acao: {resultado}")
print(f"Tipo do retorno: {type(resultado)}")

print()

# return sem valor também retorna None
def validar_campo_obrigatorio(campo, valor):
    if not valor:
        print(f"[ERRO] Campo '{campo}' está vazio!")
        return  # Encerra a função aqui
    print(f"[OK] Campo '{campo}' preenchido: {valor}")

validar_campo_obrigatorio("Nome", "João")
validar_campo_obrigatorio("Email", "")
validar_campo_obrigatorio("Telefone", "49999990000")

print("\n---\n")

print("=== 5. ESCOPO DE VARIÁVEIS ===")

# Variáveis criadas dentro da função existem apenas ali (escopo local)
ambiente_global = "produção"

def configurar_teste():
    ambiente_local = "homologação"
    print(f"Dentro da função: ambiente_local = {ambiente_local}")
    print(f"Dentro da função: ambiente_global = {ambiente_global}")

configurar_teste()
print(f"Fora da função: ambiente_global = {ambiente_global}")

# Tentar acessar ambiente_local fora da função causaria erro:
# print(ambiente_local)  # NameError: name 'ambiente_local' is not defined

print()

# Variáveis com mesmo nome em escopos diferentes
url_base = "https://api.producao.com"

def obter_url_teste():
    url_base = "https://api.homologacao.com"  # Variável local, não altera a global
    print(f"URL dentro da função: {url_base}")

obter_url_teste()
print(f"URL fora da função: {url_base}")

print("\n---\n")

print("=== 6. CHAMANDO FUNÇÕES DENTRO DE FUNÇÕES ===")

# Funções podem chamar outras funções para organizar o código
def formatar_resultado(nome, status):
    icone = "✅" if status == "PASSOU" else "❌"
    return f"{icone} {nome}: {status}"

def gerar_relatorio_suite(nome_suite, resultados):
    print(f"\n📋 Suite: {nome_suite}")
    print("=" * 40)
    for teste, status in resultados:
        linha = formatar_resultado(teste, status)  # Chamando outra função
        print(f"  {linha}")

    total = len(resultados)
    aprovados = sum(1 for _, s in resultados if s == "PASSOU")
    taxa = calcular_taxa_sucesso(total, aprovados)  # Reutilizando função anterior
    print(f"\n  Taxa de sucesso: {taxa}%")

# Usando a função com dados de teste
testes_login = [
    ("Login válido", "PASSOU"),
    ("Login inválido", "PASSOU"),
    ("Login sem senha", "FALHOU"),
    ("Login bloqueado", "PASSOU"),
]

testes_cadastro = [
    ("Cadastro completo", "PASSOU"),
    ("Cadastro sem email", "PASSOU"),
    ("Cadastro duplicado", "FALHOU"),
]

gerar_relatorio_suite("Login", testes_login)
gerar_relatorio_suite("Cadastro", testes_cadastro)

print("\n---\n")

print("=== 7. BOAS PRÁTICAS AO CRIAR FUNÇÕES ===")

# 1. Nomes descritivos que indicam a ação
def verificar_status_code(codigo):  # Bom: diz o que faz
    return 200 <= codigo < 300

# 2. Cada função faz UMA coisa
def extrair_dominio(email):
    return email.split("@")[1]

def validar_dominio_permitido(email, dominios_permitidos):
    dominio = extrair_dominio(email)
    return dominio in dominios_permitidos

# 3. Funções pequenas e focadas facilitam testes e manutenção
dominios = ["qatest.com", "empresa.com.br"]

print(f"Status 200 é sucesso? {verificar_status_code(200)}")
print(f"Status 404 é sucesso? {verificar_status_code(404)}")
print()
print(f"Domínio de 'qa@qatest.com': {extrair_dominio('qa@qatest.com')}")
print(f"'qa@qatest.com' permitido? {validar_dominio_permitido('qa@qatest.com', dominios)}")
print(f"'hacker@evil.com' permitido? {validar_dominio_permitido('hacker@evil.com', dominios)}")

print("\n---\n")

print("=== FIM DA AULA ===")