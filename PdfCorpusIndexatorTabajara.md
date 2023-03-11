# PdfCorpusIndexatorTabajara

## Sobre o projeto

O objetivo do projeto PdfCorpusIndexatorTabajara é criar um script Python capaz de ler todos os arquivos em formato PDF em um diretório específico e armazená-los em um banco de dados MySQL com o nome do arquivo e o texto completo do PDF em formato de texto simples.

## Requisitos

Para usar o PdfCorpusIndexatorTabajara, você precisará instalar as seguintes bibliotecas Python:

- pdfminer.six
- mysql-connector-python

Você pode instalá-las usando o `pip`, executando os seguintes comandos:

```
pip install pdfminer.six
pip install mysql-connector-python

```

Certifique-se de que o Python e o MySQL estejam instalados e configurados corretamente antes de executar o script.

## Como usar

1. Defina o diretório onde os arquivos PDF estão armazenados no seguinte trecho de código:

```
pdf_dir = '/path/to/pdf/files'

```

1. Certifique-se de que a tabela "pdf_files" exista no banco de dados. Caso contrário, crie a tabela com as seguintes informações:

```
CREATE TABLE pdf_files (
  id INT AUTO_INCREMENT PRIMARY KEY,
  file_name VARCHAR(255),
  text LONGTEXT
)

```

1. Execute o script e verifique se os dados foram inseridos corretamente na tabela.

## Buscando palavras em uma tabela

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
    for line in text.split('\\\\n'):
        if search_word in line:
            print('Arquivo: {}'.format(file_name))
            print('Linha: {}'.format(line))

```

Lembre-se de substituir as informações de conexão ao banco de dados (`host`, `user`, `password` e `database`) pelas informações corretas do seu banco de dados. Além disso, substitua a palavra `exemplo` pela palavra que você deseja buscar na tabela.

## Instalando o MySQL no Linux

Para instalar o MySQL no Linux, siga os seguintes passos:

1. Abra o terminal e atualize a lista de pacotes do sistema:

```
sudo apt-get update

```

1. Instale o MySQL Server:

```
sudo apt-get install mysql-server

```

1. Durante a instalação, você será solicitado a definir uma senha para o usuário root do MySQL. Certifique-se de escolher uma senha segura e anotá-la em algum lugar seguro.
2. Depois que a instalação for concluída, verifique se o serviço do MySQL está em execução:

```
systemctl status mysql

```

1. Se o serviço não estiver em execução, inicie-o:

```
sudo systemctl start mysql

```

1. Para garantir que o serviço do MySQL seja iniciado automaticamente sempre que o sistema for iniciado, execute o seguinte comando:

```
sudo systemctl enable mysql

```

1. Se você precisar acessar o banco de dados MySQL a partir de um computador remoto, você precisará permitir conexões remotas para o usuário root. Para fazer isso, abra o arquivo `mysqld.cnf`:

```
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf

```

1. Encontre a linha que começa com `bind-address` e comente-a adicionando um `#` no início da linha:

```
#bind-address = 127.0.0.1

```

1. Salve e feche o arquivo.
2. Reinicie o serviço do MySQL para aplicar as alterações:

```
sudo systemctl restart mysql

```

Depois de seguir esses passos, o MySQL deve estar instalado e em execução no seu sistema Linux.

O usuário e senha padrão do MySQL podem variar dependendo da distribuição do sistema operacional e do método de instalação. No entanto, o usuário padrão do MySQL é geralmente `root` e a senha padrão é `password`. É altamente recomendável alterar a senha padrão após a instalação do MySQL para aumentar a segurança do sistema.

# Antes de conectar será preciso alterar algumas coisas

PdfCorpusIndexatorTabajara
Sobre o projeto
O objetivo do projeto PdfCorpusIndexatorTabajara é criar um script Python capaz de ler todos os arquivos em formato PDF em um diretório específico e armazená-los em um banco de dados MySQL com o nome do arquivo e o texto completo do PDF em formato de texto simples.
Requisitos
Para usar o PdfCorpusIndexatorTabajara, você precisará instalar as seguintes bibliotecas Python:
pdfminer.six
mysql-connector-python
Você pode instalá-las usando o pip, executando os seguintes comandos:

```
sudo mysql && sudo mysql -u root

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'sua_senha';
CREATE USER 'pdftabajara'@localhost IDENTIFIED BY 'pdftabajara';
GRANT ALL PRIVILEGES ON *.* TO 'pdftabajara'@'localhost';
```

## Conectando a uma instância do MySQL

Para conectar a uma instância do MySQL, você pode usar a biblioteca `mysql.connector` do Python. Aqui está um exemplo de código que estabelece uma conexão com um servidor MySQL, cria um banco de dados e uma tabela:

```
import mysql.connector

# Conecta ao servidor MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="seu_usuario",
  password="sua_senha"
)

# Cria um banco de dados chamado "meu_banco_de_dados"
mycursor = mydb.cursor()
mycursor
```
