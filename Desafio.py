# %%
# EXERCICIO 1 - COMISSAO DOS VENDEDORES

import json

dados_json = '''
{
    "vendas": [
        { "vendedor": "Joao Silva", "valor": 1200.50 },
        { "vendedor": "Joao Silva", "valor": 950.75 },
        { "vendedor": "Joao Silva", "valor": 1800.00 },
        { "vendedor": "Joao Silva", "valor": 1400.30 },
        { "vendedor": "Joao Silva", "valor": 1100.90 },
        { "vendedor": "Joao Silva", "valor": 1550.00 },
        { "vendedor": "Joao Silva", "valor": 1700.80 },
        { "vendedor": "Joao Silva", "valor": 250.30 },
        { "vendedor": "Joao Silva", "valor": 480.75 },
        { "vendedor": "Joao Silva", "valor": 320.40 },

        { "vendedor": "Maria Souza", "valor": 2100.40 },
        { "vendedor": "Maria Souza", "valor": 1350.60 },
        { "vendedor": "Maria Souza", "valor": 950.20 },
        { "vendedor": "Maria Souza", "valor": 1600.75 },
        { "vendedor": "Maria Souza", "valor": 1750.00 },
        { "vendedor": "Maria Souza", "valor": 1450.90 },
        { "vendedor": "Maria Souza", "valor": 400.50 },
        { "vendedor": "Maria Souza", "valor": 180.20 },
        { "vendedor": "Maria Souza", "valor": 90.75 },

        { "vendedor": "Carlos Oliveira", "valor": 800.50 },
        { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
        { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
        { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
        { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
        { "vendedor": "Carlos Oliveira", "valor": 300.40 },
        { "vendedor": "Carlos Oliveira", "valor": 500.00 },
        { "vendedor": "Carlos Oliveira", "valor": 125.75 },

        { "vendedor": "Ana Lima", "valor": 1000.00 },
        { "vendedor": "Ana Lima", "valor": 1100.50 },
        { "vendedor": "Ana Lima", "valor": 1250.75 },
        { "vendedor": "Ana Lima", "valor": 1400.20 },
        { "vendedor": "Ana Lima", "valor": 1550.90 },
        { "vendedor": "Ana Lima", "valor": 1650.00 },
        { "vendedor": "Ana Lima", "valor": 75.30 },
        { "vendedor": "Ana Lima", "valor": 420.90 },
        { "vendedor": "Ana Lima", "valor": 315.40 }
    ]
}
'''

dados = json.loads(dados_json)

comissoes = {}

for venda in dados["vendas"]:

    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if valor < 100:
        comissao = 0

    elif valor < 500:
        comissao = valor * 0.01

    else:
        comissao = valor * 0.05

    if vendedor not in comissoes:
        comissoes[vendedor] = 0

    comissoes[vendedor] += comissao


print("COMISSAO DOS VENDEDORES")
print("-" * 30)

for vendedor, comissao in comissoes.items():
    print(f"{vendedor}: R$ {comissao:.2f}")


# %%
# EXERCICIO 2 - MOVIMENTACAO DE ESTOQUE

import json

dados_estoque = '''
{
    "estoque": [
        {
            "codigoProduto": 101,
            "descricaoProduto": "Caneta Azul",
            "estoque": 150
        },
        {
            "codigoProduto": 102,
            "descricaoProduto": "Caderno Universitario",
            "estoque": 75
        },
        {
            "codigoProduto": 103,
            "descricaoProduto": "Borracha Branca",
            "estoque": 200
        },
        {
            "codigoProduto": 104,
            "descricaoProduto": "Lapis Preto HB",
            "estoque": 320
        },
        {
            "codigoProduto": 105,
            "descricaoProduto": "Marcador de Texto Amarelo",
            "estoque": 90
        }
    ]
}
'''

dados = json.loads(dados_estoque)

estoque = dados["estoque"]

id_movimentacao = 1


def encontrar_produto(codigo):
    for produto in estoque:

        if produto["codigoProduto"] == codigo:
            return produto

    return None


while True:

    print("\n===== MOVIMENTACAO DE ESTOQUE =====")

    print("\nProdutos disponiveis:")

    for produto in estoque:

        print(
            f'{produto["codigoProduto"]} - '
            f'{produto["descricaoProduto"]} - '
            f'Estoque: {produto["estoque"]}'
        )
    print("\nDigite 0 para sair.")
    codigo = int(input("\nCodigo do produto: "))

    

    if codigo == 0:
        break

    produto = encontrar_produto(codigo)

    if produto is None:
        print("Produto nao encontrado.")
        continue

    print("\n1 - Entrada")
    print("2 - Saida")

    tipo = input("Tipo da movimentacao: ")

    if tipo != "1" and tipo != "2":

        print("Tipo de movimentacao invalido.")
        continue

    descricao = input("Descricao da movimentacao: ")

    quantidade = int(input("Quantidade: "))

    if quantidade <= 0:

        print("A quantidade deve ser maior que zero.")
        continue

    if tipo == "1":

        produto["estoque"] += quantidade

    else:

        if quantidade > produto["estoque"]:

            print("Erro: estoque insuficiente.")
            continue

        produto["estoque"] -= quantidade

    print("\nMovimentacao realizada com sucesso!")
    print(f"ID da movimentacao: {id_movimentacao}")
    print(f"Descricao: {descricao}")
    print(f"Produto: {produto['descricaoProduto']}")
    print(f"Estoque final: {produto['estoque']}")

    id_movimentacao += 1


# %%
# EXERCICIO 3 - CALCULO DE JUROS

from datetime import datetime


valor = float(
    input("Digite o valor da conta: R$ ")
)

data_vencimento = input(
    "Digite a data de vencimento (dd/mm/aaaa): "
)

data_vencimento = datetime.strptime(
    data_vencimento,
    "%d/%m/%Y"
).date()

data_hoje = datetime.today().date()


if data_hoje <= data_vencimento:

    print("\nA conta ainda nao esta atrasada.")
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Valor final: R$ {valor:.2f}")

else:

    dias_atraso = (
        data_hoje - data_vencimento
    ).days

    taxa_diaria = 0.025

    juros = (
        valor
        * taxa_diaria
        * dias_atraso
    )

    valor_final = valor + juros

    print("\n===== CALCULO DE JUROS =====")
    print(
        f"Valor original: R$ {valor:.2f}"
    )
    print(
        f"Data de vencimento: "
        f"{data_vencimento.strftime('%d/%m/%Y')}"
    )
    print(
        f"Data de hoje: "
        f"{data_hoje.strftime('%d/%m/%Y')}"
    )
    print(
        f"Dias de atraso: {dias_atraso}"
    )
    print(
        f"Juros: R$ {juros:.2f}"
    )
    print(
        f"Valor final: R$ {valor_final:.2f}"
    )
# %%
