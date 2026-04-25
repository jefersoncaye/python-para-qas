"""Aula: Iteração sobre Estruturas em Python"""

print("=== 1. FOR EM LISTAS ===")

# Percorrer uma lista de status codes
status_codes = [200, 404, 500, 201, 403]

for code in status_codes:
    if code >= 400:
        print(f"Status {code}: ERRO")
    else:
        print(f"Status {code}: OK")

print("\n---\n")

print("=== 2. FOR EM DICIONARIOS ===")

# Iterar sobre chaves (padrão)
config = {"timeout": 30, "retries": 3, "ambiente": "homolog"}

print("Chaves:")
for chave in config:
    print(f"  {chave}")

# Iterar sobre chave e valor com items()
print("\nConfiguracoes do teste:")
for chave, valor in config.items():
    print(f"  {chave} = {valor}")

print("\n---\n")

print("=== 3. FOR EM SETS ===")

# Percorrer um set (sem ordem garantida)
ambientes_testados = {"dev", "homolog", "prod"}

print("Ambientes verificados:")
for amb in ambientes_testados:
    print(f"  - {amb}")

# A ordem pode variar a cada execucao!

print("\n---\n")

print("=== 4. ENUMERATE: INDICE + VALOR ===")

# Sem enumerate (jeito manual)
endpoints = ["/login", "/usuarios", "/produtos", "/checkout"]

print("Sem enumerate:")
indice = 0
for ep in endpoints:
    print(f"  Teste {indice}: {ep}")
    indice += 1

# Com enumerate (jeito pythonico)
print("\nCom enumerate:")
for i, ep in enumerate(endpoints):
    print(f"  Teste {i}: {ep}")

# enumerate com start (comecando de 1)
print("\nCom enumerate(start=1):")
for num, ep in enumerate(endpoints, start=1):
    print(f"  Caso de teste #{num}: {ep}")

print("\n---\n")

print("=== 5. ZIP: COMBINAR ESTRUTURAS ===")

# Combinar duas listas relacionadas
testes = ["Login", "Busca", "Checkout"]
resultados = ["PASSOU", "FALHOU", "PASSOU"]

print("Resultados dos testes:")
for teste, resultado in zip(testes, resultados):
    print(f"  {teste}: {resultado}")

# Zip com tres listas
tempos = [120, 350, 200]

print("\nRelatorio completo:")
for teste, resultado, tempo in zip(testes, resultados, tempos):
    print(f"  {teste} | {resultado} | {tempo}ms")

print("\n---\n")

print("=== 6. APLICACAO PRATICA QA ===")

# Cenario 1: Gerar relatorio de testes com numero + resultado
casos = ["Login valido", "Login invalido", "Senha vazia", "Timeout servidor"]
status = ["PASSOU", "PASSOU", "FALHOU", "FALHOU"]

print("=== Relatorio de Testes ===")
falhas = 0
for num, (caso, resultado) in enumerate(zip(casos, status), start=1):
    marcador = "✓" if resultado == "PASSOU" else "✗"
    print(f"  {marcador} #{num} {caso}: {resultado}")
    if resultado == "FALHOU":
        falhas += 1

print(f"\nTotal: {len(casos)} testes | {len(casos) - falhas} passaram | {falhas} falharam")

# Cenario 2: Verificar configs obrigatorias percorrendo dicionario
print("\n--- Validacao de configs ---")
configs_teste = {
    "base_url": "https://api.exemplo.com",
    "token": "",
    "timeout": 30,
    "ambiente": ""
}

for chave, valor in configs_teste.items():
    if not valor:
        print(f"  ALERTA: '{chave}' esta vazio!")
    else:
        print(f"  OK: {chave} = {valor}")

print("\n---\n")

print("=== FIM DA AULA ===")