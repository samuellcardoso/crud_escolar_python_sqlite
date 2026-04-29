import sqlite3
import csv
import datetime

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Criacao do Banco e Tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome VARCHAR(150) NOT NULL,
        idade INTEGER
        );
''')

# Insercao de Registros
def cadastro_alunos():
    while True:
        nome = input('Informe o nome:\n').lower().strip()
        if not nome.replace(' ', '').isalpha():
            print('Erro... Somente letras.')
            continue
        try:
            idade = int(input('Informe sua idade:\n'))
        except ValueError:
            print('Erro... Somente numeros.')
            continue
        
        if not (0 < idade < 100):
            print('Erro... Idade invalida.')
            continue
            
        cursor.execute('''
            INSERT INTO alunos(nome, idade) 
            VALUES (?, ?);
        ''', (nome, idade))
        
        conn.commit()
        print(f'Aluno {nome} cadastrado com sucesso.\n')

        confirma = input('Continuar o cadastro? (s/n)\n').lower().strip()
        if confirma == 'n':
            break

# Atualizacao de Dados
def atualiza_dados():
    while True:
        nome = input('Informe o nome para atualizar:\n').lower().strip()
        if not nome.replace(' ', '').isalpha():
            print('Erro... Somente letras.')
            continue
        try:
            idade = int(input('Nova idade:\n'))
        except ValueError:
            print('Erro... Somente numeros.')
            continue
        
        if not (0 < idade < 100):
            print('Erro... Idade invalida')
            continue
        
        cursor.execute('''
            UPDATE alunos SET idade = ? WHERE nome LIKE ?;
                    ''', (idade, f'%{nome}%'))
        
        if cursor.rowcount == 0:
            print('Nenhum aluno encontrado para atualizar.')
        else:
            print(f'{cursor.rowcount} registros(s) atualizados(s).')
        
        conn.commit()

        confirma = input('Continuar a atualizacao? (s/n)\n').lower().strip()
        if confirma == 'n':
            break        

# Exclusao de Registros
def excluir_aluno():
    while True:
        nome = input('Informe o nome para excluir:\n').lower().strip()
        if not nome.replace(' ', '').isalpha():
            print('Erro... Somente letras.')
            continue
        
        confirma = input(f'Tem certeza que deseja excluir {nome}? (s/n)\n').lower().strip()
        if confirma != 's':
            print('Exclusao cancelada.')
            continue
        
        cursor.execute('''
            DELETE FROM alunos WHERE nome LIKE ?; 
                    ''', (f'%{nome}%',))
        
        if cursor.rowcount == 0:
            print('Nenhum aluno encontrado para excluir.')
        else:
            print(f'{cursor.rowcount} registros(s) excluido(s).')
        
        conn.commit()
        
        continua = input('Deseja excluir outro aluno? (s/n)\n').lower().strip()
        if continua == 'n':
            break 

# Buscar aluno
def buscar_aluno():
    while True:
        nome = input('Informe o nome do aluno para buscar:\n').lower().strip()
        if not nome.replace(' ', '').isalpha():
            print('Erro... Somente letras.')
            continue
        
        cursor.execute('''
            SELECT * FROM alunos WHERE nome LIKE ?;
                    ''', (f'%{nome}%',))
        resultados = cursor.fetchall()
        
        if resultados:
            print(f'Resultados encontrados para: {nome}:\n')
            for aluno in resultados:
                print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}')
        else:
            print(f'Nenhum aluno encontrado com o nome {nome}.')
            
        confirma = input('Buscar outro aluno? (s/n)\n').lower().strip()
        if confirma == 'n':
            break
        
# Listar alunos
def listar_alunos():
    cursor.execute('''
        SELECT * FROM alunos
                   ''')
    resultados = cursor.fetchall()
    if not resultados:
        print('Nenhum aluno cadastrado.')
    else:
        print(f'--- Alunos ---')
        for aluno in resultados:
            print(f'ID: {aluno[0]} | Nome: {aluno[1]} | Idade: {aluno[2]}')

# Exportacao de Dados
def exportar_dados():
    cursor.execute('''
        SELECT * FROM alunos;
                ''')
    dados = cursor.fetchall()
    nome_arquivo = f'alunos_{datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")}.csv'
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as file:
        write = csv.writer(file)
        write.writerow(['id', 'nome', 'idade'])
        write.writerows(dados)
    print('Arquivo "alunos.csv" criado com sucesso.')
    
def fechar_sistema():
    cursor.close()
    conn.close()