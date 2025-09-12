nome = input("qual é o seu nome?")
peso = int(input("qual é o seu peso?"))
altura = float(input("qual é a sua altura?"))
resultado = peso / (altura * altura)
print(resultado) 
if peso>= 30.0:
    print("está abaixo do peso")
elif peso>= 40.0: 
    print("peso normal da pessoa")
elif peso>= 59.9:
    print("sobrepeso")
elif resultado>= 64.9:
    print("obesidade grau 1 ")
else:
    resultado>= 89.9
    print("obesidade grau 2") 




numero = int(input("escreva o número que vc deseja"))
numero_inicio =int(input("escreva por onde quer começar"))
numero_final =int(input("escreva por onde quer terminar"))
for i in range(numero_inicio, numero_final): 
    print(f"{i} x {numero} = {i * numero}") 
























