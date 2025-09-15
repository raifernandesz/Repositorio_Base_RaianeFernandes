from flask import Flask, jsonify, request
import threading
import requests
import time

app = Flask(__name__)


alunos = [
    {"id": 1, "nome": "Raiane", "idade": 17},
    {"id": 2, "nome": "Leticia", "idade": 18}
]

@app.route("/")
def home():
    return "📚 API de Alunos funcionando em http://127.0.0.1:5000&quot;"

# GET - Listar todos os alunos
@app.route("/alunos", methods=["GET"])
def listar_alunos():
    return jsonify(alunos)


@app.route("/alunos", methods=["POST"])
def adicionar_aluno():
    novo_aluno = request.get_json()
    alunos.append(novo_aluno)
    return jsonify({"mensagem": "Aluno adicionado com sucesso!", "aluno": novo_aluno}), 201


@app.route("/alunos/<int:id>", methods=["PUT"])
def atualizar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({"mensagem": "Aluno atualizado!", "aluno": aluno})
    return jsonify({"erro": "Aluno não encontrado!"}), 404


@app.route("/alunos/<int:id>", methods=["DELETE"])
def deletar_aluno(id):
    for aluno in alunos:
        if aluno["id"] == id:
            alunos.remove(aluno)
            return jsonify({"mensagem": "Aluno removido com sucesso!"})
    return jsonify({"erro": "Aluno não encontrado!"}), 404



API_URL = "http://127.0.0.1:5000/alunos&quot;"

def menu():
    time.sleep(1)  
    while True:
        print("\n===== 📚 MENU API DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Adicionar aluno")
        print("3 - Atualizar aluno")
        print("4 - Remover aluno")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resposta = requests.get(API_URL)
            print("\nAlunos cadastrados:", resposta.json())

        elif opcao == "2":
            id = int(input("ID: "))
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            novo_aluno = {"id": id, "nome": nome, "idade": idade}
            resposta = requests.post(API_URL, json=novo_aluno)
            print(resposta.json())

        elif opcao == "3":
            id = int(input("ID do aluno para atualizar: "))
            nome = input("Novo nome (ou Enter p/ manter): ")
            idade = input("Nova idade (ou Enter p/ manter): ")
            dados = {}
            if nome: dados["nome"] = nome
            if idade: dados["idade"] = int(idade)
            resposta = requests.put(f"{API_URL}/{id}", json=dados)
            print(resposta.json())

        elif opcao == "4":
            id = int(input("ID do aluno a remover: "))
            resposta = requests.delete(f"{API_URL}/{id}")
            print(resposta.json())

        elif opcao == "0":
            print(" Encerrando menu...")
            break
        else:
            print("Opção inválida! Tente novamente por favor.")



if __name__ == "__main__":
    
    t = threading.Thread(target=lambda: app.run(debug=False, use_reloader=False))
    t.daemon = True
    t.start()

    
    menu()




from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'rf_fitness_secret_key'

@app.route('/', methods=['GET', 'POST'])
def etapa1():
    if request.method == 'POST':
        session['nome'] = request.form['nome']
        session['email'] = request.form['email']
        session['telefone'] = request.form['telefone']
        return redirect(url_for('etapa2'))
    return render_template('index.html')

@app.route('/etapa2', methods=['GET', 'POST'])
def etapa2():
    if request.method == 'POST':
        session['peso'] = request.form['peso']
        session['altura'] = request.form['altura']
        session['objetivo'] = request.form['objetivo']
        return redirect(url_for('obrigado'))
    return render_template('etapa2.html')

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

if __name__ == '__main__':
    app.run(debug=True)








