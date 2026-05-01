"""Aula: Leitura de Arquivos Texto em Python"""

from pathlib import Path

# Preparar arquivos de exemplo para a aula
Path("saida").mkdir(exist_ok=True)

# Arquivo de log simulado
Path("saida/log_execucao.txt").write_text(
    "2024-01-15 09:00:01 INFO  Iniciando suite de testes\n"
    "2024-01-15 09:00:02 INFO  Conectando ao ambiente hml\n"
    "2024-01-15 09:00:05 PASS  TC001 - Login com usuario valido\n"
    "2024-01-15 09:00:08 FAIL  TC002 - Login com senha errada\n"
    "2024-01-15 09:00:11 PASS  TC003 - Logout apos sessao expirada\n"
    "2024-01-15 09:00:14 ERROR TC004 - Timeout ao chamar /api/usuarios\n",
    encoding="utf-8"
)

# Arquivo de endpoints simulado
Path("saida/endpoints.txt").write_text(
    "/api/login\n"
    "/api/logout\n"
    "/api/usuarios\n"
    "/api/usuarios/{id}\n"
    "/api/produtos\n"
    "/api/pedidos\n",
    encoding="utf-8"
)

print("=== 1. ABRINDO UM ARQUIVO COM WITH OPEN ===")

# O bloco with garante que o arquivo e fechado automaticamente
# mesmo que ocorra um erro durante a leitura
# mode="r" = leitura (read) — padrao
# encoding="utf-8" — sempre especifique para evitar problemas

with open("saida/log_execucao.txt", mode="r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)

# Fora do bloco with, o arquivo ja esta fechado
# Nao e necessario chamar arquivo.close() manualmente

print("\n---\n")

print("=== 2. LENDO TODO O CONTEUDO DE UMA VEZ ===")

# .read() le o arquivo inteiro como uma unica string
with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
    texto_completo = arquivo.read()

print(f"Tipo retornado por .read(): {type(texto_completo)}")
print(f"Total de caracteres: {len(texto_completo)}")
print(f"Primeiros 50 caracteres: {repr(texto_completo[:50])}")

# Cuidado: para arquivos grandes (logs de producao, dumps de dados),
# .read() carrega TUDO na memoria de uma vez

print("\n---\n")

print("=== 3. LENDO LINHA A LINHA ===")

# .readlines() retorna uma lista com cada linha como elemento
with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()

print(f"Total de linhas: {len(linhas)}")
print(f"Tipo retornado por .readlines(): {type(linhas)}")
print(f"Primeira linha: {repr(linhas[0])}")
print(f"Ultima linha:   {repr(linhas[-1])}")

# Nota: cada linha inclui o \n no final

print("\n---\n")

print("=== 4. ITERANDO DIRETAMENTE SOBRE O ARQUIVO ===")

# A forma mais eficiente para arquivos grandes:
# o Python le uma linha por vez sem carregar tudo na memoria

print("Linhas do log:")
with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(f"  [{linha.strip()}]")  # .strip() remove o \n do final

print("\n---\n")

print("=== 5. REMOVENDO ESPACOS E QUEBRAS DE LINHA ===")

# .strip() remove espacos e \n das duas pontas
# .rstrip() remove apenas da direita (mais comum para linhas)
# .lstrip() remove apenas da esquerda

linha_exemplo = "2024-01-15 09:00:05 PASS  TC001 - Login com usuario valido\n"

print(f"Original:   {repr(linha_exemplo)}")
print(f".strip():   {repr(linha_exemplo.strip())}")
print(f".rstrip():  {repr(linha_exemplo.rstrip())}")

print("\n---\n")

print("=== 6. USANDO PATHLIB PARA LER ARQUIVOS ===")

# Path tem o metodo .read_text() que simplifica a leitura
# Ideal para arquivos pequenos onde voce quer o conteudo direto

caminho = Path("saida/endpoints.txt")
conteudo = caminho.read_text(encoding="utf-8")

print("Conteudo via Path.read_text():")
print(conteudo)

# Converter direto para lista de linhas sem \n
linhas = caminho.read_text(encoding="utf-8").splitlines()
print(f"Lista de endpoints ({len(linhas)} itens):")
for endpoint in linhas:
    print(f"  {endpoint}")

print("\n---\n")

print("=== 7. FILTRANDO LINHAS DURANTE A LEITURA ===")

# Cenario QA: extrair apenas as linhas de FALHA de um log de execucao

print("Linhas de FAIL e ERROR:")
with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha_limpa = linha.strip()
        if "FAIL" in linha_limpa or "ERROR" in linha_limpa:
            print(f"  {linha_limpa}")

print()

# Cenario QA: contar resultados por status
contagem = {"PASS": 0, "FAIL": 0, "ERROR": 0, "INFO": 0}

with open("saida/log_execucao.txt", encoding="utf-8") as arquivo:
    for linha in arquivo:
        for status in contagem:
            if status in linha:
                contagem[status] += 1
                break

print("Resumo de execucao:")
for status, total in contagem.items():
    print(f"  {status}: {total}")

print("\n---\n")

print("=== 8. LENDO COM PATHLIB E USANDO COM LISTAS ===")

# Cenario QA: carregar lista de endpoints a testar a partir de arquivo
endpoints = Path("saida/endpoints.txt").read_text(encoding="utf-8").splitlines()

# Simular verificacao de cada endpoint
status_codes_simulados = [200, 200, 200, 404, 200, 500]

print("Verificando endpoints:")
for endpoint, status in zip(endpoints, status_codes_simulados):
    resultado = "OK" if status == 200 else "FALHA"
    print(f"  [{resultado}] {endpoint} -> HTTP {status}")

print("\n---\n")

print("=== 9. TRATANDO ARQUIVO INEXISTENTE ===")

# Sempre que ler um arquivo externo, proteja com try/except
arquivo_inexistente = Path("saida/massa_usuarios.txt")

try:
    conteudo = arquivo_inexistente.read_text(encoding="utf-8")
    print(conteudo)
except FileNotFoundError:
    print(f"Arquivo nao encontrado: {arquivo_inexistente}")
    print("Verifique se o arquivo de massa de dados foi gerado corretamente.")

print("=== FIM DA AULA ===")