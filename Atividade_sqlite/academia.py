import sqlite3

try:
    #Abre o banco
    banco = sqlite3.connect("academia.db")

    #cria o cursor para executar os comandos SQL
    cursor = banco.cursor()
    print("Banco conectado!")

    #Criando a tabela
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS membros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        plano TEXT,
        mensalidade REAL,
        ativo INTEGER
    )
    """)

    #Adicionando os membros
    cursor.execute("""
        INSERT INTO membros (nome, plano, mensalidade, ativo)
        VALUES
        ("Bitelo", "Anual", "2600", "1"),
        ("Chuck Noris", "Trimestral", "800", "1"),
        ("Ice Cube", "Mensal", "300", "0"),
        ("Snoop Dog", "Anual", "2600", "0"),
        ("Fat Joe", "Trimestral", "800", "1")
    """)
    banco.commit()

    #Mostra todos os membros
    print("\n==============================")
    print("BANCO DE DADOS")
    print("==============================\n")
    cursor.execute("""
        SELECT * FROM membros
    """)
    print(cursor.fetchall())

    #Mostra somente membros com plano anual
    print("\n==============================")
    print("SOMENTE PLANO ANUAL")
    print("==============================\n")

    cursor.execute("""
        SELECT * FROM membros
        WHERE plano = "Anual"
    """)
    print(cursor.fetchall())

    #Atualização de cadastro
    print("\n==============================")
    print("ATUALIZAÇÃO - PLANO/MENSALIDADE")
    print("==============================\n")

    cursor.execute("""
        UPDATE membros
        SET plano = "Anual",
            mensalidade = "500"
        WHERE id = 2
    """)
    banco.commit()
    print("O plano do membro foi atualizado!")

    #Excluão de membro
    print("\n==============================")
    print("EXCLUSÃO - MEMBRO")
    print("==============================\n")

    cursor.execute("DELETE FROM membros WHERE id = 3")
    banco.commit()
    print("O membro foi deletado do banco!")

    
    print("\n==============================")
    print("EXTRA - RECEITA MENSAL TOTAL")
    print("==============================\n")

    cursor.execute("""
        SELECT SUM(mensalidade) AS total
        FROM membros
        WHERE plano = "Mensal"
    """)
    print(cursor.fetchall())

    cursor.execute("""
        DELETE FROM membros 
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM membros
            GROUP BY nome
        )
    """)
except sqlite3.Error as erro:
    print("Erro no banco de dados:", erro)
    
    
finally:
    if banco is not None:
        banco.close()