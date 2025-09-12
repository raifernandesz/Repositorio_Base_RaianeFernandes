def converter_dolar_para_real():
   cotacao_dolar = 5.64
   dolares = float(input("Digite o valor em dólares (USD): "))
   reais = dolares * cotacao_dolar
   print("--------------------")
   print(f"{dolares} USD esquivale a R$ {reais:.2f}")


def converter_real_para_dolar():
    cotacao_dolar = 5.64
    reais = float(input("Digite o valor em reais (BRL): "))
    dolares = reais / cotacao_dolar
    print("--------------------")
    print(f"{reais} BRL equivale a US$ {dolares:.2f}")


def menu():
   while True:
      print("\nConversor de Moedas")
      print("[1] Converter Dólar para Real")
      print("[2] Converter Real para Dólar")
      print("[0] Sair")
      opcao = input ("Escolha uma opção: ")
      if opcao == '1':
         converter_dolar_para_real()
      elif opcao == '2':
         converter_real_para_dolar()   
      elif opcao == '0':
         print("Saindo...")
         break
      else:
            print("!!! Opção inválida . Tente novamente ")
menu()








def menu():
   cadastro = []
   while True:
      print("\n--------Cadastro de funcionarios------------")
      print("[1] Cadastrar Pessoa")
      print("[2] Listar Pessoas ")
      print("[3] Excluir Pessoa")
      print("[0]")
      opcao = input ("Escolha uma opção: ")

      if opcao == '1':
         novo_nome = input("Digite o nome da Pessoa")
         cadastro.append(novo_nome)
         print(f"Usuário {novo_nome} foi adicionado com sucesso")
    
      elif opcao == '2':
         print("\nLista de nomes Cadastrados: ")
         for i, nome in enumerate(cadastro, start=1):
             print(f"{i} .{nome}")
      elif opcao == '3':
         excluir_nome = input("Digite o nome para excluir: ")
         if excluir_nome in cadastro:
             print(f"{excluir_nome} foi removido. ")
         else:    
          print("Saindo...")
         break
      else:
            print("!!! Opção inválida . Tente novamente. !!! ")
menu()
















