import sqlite3


conexao = sqlite3.connect("escola.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
idade INTEGER,
curso TEXT
)
""")

print("Banco conectado!")


cursor.execute(
"INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)",
("Maria", 21, "Informática")
)


conexao.commit()