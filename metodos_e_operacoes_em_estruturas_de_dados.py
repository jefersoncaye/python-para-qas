"""
Aula: Métodos e Operações em Estruturas de Dados em Python
"""

print("=== 1. ORDENANDO LISTAS: sort() E sorted() ===")

# sort() — altera a lista original
status_codes = [500, 200, 404, 201, 400]
print("Original:", status_codes)

status_codes.sort()
print("Crescente:", status_codes)

status_codes.sort(reverse=True)
print("Decrescente:", status_codes)

# sorted() — retorna nova lista, sem alterar a original
endpoints = ["/usuarios", "/login", "/produtos", "/logout"]
print("\nEndpoints:", endpoints)
print("Ordenados:", sorted(endpoints))
print("Original intacta:", endpoints)

print("\n---\n")

print("=== 2. CONTAGEM, BUSCA E INVERSAO ===")

# count() — quantas vezes um valor aparece
resultados = ["PASSOU", "FALHOU", "PASSOU", "PASSOU", "FALHOU"]
print("PASSOU:", resultados.count("PASSOU"), "vezes")
print("FALHOU:", resultados.count("FALHOU"), "vezes")

# index() — posição da primeira ocorrência
print("Primeira falha no índice:", resultados.index("FALHOU"))

# reverse() — inverte a ordem
etapas = ["login", "busca", "carrinho", "pagamento"]
etapas.reverse()
print("\nEtapas invertidas:", etapas)

print("\n---\n")

print("=== 3. COPIANDO, LIMPANDO E COMBINANDO ===")

# copy() — cópia independente (alterar a cópia não afeta o original)
usuarios = ["ana@email.com", "carlos@email.com"]
copia = usuarios.copy()
copia.append("maria@email.com")
print("Original:", usuarios)
print("Cópia:", copia)

# clear() — remove tudo
logs = ["log1", "log2", "log3"]
logs.clear()
print("\nLogs após clear:", logs)

# extend() — combina listas (diferente de append)
ambientes_br = ["dev-br", "hml-br"]
ambientes_us = ["dev-us", "hml-us"]
ambientes_br.extend(ambientes_us)
print("Ambientes combinados:", ambientes_br)

print("\n---\n")

print("=== 4. JOIN E SPLIT ===")

# join() — lista de strings → string única
campos = ["nome", "email", "senha"]
print("Campos:", ", ".join(campos))

# split() — string → lista
csv_linha = "200,OK,120ms"
valores = csv_linha.split(",")
print("CSV parseado:", valores)

print("\n---\n")

print("=== 5. METODOS DE DICIONARIOS: keys(), values(), items() ===")

resposta_api = {
    "status_code": 200,
    "mensagem": "Sucesso",
    "tempo_resposta": 120
}

print("Chaves:", list(resposta_api.keys()))
print("Valores:", list(resposta_api.values()))
print("Itens:", list(resposta_api.items()))

# setdefault() — define valor só se a chave não existir
usuario = {"nome": "Carlos", "idade": 30}
usuario.setdefault("perfil", "viewer")
usuario.setdefault("nome", "Outro")  # NÃO sobrescreve
print("\nApós setdefault:", usuario)

# update() — mescla dicionários
usuario.update({"cidade": "Curitiba", "idade": 31})
print("Após update:", usuario)

print("\n---\n")

print("=== 6. CONVERSAO ENTRE ESTRUTURAS ===")

# Lista → Set → Lista (remover duplicatas)
ids = [101, 102, 103, 101, 102]
ids_unicos = list(set(ids))
print("IDs sem duplicatas:", ids_unicos)

# Lista de tuplas → Dict
pares = [("nome", "Ana"), ("perfil", "admin")]
print("Dict:", dict(pares))

# Dict → Lista de tuplas
config = {"timeout": 30, "retries": 3}
print("Tuplas:", list(config.items()))

print("\n---\n")

print("=== 7. APLICACAO PRATICA QA ===")

# Validar campos obrigatórios em resposta de API
campos_obrigatorios = {"id", "nome", "email", "status"}
resposta = {"id": 1, "nome": "Ana", "status": "ativo"}

faltando = campos_obrigatorios - set(resposta.keys())

if faltando:
    print(f"Campos obrigatórios faltando: {faltando}")
else:
    print("Todos os campos presentes")

print("\n---\n")

print("=== FIM DA AULA ===")