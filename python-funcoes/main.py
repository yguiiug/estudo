import minha_biblioteca as mb

while True:
    mb.menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Área do triângulo:", mb.area_triangulo())
    elif opcao == "2":
        print("Área do círculo:", mb.area_circulo())
    elif opcao == "3":
        print("Área do quadrado:", mb.area_quadrado())
    elif opcao == "4":
        print("Raiz quadrada:", mb.raiz_quadrada())
    elif opcao == "5":
        print("Fatorial:", mb.fatorial())
    elif opcao == "6":
        print("É primo?:", mb.eh_primo())
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")

    if not mb.deseja_continuar():
        break
