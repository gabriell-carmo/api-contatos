import sqlite3

# Conecta ao banco (cria o arquivo se não existir)
conn = sqlite3.connect('teste.db')
cursor = conn.cursor()

# CREATE — cria a tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT
    )
''')

# INSERT — insere dados
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Gabriel", "gabriel@email.com"))
cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", ("Ana", "ana@email.com"))

# SELECT — busca dados
cursor.execute("SELECT * FROM usuarios")
print("Todos os usuários:", cursor.fetchall())

# UPDATE — atualiza dados
cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", ("novo@email.com", 1))

# SELECT após UPDATE
cursor.execute("SELECT * FROM usuarios")
print("Após UPDATE:", cursor.fetchall())

# DELETE — remove dados
cursor.execute("DELETE FROM usuarios WHERE id = 2")

# SELECT após DELETE
cursor.execute("SELECT * FROM usuarios")
print("Após DELETE:", cursor.fetchall())

conn.commit()
conn.close()
print("Banco fechado com sucesso!")