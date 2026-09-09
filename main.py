option = 0
despesas = [{"despesa": "monster","categoria":"Sumo","valor":12},
            {"despesa": "redbull","categoria":"Sumo","valor":16},
            {"despesa": "Huawei GT6","categoria":"Lazer","valor":200},
            {"despesa": "iPhone 17ProMax","categoria":"Lazer","valor":2000}]
#despesas,categoria,valor e talvez data
while (option != 7):
    print("1- Adicionar despesa : ")
    print("2- Ver despesas")
    print("3- Total gasto")
    print("4- Filtrar despesas")
    print("5- Ordenar depesas")
    print("6- Estatisticas")
    print("7- Sair")
    option = int(input("Escolhe um opção :"))

    if option == 1:
        print("-- ADICIONAR DESPESA --")
        despesa = input(str("Insere o nome da despesa : "))
        categoria = input(str("Insere a categoria : "))
        valor = input(str("Insere o valor da categoria : "))
        dicionariosDados = {"despesa": despesa,"categoria":categoria,"valor":valor}
        despesas.append(dicionariosDados)
        print(despesas)
    elif option == 2:
        print("-- VER DESPESAS --")
        for x in despesas:
            print(x)
    elif option == 3:
        print("-- TOTAL GASTO --")
        soma = 0
        for x in despesas:
            soma += int(x["valor"])
        print(soma)
    elif option == 4:
        print("-- FILTRAR DESPESAS --")
        print("Escolha como quer filtrar as despesas :")
        print("1- Filtrar por categoria")
        print("2- Filtrar por valor minimo")
        print("3- Filtrar por valor maximo")
        print("4- Filtrar por intervalo de valores")
        print("5- Filtrar por nome")
        print("6- Voltar")
        x = input("-> ")
        if int(x) == 1:
            print("...filtrar por categoria...")
        elif int(x) == 2:
            print("...filtrar por valor minimo...")
        elif int(x) == 3:
            print("...filtrar por valor maximo...")    
        elif int(x) == 4:
            print("...filtrar por intervalo...") 
        elif int(x) == 5:
            print("...filtrar por nome...") 
    elif option == 5:#menu concluido
        print("-- ORDENAR DESPESAS --")
        print("Escolha como quer ordenar as despesas :")
        print("1- Ordenar do mais caro para o mais barato")
        print("2- Ordenar do mais barato para o mais caro")
        print("3- Ordenar categoria de A-Z")
        print("4- Ordenar categoria de Z-A")
        print("5- Ordenar nome de A-Z")
        print("6- Ordenar nome de Z-A")
        ordenar_option = int(input(": "))
        if ordenar_option == 1:
            print("")
            print("Aqui esta ordenado do mais caro para o mais barato")
            ordenar_preco = sorted(despesas,key=lambda x:x["valor"],reverse=True)
            for y in ordenar_preco:
                print(f"Preço : {y['valor']}, despesa : {y['despesa']} categoria : {y['categoria']}") 
            print("")
        elif ordenar_option == 2:
            print("")
            print("Aqui esta ordenado do mais barato para o mais caro")
            ordenar_preco = sorted(despesas,key=lambda x:x["valor"])
            for y in ordenar_preco:
                print(f"Preço : {y['valor']}, despesa : {y['despesa']} categoria : {y['categoria']}") 
            print("")
        elif ordenar_option == 3:
            print("")
            print("Aqui estao as categorias ordenadas de A-Z")
            ordenar_az = sorted(despesas,key=lambda x :x["categoria"])
            for y in ordenar_az:
                print(f"Nome Categoria : {y['categoria']}, despesa : {y['despesa']} custou : {y['valor']}$") 
            print("")
        elif ordenar_option == 4:
            print("")
            print("Aqui estao as categorias ordenadas de Z-A")
            ordenar_az = sorted(despesas,key=lambda x :x["categoria"],reverse=True)
            for y in ordenar_az:
                print(f"Nome Categoria : {y['categoria']}, despesa : {y['despesa']} custou : {y['valor']}$") 
            print("")
        elif ordenar_option == 5:
            print("")
            print("Aqui estao as despesas ordenadas de A-Z")
            ordenar_az = sorted(despesas,key=lambda x :x["despesa"])
            for y in ordenar_az:
                print(f"Nome : {y['despesa']} custou : {y['valor']}$") 
            print("")
        elif ordenar_option == 6:
            print("")
            print("Aqui estao as despesas ordenadas de Z-A")
            ordenar_za = sorted(despesas,key=lambda x :x["despesa"],reverse=True)
            for y in ordenar_za:
                print(f"Nome : {y['despesa']} custou : {y['valor']}$") 
            print("")
    elif option == 6:#menu concluido
        print(" ")
        print("-- ESTATISTICAS --")
        #numero total de despesas
        print(f"Voce tem um total de {len(despesas)} despesa/s")
        #total gasto
        soma = [ int(x["valor"]) for x in despesas ]
        print(f"Total gasto foi {sum(soma)} euros")
        #media por despesa
        print(f"Media por despesa e de {sum(soma)/len(despesas)} euros")
        #despesa mais cara
        print(f"A despesa mais cara foi de {max(soma)}")
        #despesa mais barata
        print(f"A despesa mais barata foi de {min(soma)}")
        #total gasto por categoria
        gasto_por_categoria = {}
        for x in despesas:
            if x["categoria"] not in gasto_por_categoria:
                gasto_por_categoria.update({x["categoria"]:int(x["valor"])})
            else:
                gasto_por_categoria[x["categoria"]] += int(x["valor"])
        for x in gasto_por_categoria:
            print(f"{x} : {gasto_por_categoria.get(x)}")                
        #categoria onde gastaste mais dinheiro
        categoria_despendiosa = max(gasto_por_categoria , key=gasto_por_categoria.get)
        valor_despendioso = gasto_por_categoria[categoria_despendiosa]
        print(f"A categoria onde mais gastaste dinheiro foi {categoria_despendiosa} num total de {valor_despendioso}")
        print(" ")        
