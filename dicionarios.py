"""
Aula: Dicionários em Python
Descrição: Uso prático de dicionários com foco em QA e automação.
"""

print("=== 1. CRIANDO DICIONARIOS ===")

# Dicionário representando um usuário
usuario = {
    "nome": "Carlos",
    "idade": 30,
    "ativo": True
}

print("Usuário:", usuario)

print("\n---\n")

print("=== 2. ACESSANDO VALORES ===")

print("Nome:", usuario["nome"])
print("Idade:", usuario["idade"])

print("\n---\n")

print("=== 3. ADICIONANDO VALORES ===")

# Adicionando nova chave
usuario["cidade"] = "Curitiba"

print("Após adicionar cidade:", usuario)

print("\n---\n")

print("=== 4. ALTERANDO VALORES ===")

# Alterando valor existente
usuario["idade"] = 31

print("Após alterar idade:", usuario)

print("\n---\n")

print("=== 5. REMOVENDO ELEMENTOS ===")

# Removendo chave com pop
usuario.pop("cidade")

print("Após remover cidade:", usuario)

print("\n---\n")

print("=== 6. TAMANHO DO DICIONARIO ===")

print("Quantidade de campos:", len(usuario))

print("\n---\n")

print("=== 7. PERCORRENDO CHAVES ===")

for chave in usuario:
    print("Chave:", chave)

print("\n---\n")

print("=== 8. PERCORRENDO CHAVE E VALOR ===")

for chave, valor in usuario.items():
    print(chave, ":", valor)

print("\n---\n")

print("=== 9. VERIFICANDO EXISTENCIA DE CHAVE ===")

if "nome" in usuario:
    print("Chave 'nome' encontrada")

if "email" not in usuario:
    print("Chave 'email' não existe")

print("\n---\n")

print("=== 10. APLICACAO PRATICA QA ===")

# Simulando resposta de API
resposta_api = {
    "status_code": 200,
    "mensagem": "Sucesso",
    "tempo_resposta": 120
}

# Validação comum em testes
if resposta_api["status_code"] != 200:
    print("Erro na API")
else:
    print("API respondeu com sucesso")

print("Tempo de resposta:", resposta_api["tempo_resposta"], "ms")

print("\n---\n")

print("=== 11. CUIDADO COM CHAVE INEXISTENTE ===")

usuario = {
    "nome": "Carlos"
}

# Acesso seguro usando get()
idade = usuario.get("idade")

print("Idade (get):", idade)  # None se não existir

# Forma insegura (comentada para não quebrar o script)
# print(usuario["idade"])  # KeyError

print("\n---\n")
