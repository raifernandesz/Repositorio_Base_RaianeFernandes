

import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco'
hospital = sqlite3.connect('hospital.db')


# Criamos a variavel cursor e colocamos em uma variavel
cursor = hospital.cursor()




# # # update 
##       (Tabela)  coluna | valor alterado | quando acharmos o valor

cursor.execute("SELECT * FROM pacientes WHERE cidade = 'São Paulo';")


hospital.commit()
print(cursor.fetchall())





import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco#'
cinema = sqlite3.connect('cinema.db')


# Criamos a variavel cursor e colocamos em uma variavel
cursor = cinema.cursor()

 # #Criando a tabela funiconarios com os campos necessarios
# cursor.execute("CREATE TABLE filmes(id, titulo, genero, ano, avaliacao)")


# # # Inserindo na tabela desejada os valores 
# cursor.execute("INSERT INTO filmes VALUES(10,'matrix','acao', 1999, 4)")


# # # ENVIANDO OS DADOS 
cinema.commit()


# # PRINTAR A INFORMAÇÃO
cursor.execute("SELECT  ano, avaliacao  From filmes where ano > 2010")
print(cursor.fetchall())






import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco#'
banco = sqlite3.connect('banco.db')


# Criamos a variavel cursor e colocamos em uma variavel
cursor = banco.cursor()

 # #Criando a tabela pessoas com os campos necessarios
# cursor.execute("CREATE TABLE pessoas (nome text,cpf integer,validade DATE, nome_do_produto text, quantidade integer)")


# # # Inserindo na tabela desejada os valores 
cursor.execute("INSERT INTO pessoas VALUES('Raiane', 54726752863, '10/19/25','Creme Seda', 2)")


# # # ENVIANDO OS DADOS 
banco.commit()


# # PRINTAR A INFORMAÇÃO
cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall())





import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco#'
loja = sqlite3.connect('loja.db')


# Criamos a variavel cursor e colocamos em uma variavel
cursor = loja.cursor()

 # #Criando a tabela funiconarios com os campos necessarios
# cursor.execute("CREATE TABLE vendas(id integer, produto text, quantidade integer, preco_unitario integer, cliente text)")


# # # Inserindo na tabela desejada os valores 
#cursor.execute("INSERT INTO vendas VALUES(8,'computador', 1, 1500, 'Joao')")


# # # ENVIANDO OS DADOS 
loja.commit()


# # PRINTAR A INFORMAÇÃO
cursor.execute("SELECT produto,cliente FROM vendas ")
print(cursor.fetchall())






import sqlite3

#Criamos a conexao com o banco e guardamos na variavel 'Banco#'
escola = sqlite3.connect('escola.db')


# Criamos a variavel cursor e colocamos em uma variavel
cursor = escola.cursor()

 # #Criando a tabela pessoas com os campos necessarios
# cursor.execute("CREATE TABLE alunos (id  integer,nome text,idade integer,nota integer , turma text)")


# # # Inserindo na tabela desejada os valores 
cursor.execute("INSERT INTO alunos VALUES(12,'Rai',17,10, 'B')")


# # # ENVIANDO OS DADOS 
escola.commit()


# # PRINTAR A INFORMAÇÃO
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())














