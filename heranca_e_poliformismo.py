"""Aula: Herança e Polimorfismo em Python"""

print("=== 1. O QUE E HERANCA ===")

# Herança permite criar uma classe nova baseada em outra existente
# A classe filha HERDA atributos e métodos da classe pai
# E pode ADICIONAR ou SOBRESCREVER comportamentos

class Teste:
    """Classe base para qualquer tipo de teste."""

    def __init__(self, nome, prioridade="media"):
        self.nome = nome
        self.prioridade = prioridade
        self._status = "pendente"
        self._duracao_ms = 0

    def executar(self, duracao_ms):
        """Executa o teste (implementação base)."""
        self._duracao_ms = duracao_ms
        self._status = "executado"

    def resumo(self):
        return f"[{self._status.upper()}] {self.nome} ({self._duracao_ms}ms)"


# Classe filha herda TUDO de Teste
class TesteAPI(Teste):
    """Teste específico para endpoints de API."""

    def __init__(self, nome, endpoint, metodo="GET", prioridade="media"):
        super().__init__(nome, prioridade)  # chama o __init__ do pai
        self.endpoint = endpoint
        self.metodo = metodo
        self.status_code = None

    def executar(self, duracao_ms, status_code=200):
        """Sobrescreve executar() adicionando status_code."""
        super().executar(duracao_ms)  # chama executar() do pai
        self.status_code = status_code
        self._status = "passou" if 200 <= status_code < 300 else "falhou"

    def resumo(self):
        """Sobrescreve resumo() com detalhes de API."""
        base = super().resumo()
        return f"{base} | {self.metodo} {self.endpoint} -> {self.status_code}"


# Usando
teste_api = TesteAPI("Listar usuários", "/api/users", "GET", "alta")
teste_api.executar(150, status_code=200)
print(teste_api.resumo())

teste_api2 = TesteAPI("Criar pedido", "/api/orders", "POST")
teste_api2.executar(800, status_code=500)
print(teste_api2.resumo())

print("\n---\n")

print("=== 2. SUPER() E A CADEIA DE HERANCA ===")

# super() chama o método da classe pai
# Evita duplicar código que já existe na classe base

class TesteUI(Teste):
    """Teste específico para interface web."""

    def __init__(self, nome, pagina, seletor, prioridade="media"):
        super().__init__(nome, prioridade)
        self.pagina = pagina
        self.seletor = seletor
        self.screenshot = None

    def executar(self, duracao_ms, elemento_encontrado=True):
        super().executar(duracao_ms)
        if elemento_encontrado:
            self._status = "passou"
            self.screenshot = f"screenshots/{self.nome.lower().replace(' ', '_')}.png"
        else:
            self._status = "falhou"
            self.screenshot = f"screenshots/FALHA_{self.nome.lower().replace(' ', '_')}.png"

    def resumo(self):
        base = super().resumo()
        return f"{base} | Página: {self.pagina} | Screenshot: {self.screenshot}"


teste_ui = TesteUI("Botão de login visível", "/login", "#btn-login", "alta")
teste_ui.executar(2500, elemento_encontrado=True)
print(teste_ui.resumo())

teste_ui2 = TesteUI("Menu lateral presente", "/dashboard", "#sidebar")
teste_ui2.executar(3200, elemento_encontrado=False)
print(teste_ui2.resumo())

print("\n---\n")

print("=== 3. VERIFICANDO HERANCA ===")

# isinstance() verifica se um objeto é instância de uma classe (ou suas filhas)
# issubclass() verifica se uma classe é filha de outra

teste_base = Teste("Teste genérico")
teste_api = TesteAPI("Login", "/api/auth", "POST")
teste_ui = TesteUI("Título da página", "/home", "h1")

print("isinstance(teste_api, TesteAPI):", isinstance(teste_api, TesteAPI))
print("isinstance(teste_api, Teste):", isinstance(teste_api, Teste))
print("isinstance(teste_base, TesteAPI):", isinstance(teste_base, TesteAPI))

print()
print("issubclass(TesteAPI, Teste):", issubclass(TesteAPI, Teste))
print("issubclass(TesteUI, Teste):", issubclass(TesteUI, Teste))
print("issubclass(Teste, TesteAPI):", issubclass(Teste, TesteAPI))

print("\n---\n")

print("=== 4. POLIMORFISMO ===")

# Polimorfismo: objetos de classes diferentes respondem ao MESMO método
# de formas diferentes, sem precisar verificar o tipo

# Sem polimorfismo, você teria que fazer isso:
print("SEM polimorfismo (if/elif para cada tipo):")
print("-" * 50)

suite_exemplo = [
    Teste("Health check básico"),
    TesteAPI("Buscar produto", "/api/products/1", "GET"),
    TesteUI("Logo no header", "/home", "#logo"),
]

suite_exemplo[0].executar(50)
suite_exemplo[1].executar(120, status_code=200)
suite_exemplo[2].executar(1800, elemento_encontrado=True)

for teste in suite_exemplo:
    if isinstance(teste, TesteAPI):
        print(f"  [{teste._status.upper()}] {teste.nome} | {teste.metodo} {teste.endpoint}")
    elif isinstance(teste, TesteUI):
        print(f"  [{teste._status.upper()}] {teste.nome} | Página: {teste.pagina}")
    else:
        print(f"  [{teste._status.upper()}] {teste.nome}")

# Com polimorfismo: cada objeto já sabe como gerar seu resumo
print()
print("COM polimorfismo (mesmo método, resultados diferentes):")
print("-" * 50)

suite = [
    Teste("Health check básico"),
    TesteAPI("Buscar produto", "/api/products/1", "GET"),
    TesteAPI("Deletar cache", "/api/cache", "DELETE"),
    TesteUI("Logo no header", "/home", "#logo"),
    TesteUI("Footer com copyright", "/home", "#footer"),
]

# Executando todos
suite[0].executar(50)
suite[1].executar(120, status_code=200)
suite[2].executar(95, status_code=204)
suite[3].executar(1800, elemento_encontrado=True)
suite[4].executar(2100, elemento_encontrado=False)

# O loop é o mesmo para todos
for teste in suite:
    print(f"  {teste.resumo()}")

print("-" * 50)

# Contando resultados
total = len(suite)
passou = 0
falhou = 0
for teste in suite:
    if teste._status == "passou":
        passou += 1
    else:
        falhou += 1

print(f"Total: {total} | Passou: {passou} | Falhou: {falhou}")

print("\n---\n")

print("=== 5. DUCK TYPING ===")

# Python não exige herança para polimorfismo
# "Se anda como pato e faz quack como pato, é um pato"
# Basta ter o mesmo método, não precisa herdar da mesma classe

class TestePerformance:
    """Teste de performance (NÃO herda de Teste)."""

    def __init__(self, nome, requisicoes=100):
        self.nome = nome
        self.requisicoes = requisicoes
        self.tempo_medio_ms = 0

    def executar(self, tempo_medio_ms):
        self.tempo_medio_ms = tempo_medio_ms

    def resumo(self):
        status = "OK" if self.tempo_medio_ms < 500 else "LENTO"
        return (
            f"[{status}] {self.nome} | "
            f"{self.requisicoes} reqs, média: {self.tempo_medio_ms}ms"
        )


# Duck typing em ação: mesma interface, classes sem relação de herança
todos_os_testes = [
    TesteAPI("Login", "/api/auth", "POST"),
    TestePerformance("Carga na API", 1000),
]

todos_os_testes[0].executar(120, status_code=200)
todos_os_testes[1].executar(350)

print("Duck Typing:")
for t in todos_os_testes:
    print(f"  {t.resumo()}")  # funciona para ambos!

print()
print(f"TestePerformance herda de Teste? {issubclass(TestePerformance, Teste)}")
print("Mas funciona no mesmo loop porque tem o método resumo()")

print("\n---\n")

print("=== 6. QUANDO USAR HERANCA ===")

# Use herança quando existe relação "É UM":
#   TesteAPI É UM Teste -> sim, herança
#   TesteUI É UM Teste -> sim, herança
#
# NÃO use herança para relação "TEM UM":
#   Suite TEM testes -> não, composição (próxima aula)
#   Relatório TEM resultados -> não, composição (próxima aula)

print("Regra prática:")
print("  'É UM'  -> herança    (TesteAPI É UM Teste)")
print("  'TEM UM' -> composição (Suite TEM testes)")
print()
print("Exemplos:")

exemplos = [
    ("TesteAPI é um Teste", True),
    ("TesteUI é um Teste", True),
    ("Suite tem testes", False),
    ("Relatório tem resultados", False),
]

for descricao, usar_heranca in exemplos:
    tipo = "Herança" if usar_heranca else "Composição"
    print(f"  {descricao} -> {tipo}")

print("\n---\n")

print("=== FIM DA AULA ===")