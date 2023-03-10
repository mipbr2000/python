Segue um exemplo de script em Python que busca por uma palavra em uma tabela MySQL com as colunas `filename` e `text`, retornando o nome do arquivo e a linha do texto contendo a palavra:

```
import mysql.connector

# Conecta ao banco de dados
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()

# Define a palavra a ser buscada
search_word = 'exemplo'

# Executa a busca na tabela
sql = "SELECT file_name, text FROM pdf_files WHERE text LIKE '%{}%'".format(search_word)
mycursor.execute(sql)

# Itera sobre os resultados e imprime o nome do arquivo e a linha do texto contendo a palavra
for result in mycursor.fetchall():
    file_name = result[0]
    text = result[1]
    for line in text.split('\\n'):
        if search_word in line:
            print('Arquivo: {}'.format(file_name))
            print('Linha: {}'.format(line))

```

Lembre-se de substituir as informações de conexão ao banco de dados (`host`, `user`, `password` e `database`) pelas informações corretas do seu banco de dados. Além disso, substitua a palavra `exemplo` pela palavra que você deseja buscar na tabela.

Espero que isso ajude!
