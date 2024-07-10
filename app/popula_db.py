import sqlite3


def popula_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DELETE FROM produtos")
    c.execute("DELETE FROM users")

    usuarios = [
        ('Ricardo', 'black533', 'admin'),
        ('Maria', 'senha123', 'cliente'),
        ('João', 'joao123', 'cliente'),
        ('Ana', 'ana123', 'cliente'),
        ('Paulo', 'paulo123', 'vendedor'),
        ('Carla', 'carla123', 'cliente'),
        ('Marcos', 'marcos123', 'vendedor'),
        ('Fernanda', 'fernanda123', 'cliente'),
        ('Lucas', 'lucas123', 'cliente'),
        ('Juliana', 'juliana123', 'cliente'),
        ('Gustavo', 'gustavo123', 'cliente'),
        ('Camila', 'camila123', 'cliente'),
        ('Rodrigo', 'rodrigo123', 'vendedor'),
        ('Beatriz', 'beatriz123', 'cliente'),
        ('Felipe', 'felipe123', 'cliente'),
        ('Larissa', 'larissa123', 'cliente'),
        ('Thiago', 'thiago123', 'cliente'),
        ('Patrícia', 'patricia123', 'cliente'),
        ('Rafael', 'rafael123', 'cliente'),
        ('Bruna', 'bruna123', 'cliente')
    ]

    for usuario in usuarios:
        c.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", usuario)

    produtos = [
        ('Cadeira de Escritório', 'Descrição do Produto 1', 'R$ 10,00', '/static/img/cadeira_de_escritorio.jpg'),
        ('Cavalete de Madeira', 'Descrição do Produto 2', 'R$ 20,00', '/static/img/cavalete_madeira.jpg'),
        ('Espelho Color Preto', 'Descrição do Produto 3', 'R$ 30,00', '/static/img/espelho_color_preto.jpg'),
        ('Kit Vaso Sanitário', 'Descrição do Produto 4', 'R$ 40,00', '/static/img/kit_vaso_sanitario.jpeg'),
        ('Banqueta Plástica', 'Descrição do Produto 5', 'R$ 50,00', '/static/img/banqueta_plastica.jpg'),
        ('Poltrona Reclinável', 'Descrição do Produto 6', 'R$ 60,00', '/static/img/poltrona_reclinavel.jpg')
    ]

    for produto in produtos:
        c.execute("INSERT OR IGNORE INTO produtos (nome, descricao, preco, imagem) VALUES (?, ?, ?, ?)", produto)

    conn.commit()
    conn.close()
