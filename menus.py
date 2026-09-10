def showMainMenu():
    print("1- Adicionar despesa : ")
    print("2- Ver despesas")
    print("3- Total gasto")
    print("4- Filtrar despesas")
    print("5- Ordenar depesas")
    print("6- Estatisticas")
    print("7- Sair")

def addExpense(despesas):
    print("-- ADICIONAR DESPESA --")
    despesa = input(str("Insere o nome da despesa : "))
    categoria = input(str("Insere a categoria : "))
    valor = input(str("Insere o valor da categoria : "))
    dicionariosDados = {"despesa": despesa,"categoria":categoria,"valor":valor}
    despesas.append(dicionariosDados)
    print(despesas)

def checkExpenses(despesas):
    print("-- VER DESPESAS --")#formatar print
    for x in despesas:
        print(f"Nome: {x['despesa']} | Categoria: {x['categoria']} | Valor: {x['valor']}$")
    