"""Aula: Manipulação de Arquivos JSON em Python"""

import json
from pathlib import Path
from unittest.mock import MagicMock

Path("saida").mkdir(exist_ok=True)

# Dado real retornado por: GET https://jsonplaceholder.typicode.com/users/1
# Cole no seu ambiente e rode com requests normalmente:
#   import requests
#   resposta = requests.get("https://jsonplaceholder.typicode.com/users/1")
#   dados = resposta.json()

RESPOSTA_JSONPLACEHOLDER = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "city": "Gwenborough",
        "geo": {"lat": "-37.3159", "lng": "81.1496"}
    },
    "phone": "1-770-736-0988 x56442",
    "company": {"name": "Romaguera-Crona"}
}

print("=== 1. CORRESPONDENCIA DE TIPOS JSON E PYTHON ===")

mapeamento = [
    ('"texto"',          "str"),
    ("42",               "int"),
    ("3.14",             "float"),
    ("true",             "True (bool)"),
    ("false",            "False (bool)"),
    ("null",             "None"),
    ("[1, 2, 3]",        "list"),
    ('{"chave": "val"}', "dict"),
]

print(f"  {'JSON':<20} Python")
print("  " + "-" * 38)
for exemplo, python in mapeamento:
    print(f"  {exemplo:<20} ->  {python}")

print("\n---\n")

print("=== 2. LENDO JSON DE UMA RESPOSTA DE API ===")

# Na sua maquina, use assim:
#
#   import requests
#   resposta = requests.get("https://jsonplaceholder.typicode.com/users/1")
#   dados = resposta.json()
#
# Este script simula a resposta para rodar sem internet

dados = RESPOSTA_JSONPLACEHOLDER

print(f"Nome:   {dados['name']}")
print(f"Email:  {dados['email']}")
print(f"ID:     {dados['id']}  (tipo: {type(dados['id']).__name__})")

print("\n---\n")

print("=== 3. LENDO JSON DE UM ARQUIVO COM JSON.LOAD ===")

fixture = {
    "id": 1,
    "nome": "Ana Silva",
    "email": "ana@empresa.com",
    "ativo": True,
    "perfil": "admin"
}

with open("saida/fixture_usuario.json", mode="w", encoding="utf-8") as f:
    json.dump(fixture, f, indent=2, ensure_ascii=False)

with open("saida/fixture_usuario.json", encoding="utf-8") as f:
    dados_fixture = json.load(f)

print(f"Nome:  {dados_fixture['nome']}")
print(f"Ativo: {dados_fixture['ativo']}  (tipo: {type(dados_fixture['ativo']).__name__})")

print("\n---\n")

print("=== 4. ACESSANDO DADOS ANINHADOS ===")

usuario = RESPOSTA_JSONPLACEHOLDER

print(f"Nome:    {usuario['name']}")
print(f"Cidade:  {usuario['address']['city']}")
print(f"Lat:     {usuario['address']['geo']['lat']}")
print(f"Empresa: {usuario['company']['name']}")

print("\n---\n")

print("=== 5. ACESSANDO CAMPOS COM GET PARA CAMPOS OPCIONAIS ===")

dados = RESPOSTA_JSONPLACEHOLDER

nome    = dados.get("name")
apelido = dados.get("apelido")
perfil  = dados.get("perfil", "sem perfil")

print(f"Nome:    {nome}")
print(f"Apelido: {apelido}")   # None - campo nao existe na resposta
print(f"Perfil:  {perfil}")    # sem perfil - valor padrao

print("\n---\n")

print("=== 6. SALVANDO JSON EM ARQUIVO COM JSON.DUMP ===")

fixture_completa = {
    "id": 10,
    "nome": "Fernanda Oliveira",
    "email": "fernanda@empresa.com",
    "ativo": True,
    "permissoes": ["ler", "escrever", "publicar"]
}

with open("saida/fixture_completa.json", mode="w", encoding="utf-8") as f:
    json.dump(fixture_completa, f, indent=2, ensure_ascii=False)

print("Fixture salva:")
print(Path("saida/fixture_completa.json").read_text(encoding="utf-8"))

print("\n---\n")

print("=== 7. TRATANDO ERROS DE JSON INVALIDO ===")

class RespostaFalsa:
    text = "internal server error"
    def json(self):
        raise ValueError("nao e JSON")

try:
    dados = RespostaFalsa().json()
except Exception:
    print(f"Resposta nao e JSON valido: {RespostaFalsa().text}")

# Validar campos de uma resposta
dados = RESPOSTA_JSONPLACEHOLDER

assert "id" in dados, "Campo 'id' ausente na resposta"
assert isinstance(dados["id"], int), "'id' deve ser int"
print(f"Resposta valida: id={dados['id']}, nome={dados['name']}")

print("=== FIM DA AULA ===")