import sqlite3
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
print("Banco conectado!")



cursor.execute("DELETE FROM livros WHERE id = ?", (5,))

conexao.commit()



#show 