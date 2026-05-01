"""Aula: Escrita e Append em Arquivos Texto em Python"""

from pathlib import Path
from datetime import datetime

Path("saida").mkdir(exist_ok=True)

print("=== 1. ESCREVENDO UM ARQUIVO COM MODE W ===")

# mode="w" cria o arquivo se nao existir
# Se o arquivo JA EXISTIR, ele e SOBRESCRITO completamente

with open("saida/resultado_teste.txt", mode="w", encoding="utf-8") as arquivo:
    arquivo.write("Resultado da Execucao\n")
    arquivo.write("Suite: Regressao Login\n")
    arquivo.write("Ambiente: HML\n")

print("Arquivo criado. Conteudo:")
print(Path("saida/resultado_teste.txt").read_text(encoding="utf-8"))

# Cuidado: rodar com mode="w" novamente apaga tudo que foi escrito antes

print("\n---\n")

print("=== 2. SOBRESCRITA: O PERIGO DO MODE W ===")

# Demonstrando que mode="w" apaga o conteudo anterior
with open("saida/resultado_teste.txt", mode="w", encoding="utf-8") as arquivo:
    arquivo.write("Este conteudo SUBSTITUIU tudo que existia antes.\n")

print("Apos segunda abertura com mode='w':")
print(Path("saida/resultado_teste.txt").read_text(encoding="utf-8"))

# Use mode="w" quando voce quer gerar um relatorio do zero a cada execucao

print("\n---\n")

print("=== 3. ADICIONANDO CONTEUDO COM MODE A (APPEND) ===")

# mode="a" preserva o conteudo existente e adiciona ao FINAL
# Se o arquivo nao existir, ele e criado normalmente

log_path = "saida/log_suite.txt"

# Simular 3 execucoes de teste sendo registradas
execucoes = [
    ("TC001", "Login valido", "PASS"),
    ("TC002", "Login senha errada", "FAIL"),
    ("TC003", "Login usuario bloqueado", "PASS"),
]

for tc_id, descricao, resultado in execucoes:
    with open(log_path, mode="a", encoding="utf-8") as log:
        log.write(f"{tc_id} | {descricao} | {resultado}\n")

print("Log acumulado apos 3 execucoes:")
print(Path(log_path).read_text(encoding="utf-8"))

print("\n---\n")

print("=== 4. ESCREVENDO MULTIPLAS LINHAS COM WRITELINES ===")

# .writelines() recebe uma lista e escreve cada item sem separador
# Voce mesmo controla as quebras de linha

linhas = [
    "Ambiente: PROD\n",
    "Data: 2024-01-15\n",
    "Executor: pipeline-ci\n",
    "Total de casos: 42\n",
    "Aprovados: 39\n",
    "Reprovados: 3\n",
]

with open("saida/cabecalho_relatorio.txt", mode="w", encoding="utf-8") as f:
    f.writelines(linhas)

print("Arquivo gerado com writelines:")
print(Path("saida/cabecalho_relatorio.txt").read_text(encoding="utf-8"))

print("\n---\n")

print("=== 5. ESCREVENDO COM PATHLIB ===")

# Path.write_text() e o atalho mais direto para escrever strings
# Sempre sobrescreve o arquivo (equivalente ao mode="w")

relatorio = "Relatorio de Aceitacao\nStatus: APROVADO\nRevisado por: QA Lead\n"

Path("saida/relatorio_aceitacao.txt").write_text(relatorio, encoding="utf-8")

print("Arquivo criado com Path.write_text():")
print(Path("saida/relatorio_aceitacao.txt").read_text(encoding="utf-8"))

print("\n---\n")

print("=== 6. GERANDO UM LOG DE EXECUCAO COM TIMESTAMP ===")

# Cenario real: script de testes que registra cada acao com horario

def registrar_log(caminho: str, nivel: str, mensagem: str):
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"{agora} {nivel:<5} {mensagem}\n"
    with open(caminho, mode="a", encoding="utf-8") as f:
        f.write(linha)

log_path_timestamped = "saida/execucao_timestamped.log"

# Simulando uma execucao de testes
registrar_log(log_path_timestamped, "INFO", "Iniciando suite de regressao")
registrar_log(log_path_timestamped, "INFO", "Conectando ao ambiente HML")
registrar_log(log_path_timestamped, "PASS", "TC001 - Login com credenciais validas")
registrar_log(log_path_timestamped, "FAIL", "TC002 - Login com senha incorreta retornou 200")
registrar_log(log_path_timestamped, "INFO", "Suite finalizada")

print("Log de execucao com timestamp:")
print(Path(log_path_timestamped).read_text(encoding="utf-8"))

print("\n---\n")

print("=== 7. GERANDO RELATORIO DE TESTE COMPLETO ===")

# Estruturando um relatorio com cabecalho, corpo e rodape

casos_de_teste = [
    {"id": "TC001", "descricao": "Login com usuario valido",          "status": "PASS"},
    {"id": "TC002", "descricao": "Login com senha incorreta",         "status": "FAIL"},
    {"id": "TC003", "descricao": "Login com usuario bloqueado",       "status": "PASS"},
    {"id": "TC004", "descricao": "Timeout na API de autenticacao",    "status": "ERROR"},
    {"id": "TC005", "descricao": "Logout apos sessao expirada",       "status": "PASS"},
]

relatorio_path = "saida/relatorio_final.txt"

with open(relatorio_path, mode="w", encoding="utf-8") as f:
    # Cabecalho
    f.write("=" * 50 + "\n")
    f.write("RELATORIO DE EXECUCAO DE TESTES\n")
    f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    f.write(f"Ambiente: HML\n")
    f.write("=" * 50 + "\n\n")

    # Resultados de cada caso
    for caso in casos_de_teste:
        f.write(f"[{caso['status']:<5}] {caso['id']} - {caso['descricao']}\n")

    # Rodape com resumo
    total = len(casos_de_teste)
    aprovados = sum(1 for c in casos_de_teste if c["status"] == "PASS")
    reprovados = sum(1 for c in casos_de_teste if c["status"] == "FAIL")
    erros = sum(1 for c in casos_de_teste if c["status"] == "ERROR")

    f.write("\n" + "-" * 50 + "\n")
    f.write(f"Total:      {total}\n")
    f.write(f"Aprovados:  {aprovados}\n")
    f.write(f"Reprovados: {reprovados}\n")
    f.write(f"Erros:      {erros}\n")

print("Relatorio final gerado:")
print(Path(relatorio_path).read_text(encoding="utf-8"))

print("\n---\n")

print("=== 8. TABELA DE MODOS DE ABERTURA ===")

# Resumo dos modos mais usados em QA
modos = {
    "r":  "Leitura. Erro se o arquivo nao existir.",
    "w":  "Escrita. Cria o arquivo. SOBRESCREVE se ja existir.",
    "a":  "Append. Cria o arquivo. PRESERVA conteudo existente.",
    "r+": "Leitura e escrita. Nao sobrescreve, nao cria.",
}

for modo, descricao in modos.items():
    print(f"  mode='{modo}' -> {descricao}")

print("=== FIM DA AULA ===")