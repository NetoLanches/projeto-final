import sqlite3
import pandas as pd

conn = sqlite3.connect("banco_sono.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pessoas (
    id_pessoas INTEGER PRIMARY KEY AUTOINCREMENT,
    genero TEXT NOT NULL,
    idade INTEGER NOT NULL,
    profissao TEXT NOT NULL,
    duracao_sono DECIMAL NOT NULL,
    qualidade_sono INTEGER NOT NULL,
    atividade_fisica INTEGER NOT NULL,
    nivel_estresse INTEGER NOT NULL,
    nivel_IMC TEXT NOT NULL,
    pressao_sanguinea DECIMAL(5, 2) NOT NULL,
    taxa_batimentos INT NOT NULL,
    passos_diarios INT NOT NULL,
    condicao_sono TEXT
)
''')

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
cursor.execute('SELECT COUNT(*) FROM pessoas')
if cursor.fetchone()[0] == 0:
    for _, linha in df.iterrows():
        cursor.execute('''
            INSERT INTO pessoas 
            (id_pessoas, genero, idade, profissao, duracao_sono, qualidade_sono, atividade_fisica,
            nivel_estresse, nivel_IMC, pressao_sanguinea, taxa_batimentos, passos_diarios, condicao_sono) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (linha['Person ID'], linha['Gender'], linha['Age'], linha['Occupation'], linha['Sleep Duration'], linha['Quality of Sleep'], linha['Physical Activity Level'],
            linha['Stress Level'], linha['BMI Category'], linha['Blood Pressure'], linha['Heart Rate'], linha['Daily Steps'], linha['Sleep Disorder']))


cursor.execute('''
UPDATE pessoas
SET nivel_IMC = 'Normal'
WHERE nivel_IMC = 'Normal Weight';
''')

cursor.execute('''
UPDATE pessoas
SET condicao_sono = 'Normal'
WHERE condicao_sono IS NULL;
''')

conn.commit()
conn.close()

