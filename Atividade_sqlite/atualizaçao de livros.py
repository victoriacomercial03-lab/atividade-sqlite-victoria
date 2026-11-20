import sqlite3
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
print("Banco conectado!")



cursor.execute(
"UPDATE livros SET disponivel = ? WHERE id = ?",
(0, 1)
)
conexao.commit()