"""Aula: Formatação e f-strings em Python"""

print("=== 1. O PROBLEMA DE MONTAR STRINGS COM + ===")

# Antes das f-strings, concatenar variáveis em texto era verboso e propenso a erro
status_code = 404
endpoint = "/usuarios/99"
tempo_resposta = 230

# Jeito antigo — concatenação com +
# Problema: precisa converter int para str manualmente, fica difícil de ler
mensagem = "Status: " + str(status_code) + " | Endpoint: " + endpoint + " | Tempo: " + str(tempo_resposta) + "ms"
print(mensagem)

# .format() — outra forma antiga, ainda encontrada em código legado
mensagem_format = "Status: {} | Endpoint: {} | Tempo: {}ms".format(status_code, endpoint, tempo_resposta)
print(mensagem_format)

# Ambas funcionam, mas são mais verbosas e difíceis de manter

print("\n---\n")

print("=== 2. F-STRINGS — SINTAXE BÁSICA ===")

# f-strings: prefixo f antes das aspas, variáveis entre chaves {}
# Disponível a partir do Python 3.6
status_code = 200
endpoint = "/login"
tempo_resposta = 145

mensagem = f"Status: {status_code} | Endpoint: {endpoint} | Tempo: {tempo_resposta}ms"
print(mensagem)

# Qualquer expressão Python funciona dentro das chaves
usuario = "maria"
perfil = "admin"
ativo = True

print(f"Usuário: {usuario.upper()}")
print(f"Perfil: {perfil.title()}")
print(f"Conta ativa: {ativo}")
print(f"Tamanho do nome: {len(usuario)} caracteres")

# Expressões diretas dentro das chaves
preco = 99.9
quantidade = 3
print(f"Total do pedido: {preco * quantidade}")

print("\n---\n")

print("=== 3. FORMATAÇÃO DE NÚMEROS ===")

# Casas decimais — formato :.Nf
taxa_erro = 0.03478
cobertura_testes = 87.5612

print(f"Taxa de erro:       {taxa_erro:.2f}")        # 2 casas decimais
print(f"Cobertura de testes: {cobertura_testes:.1f}%") # 1 casa decimal

# Porcentagem — formato :.N%  (multiplica por 100 automaticamente)
taxa_sucesso = 0.9823
print(f"Taxa de sucesso: {taxa_sucesso:.1%}")   # 98.2%
print(f"Taxa de falha:   {1 - taxa_sucesso:.1%}")

# Separador de milhar — formato :,
total_requisicoes = 1482930
tempo_total_ms = 3750000
print(f"\nTotal de requisições: {total_requisicoes:,}")
print(f"Tempo total:          {tempo_total_ms:,}ms")

# Zeros à esquerda — útil para IDs e códigos
id_teste = 7
print(f"\nID do teste: {id_teste:04d}")   # 0007

print("\n---\n")

print("=== 4. ALINHAMENTO E LARGURA FIXA ===")

# Alinhar colunas em relatórios de teste — formato :<N, :>N, :^N
print(f"{'Endpoint':<30} {'Status':>8} {'Tempo':>10}")
print("-" * 50)

resultados = [
    ("/login", 200, "145ms"),
    ("/usuarios", 200, "89ms"),
    ("/produtos/busca", 404, "12ms"),
    ("/relatorio/exportar", 500, "3200ms"),
    ("/auth/refresh", 401, "34ms"),
]

for endpoint, status, tempo in resultados:
    print(f"{endpoint:<30} {status:>8} {tempo:>10}")

print("\n---\n")

print("=== 5. F-STRINGS MULTILINHA E BLOCOS ===")

# F-strings com múltiplas linhas — útil para montar corpos de requisição ou mensagens de log
metodo = "POST"
url = "https://api.exemplo.com/v1/usuarios"
status = 201
body = '{"id": 42, "nome": "João"}'

log_requisicao = (
    f"[REQUISIÇÃO]\n"
    f"  Método:  {metodo}\n"
    f"  URL:     {url}\n"
    f"  Status:  {status}\n"
    f"  Body:    {body}"
)
print(log_requisicao)

print()

# Mensagem de assert — quando um teste falha, a mensagem precisa ser clara
campo = "email"
valor_recebido = ""
valor_esperado = "usuario@teste.com"

mensagem_assert = (
    f"Falha na validação do campo '{campo}'.\n"
    f"  Esperado: '{valor_esperado}'\n"
    f"  Recebido: '{valor_recebido}'"
)
print(mensagem_assert)

print("\n---\n")

print("=== 6. APLICAÇÃO PRÁTICA — RELATÓRIOS E LOGS DE QA ===")

# Cenário 1: Montar mensagem de resultado de teste
def relatar_teste(nome, passou, tempo_ms, detalhe=""):
    status_label = "PASSOU" if passou else "FALHOU"
    base = f"[{status_label}] {nome} ({tempo_ms}ms)"
    if detalhe:
        base += f" — {detalhe}"
    return base

print(relatar_teste("Login com credenciais válidas", True, 145))
print(relatar_teste("Login com senha errada", False, 89, "esperado 401, recebido 200"))
print(relatar_teste("Busca de produto inexistente", True, 34))
print(relatar_teste("Exportar relatório CSV", False, 5001, "timeout após 5000ms"))

print()

# Cenário 2: Gerar dados de teste nomeados
ambientes = ["dev", "hml", "prod"]
for i, ambiente in enumerate(ambientes, start=1):
    usuario = f"qa_user_{ambiente}_{i:02d}@teste.com"
    senha = f"Senha@{ambiente.upper()}#2024"
    print(f"Ambiente {ambiente.upper():>4}: {usuario:<35} | Senha: {senha}")

print()

# Cenário 3: Relatório de cobertura de API
endpoints_testados = [
    ("GET",    "/usuarios",         True,  95),
    ("POST",   "/usuarios",         True,  87),
    ("DELETE", "/usuarios/{id}",    False, 0),
    ("GET",    "/produtos",         True,  100),
    ("PATCH",  "/produtos/{id}",    False, 0),
]

print(f"{'Método':<8} {'Endpoint':<25} {'Coberto':>8} {'Cobertura':>12}")
print("-" * 57)
for metodo, ep, coberto, cobertura in endpoints_testados:
    status_icon = "Sim" if coberto else "Nao"
    print(f"{metodo:<8} {ep:<25} {status_icon:>8} {cobertura:>11}%")

cobertos = sum(1 for _, _, c, _ in endpoints_testados if c)
total = len(endpoints_testados)
print("-" * 57)
print(f"{'TOTAL':<34} {cobertos}/{total} endpoints  {cobertos/total:.0%}")

print("\n---\n")

print("=== RESUMO ===")
print("  Sintaxe básica:       f'texto {variavel}'")
print("  Expressões:           f'{variavel.upper()}'  f'{a * b}'")
print("  Decimais:             f'{valor:.2f}'")
print("  Porcentagem:          f'{valor:.1%}'")
print("  Separador de milhar:  f'{valor:,}'")
print("  Zeros à esquerda:     f'{valor:04d}'")
print("  Alinhamento:          f'{texto:<20}'  f'{texto:>20}'")

print("\n=== FIM DA AULA ===")