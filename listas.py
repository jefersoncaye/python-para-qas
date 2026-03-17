"""
Aula: Listas em Python
"""

print("=== 1. CRIANDO LISTAS ===")

# Lista de usuários para teste
usuarios = ["ana@email.com", "carlos@email.com", "maria@email.com"]
print("Usuários:", usuarios)

# Lista de status HTTP
codigos_http = [200, 201, 400, 404, 500]
print("Códigos HTTP:", codigos_http)

# Lista com tipos mistos
dados_mistos = ["Ana", 30, True, None]
print("Dados mistos:", dados_mistos)

# Lista vazia (uso comum em testes dinâmicos)
resultados = []
print("Lista vazia:", resultados)

print("\n---\n")

print("=== 2. ACESSANDO ELEMENTOS ===")

ambientes = ["desenvolvimento", "homologacao", "producao"]

print("Primeiro ambiente:", ambientes[0])
print("Segundo ambiente:", ambientes[1])
print("Terceiro ambiente:", ambientes[2])

print("\n---\n")

print("=== 3. INDICES NEGATIVOS ===")

print("Último ambiente:", ambientes[-1])
print("Penúltimo ambiente:", ambientes[-2])

# Caso prático: pegar último resultado de execução
execucoes = ["PASSOU", "PASSOU", "FALHOU", "PASSOU"]
ultimo_resultado = execucoes[-1]

print("Execuções:", execucoes)
print("Último resultado:", ultimo_resultado)

print("\n---\n")

print("=== 4. MODIFICANDO VALORES ===")

usuarios = ["ana@email.com", "carlso@email.com", "maria@email.com"]

# Corrigindo erro de digitação
usuarios[1] = "carlos@email.com"

print("Usuários corrigidos:", usuarios)

print("\n---\n")

print("=== 5. ADICIONANDO ELEMENTOS ===")

usuarios = ["ana@email.com", "carlos@email.com"]

# Adicionando no final
usuarios.append("maria@email.com")
usuarios.append("pedro@email.com")

print("Após append:", usuarios)

# Inserindo em posição específica
usuarios.insert(0, "admin@email.com")

print("Após insert:", usuarios)

print("\n---\n")

print("=== 6. REMOVENDO ELEMENTOS ===")

usuarios = ["ana@email.com", "carlos@email.com", "maria@email.com"]

# Removendo por valor
usuarios.remove("carlos@email.com")
print("Após remove:", usuarios)

# Removendo por índice
removido = usuarios.pop(1)

print("Elemento removido:", removido)
print("Lista atualizada:", usuarios)

print("\n---\n")

print("=== 7. TAMANHO DA LISTA ===")

resultados_api = ["item1", "item2", "item3", "item4", "item5"]

total = len(resultados_api)

print("Resultados:", resultados_api)
print("Total de resultados:", total)

# Validação comum em QA
esperado = 5

if len(resultados_api) == esperado:
    print("Quantidade de resultados correta!")
else:
    print("Quantidade incorreta!")

print("\n---\n")

print("=== 8. PERCORRENDO LISTAS ===")

ambientes = ["desenvolvimento", "homologacao", "producao"]

for ambiente in ambientes:
    print("Testando em:", ambiente)

print("\n---\n")

print("=== 9. PERCORRENDO COM INDICE (ENUMERATE) ===")

casos_de_teste = ["Login válido", "Login inválido", "Login sem senha"]

for indice, caso in enumerate(casos_de_teste):
    print(f"Caso {indice + 1}: {caso}")

print("\n---\n")

print("=== 10. VERIFICANDO EXISTENCIA ===")

codigos_sucesso = [200, 201, 204]
codigo_recebido = 201

if codigo_recebido in codigos_sucesso:
    print(f"Código {codigo_recebido} é sucesso")
else:
    print(f"Código {codigo_recebido} NÃO esperado")

# Verificando ausência
erros_criticos = [500, 502, 503]
codigo = 404

if codigo not in erros_criticos:
    print(f"Código {codigo} não é erro crítico")

print("\n---\n")

print("=== FIM DA AULA ===")