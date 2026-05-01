"""Aula: Caminhos de Arquivo com pathlib em Python"""

from pathlib import Path

print("=== 1. O QUE E PATHLIB E POR QUE USAR ===")

# pathlib representa caminhos como objetos, nao como strings brutas
# Isso evita erros comuns com separadores de pasta (/ no Linux, \ no Windows)

caminho = Path("relatorios") / "2024" / "resultado.txt"
print(f"Caminho construido: {caminho}")
print(f"Tipo do objeto: {type(caminho)}")

# Em QA, caminhos aparecem em:
# - Fixtures de teste: data/fixtures/usuarios.json
# - Evidencias de bug: evidencias/sprint42/screenshot.png
# - Logs de execucao: logs/regressao/resultado.log

print("\n---\n")

print("=== 2. CRIANDO CAMINHOS COM PATH ===")

# Caminho absoluto: ponto de partida fixo no sistema de arquivos
caminho_absoluto = Path("/home/qa/projeto/tests/fixtures")
print(f"Absoluto: {caminho_absoluto}")

# Caminho relativo: relativo ao diretorio atual de execucao
caminho_relativo = Path("tests") / "fixtures" / "usuarios.json"
print(f"Relativo: {caminho_relativo}")

# Caminho do diretorio atual
diretorio_atual = Path.cwd()
print(f"Diretorio atual: {diretorio_atual}")

# Caminho do diretorio home do usuario
home = Path.home()
print(f"Home do usuario: {home}")

print("\n---\n")

print("=== 3. INSPECIONANDO PARTES DO CAMINHO ===")

arquivo = Path("evidencias/sprint42/login_bug_001.png")

print(f"Caminho completo:  {arquivo}")
print(f"Diretorio pai:     {arquivo.parent}")
print(f"Nome do arquivo:   {arquivo.name}")
print(f"Extensao:          {arquivo.suffix}")
print(f"Nome sem extensao: {arquivo.stem}")
print(f"Todas as partes:   {arquivo.parts}")

# Util para QA: extrair nome do teste a partir do caminho de evidencia
nome_teste = arquivo.stem
print(f"\nNome do teste extraido: {nome_teste}")

print("\n---\n")

print("=== 4. VERIFICANDO EXISTENCIA DE ARQUIVOS E PASTAS ===")

# Simulando verificacoes que QAs fazem antes de rodar testes
base = Path.cwd()

pasta_fixtures = base / "fixtures"
arquivo_config = base / "config.json"

print(f"fixtures/ existe? {pasta_fixtures.exists()}")
print(f"config.json existe? {arquivo_config.exists()}")

# Diferenciar entre arquivo e pasta
print(f"fixtures/ e uma pasta? {pasta_fixtures.is_dir()}")
print(f"config.json e um arquivo? {arquivo_config.is_file()}")

# Exemplo: checar se massa de dados existe antes do teste rodar
arquivo_massa = Path("data") / "usuarios_teste.csv"
if arquivo_massa.exists():
    print(f"Massa de dados encontrada: {arquivo_massa}")
else:
    print(f"ATENCAO: Massa de dados nao encontrada em {arquivo_massa}")

print("\n---\n")

print("=== 5. CRIANDO PASTAS AUTOMATICAMENTE ===")

# mkdir cria a pasta. parents=True cria toda a arvore necessaria
# exist_ok=True nao levanta erro se a pasta ja existe

pasta_logs = Path("saida") / "logs" / "regressao"
pasta_logs.mkdir(parents=True, exist_ok=True)
print(f"Pasta criada: {pasta_logs}")
print(f"Pasta existe agora? {pasta_logs.exists()}")

pasta_evidencias = Path("saida") / "evidencias" / "sprint43"
pasta_evidencias.mkdir(parents=True, exist_ok=True)
print(f"Pasta criada: {pasta_evidencias}")

# QA usa isso para organizar saidas de testes por sprint ou data

print("\n---\n")

print("=== 6. CONSTRUINDO CAMINHOS DINAMICAMENTE ===")

# Cenario: montar caminho de arquivo de log com base no ambiente
def caminho_log(ambiente: str, suite: str) -> Path:
    return Path("logs") / ambiente / f"{suite}.log"

for ambiente in ["dev", "hml", "prod"]:
    caminho = caminho_log(ambiente, "regressao_login")
    print(f"  {caminho}")

print()

# Cenario: montar caminho de fixture por tipo de usuario
def fixture_usuario(perfil: str) -> Path:
    return Path("data") / "fixtures" / f"usuario_{perfil}.json"

for perfil in ["admin", "editor", "viewer"]:
    print(f"  {fixture_usuario(perfil)}")

print("\n---\n")

print("=== 7. LISTANDO ARQUIVOS EM UMA PASTA ===")

# Criar alguns arquivos de exemplo para listar
pasta_exemplo = Path("saida") / "fixtures_exemplo"
pasta_exemplo.mkdir(parents=True, exist_ok=True)

arquivos_exemplo = ["usuario_admin.json", "usuario_editor.json", "cenarios.csv", "config.yaml"]
for nome in arquivos_exemplo:
    (pasta_exemplo / nome).write_text("conteudo de exemplo")

print(f"Arquivos em {pasta_exemplo}:")
for arquivo in pasta_exemplo.iterdir():
    print(f"  {arquivo.name}")

print()

# Filtrar por extensao usando glob
print("Apenas arquivos .json:")
for arquivo in pasta_exemplo.glob("*.json"):
    print(f"  {arquivo.name}")

print()

# Busca recursiva com rglob (util para encontrar fixtures espalhadas)
print("Busca recursiva por .json em saida/:")
pasta_raiz = Path("saida")
for arquivo in pasta_raiz.rglob("*.json"):
    print(f"  {arquivo}")

print("\n---\n")

print("=== 8. RENOMEAR E MOVER ARQUIVOS ===")

# Criar arquivo para demonstrar
arquivo_origem = Path("saida") / "relatorio_temp.txt"
arquivo_origem.write_text("relatorio de teste")

arquivo_destino = Path("saida") / "relatorio_final.txt"

# rename move e renomeia ao mesmo tempo
arquivo_origem.rename(arquivo_destino)
print(f"Arquivo movido/renomeado para: {arquivo_destino}")
print(f"Original ainda existe? {arquivo_origem.exists()}")
print(f"Destino existe? {arquivo_destino.exists()}")

print("\n---\n")

print("=== 9. INFORMACOES EXTRAS SOBRE O ARQUIVO ===")

arquivo_info = Path("saida") / "relatorio_final.txt"
stat = arquivo_info.stat()

print(f"Arquivo: {arquivo_info.name}")
print(f"Tamanho: {stat.st_size} bytes")
print(f"Caminho absoluto: {arquivo_info.resolve()}")

# Trocar extensao sem mexer no nome
novo_caminho = arquivo_info.with_suffix(".log")
print(f"Mesmo arquivo com extensao .log: {novo_caminho}")

print("=== FIM DA AULA ===")