"""Aula: Exceções e o bloco try/except em Python"""

print("=== 1. O QUE E UMA EXCECAO ===")

# Excecoes sao erros que acontecem durante a execucao do programa
# Em vez de travar tudo, Python "lanca" uma excecao que pode ser capturada

# Exemplo: tentar acessar uma chave que nao existe em um dicionario
resposta_api = {
    "status": 200,
    "body": {"usuario": "qa_tester"}
}

# Sem tratamento, isso quebraria o programa:
# print(resposta_api["token"])  # KeyError!

# Veja o que aconteceria com cada erro comum:
print("Erros mais comuns em automacao de testes:")
print("  KeyError     -> acessar chave inexistente em dict")
print("  TypeError    -> operacao com tipo errado")
print("  ValueError   -> valor invalido para a operacao")
print("  IndexError   -> indice fora do range em lista")
print("  FileNotFoundError -> arquivo nao encontrado")

print("\n---\n")

print("=== 2. BLOCO TRY E EXCEPT BASICO ===")

# Estrutura: tenta executar o bloco try
# Se der erro, executa o bloco except

# Cenario: extrair campo de resposta de API
def extrair_campo_resposta(resposta, campo):
    try:
        valor = resposta[campo]
        print(f"[OK] Campo '{campo}' encontrado: {valor}")
        return valor
    except KeyError:
        print(f"[ERRO] Campo '{campo}' nao existe na resposta")
        return None

# Resposta simulada de uma API de login
resposta_login = {
    "status_code": 200,
    "token": "abc123xyz",
    "usuario": "qa@empresa.com"
}

extrair_campo_resposta(resposta_login, "token")
extrair_campo_resposta(resposta_login, "status_code")
extrair_campo_resposta(resposta_login, "expiracao")  # Campo inexistente

print("\n---\n")

print("=== 3. CAPTURANDO EXCECOES ESPECIFICAS ===")

# Boas praticas: capturar a excecao mais especifica possivel
# Multiplos excepts para diferentes tipos de erro

def processar_status_code(valor):
    try:
        codigo = int(valor)           # Pode gerar ValueError
        categoria = {                 # Pode gerar KeyError
            2: "Sucesso",
            3: "Redirecionamento",
            4: "Erro do cliente",
            5: "Erro do servidor"
        }[codigo // 100]
        print(f"[OK] Codigo {codigo} -> {categoria}")
        return categoria
    except ValueError:
        print(f"[ERRO] '{valor}' nao e um numero valido")
        return None
    except KeyError:
        print(f"[ERRO] Codigo {valor} nao reconhecido")
        return None

# Testando com diferentes entradas
processar_status_code(200)
processar_status_code(404)
processar_status_code(500)
processar_status_code("abc")     # ValueError
processar_status_code(999)       # KeyError

print("\n---\n")

print("=== 4. EXCECOES PADRÃO MAIS COMUNS EM QA ===")

# --- KeyError: chave inexistente em dicionario ---
print(">>> KeyError:")
headers = {"Content-Type": "application/json", "Authorization": "Bearer xyz"}
try:
    token = headers["X-Api-Key"]
except KeyError as e:
    print(f"Header ausente: {e}")

# --- TypeError: tipo incompativel ---
print("\n>>> TypeError:")
try:
    total = "3" + 2  # Nao pode somar str com int
except TypeError as e:
    print(f"Tipo incompativel: {e}")

# --- ValueError: valor invalido ---
print("\n>>> ValueError:")
try:
    tempo_resposta = float("N/A")  # Nao converte para float
except ValueError as e:
    print(f"Valor invalido: {e}")

# --- IndexError: indice fora do range ---
print("\n>>> IndexError:")
resultados_suite = ["PASSOU", "PASSOU", "FALHOU"]
try:
    quinto = resultados_suite[10]
except IndexError as e:
    print(f"Indice invalido: {e}")

# --- FileNotFoundError: arquivo nao encontrado ---
print("\n>>> FileNotFoundError:")
try:
    with open("relatorio_inexistente.json", "r") as f:
        conteudo = f.read()
except FileNotFoundError as e:
    print(f"Arquivo nao encontrado: {e}")

print("\n---\n")

print("=== 5. CAPTURANDO A EXCECAO COMO VARIAVEL ===")

# Usar 'as e' permite inspecionar detalhes do erro
# Util para logging e mensagens de erro precisas

def carregar_massa_de_teste(arquivo):
    try:
        with open(arquivo, "r") as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"[FALHA] Arquivo de massa nao encontrado: {arquivo}")
        print(f"[DETALHE] {e}")
        return None
    except PermissionError as e:
        print(f"[FALHA] Sem permissao para ler: {arquivo}")
        print(f"[DETALHE] {e}")
        return None

carregar_massa_de_teste("usuarios_teste.csv")
carregar_massa_de_teste("dados_producao.csv")

print("\n---\n")

print("=== 6. EXCECAO GENERICA COMO ULTIMO RECURSO ===")

# Exception captura qualquer excecao — usar apenas como fallback
# Nunca usar sozinha como unica clausula except

def validar_resposta_completa(resposta):
    try:
        status = int(resposta["status"])
        corpo = resposta["body"]
        usuario = corpo["nome"]
        print(f"[OK] Resposta valida | status={status} | usuario={usuario}")
        return True
    except KeyError as e:
        print(f"[ERRO] Campo obrigatorio ausente: {e}")
        return False
    except (TypeError, ValueError) as e:
        print(f"[ERRO] Formato de dado invalido: {e}")
        return False
    except Exception as e:
        print(f"[ERRO] Falha inesperada: {type(e).__name__}: {e}")
        return False

# Resposta valida
validar_resposta_completa({
    "status": "200",
    "body": {"nome": "Ana QA"}
})

# Resposta com campo ausente
validar_resposta_completa({
    "status": "200",
    "body": {}
})

# Resposta com status invalido
validar_resposta_completa({
    "status": None,
    "body": {"nome": "Carlos"}
})

print("\n---\n")

print("=== FIM DA AULA ===")