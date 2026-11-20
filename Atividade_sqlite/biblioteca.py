import sqlite3
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()
print("Banco conectado!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo TEXT NOT NULL,
autor TEXT,
ano INTEGER,
disponivel INTEGER)
""")


livros = [

    (1, "O Estrangeiro", "Albert Camus", 1942, 1),
    (2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 1),
    (3, "Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, 0),
    (4, "As Vinhas da Ira", "John Steinbeck", 1939, 0),
    (5, "Dom Quixote", "Miguel de Cervantes", 1605, 1)
]

cursor.executemany(
    "INSERT INTO livros (id, titulo, autor, ano, disponivel) VALUES (?, ?, ?, ?, ?)", 
    livros,
)

conexao.commit()



cursor.execute(
"UPDATE livros SET disponivel = ? WHERE id = ?",
(0, 1)
)



conexao.commit()













