import sqlite3

try:
    banco = sqlite3.connect("petshop.db")

    cursor = banco.cursor()
    print("Banco conectado!")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        especie TEXT,
        tutor TEXT,
        idade INTEGER
    )
    """)

    cursor.execute("""
        INSERT INTO pets (nome, especie, tutor, idade)
        VALUES
        ("Pikachu", "Hamster", "Manoel Gomes", "2"),
        ("Tortuguita", "Tartaruga", "Splinter", "1"),
        ("Uni", "Poney", "Mestre dos magos", "4"),
        ("Megazord", "Cachorro", "Vorcaro", "8"),
        ("Cachorro", "Gato", "Luisa Mel", "5")
    """)
    banco.commit()

    print("\n==============================")
    print("BANCO DE DADOS")
    print("==============================\n")
    cursor.execute("""
        SELECT * FROM pets
    """)

    print("\n==============================")
    print("SOMENTE ESPÉCIE - CACHORRO")
    print("==============================\n")

    cursor.execute("""
        SELECT * FROM pets
        WHERE especie = "Cachorro"
    """)
    print(cursor.fetchall())

    print("\n==============================")
    print("ATUALIZAÇÃO - TUTOR")
    print("==============================\n")

    cursor.execute("""
        UPDATE pets SET tutor = "Zé da manga" WHERE id = 1
    """)
    banco.commit()
    print("O nome do tutor foi atualizado!")

    print("\n==============================")
    print("EXCLUSÃO - PET")
    print("==============================\n")

    cursor.execute("DELETE FROM pets WHERE id = 3")
    banco.commit()
    print("O pet foi deletado do banco!")

    print("\n==============================")
    print("EXTRA - NOME E TUTOR")
    print("==============================\n")

    cursor.execute("""
        SELECT nome, tutor FROM pets
        WHERE especie = "Cachorro"
    """)
    print(cursor.fetchall())

    cursor.execute("""
        DELETE FROM pets 
        WHERE rowid NOT IN (
            SELECT MIN(rowid)
            FROM pets
            GROUP BY nome
        )
    """)
    
except sqlite3.Error as erro:
    print("Erro no banco de dados:", erro)
    
    
finally:
    if banco is not None:
        banco.close()

