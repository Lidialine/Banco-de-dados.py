import sqlite3

conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	quantidade INTEGER NOT NULL,
	preco REAL NOT NULL
)
""")

for i in range (0,3):
    nome = input("Digite o nome do produto: "),
    quantidade = int(input("Digite a quantidade: ")),
    preco = int(input("Digite o valor: ")),
    cursor.execute("""
    ("INSERT INTO Produtos (nome, quantidade, preco), 
    VALUES """ ('?', '?', '?')),

cursor.execute("SELECT * FROM Produtos")
dados = cursor.fetchall()

for Produtos in dados:
    print(Produtos)

conexao.commit()

conexao.close()