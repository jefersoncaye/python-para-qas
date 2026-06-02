"""Aula: Logging básico para QA"""

import logging
import os

# =============================================================
print("=== 1. POR QUE LOGGING E NAO PRINT ===")
# =============================================================
# print() não tem nível de severidade, não salva em arquivo,
# não mostra timestamp e não indica a origem da mensagem.
# O módulo logging resolve todos esses problemas de uma vez.

print("\n---\n")

# =============================================================
print("=== 2. USO BASICO — OS CINCO NIVEIS NA PRATICA ===")
# =============================================================
# basicConfig SEMPRE antes de qualquer chamada de log.
# Aqui usamos o logger raiz (root) só para demonstrar o mínimo.

logging.basicConfig(level=logging.DEBUG)

logging.debug("Iniciando coleta de dados")
logging.info("Suite iniciada")
logging.warning("Ambiente instável")
logging.error("Endpoint retornou 500")
logging.critical("Banco inacessível — abortando")

# Saída:
# DEBUG:root:Iniciando coleta de dados
# INFO:root:Suite iniciada
# WARNING:root:Ambiente instável
# ERROR:root:Endpoint retornou 500
# CRITICAL:root:Banco inacessível — abortando

# O nível funciona como filtro:
# - level=logging.INFO    -> silencia DEBUG
# - level=logging.WARNING -> silencia DEBUG e INFO

print("\n---\n")

# =============================================================
print("=== 3. CONFIGURACAO COMPLETA ===")
# =============================================================
# Criamos um logger nomeado com propagate=False para não acumular
# com o handler do logger raiz configurado na seção anterior.

logger = logging.getLogger("suite_qa")
logger.propagate = False
logger.setLevel(logging.DEBUG)

handler_console = logging.StreamHandler()
handler_console.setLevel(logging.DEBUG)
handler_console.setFormatter(logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
))
logger.addHandler(handler_console)

logger.debug("Iniciando coleta de dados")
logger.info("Suite iniciada")
logger.warning("Ambiente instável")
logger.error("Endpoint retornou 500")
logger.critical("Banco inacessível — abortando")

# Saída:
# 13:07:48 [DEBUG] Iniciando coleta de dados
# 13:07:48 [INFO] Suite iniciada
# 13:07:48 [WARNING] Ambiente instável
# 13:07:48 [ERROR] Endpoint retornou 500
# 13:07:48 [CRITICAL] Banco inacessível — abortando

# Variáveis de formato mais usadas:
# %(asctime)s   -> timestamp
# %(levelname)s -> nível (DEBUG, INFO, etc.)
# %(message)s   -> texto da mensagem
# %(name)s      -> nome do logger
# %(filename)s  -> nome do arquivo Python

print("\n---\n")

# =============================================================
print("=== 4. LOGGERS NOMEADOS POR MODULO ===")
# =============================================================
# Loggers filhos herdam o handler do logger pai "suite_qa".
# O nome hierárquico (ponto) identifica a origem de cada mensagem.

logger_api   = logging.getLogger("suite_qa.api")
logger_auth  = logging.getLogger("suite_qa.auth")
logger_dados = logging.getLogger("suite_qa.dados")

logger_auth.info("Autenticando qa@empresa.com")
logger_api.warning("Tempo de resposta elevado: 3.8s")
logger_dados.debug("50 usuários carregados")

# Saída:
# 13:07:48 [INFO] Autenticando qa@empresa.com
# 13:07:48 [WARNING] Tempo de resposta elevado: 3.8s
# 13:07:48 [DEBUG] 50 usuários carregados

print("\n---\n")

# =============================================================
print("=== 5. SALVANDO LOGS EM ARQUIVO ===")
# =============================================================
# FileHandler adiciona um destino de arquivo ao logger.
# O logger escreve no terminal E no arquivo ao mesmo tempo.

logger_relatorio = logging.getLogger("suite_qa.relatorio")

# Handler para arquivo com formato mais detalhado (data completa)
file_handler = logging.FileHandler("execucao_testes.log", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
))

# addHandler soma destinos, não substitui o anterior
logger_relatorio.addHandler(file_handler)

logger_relatorio.info("[PASSOU] Login com credenciais válidas")
logger_relatorio.error("[FALHOU] Acessar rota protegida sem token")
logger_relatorio.info("Suite finalizada: 4/5 testes passaram")

# Terminal usa só horário (formato curto — acompanhar ao vivo)
# Arquivo usa data completa + nome do logger (consulta posterior)
#
# Dica: use timestamp no nome do arquivo para manter histórico:
# logging.FileHandler("execucao_2026-06-02.log")
# Em CI, arquive esses logs como artefatos do pipeline.

print("\n---\n")

# =============================================================
print("=== 6. NIVEL DE LOG POR AMBIENTE ===")
# =============================================================
# Lê a variável de ambiente AMBIENTE e ajusta o nível do logging.
# basicConfig SEMPRE antes de qualquer chamada de log.

nivel_map = {
    "dev":  logging.DEBUG,    # tudo — desenvolvimento local
    "hml":  logging.INFO,     # progresso — homologação
    "prod": logging.WARNING,  # só problemas — produção
    "ci":   logging.INFO,     # progresso — pipeline de CI
}

ambiente = os.environ.get("AMBIENTE", "dev")
nivel = nivel_map.get(ambiente, logging.DEBUG)

logger_env = logging.getLogger("suite_qa.env")
logger_env.propagate = False
logger_env.setLevel(nivel)

handler_env = logging.StreamHandler()
handler_env.setLevel(nivel)
handler_env.setFormatter(logging.Formatter(
    fmt="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    datefmt="%H:%M:%S"
))
logger_env.addHandler(handler_env)

logger_env.info(
    f"Ambiente detectado: {ambiente} | "
    f"Nível configurado: {logging.getLevelName(nivel)}"
)

# Como definir a variável antes de rodar:
#
# Windows (PowerShell):
#   $env:AMBIENTE = "prod"
#   python logging_basico_para_qa.py
#
# Linux / Mac:
#   AMBIENTE=prod python logging_basico_para_qa.py

print("\n---\n")

print("=== FIM DA AULA ===")