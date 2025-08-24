in_the_loop = True
while in_the_loop:
    print("Escolha a operação desejada:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão \n")

    opcao = int(input("Digite a opção desejada: "))

    if opcao>=1 and opcao <=4:
        primeiro_numero = float(input("Primeiro Valor: "))
        segundo_numero = float(input("Segundo valor: "))
        
        match opcao:
            case 1:
                resultado = primeiro_numero + segundo_numero
            case 2:
                resultado = primeiro_numero - segundo_numero
            case 3:
                resultado = primeiro_numero * segundo_numero
            case 4:
                if segundo_numero == 0:
                    print("Não é possível dividir por 0")
                    segundo_numero = float(input("Segundo número: "))
                    resultado = primeiro_numero / segundo_numero
                else:
                    resultado = primeiro_numero / segundo_numero
        
        print(f"O resultado é {resultado} \n")
        
        is_continuar = input("Deseja fazer um novo cálculo? (s/n) ")
        if is_continuar == "s":
            in_the_loop = True
        else:
            in_the_loop = False

    else:
        print("Esta opção não existe. Escolha uma opção válida")
print("Calculadora Finalizada")