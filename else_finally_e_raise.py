"""Aula: else, finally, raise e boas práticas em exceções"""

print("=== 1. BLOCO ELSE NO TRY/EXCEPT ===")

# O bloco else executa APENAS se nenhuma excecao ocorreu no try
# Util para separar o codigo de "sucesso" do codigo de "tratamento de erro"

def consultar_endpoint(url, dados):
    try:
        # Simulando validacao da URL
        if not url.startswith("http"):
            raise ValueError(f"URL invalida: {url}")
        if not dados:
            raise ValueError("Payload vazio nao permitido")
        resultado = {"status": 200, "body": "OK"}
    except ValueError as e:
        print(f"[ERRO] Validacao falhou: {e}")
        return None
    else:
        # So executa se o try passou sem erros
        print(f"[OK] Requisicao enviada para {url}")
        print(f"[OK] Status: {resultado['status']}")
        return resultado

# Testes
consultar_endpoint("https://api.empresa.com/login", {"user": "qa"})
consultar_endpoint("api.empresa.com/login", {"user": "qa"})   # URL invalida
consultar_endpoint("https://api.empresa.com/login", {})        # Payload vazio

print("\n---\n")

print("=== 2. BLOCO FINALLY ===")

# O bloco finally SEMPRE executa, independente de erro ou sucesso
# Ideal para: fechar arquivos, encerrar conexoes, limpar recursos, logs de encerramento

def executar_suite_testes(nome_suite, testes):
    print(f"\n[INICIO] Suite: {nome_suite}")
    aprovados = 0
    try:
        for nome, fn in testes:
            resultado = fn()
            if resultado:
                aprovados += 1
                print(f"  [PASSOU] {nome}")
            else:
                print(f"  [FALHOU] {nome}")
        if aprovados == 0:
            raise RuntimeError("Nenhum teste passou na suite")
    except RuntimeError as e:
        print(f"[CRITICO] {e}")
    finally:
        # Sempre executa — ideal para teardown
        total = len(testes)
        print(f"[ENCERRAMENTO] Suite '{nome_suite}' finalizada: {aprovados}/{total} passaram")

# Funcoes de teste simuladas
testes_api = [
    ("GET /usuarios retorna 200",   lambda: True),
    ("POST /login com dados validos", lambda: True),
    ("GET /recurso sem auth retorna 401", lambda: False),
    ("DELETE /usuario retorna 204", lambda: True),
]

testes_vazios = [
    ("Teste que sempre falha", lambda: False),
]

executar_suite_testes("Autenticacao e Usuarios", testes_api)
executar_suite_testes("Suite com falha total", testes_vazios)

print("\n---\n")

print("=== 3. RAISE: RELANCANDO E LANCANDO EXCECOES ===")

# raise permite lancar uma excecao manualmente
# Usado quando voce detecta uma condicao de erro que o Python nao detectaria sozinho

def validar_status_code(codigo):
    if not isinstance(codigo, int):
        raise TypeError(f"Status code deve ser int, recebeu {type(codigo).__name__}")
    if codigo < 100 or codigo > 599:
        raise ValueError(f"Status code fora do range HTTP valido: {codigo}")
    return True

# Testando o raise
for codigo in [200, 404, "200", 999, 500]:
    try:
        validar_status_code(codigo)
        print(f"[OK] Status {codigo} valido")
    except (TypeError, ValueError) as e:
        print(f"[ERRO] {e}")

print()

# Relancando excecao apos logar
def processar_resposta(json_resposta):
    try:
        return json_resposta["data"]["resultado"]
    except KeyError as e:
        print(f"[LOG] Estrutura inesperada na resposta: {e}")
        raise  # Relanca a mesma excecao para quem chamou tratar

try:
    processar_resposta({"data": {}})
except KeyError:
    print("[CALLER] Capturou o erro relancado e abortou o teste")

print("\n---\n")

print("=== 4. BOAS PRATICAS EM EXCECOES ===")

# --- MAU USO: except generico sem tipo ---
print(">>> Antipadrao: except vazio (nao faca isso)")

def buscar_usuario_ruim(usuarios, email):
    try:
        return next(u for u in usuarios if u["email"] == email)
    except:  # Captura TUDO, incluindo KeyboardInterrupt e SystemExit
        return None

# --- BOM USO: especifico e informativo ---
print(">>> Bom padrao: excecao especifica + mensagem util")

def buscar_usuario(usuarios, email):
    try:
        usuario = next(
            (u for u in usuarios if u.get("email") == email),
            None
        )
        if usuario is None:
            raise LookupError(f"Usuario '{email}' nao encontrado na massa de teste")
        return usuario
    except LookupError as e:
        print(f"[AVISO] {e}")
        return None
    except (TypeError, StopIteration) as e:
        print(f"[ERRO] Problema ao buscar usuario: {e}")
        return None

# Massa de teste
usuarios = [
    {"email": "qa1@empresa.com", "perfil": "admin"},
    {"email": "qa2@empresa.com", "perfil": "viewer"},
]

resultado = buscar_usuario(usuarios, "qa1@empresa.com")
print(f"Encontrado: {resultado}")

resultado = buscar_usuario(usuarios, "inexistente@empresa.com")
print(f"Encontrado: {resultado}")

print()

# --- Nunca usar excecao para controle de fluxo normal ---
print(">>> Antipadrao: usar excecao como if/else")

def verificar_admin_ruim(usuario):
    try:
        assert usuario["perfil"] == "admin"
        return True
    except AssertionError:
        return False

print(">>> Bom padrao: verificacao direta")

def verificar_admin(usuario):
    return usuario.get("perfil") == "admin"

print(f"qa1 e admin? {verificar_admin(usuarios[0])}")
print(f"qa2 e admin? {verificar_admin(usuarios[1])}")

print("\n---\n")

print("=== 5. ESTRUTURA COMPLETA TRY/EXCEPT/ELSE/FINALLY ===")

# Exemplo unificando todos os blocos em um cenario de QA real

def executar_requisicao_simulada(endpoint, payload, simular_erro=False):
    print(f"\n[TESTE] {endpoint}")
    conexao_aberta = False
    try:
        # Abrindo "conexao"
        conexao_aberta = True
        print(f"  [CONN] Conexao aberta")

        if simular_erro:
            raise ConnectionError("Timeout ao conectar ao servidor")

        if not payload.get("token"):
            raise ValueError("Token de autorizacao ausente no payload")

        resposta = {"status": 200, "body": "Autenticado com sucesso"}

    except ConnectionError as e:
        print(f"  [FALHA] Erro de rede: {e}")
        return None
    except ValueError as e:
        print(f"  [FALHA] Payload invalido: {e}")
        return None
    else:
        print(f"  [OK] Resposta: {resposta['status']} - {resposta['body']}")
        return resposta
    finally:
        if conexao_aberta:
            print(f"  [CONN] Conexao encerrada")

executar_requisicao_simulada(
    "POST /api/autenticar",
    {"token": "Bearer abc123"}
)

executar_requisicao_simulada(
    "POST /api/autenticar",
    {"usuario": "qa@empresa.com"}  # Sem token
)

executar_requisicao_simulada(
    "POST /api/autenticar",
    {"token": "Bearer abc123"},
    simular_erro=True
)

print("\n---\n")

print("=== FIM DA AULA ===")