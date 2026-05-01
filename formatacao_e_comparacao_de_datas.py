"""Aula: Formatação e Comparação de Datas em Python"""

from datetime import datetime, date, timedelta

print("=== 1. O PROBLEMA COM O FORMATO PADRÃO ===")

# Por padrão, datetime exibe datas no formato ISO 8601
agora = datetime(2024, 6, 20, 14, 32, 5)
print(f"Formato padrão Python: {agora}")
# 2024-06-20 14:32:05

# APIs, logs e sistemas usam formatos variados — precisamos converter nos dois sentidos:
# datetime -> string  (para exibir, logar, comparar com texto)
# string -> datetime  (para processar timestamps vindos de APIs e arquivos)

exemplos_reais = [
    "20/06/2024 14:32:05",       # formato brasileiro
    "Jun 20, 2024",              # formato de relatório
    "2024-06-20T14:32:05Z",      # ISO 8601 com T e Z (muito comum em APIs REST)
    "Thu, 20 Jun 2024 14:32:05", # formato de header HTTP
    "20240620",                  # formato compacto de arquivo/log
]

print("\nFormatos encontrados no dia a dia de QA:")
for fmt in exemplos_reais:
    print(f"  {fmt}")

print("\n---\n")

print("=== 2. STRFTIME — DATETIME PARA STRING ===")

# strftime = "string format time"
# Converte um objeto datetime em string usando códigos de formato

dt = datetime(2024, 6, 20, 14, 32, 5)

# Códigos mais usados:
# %Y = ano com 4 dígitos     %m = mês com 2 dígitos    %d = dia com 2 dígitos
# %H = hora (00-23)          %M = minuto                %S = segundo
# %d/%m/%Y = formato BR      %B = nome do mês           %A = nome do dia

print(f"datetime original: {dt}")
print()
print(f"Formato BR:        {dt.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Formato ISO 8601:  {dt.strftime('%Y-%m-%dT%H:%M:%SZ')}")
print(f"Só a data BR:      {dt.strftime('%d/%m/%Y')}")
print(f"Só a hora:         {dt.strftime('%H:%M:%S')}")
print(f"Compacto arquivo:  {dt.strftime('%Y%m%d_%H%M%S')}")
print(f"Legível relatório: {dt.strftime('%d de %B de %Y às %H:%M')}")
print(f"Header HTTP:       {dt.strftime('%a, %d %b %Y %H:%M:%S')}")

print("\n---\n")

print("=== 3. STRPTIME — STRING PARA DATETIME ===")

# strptime = "string parse time"
# Converte uma string em objeto datetime — o formato precisa bater exatamente

# Formato BR vindo de um formulário
data_str_br = "20/06/2024 14:32:05"
dt_br = datetime.strptime(data_str_br, "%d/%m/%Y %H:%M:%S")
print(f"String BR:        '{data_str_br}'")
print(f"Convertido:       {dt_br}")
print(f"Tipo:             {type(dt_br)}")

print()

# Timestamp ISO 8601 vindo de uma API REST
timestamp_api = "2024-06-20T09:15:30Z"
dt_api = datetime.strptime(timestamp_api, "%Y-%m-%dT%H:%M:%SZ")
print(f"Timestamp API:    '{timestamp_api}'")
print(f"Convertido:       {dt_api}")

print()

# Formato compacto de nome de arquivo de log
nome_arquivo = "relatorio_20240620_143205.csv"
# Extrair só a parte da data do nome
parte_data = nome_arquivo[10:25]  # "20240620_143205"
dt_arquivo = datetime.strptime(parte_data, "%Y%m%d_%H%M%S")
print(f"Nome do arquivo:  '{nome_arquivo}'")
print(f"Parte extraída:   '{parte_data}'")
print(f"Convertido:       {dt_arquivo}")

print("\n---\n")

print("=== 4. TABELA DE CÓDIGOS DE FORMATO ===")

dt = datetime(2024, 6, 20, 14, 32, 5)

codigos = [
    ("%Y", "Ano com 4 dígitos"),
    ("%m", "Mês com 2 dígitos (01-12)"),
    ("%d", "Dia com 2 dígitos (01-31)"),
    ("%H", "Hora no formato 24h (00-23)"),
    ("%M", "Minuto (00-59)"),
    ("%S", "Segundo (00-59)"),
    ("%B", "Nome completo do mês"),
    ("%b", "Nome abreviado do mês"),
    ("%A", "Nome completo do dia da semana"),
    ("%a", "Nome abreviado do dia da semana"),
]

print(f"{'Código':<8} {'Significado':<35} {'Exemplo'}")
print("-" * 65)
for codigo, significado in codigos:
    print(f"{codigo:<8} {significado:<35} {dt.strftime(codigo)}")

print("\n---\n")

print("=== 5. COMPARAÇÃO DE DATAS VINDAS COMO STRING ===")

# Problema comum: timestamps chegam como string em respostas de API
# Para comparar, é preciso converter para datetime primeiro

resposta_api = {
    "id": "req_001",
    "criado_em": "2024-06-20T08:00:00Z",
    "atualizado_em": "2024-06-20T14:32:05Z",
    "expira_em": "2024-06-21T08:00:00Z",
}

fmt_iso = "%Y-%m-%dT%H:%M:%SZ"

criado_em     = datetime.strptime(resposta_api["criado_em"],     fmt_iso)
atualizado_em = datetime.strptime(resposta_api["atualizado_em"], fmt_iso)
expira_em     = datetime.strptime(resposta_api["expira_em"],     fmt_iso)

print("Dados da API (como string):")
for k, v in resposta_api.items():
    if k != "id":
        print(f"  {k}: {v}")

print()

# Agora podemos comparar normalmente
foi_atualizado = atualizado_em > criado_em
print(f"Foi atualizado após criação: {foi_atualizado}")

momento_teste = datetime(2024, 6, 20, 18, 0, 0)
ainda_valido = momento_teste < expira_em
print(f"Ainda válido às 18h:        {ainda_valido}")

tempo_ativo = atualizado_em - criado_em
print(f"Tempo entre criação e update: {int(tempo_ativo.total_seconds() / 3600)}h {int((tempo_ativo.total_seconds() % 3600) / 60)}min")

print("\n---\n")

print("=== 6. APLICAÇÃO PRÁTICA — CENÁRIOS DE QA ===")

# Cenário 1: Validar formato de data retornado pela API
print("--- Validação de Formato de Data na API ---")

def validar_formato_iso(timestamp_str):
    try:
        datetime.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
        return True
    except ValueError:
        return False

timestamps_para_validar = [
    "2024-06-20T14:32:05Z",   # correto
    "20/06/2024 14:32:05",    # formato errado para API REST
    "2024-06-20 14:32:05",    # faltando T e Z
    "2024-13-20T14:32:05Z",   # mês inválido
    "2024-06-20T14:32:05Z",   # correto
]

for ts in timestamps_para_validar:
    valido = validar_formato_iso(ts)
    status = "OK " if valido else "FALHOU"
    print(f"  [{status}] '{ts}'")

print()

# Cenário 2: Ordenar logs por timestamp
print("--- Ordenação de Logs por Timestamp ---")

logs_brutos = [
    "2024-06-20T14:32:05Z | ERROR | NullPointerException",
    "2024-06-20T09:01:12Z | INFO  | Deploy iniciado",
    "2024-06-20T11:45:33Z | WARN  | Timeout na conexão",
    "2024-06-20T09:01:45Z | INFO  | Deploy concluído",
    "2024-06-20T14:31:58Z | ERROR | Falha na autenticação",
]

def extrair_timestamp(linha):
    parte = linha.split(" | ")[0]
    return datetime.strptime(parte, "%Y-%m-%dT%H:%M:%SZ")

logs_ordenados = sorted(logs_brutos, key=extrair_timestamp)

print("Logs em ordem cronológica:")
for log in logs_ordenados:
    print(f"  {log}")

print()

# Cenário 3: Gerar nome de arquivo com timestamp para relatório
print("--- Geração de Nomes de Arquivo com Timestamp ---")

execucao = datetime(2024, 6, 20, 14, 32, 5)
suite = "regressao_checkout"

nome_relatorio = f"relatorio_{suite}_{execucao.strftime('%Y%m%d_%H%M%S')}.html"
nome_screenshot = f"screenshot_{execucao.strftime('%d%m%Y_%H%M%S')}.png"
nome_log = f"log_{execucao.strftime('%Y-%m-%d')}.txt"

print(f"Relatório:   {nome_relatorio}")
print(f"Screenshot:  {nome_screenshot}")
print(f"Log:         {nome_log}")

print()

# Cenário 4: Verificar SLA com timestamps de API
print("--- Verificação de SLA com Timestamps de API ---")

registros = [
    {"id": "req_001", "inicio": "2024-06-20T10:00:00Z", "fim": "2024-06-20T10:00:02Z"},
    {"id": "req_002", "inicio": "2024-06-20T10:00:05Z", "fim": "2024-06-20T10:00:09Z"},
    {"id": "req_003", "inicio": "2024-06-20T10:00:10Z", "fim": "2024-06-20T10:00:11Z"},
    {"id": "req_004", "inicio": "2024-06-20T10:00:15Z", "fim": "2024-06-20T10:00:21Z"},
]

sla_segundos = 3.0
fmt = "%Y-%m-%dT%H:%M:%SZ"

sla_header = f"SLA ({sla_segundos}s)"
print(f"{'ID':<10} {'Duração':>10} {sla_header:>14}")
print("-" * 36)
for r in registros:
    inicio = datetime.strptime(r["inicio"], fmt)
    fim    = datetime.strptime(r["fim"],    fmt)
    dur    = (fim - inicio).total_seconds()
    ok     = "OK" if dur <= sla_segundos else "VIOLADO"
    print(f"{r['id']:<10} {dur:>9.1f}s {ok:>14}")

print("\n=== FIM DA AULA ===")