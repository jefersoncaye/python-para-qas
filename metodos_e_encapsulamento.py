"""Aula: Métodos e Encapsulamento em Python"""

print("=== 1. METODOS QUE CHAMAM OUTROS METODOS ===")

# Dentro de uma classe, um método pode chamar outro usando self
# Isso permite compor comportamentos complexos a partir de partes simples

class ValidadorEndpoint:
    """Valida configurações de endpoints de API."""

    def __init__(self, endpoint, metodo, requer_auth=False):
        self.endpoint = endpoint
        self.metodo = metodo
        self.requer_auth = requer_auth
        self._erros = []  # atributo "privado" (veremos adiante)

    def _validar_formato(self):
        """Verifica se o endpoint começa com /."""
        if not self.endpoint.startswith("/"):
            self._erros.append("Endpoint deve começar com /")

    def _validar_metodo(self):
        """Verifica se o método HTTP é válido."""
        metodos_validos = {"GET", "POST", "PUT", "PATCH", "DELETE"}
        if self.metodo.upper() not in metodos_validos:
            self._erros.append(f"Método '{self.metodo}' não é válido")

    def _validar_auth(self):
        """Verifica consistência de autenticação."""
        rotas_publicas = {"/api/health", "/api/status", "/api/version"}
        if self.endpoint in rotas_publicas and self.requer_auth:
            self._erros.append("Rota pública não deveria exigir autenticação")

    def validar(self):
        """Executa todas as validações e retorna resultado."""
        self._erros = []  # limpa erros anteriores
        self._validar_formato()
        self._validar_metodo()
        self._validar_auth()
        return {
            "endpoint": self.endpoint,
            "valido": len(self._erros) == 0,
            "erros": self._erros.copy(),
        }


# Testando
endpoints = [
    ValidadorEndpoint("/api/users", "GET"),
    ValidadorEndpoint("api/login", "POST"),           # sem /
    ValidadorEndpoint("/api/health", "FETCH"),         # método inválido
    ValidadorEndpoint("/api/health", "GET", True),     # pública com auth
]

for v in endpoints:
    resultado = v.validar()
    status = "OK" if resultado["valido"] else "FALHA"
    erros = ", ".join(resultado["erros"]) if resultado["erros"] else "nenhum"
    print(f"  [{status}] {resultado['endpoint']} | Erros: {erros}")

print("\n---\n")

print("=== 2. ATRIBUTOS PUBLICOS VS PRIVADOS ===")

# Python não tem privacidade real como Java/C#
# Usa CONVENÇÕES para indicar intenção:
#   nome      -> público: pode acessar livremente
#   _nome     -> protegido: "use com cuidado, detalhe interno"
#   __nome    -> privado: name mangling (Python renomeia internamente)

class ContadorTestes:
    """Conta resultados de uma suíte de testes."""

    def __init__(self, nome_suite):
        self.nome_suite = nome_suite    # público: qualquer um acessa
        self._total = 0                 # protegido: detalhe interno
        self.__segredo = "v1.0"         # privado: name mangling

    def registrar(self, resultado):
        """Registra um resultado de teste."""
        self._total += 1

    def get_total(self):
        return self._total


contador = ContadorTestes("Smoke Test")
contador.registrar("passou")
contador.registrar("falhou")

# Acesso público: funciona normalmente
print(f"Suite: {contador.nome_suite}")

# Acesso protegido: funciona, mas o _ avisa "cuidado"
print(f"Total (via _total): {contador._total}")

# Acesso privado: o nome original não funciona
try:
    print(contador.__segredo)
except AttributeError as e:
    print(f"Erro ao acessar __segredo: {e}")

# Python renomeia para _NomeDaClasse__atributo (name mangling)
print(f"Via name mangling: {contador._ContadorTestes__segredo}")
print("(Funciona, mas nunca faça isso em código real)")

print("\n---\n")

print("=== 3. POR QUE PROTEGER ATRIBUTOS ===")

# Sem proteção, qualquer código externo pode colocar o objeto em estado inválido

class ResultadoTesteSemProtecao:
    def __init__(self, nome):
        self.nome = nome
        self.status = "pendente"

teste = ResultadoTesteSemProtecao("Login")
teste.status = "banana"  # ninguém impede isso!
print(f"Status inválido aceito: {teste.status}")

# Com proteção via método, podemos validar antes de aceitar
class ResultadoTesteProtegido:
    def __init__(self, nome):
        self.nome = nome
        self._status = "pendente"

    def definir_status(self, novo_status):
        """Define o status com validação."""
        validos = {"pendente", "passou", "falhou", "bloqueado"}
        if novo_status not in validos:
            raise ValueError(
                f"Status '{novo_status}' inválido. "
                f"Use: {', '.join(sorted(validos))}"
            )
        self._status = novo_status

    def get_status(self):
        return self._status


teste2 = ResultadoTesteProtegido("Login")
teste2.definir_status("passou")
print(f"Status válido: {teste2.get_status()}")

try:
    teste2.definir_status("banana")
except ValueError as e:
    print(f"Validação funcionou: {e}")

print("\n---\n")

print("=== 4. O DECORADOR @PROPERTY ===")

# @property transforma um método em algo que parece um atributo
# Permite validação sem mudar a interface de uso

class Ambiente:
    """Ambiente de teste com URL protegida."""

    def __init__(self, nome, url):
        self.nome = nome
        self._url = url  # armazena internamente com _

    @property
    def url(self):
        """Getter: retorna a URL ao acessar ambiente.url."""
        return self._url

    @url.setter
    def url(self, nova_url):
        """Setter: valida antes de aceitar a nova URL."""
        if not nova_url.startswith("https://"):
            raise ValueError(f"URL deve começar com https:// (recebido: {nova_url})")
        self._url = nova_url

    @property
    def esta_ativo(self):
        """Property somente leitura (sem setter)."""
        return self._url is not None and len(self._url) > 0


amb = Ambiente("hml", "https://hml.api.empresa.com")

# Acessa como atributo, mas executa o método getter
print(f"URL: {amb.url}")
print(f"Ativo: {amb.esta_ativo}")

# Atribui como atributo, mas executa o método setter com validação
amb.url = "https://nova-hml.api.empresa.com"
print(f"URL atualizada: {amb.url}")

# Tentar URL inválida
try:
    amb.url = "http://inseguro.com"
except ValueError as e:
    print(f"Validação do setter: {e}")

# Property somente leitura não permite atribuição
try:
    amb.esta_ativo = False
except AttributeError as e:
    print(f"Somente leitura: {e}")

print("\n---\n")

print("=== 5. METODO __STR__ E __REPR__ ===")

# __str__ define como o objeto aparece no print()
# __repr__ define a representação técnica (útil para debug)

class CasoTeste:
    """Caso de teste com representação legível."""

    def __init__(self, id_teste, nome, prioridade="media"):
        self.id_teste = id_teste
        self.nome = nome
        self.prioridade = prioridade
        self._status = "pendente"

    def __str__(self):
        """Para humanos: print() e f-strings."""
        return f"[{self._status.upper()}] {self.id_teste}: {self.nome}"

    def __repr__(self):
        """Para desenvolvedores: debug e logs."""
        return (
            f"CasoTeste(id_teste='{self.id_teste}', "
            f"nome='{self.nome}', prioridade='{self.prioridade}')"
        )


tc = CasoTeste("TC-001", "Login com credenciais válidas", "alta")

# __str__: usado por print() e f-strings
print(f"str:  {tc}")

# __repr__: usado pelo interpretador e em listas
print(f"repr: {tc!r}")

# Em listas, Python usa __repr__
suite = [
    CasoTeste("TC-001", "Login válido"),
    CasoTeste("TC-002", "Login inválido"),
    CasoTeste("TC-003", "Recuperar senha"),
]
print(f"\nSuite: {suite}")

print("\n---\n")

print("=== 6. APLICACAO PRATICA: CONFIGURACAO DE TESTE ===")

class ConfiguracaoTeste:
    """Gerencia configuração de execução de testes com validação."""

    AMBIENTES_VALIDOS = {"dev", "hml", "prod", "ci"}
    BROWSERS_VALIDOS = {"chrome", "firefox", "edge"}

    def __init__(self, ambiente="hml", browser="chrome", timeout=30, headless=False):
        self.ambiente = ambiente   # usa o setter via @property
        self.browser = browser     # usa o setter via @property
        self._timeout = timeout
        self._headless = headless

    @property
    def ambiente(self):
        return self._ambiente

    @ambiente.setter
    def ambiente(self, valor):
        if valor not in self.AMBIENTES_VALIDOS:
            raise ValueError(
                f"Ambiente '{valor}' inválido. "
                f"Use: {', '.join(sorted(self.AMBIENTES_VALIDOS))}"
            )
        self._ambiente = valor

    @property
    def browser(self):
        return self._browser

    @browser.setter
    def browser(self, valor):
        if valor.lower() not in self.BROWSERS_VALIDOS:
            raise ValueError(
                f"Browser '{valor}' inválido. "
                f"Use: {', '.join(sorted(self.BROWSERS_VALIDOS))}"
            )
        self._browser = valor.lower()

    @property
    def timeout(self):
        return self._timeout

    @timeout.setter
    def timeout(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(f"Timeout deve ser positivo (recebido: {valor})")
        self._timeout = valor

    @property
    def base_url(self):
        """URL base calculada a partir do ambiente (somente leitura)."""
        urls = {
            "dev": "https://dev.api.empresa.com",
            "hml": "https://hml.api.empresa.com",
            "prod": "https://api.empresa.com",
            "ci": "https://ci.api.empresa.com",
        }
        return urls[self._ambiente]

    def __str__(self):
        return (
            f"Config(ambiente={self._ambiente}, browser={self._browser}, "
            f"timeout={self._timeout}s, headless={self._headless})"
        )


# Uso normal
config = ConfiguracaoTeste(ambiente="hml", browser="chrome", timeout=15)
print(config)
print(f"Base URL: {config.base_url}")

# Mudando ambiente (setter valida)
config.ambiente = "dev"
print(f"\nAmbiente alterado: {config.ambiente}")
print(f"Base URL recalculada: {config.base_url}")

# Tentando valores inválidos
erros_teste = [
    ("ambiente", "staging"),
    ("browser", "safari"),
    ("timeout", -5),
]

print("\nTentando valores inválidos:")
for attr, valor in erros_teste:
    try:
        setattr(config, attr, valor)
    except ValueError as e:
        print(f"  {attr}={valor!r}: {e}")

print("\n---\n")

print("=== FIM DA AULA ===")