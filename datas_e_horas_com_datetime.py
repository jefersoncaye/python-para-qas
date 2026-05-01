"""Aula: Datas e Horas com datetime em Python"""

from datetime import datetime, date, time, timedelta

print("=== 1. O MÓDULO DATETIME ===")

# O módulo datetime oferece 4 tipos principais:
# - date:      apenas data (ano, mês, dia)
# - time:      apenas hora (hora, minuto, segundo, microsegundo)
# - datetime:  data + hora combinados
# - timedelta: representa uma duração (diferença entre dois momentos)

# Data atual
hoje = date.today()
print(f"Hoje:          {hoje}")
print(f"Tipo:          {type(hoje)}")

# Data e hora atuais
agora = datetime.now()
print(f"\nAgora:         {agora}")
print(f"Tipo:          {type(agora)}")

# Criando datas manualmente — útil para dados de teste fixos
data_release = date(2024, 3, 15)
print(f"\nData de release: {data_release}")

# Criando datetime manualmente
dt_deploy = datetime(2024, 3, 15, 14, 30, 0)
print(f"Deploy agendado: {dt_deploy}")

print("\n---\n")

print("=== 2. ACESSANDO COMPONENTES DE UMA DATA ===")

agora = datetime(2024, 6, 20, 9, 45, 32)

print(f"Datetime completo: {agora}")
print(f"  .year:           {agora.year}")
print(f"  .month:          {agora.month}")
print(f"  .day:            {agora.day}")
print(f"  .hour:           {agora.hour}")
print(f"  .minute:         {agora.minute}")
print(f"  .second:         {agora.second}")

# Dia da semana — 0 = segunda, 6 = domingo
print(f"  .weekday():      {agora.weekday()} (0=seg, 6=dom)")

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
print(f"  Dia da semana:   {dias_semana[agora.weekday()]}")

# Contexto QA: verificar se um log foi gerado em dia útil
def e_dia_util(dt):
    return dt.weekday() < 5  # 0-4 = seg a sex

print(f"\nO evento ocorreu em dia útil: {e_dia_util(agora)}")

print("\n---\n")

print("=== 3. TIMEDELTA — REPRESENTANDO DURAÇÃO ===")

# timedelta representa uma diferença de tempo
# Parâmetros: days, seconds, microseconds, milliseconds, minutes, hours, weeks

uma_semana = timedelta(weeks=1)
dois_dias = timedelta(days=2)
duas_horas = timedelta(hours=2)
trinta_min = timedelta(minutes=30)

print(f"Uma semana:  {uma_semana}")
print(f"Dois dias:   {dois_dias}")
print(f"Duas horas:  {duas_horas}")
print(f"30 minutos:  {trinta_min}")

# Aritmética com datas — soma e subtração
hoje = date(2024, 6, 20)
print(f"\nHoje:               {hoje}")
print(f"Daqui a 7 dias:     {hoje + timedelta(days=7)}")
print(f"Há 30 dias:         {hoje - timedelta(days=30)}")

# Contexto QA: calcular data de expiração de um token
data_criacao = datetime(2024, 6, 20, 10, 0, 0)
validade = timedelta(hours=24)
data_expiracao = data_criacao + validade

print(f"\nToken criado em:    {data_criacao}")
print(f"Expira em:          {data_expiracao}")

# Simular verificação de token expirado
momento_acesso = datetime(2024, 6, 21, 11, 0, 0)
print(f"Acesso em:          {momento_acesso}")
print(f"Token expirado:     {momento_acesso > data_expiracao}")

print("\n---\n")

print("=== 4. DIFERENÇA ENTRE DATAS ===")

# Subtrair dois datetime gera um timedelta automaticamente
inicio_teste = datetime(2024, 6, 20, 9, 0, 0)
fim_teste = datetime(2024, 6, 20, 11, 37, 45)

duracao = fim_teste - inicio_teste
print(f"Início da suíte:  {inicio_teste}")
print(f"Fim da suíte:     {fim_teste}")
print(f"Duração (delta):  {duracao}")
print(f"  .days:          {duracao.days}")
print(f"  .seconds:       {duracao.seconds}")

# Converter para unidades mais legíveis
total_segundos = int(duracao.total_seconds())
minutos = total_segundos // 60
segundos_resto = total_segundos % 60
print(f"  Total em seg:   {total_segundos}s")
print(f"  Legível:        {minutos}m {segundos_resto}s")

# Contexto QA: verificar SLA de resposta
print()
inicio = datetime(2024, 6, 20, 8, 0, 0)
fim = datetime(2024, 6, 20, 8, 0, 4)
tempo_resposta = (fim - inicio).total_seconds()
sla_segundos = 3.0

print(f"Tempo de resposta: {tempo_resposta}s")
print(f"SLA:               {sla_segundos}s")
print(f"Dentro do SLA:     {tempo_resposta <= sla_segundos}")

print("\n---\n")

print("=== 5. COMPARAÇÃO ENTRE DATAS ===")

# Datas e datetimes suportam todos os operadores de comparação
d1 = datetime(2024, 1, 15, 10, 0, 0)
d2 = datetime(2024, 3, 20, 14, 30, 0)
d3 = datetime(2024, 1, 15, 10, 0, 0)

print(f"d1: {d1}")
print(f"d2: {d2}")
print(f"d3: {d3}")
print()
print(f"d1 < d2:   {d1 < d2}")    # True  — d1 é anterior
print(f"d1 > d2:   {d1 > d2}")    # False
print(f"d1 == d3:  {d1 == d3}")   # True  — mesma data e hora
print(f"d1 != d2:  {d1 != d2}")   # True

# Contexto QA: validar janela de tempo de um evento
print()
inicio_janela = datetime(2024, 6, 20, 8, 0, 0)
fim_janela = datetime(2024, 6, 20, 18, 0, 0)
evento = datetime(2024, 6, 20, 14, 32, 0)

dentro_da_janela = inicio_janela <= evento <= fim_janela
print(f"Janela:  {inicio_janela} até {fim_janela}")
print(f"Evento:  {evento}")
print(f"Dentro da janela de manutenção: {dentro_da_janela}")

print("\n---\n")

print("=== 6. APLICAÇÃO PRÁTICA — CENÁRIOS DE QA ===")

# Cenário 1: Verificar se uma sessão de usuário ainda é válida
print("--- Validade de Sessão ---")
login_em = datetime(2024, 6, 20, 8, 0, 0)
timeout_sessao = timedelta(minutes=30)
expira_em = login_em + timeout_sessao

tentativa_acesso = datetime(2024, 6, 20, 8, 45, 0)
sessao_valida = tentativa_acesso <= expira_em

print(f"Login:            {login_em}")
print(f"Expira:           {expira_em}")
print(f"Tentativa:        {tentativa_acesso}")
print(f"Sessão válida:    {sessao_valida}")

print()

# Cenário 2: Calcular tempo de execução de uma suíte de testes
print("--- Suíte de Testes ---")
execucoes = [
    ("Login",          datetime(2024, 6, 20, 9, 0, 0),  datetime(2024, 6, 20, 9, 0, 2)),
    ("Cadastro",       datetime(2024, 6, 20, 9, 0, 2),  datetime(2024, 6, 20, 9, 0, 8)),
    ("Busca produto",  datetime(2024, 6, 20, 9, 0, 8),  datetime(2024, 6, 20, 9, 0, 9)),
    ("Checkout",       datetime(2024, 6, 20, 9, 0, 9),  datetime(2024, 6, 20, 9, 0, 25)),
]

print(f"{'Teste':<20} {'Duração':>10}")
print("-" * 32)
total = timedelta()
for nome, ini, fim in execucoes:
    dur = fim - ini
    total += dur
    print(f"{nome:<20} {dur.seconds:>8}s")

print("-" * 32)
print(f"{'TOTAL':<20} {total.seconds:>8}s")

print()

# Cenário 3: Verificar se um log está dentro do período esperado de deploy
print("--- Validação de Log pós-Deploy ---")
deploy_em = datetime(2024, 6, 20, 2, 0, 0)
janela_pos_deploy = timedelta(hours=1)

logs = [
    datetime(2024, 6, 20, 2, 15, 0),   # durante deploy
    datetime(2024, 6, 20, 2, 58, 0),   # durante deploy
    datetime(2024, 6, 20, 3, 10, 0),   # fora da janela
    datetime(2024, 6, 20, 4, 0, 0),    # fora da janela
]

print(f"Deploy:         {deploy_em}")
print(f"Janela:         até {deploy_em + janela_pos_deploy}")
print()
for log_dt in logs:
    dentro = log_dt <= deploy_em + janela_pos_deploy
    label = "janela de deploy" if dentro else "fora da janela"
    print(f"  {log_dt}  ->  {label}")

print("\n=== FIM DA AULA ===")