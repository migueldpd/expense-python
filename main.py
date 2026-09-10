from menus import *
option = 0
despesas = [{"despesa": "Monster","categoria":"Sumo","valor":12},
            {"despesa": "Redbull","categoria":"Sumo","valor":16},
            {"despesa": "Huawei GT6","categoria":"Lazer","valor":200},
            {"despesa": "Autocarro","categoria":"Transporte","valor":2},
            {"despesa": "iPhone 17ProMax","categoria":"Lazer","valor":2000}]
#despesas,categoria,valor e talvez data
while (option != 7):
    showMainMenu()
    try:
        option = int(input("Escolhe um opção :"))
    except ValueError:
        print("Value Error")
    if option == 1:
        addExpense(despesas)
    elif option == 2:#menu concluido
        checkExpenses(despesas)
    elif option == 3:#menu concluido
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
        x=0
        try:
            x = int(input(": "))
        except ValueError:
            print("Value Error")
        if x == 1:
            print("Filtrar por Categoria")
            #primeiro mostrar categorias que existem
            lista_categorias = []
            count = 1
            for x in despesas:
                if x['categoria'] not in lista_categorias:
                    lista_categorias.append(x['categoria'])
            for x in lista_categorias:
                print(f"{count}-{x}")
                count += 1
            filtro = int(input("Escolha a opçao referente à categoria que quer filtrar: "))
            filtro -= 1
            if(filtro >= 0 and filtro <= len(lista_categorias)-1):
                print("")
                print(f"Despesas relativas à categoria {lista_categorias[filtro]}")
                for x in despesas :
                    if x['categoria'] == lista_categorias[filtro]:
                        print(f"{x['despesa']}-{x['valor']}$")
            else:
                print("data not found")
        elif x == 2:
            print("")
            val_min = int(input("Insira o valor minimo para filtrar : "))
            print("")
            array_filtrado = [ x for x in despesas if x["valor"] >= val_min]
            if not array_filtrado:
                print("... data not found ...")
            else:
                for x in array_filtrado:    
                    print(f"{x['despesa']} custou {x['valor']}$")
            print("")
        elif x == 3:
            print("")
            val_max = int(input("Insira o valor maximo para filtrar : "))
            print("")
            array_filtrado = [ x for x in despesas if x["valor"] <= val_max]
            if not array_filtrado:
                print("... data not found ...")
            else:
                for x in array_filtrado:    
                    print(f"{x['despesa']} custou {x['valor']}$")
            print("")
        elif x == 4:
            print("")
            number_x = input("Insira o primeiro numero do intervalo :")
            number_y = input("Insira o segundo numero do intervalo :")
            if(int(number_x) < 0 or int(number_y) < 0):
                print("Nao pode por um intervalo com numeros negativos")
            elif(int(number_x) == int(number_y)):
                print("Nao pode inserir intervalos com valores iguais")
            else:
                print("")
                num_min = int(min(number_x,number_y))
                num_max = int(max(number_x,number_y))
                print(f"Mostrar as despesas dentro do intervalo {num_min} e {num_max}")
                filter_int = list(filter(lambda x:num_min <= x['valor'] <= num_max,despesas))
                for x in filter_int:
                    print(f"{x['despesa']} custou {x['valor']}$")
        elif x == 5:
            print("...filtrar por nome...")  #TO DO
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
