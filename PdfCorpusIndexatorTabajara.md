# PdfCorpusIndexatorTabajara

Este documento descreve as etapas necessárias para criar um script Python capaz de ler todos os arquivos em formato PDF em um diretório específico e armazenar em um banco de dados MySQL o nome do arquivo e o texto completo do PDF em formato de texto simples.

## Etapas

Para criar o script, siga as seguintes etapas:

1. Importe as bibliotecas necessárias:

```
import os
import mysql.connector
from pdfminer.high_level import extract_text

```

1. Defina as informações do banco de dados:

```
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()

```

1. Defina o diretório onde estão os arquivos PDF:

```
pdf_dir = '/path/to/pdf/files'

```

1. Percorra todos os arquivos no diretório e extraia o nome do arquivo e o texto do PDF:

```
for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        # Extrai o texto do PDF
        text = extract_text(os.path.join(pdf_dir, filename))
        # Insere o nome do arquivo e o texto do PDF no banco de dados
        sql = "INSERT INTO pdf_files (file_name, text) VALUES (%s, %s)"
        val = (filename, text)
        mycursor.execute(sql, val)
        mydb.commit()

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

Com essas etapas, você será capaz de criar um script Python capaz de ler todos os arquivos em formato PDF em um diretório específico e armazená-los em um banco de dados MySQL com o nome do arquivo e o texto completo do PDF em formato de texto simples.

```
import os
import mysql.connector
from pdfminer.high_level import extract_text

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)
mycursor = mydb.cursor()

pdf_dir = '/path/to/pdf/files'

for filename in os.listdir(pdf_dir):
    if filename.endswith('.pdf'):
        text = extract_text(os.path.join(pdf_dir, filename))
        sql = "INSERT INTO pdf_files (file_name, text) VALUES (%s, %s)"
        val = (filename, text)
        mycursor.execute(sql, val)
        mydb.commit()

```

Certifique-se de que a tabela "pdf_files" exista no banco de dados. Caso contrário, crie a tabela com as seguintes informações:

```
CREATE TABLE pdf_files (
  id INT AUTO_INCREMENT PRIMARY KEY,
  file_name VARCHAR(255),
  text LONGTEXT
)

```

Com essas etapas, você será capaz de criar um script Python capaz de ler todos os arquivos em formato PDF em um diretório específico e armazená-los em um banco de dados MySQL com o nome do arquivo e o texto completo do PDF em formato de texto simples.

Para usar o PdfCorpusIndexatorTabajara, você precisará instalar as seguintes bibliotecas Python:

- pdfminer.six
- mysql-connector-python

Você pode instalá-las usando o `pip`, executando os seguintes comandos:

```
pip install pdfminer.six
pip install mysql-connector-python

```

Certifique-se de que o Python e o MySQL estejam instalados e configurados corretamente antes de executar o script.
