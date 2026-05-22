"""Aula: Composição e Dataclasses em Python"""

print("=== 1. O QUE E COMPOSICAO ===")

# Composição: um objeto CONTÉM outros objetos como atributos
# Diferente de herança ("É UM"), composição modela "TEM UM"
# Suite TEM testes, Relatório TEM resultados

class ResultadoTeste:
    """Representa o resultado de um único teste."""

    def __init__(self, nome, status, duracao_ms):
        self.nome = nome
        self.status = status  # "passou", "falhou", "bloqueado"
        self.duracao_ms = duracao_ms"""Aula: Composição e Dataclasses em Python"""

print("=== 1. O QUE E COMPOSICAO ===")

# Composição: um objeto CONTÉM outros objetos como atributos
# Diferente de herança ("É UM"), composição modela "TEM UM"
# Suite TEM testes, Relatório TEM resultados

class ResultadoTeste:
    """Representa o resultado de um único teste."""

    def __init__(self, nome, status, duracao_ms):
        self.nome = nome
        self.status = status  # "passou", "falhou", "bloqueado"
        self.duracao_ms = duracao_ms

    def __str__(self):
        return f"[{self.status.upper()}] {self.nome} ({self.duracao_ms}ms)"


class SuiteTeste:
    """Suite que CONTÉM resultados de testes (composição)."""

    def __init__(self, nome):
        self.nome = nome
        self._resultados = []  # lista de objetos ResultadoTeste

    def adicionar(self, resultado):
        """Adiciona um ResultadoTeste à suite."""
        self._resultados.append(resultado)

    @property
    def total(self):
        return len(self._resultados)

    @property
    def passou(self):
        return sum(1 for r in self._resultados if r.status == "passou")

    @property
    def falhou(self):
        return sum(1 for r in self._resultados if r.status == "falhou")

    @property
    def duracao_total_ms(self):
        return sum(r.duracao_ms for r in self._resultados)

    @property
    def taxa_sucesso(self):
        if self.total == 0:
            return 0.0
        return round((self.passou / self.total) * 100, 1)

    def relatorio(self):
        """Gera relatório completo da suite."""
        linhas = [f"Suite: {self.nome}", "-" * 50]
        for r in self._resultados:
            linhas.append(f"  {r}")
        linhas.append("-" * 50)
        linhas.append(
            f"Total: {self.total} | Passou: {self.passou} | "
            f"Falhou: {self.falhou} | Taxa: {self.taxa_sucesso}% | "
            f"Duração: {self.duracao_total_ms}ms"
        )
        return "\n".join(linhas)


# Usando composição
suite = SuiteTeste("Smoke Test - API Auth")
suite.adicionar(ResultadoTeste("Login válido", "passou", 120))
suite.adicionar(ResultadoTeste("Login inválido", "passou", 95))
suite.adicionar(ResultadoTeste("Token expirado", "falhou", 200))
suite.adicionar(ResultadoTeste("Logout", "passou", 80))

print(suite.relatorio())

print("\n---\n")

print("=== 2. COMPOSICAO VS HERANCA ===")

# Herança: TesteAPI É UM Teste (relação vertical)
# Composição: Suite TEM Testes (relação horizontal)

# Composição é mais flexível: você pode trocar os componentes em runtime

class Ambiente:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

    def __str__(self):
        return f"{self.nome} ({self.url})"


class ConfigExecucao:
    """Configuração que CONTÉM um ambiente e uma suite."""

    def __init__(self, ambiente, suite, paralelo=False):
        self.ambiente = ambiente    # objeto Ambiente
        self.suite = suite          # objeto SuiteTeste
        self.paralelo = paralelo

    def resumo(self):
        modo = "paralelo" if self.paralelo else "sequencial"
        return (
            f"Execução: {self.suite.nome}\n"
            f"Ambiente: {self.ambiente}\n"
            f"Modo: {modo}\n"
            f"Testes: {self.suite.total}"
        )


amb_hml = Ambiente("hml", "https://hml.api.empresa.com")
config = ConfigExecucao(amb_hml, suite, paralelo=True)
print(config.resumo())

# Trocar ambiente em runtime (flexibilidade da composição)
amb_prod = Ambiente("prod", "https://api.empresa.com")
config.ambiente = amb_prod
print(f"\nAmbiente trocado para: {config.ambiente}")

print("\n---\n")

print("=== 3. COMPOSICAO COM MULTIPLOS NIVEIS ===")

# Objetos dentro de objetos dentro de objetos

class Endpoint:
    def __init__(self, caminho, metodo="GET"):
        self.caminho = caminho
        self.metodo = metodo

    def __str__(self):
        return f"{self.metodo} {self.caminho}"


class Requisicao:
    """CONTÉM um Endpoint, headers e corpo."""

    def __init__(self, endpoint, headers=None, corpo=None):
        self.endpoint = endpoint    # objeto Endpoint
        self.headers = headers or {}
        self.corpo = corpo

    def __str__(self):
        auth = "com auth" if "Authorization" in self.headers else "sem auth"
        return f"{self.endpoint} ({auth})"


class CasoTesteAPI:
    """CONTÉM uma Requisição e validações esperadas."""

    def __init__(self, nome, requisicao, status_esperado=200):
        self.nome = nome
        self.requisicao = requisicao    # objeto Requisicao
        self.status_esperado = status_esperado

    def __str__(self):
        return f"{self.nome}: {self.requisicao} -> espera {self.status_esperado}"


# Construindo de dentro para fora
endpoint = Endpoint("/api/users", "POST")
headers = {"Authorization": "Bearer token123", "Content-Type": "application/json"}
corpo = {"nome": "QA User", "email": "qa@empresa.com"}

requisicao = Requisicao(endpoint, headers, corpo)
caso = CasoTesteAPI("Criar usuário", requisicao, 201)

print(caso)
print(f"  Endpoint: {caso.requisicao.endpoint}")
print(f"  Método: {caso.requisicao.endpoint.metodo}")
print(f"  Auth: {caso.requisicao.headers.get('Authorization', 'nenhum')}")

print("\n---\n")

print("=== 4. DATACLASSES ===")

# Dataclasses simplificam a criação de classes que guardam dados
# Python gera __init__, __repr__ e __eq__ automaticamente

from dataclasses import dataclass, field

@dataclass
class Usuario:
    nome: str
    email: str
    perfil: str = "viewer"     # valor padrão
    ativo: bool = True         # valor padrão

# Python gera o __init__ automaticamente:
# def __init__(self, nome, email, perfil="viewer", ativo=True)

u1 = Usuario("Ana QA", "ana@empresa.com", "admin")
u2 = Usuario("Carlos Dev", "carlos@empresa.com")
u3 = Usuario("Ana QA", "ana@empresa.com", "admin")

# __repr__ gerado automaticamente
print(u1)
print(u2)

# __eq__ gerado automaticamente (compara todos os campos)
print(f"\nu1 == u3? {u1 == u3}")  # True (mesmos valores)
print(f"u1 == u2? {u1 == u2}")    # False

print("\n---\n")

print("=== 5. DATACLASSES COM FIELD E VALORES COMPUTADOS ===")

from dataclasses import dataclass, field
from typing import Optional

@dataclass
class RespostaAPI:
    endpoint: str
    status_code: int
    corpo: dict
    tempo_ms: float
    headers: dict = field(default_factory=dict)  # mutável precisa de field()

    @property
    def sucesso(self):
        """Calculado a partir do status_code."""
        return 200 <= self.status_code < 300

    @property
    def lento(self):
        """Calculado a partir do tempo."""
        return self.tempo_ms > 500

    def resumo(self):
        status = "OK" if self.sucesso else "ERRO"
        velocidade = " [LENTO]" if self.lento else ""
        return f"[{status}] {self.endpoint} -> {self.status_code} ({self.tempo_ms}ms){velocidade}"


respostas = [
    RespostaAPI("/api/users", 200, {"total": 5}, 120.5),
    RespostaAPI("/api/products", 500, {"error": "internal"}, 2300.0),
    RespostaAPI("/api/orders", 200, {"items": []}, 80.2),
]

print("Validação de respostas:")
for r in respostas:
    print(f"  {r.resumo()}")

# __repr__ mostra todos os campos para debug
print(f"\nDebug: {respostas[0]!r}")

print("\n---\n")

print("=== 6. DATACLASSES COMO MASSA DE TESTE ===")

@dataclass
class CredencialTeste:
    usuario: str
    senha: str
    esperado: str       # "sucesso" ou "erro"
    descricao: str = ""

# Massa de teste limpa e tipada
massa_login = [
    CredencialTeste("admin@empresa.com", "Admin123!", "sucesso", "Admin válido"),
    CredencialTeste("user@empresa.com", "User456!", "sucesso", "User válido"),
    CredencialTeste("admin@empresa.com", "errada", "erro", "Senha incorreta"),
    CredencialTeste("", "qualquer", "erro", "Email vazio"),
    CredencialTeste("invalido", "qualquer", "erro", "Email sem @"),
]

print("Massa de teste para Login:")
print(f"{'Descrição':<20} {'Usuário':<25} {'Esperado':<10}")
print("-" * 55)
for c in massa_login:
    print(f"{c.descricao:<20} {c.usuario:<25} {c.esperado:<10}")

# Filtrar cenários de erro
erros = [c for c in massa_login if c.esperado == "erro"]
print(f"\nCenários de erro: {len(erros)}")

print("\n---\n")

print("=== 7. APLICACAO PRATICA: RELATORIO COMPOSTO ===")

@dataclass
class ItemRelatorio:
    teste: str
    status: str
    duracao_ms: float
    detalhes: str = ""


class RelatorioExecucao:
    """Relatório que CONTÉM itens e um ambiente (composição + dataclass)."""

    def __init__(self, nome, ambiente):
        self.nome = nome
        self.ambiente = ambiente      # objeto Ambiente
        self._itens = []              # lista de ItemRelatorio (dataclass)

    def adicionar(self, item):
        self._itens.append(item)

    @property
    def total(self):
        return len(self._itens)

    @property
    def taxa_sucesso(self):
        if self.total == 0:
            return 0.0
        ok = sum(1 for i in self._itens if i.status == "passou")
        return round((ok / self.total) * 100, 1)

    def gerar(self):
        linhas = [
            f"RELATÓRIO: {self.nome}",
            f"Ambiente: {self.ambiente}",
            "=" * 60,
        ]
        for item in self._itens:
            detalhe = f" | {item.detalhes}" if item.detalhes else ""
            linhas.append(
                f"  [{item.status.upper():<7}] {item.teste} "
                f"({item.duracao_ms}ms){detalhe}"
            )
        linhas.append("=" * 60)
        linhas.append(f"Total: {self.total} | Taxa de sucesso: {self.taxa_sucesso}%")
        return "\n".join(linhas)


# Montando o relatório
relatorio = RelatorioExecucao("Sprint 15 - Regressão", amb_hml)
relatorio.adicionar(ItemRelatorio("Login POST", "passou", 120))
relatorio.adicionar(ItemRelatorio("Listar users GET", "passou", 85))
relatorio.adicionar(ItemRelatorio("Criar order POST", "falhou", 800, "Timeout no banco"))
relatorio.adicionar(ItemRelatorio("Health check GET", "passou", 45))

print(relatorio.gerar())

print("\n---\n")

print("=== FIM DA AULA ===")

    def __str__(self):
        return f"[{self.status.upper()}] {self.nome} ({self.duracao_ms}ms)"


class SuiteTeste:
    """Suite que CONTÉM resultados de testes (composição)."""

    def __init__(self, nome):
        self.nome = nome
        self._resultados = []  # lista de objetos ResultadoTeste

    def adicionar(self, resultado):
        """Adiciona um ResultadoTeste à suite."""
        self._resultados.append(resultado)

    @property
    def total(self):
        return len(self._resultados)

    @property
    def passou(self):
        return sum(1 for r in self._resultados if r.status == "passou")

    @property
    def falhou(self):
        return sum(1 for r in self._resultados if r.status == "falhou")

    @property
    def duracao_total_ms(self):
        return sum(r.duracao_ms for r in self._resultados)

    @property
    def taxa_sucesso(self):
        if self.total == 0:
            return 0.0
        return round((self.passou / self.total) * 100, 1)

    def relatorio(self):
        """Gera relatório completo da suite."""
        linhas = [f"Suite: {self.nome}", "-" * 50]
        for r in self._resultados:
            linhas.append(f"  {r}")
        linhas.append("-" * 50)
        linhas.append(
            f"Total: {self.total} | Passou: {self.passou} | "
            f"Falhou: {self.falhou} | Taxa: {self.taxa_sucesso}% | "
            f"Duração: {self.duracao_total_ms}ms"
        )
        return "\n".join(linhas)


# Usando composição
suite = SuiteTeste("Smoke Test - API Auth")
suite.adicionar(ResultadoTeste("Login válido", "passou", 120))
suite.adicionar(ResultadoTeste("Login inválido", "passou", 95))
suite.adicionar(ResultadoTeste("Token expirado", "falhou", 200))
suite.adicionar(ResultadoTeste("Logout", "passou", 80))

print(suite.relatorio())

print("\n---\n")

print("=== 2. COMPOSICAO VS HERANCA ===")

# Herança: TesteAPI É UM Teste (relação vertical)
# Composição: Suite TEM Testes (relação horizontal)

# Composição é mais flexível: você pode trocar os componentes em runtime

class Ambiente:
    def __init__(self, nome, url):
        self.nome = nome
        self.url = url

    def __str__(self):
        return f"{self.nome} ({self.url})"


class ConfigExecucao:
    """Configuração que CONTÉM um ambiente e uma suite."""

    def __init__(self, ambiente, suite, paralelo=False):
        self.ambiente = ambiente    # objeto Ambiente
        self.suite = suite          # objeto SuiteTeste
        self.paralelo = paralelo

    def resumo(self):
        modo = "paralelo" if self.paralelo else "sequencial"
        return (
            f"Execução: {self.suite.nome}\n"
            f"Ambiente: {self.ambiente}\n"
            f"Modo: {modo}\n"
            f"Testes: {self.suite.total}"
        )


amb_hml = Ambiente("hml", "https://hml.api.empresa.com")
config = ConfigExecucao(amb_hml, suite, paralelo=True)
print(config.resumo())

# Trocar ambiente em runtime (flexibilidade da composição)
amb_prod = Ambiente("prod", "https://api.empresa.com")
config.ambiente = amb_prod
print(f"\nAmbiente trocado para: {config.ambiente}")

print("\n---\n")

print("=== 3. COMPOSICAO COM MULTIPLOS NIVEIS ===")

# Objetos dentro de objetos dentro de objetos

class Endpoint:
    def __init__(self, caminho, metodo="GET"):
        self.caminho = caminho
        self.metodo = metodo

    def __str__(self):
        return f"{self.metodo} {self.caminho}"


class Requisicao:
    """CONTÉM um Endpoint, headers e corpo."""

    def __init__(self, endpoint, headers=None, corpo=None):
        self.endpoint = endpoint    # objeto Endpoint
        self.headers = headers or {}
        self.corpo = corpo

    def __str__(self):
        auth = "com auth" if "Authorization" in self.headers else "sem auth"
        return f"{self.endpoint} ({auth})"


class CasoTesteAPI:
    """CONTÉM uma Requisição e validações esperadas."""

    def __init__(self, nome, requisicao, status_esperado=200):
        self.nome = nome
        self.requisicao = requisicao    # objeto Requisicao
        self.status_esperado = status_esperado

    def __str__(self):
        return f"{self.nome}: {self.requisicao} -> espera {self.status_esperado}"


# Construindo de dentro para fora
endpoint = Endpoint("/api/users", "POST")
headers = {"Authorization": "Bearer token123", "Content-Type": "application/json"}
corpo = {"nome": "QA User", "email": "qa@empresa.com"}

requisicao = Requisicao(endpoint, headers, corpo)
caso = CasoTesteAPI("Criar usuário", requisicao, 201)

print(caso)
print(f"  Endpoint: {caso.requisicao.endpoint}")
print(f"  Método: {caso.requisicao.endpoint.metodo}")
print(f"  Auth: {caso.requisicao.headers.get('Authorization', 'nenhum')}")

print("\n---\n")

print("=== 4. DATACLASSES ===")

# Dataclasses simplificam a criação de classes que guardam dados
# Python gera __init__, __repr__ e __eq__ automaticamente

from dataclasses import dataclass, field

@dataclass
class Usuario:
    nome: str
    email: str
    perfil: str = "viewer"     # valor padrão
    ativo: bool = True         # valor padrão

# Python gera o __init__ automaticamente:
# def __init__(self, nome, email, perfil="viewer", ativo=True)

u1 = Usuario("Ana QA", "ana@empresa.com", "admin")
u2 = Usuario("Carlos Dev", "carlos@empresa.com")
u3 = Usuario("Ana QA", "ana@empresa.com", "admin")

# __repr__ gerado automaticamente
print(u1)
print(u2)

# __eq__ gerado automaticamente (compara todos os campos)
print(f"\nu1 == u3? {u1 == u3}")  # True (mesmos valores)
print(f"u1 == u2? {u1 == u2}")    # False

print("\n---\n")

print("=== 5. DATACLASSES COMO MASSA DE TESTE ===")

@dataclass
class CredencialTeste:
    usuario: str
    senha: str
    esperado: str       # "sucesso" ou "erro"
    descricao: str = ""

# Massa de teste limpa e tipada
massa_login = [
    CredencialTeste("admin@empresa.com", "Admin123!", "sucesso", "Admin válido"),
    CredencialTeste("user@empresa.com", "User456!", "sucesso", "User válido"),
    CredencialTeste("admin@empresa.com", "errada", "erro", "Senha incorreta"),
    CredencialTeste("", "qualquer", "erro", "Email vazio"),
    CredencialTeste("invalido", "qualquer", "erro", "Email sem @"),
]

print("Massa de teste para Login:")
print(f"{'Descrição':<20} {'Usuário':<25} {'Esperado':<10}")
print("-" * 55)
for c in massa_login:
    print(f"{c.descricao:<20} {c.usuario:<25} {c.esperado:<10}")

# Filtrar cenários de erro
erros = [c for c in massa_login if c.esperado == "erro"]
print(f"\nCenários de erro: {len(erros)}")

print("\n---\n")

print("=== 6. APLICACAO PRATICA: RELATORIO COMPOSTO ===")

@dataclass
class ItemRelatorio:
    teste: str
    status: str
    duracao_ms: float
    detalhes: str = ""


class RelatorioExecucao:
    """Relatório que CONTÉM itens e um ambiente (composição + dataclass)."""

    def __init__(self, nome, ambiente):
        self.nome = nome
        self.ambiente = ambiente      # objeto Ambiente
        self._itens = []              # lista de ItemRelatorio (dataclass)

    def adicionar(self, item):
        self._itens.append(item)

    @property
    def total(self):
        return len(self._itens)

    @property
    def taxa_sucesso(self):
        if self.total == 0:
            return 0.0
        ok = sum(1 for i in self._itens if i.status == "passou")
        return round((ok / self.total) * 100, 1)

    def gerar(self):
        linhas = [
            f"RELATÓRIO: {self.nome}",
            f"Ambiente: {self.ambiente}",
            "=" * 60,
        ]
        for item in self._itens:
            detalhe = f" | {item.detalhes}" if item.detalhes else ""
            linhas.append(
                f"  [{item.status.upper():<7}] {item.teste} "
                f"({item.duracao_ms}ms){detalhe}"
            )
        linhas.append("=" * 60)
        linhas.append(f"Total: {self.total} | Taxa de sucesso: {self.taxa_sucesso}%")
        return "\n".join(linhas)


# Montando o relatório
relatorio = RelatorioExecucao("Sprint 15 - Regressão", amb_hml)
relatorio.adicionar(ItemRelatorio("Login POST", "passou", 120))
relatorio.adicionar(ItemRelatorio("Listar users GET", "passou", 85))
relatorio.adicionar(ItemRelatorio("Criar order POST", "falhou", 800, "Timeout no banco"))
relatorio.adicionar(ItemRelatorio("Health check GET", "passou", 45))

print(relatorio.gerar())

print("\n---\n")

print("=== FIM DA AULA ===")