"""Aula: Introdução a POO em Python"""

print("=== 1. O QUE E PROGRAMACAO ORIENTADA A OBJETOS ===")

# Até agora, escrevemos código procedural: funções soltas organizando a lógica
# POO agrupa DADOS e COMPORTAMENTOS relacionados em uma única estrutura: a classe

# Exemplo procedural (como fizemos até agora):
usuario_nome = "qa_admin"
usuario_email = "qa@empresa.com"
usuario_ativo = True

def exibir_usuario(nome, email, ativo):
    status = "ativo" if ativo else "inativo"
    return f"{nome} ({email}) - {status}"

print("Procedural:", exibir_usuario(usuario_nome, usuario_email, usuario_ativo))

# O problema: dados e funções ficam separados
# Quando o projeto cresce, fica difícil saber qual função opera sobre quais dados

print("\n---\n")

print("=== 2. CLASSES E OBJETOS ===")

# Classe = molde/template que define estrutura e comportamento
# Objeto = instância concreta criada a partir da classe

class Usuario:
    """Representa um usuário do sistema sob teste."""
    pass  # classe vazia por enquanto

# Criando objetos (instâncias)
usuario1 = Usuario()
usuario2 = Usuario()

print(f"usuario1: {usuario1}")
print(f"usuario2: {usuario2}")
print(f"São o mesmo objeto? {usuario1 is usuario2}")

# Cada objeto é independente, mesmo vindo da mesma classe

print("\n---\n")

print("=== 3. O METODO __INIT__ E O PARAMETRO SELF ===")

# __init__ é o construtor: executa automaticamente ao criar o objeto
# self é a referência ao próprio objeto sendo criado

class AmbienteTeste:
    """Representa um ambiente de teste (dev, hml, prod)."""

    def __init__(self, nome, url, ativo=True):
        self.nome = nome      # atributo de instância
        self.url = url         # atributo de instância
        self.ativo = ativo     # atributo com valor padrão

# Criando objetos com dados
dev = AmbienteTeste("dev", "https://dev.api.empresa.com")
hml = AmbienteTeste("hml", "https://hml.api.empresa.com")
prod = AmbienteTeste("prod", "https://api.empresa.com", ativo=False)

print(f"Ambiente: {dev.nome} | URL: {dev.url} | Ativo: {dev.ativo}")
print(f"Ambiente: {hml.nome} | URL: {hml.url} | Ativo: {hml.ativo}")
print(f"Ambiente: {prod.nome} | URL: {prod.url} | Ativo: {prod.ativo}")

print("\n---\n")

print("=== 4. METODOS DE INSTANCIA ===")

# Métodos são funções definidas dentro da classe
# Sempre recebem self como primeiro parâmetro

class CasoTeste:
    """Representa um caso de teste com nome, status e duração."""

    def __init__(self, nome, endpoint, metodo="GET"):
        self.nome = nome
        self.endpoint = endpoint
        self.metodo = metodo
        self.status = "pendente"
        self.duracao_ms = 0

    def executar(self, duracao_ms, sucesso=True):
        """Simula a execução do caso de teste."""
        self.duracao_ms = duracao_ms
        self.status = "passou" if sucesso else "falhou"

    def resumo(self):
        """Retorna string formatada com o resumo do teste."""
        return (
            f"[{self.status.upper()}] {self.metodo} {self.endpoint} "
            f"- {self.nome} ({self.duracao_ms}ms)"
        )

# Criando e usando objetos
teste_login = CasoTeste("Login válido", "/api/auth/login", "POST")
teste_perfil = CasoTeste("Buscar perfil", "/api/users/me")
teste_logout = CasoTeste("Logout", "/api/auth/logout", "POST")

# Executando testes
teste_login.executar(120, sucesso=True)
teste_perfil.executar(85, sucesso=True)
teste_logout.executar(200, sucesso=False)

# Exibindo resultados
print(teste_login.resumo())
print(teste_perfil.resumo())
print(teste_logout.resumo())

print("\n---\n")

print("=== 5. OBJETOS EM COLECOES ===")

# Objetos podem ser armazenados em listas, dicionários, etc.
# Isso conecta POO com tudo que já aprendemos sobre estruturas de dados

suite = [teste_login, teste_perfil, teste_logout]

print("Relatório da Suite:")
print("-" * 50)

total = len(suite)
passou = sum(1 for t in suite if t.status == "passou")
falhou = total - passou

for teste in suite:
    print(f"  {teste.resumo()}")

print("-" * 50)
print(f"Total: {total} | Passou: {passou} | Falhou: {falhou}")

print("\n---\n")

print("=== 6. COMPARACAO PROCEDURAL VS POO ===")

# PROCEDURAL: dados em dicionários, funções soltas
resultado_proc = {"nome": "Login", "status": "passou", "ms": 120}

def resumo_proc(r):
    return f"[{r['status'].upper()}] {r['nome']} ({r['ms']}ms)"

print("Procedural:", resumo_proc(resultado_proc))

# POO: dados e comportamento juntos no objeto
print("POO:       ", teste_login.resumo())

# Em projetos pequenos, não faz diferença
# Em projetos com dezenas de testes, a organização da POO escala melhor

print("\n---\n")

print("=== 7. APLICACAO PRATICA: VALIDADOR DE RESPOSTA API ===")

class RespostaAPI:
    """Representa uma resposta de API para validação."""

    def __init__(self, endpoint, status_code, corpo, tempo_ms):
        self.endpoint = endpoint
        self.status_code = status_code
        self.corpo = corpo
        self.tempo_ms = tempo_ms

    def is_sucesso(self):
        """Verifica se o status code indica sucesso (2xx)."""
        return 200 <= self.status_code < 300

    def is_lento(self, limite_ms=500):
        """Verifica se o tempo de resposta excede o limite."""
        return self.tempo_ms > limite_ms

    def tem_campo(self, campo):
        """Verifica se o corpo da resposta contém um campo específico."""
        return campo in self.corpo

    def validar(self, campo_obrigatorio=None, limite_ms=500):
        """Executa validação completa e retorna relatório."""
        problemas = []

        if not self.is_sucesso():
            problemas.append(f"Status {self.status_code} (esperado 2xx)")

        if self.is_lento(limite_ms):
            problemas.append(f"Lento: {self.tempo_ms}ms (limite: {limite_ms}ms)")

        if campo_obrigatorio and not self.tem_campo(campo_obrigatorio):
            problemas.append(f"Campo '{campo_obrigatorio}' ausente")

        status = "OK" if not problemas else "FALHA"
        return {
            "endpoint": self.endpoint,
            "status": status,
            "problemas": problemas,
        }


# Simulando respostas de API
respostas = [
    RespostaAPI("/api/users", 200, {"users": [], "total": 0}, 120),
    RespostaAPI("/api/products", 500, {"error": "internal"}, 2300),
    RespostaAPI("/api/orders", 200, {"items": []}, 80),
]

print("Validação de Respostas da API:")
print("-" * 50)

for resp in respostas:
    resultado = resp.validar(campo_obrigatorio="total", limite_ms=500)
    problemas_str = ", ".join(resultado["problemas"]) if resultado["problemas"] else "nenhum"
    print(f"  {resultado['endpoint']}: [{resultado['status']}] Problemas: {problemas_str}")

print("\n---\n")

print("=== FIM DA AULA ===")