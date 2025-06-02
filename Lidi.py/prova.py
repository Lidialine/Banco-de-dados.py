import sqlite3

conexao = sqlite3.connect("produtos.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Produtos (
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    quantidade INTERGER NOT NULL,
    preco INTERGER NOT NULL
)
""")

for i in range(0,3):
    nome  = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    preco = int(input("Digite o preco: "))

    if preco < 0:
        print("Preco invalido!")
    if preco > 1:
        print("Produto cadastrado com sucesso!")
    cursor. execute("""               
    ("INSERT INTO produtos (nome, quantidade, preco ) VALUES (?, ?, ?)
    """, (nome, quantidade, preco))

#contando estoque
cursor.execute("""
SELECT nome count (*) Produtos
""")

#alterando o preco
cursor.execute("""
UPDATE produtos SET preco = '?' WHERE nome= '?'
""")

#Deletar 
cursor.execute("""
DELETE FROM Produtos
WHERE quantidade = 0
""")

#ordenando estoque 
cursor.execute("""
SELECT nome FROM Produtos WHERE preco ORDER BY
""")
#calculo de vendas
cursor.execute("""
SELECT preco + imposto As preco_total FROM Produtos
""")

cursor.execute("SELECT * FROM Produtos")
print("Estoque atualizado com sucesso!")
dados = cursor.fetchall()

for Produtos in dados:
    print(Produtos)

conexao.commit()

conexao.close()