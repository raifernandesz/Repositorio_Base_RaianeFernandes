import requests

pegar = requests.get("http://172.25.253.124:5000/alunos")
print('Status_code', pegar.status_code)


dados = {
    "nome": 'Raiane Fernandes ',
    "email": 'raifernandes@gmail.com',
}

response = requests.post('http://172.25.253.124:5000/alunos' , json = dados)


print('Dados enviados!')
print(response.json())






import requests
url = ("http://172.25.253.124:5000/put_alunos")

dados = {
    "nome": 'Raiane Fernandes ',
    "email": 'raifernandes@gmail.com',
}

id = 7

response = requests.put(f"{url}/{id}", json = dados)
print(response.status_code) 











