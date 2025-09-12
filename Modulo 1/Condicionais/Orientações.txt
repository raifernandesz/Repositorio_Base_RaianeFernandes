try:
    nome_do_paciente = input("Escreva o nome do paciente: ")
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    
    # Calculando o IMC
    imc = peso / (altura * altura)

    # Exibindo a classificação do IMC
    if imc < 18.5:
        print("Abaixo do peso")
    elif 18.5 <= imc <= 24.9:
        print("Peso normal")
    elif 25.0 <= imc <= 29.9:
        print("Sobrepeso")
    elif 30.0 <= imc <= 34.9:
        print("Obesidade Grau I")
    elif 35.0 <= imc <= 39.9:
        print("Obesidade Grau II")
    else:
        print("Obesidade Grau III mórbida")

    # Exibindo o resultado final
    print(f"O paciente {nome_do_paciente} tem um IMC de {imc:.1f}")

except ValueError:
    print("Erro: Por favor, insira valores numéricos válidos para peso e altura.")
except KeyboardInterrupt:
    print("\nEntrada interrompida pelo usuário. O programa será encerrado.")


with open ("cadastro_imc.txt",  "a") as arquivo:
    arquivo.write(f"Nome: {nome_do_paciente} \nIMC: {imc:.2f}")
    arquivo.write("\n-------------------------------------")
