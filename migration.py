import sqlite3

conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(contatos)")
colunas = [col[1] for col in cursor.fetchall()]

if 'favorito' not in colunas:
    cursor.execute('ALTER TABLE contatos ADD COLUMN favorito INTEGER DEFAULT 0')
    print("Coluna 'favorito' adicionada com sucesso!")
else:
    print("Coluna 'favorito' já existe — nenhuma alteração necessária.")

if 'observacao' not in colunas:
    cursor.execute('ALTER TABLE contatos ADD COLUMN observacao TEXT DEFAULT ""')
    print("Coluna 'observacao' adicionada com sucesso!")
else:
    print("Coluna 'observacao' já existe — nenhuma alteração necessária.")

conn.commit()
conn.close()