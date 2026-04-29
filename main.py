import db

def menu():
    opcoes = [
        'Cadastrar aluno',
        'Atualizar dados',
        'Excluir aluno',
        'Buscar aluno',
        'Listar alunos',
        'Exportar dados',
        'Sair'
    ]

    while True:
        print('--- Sistema Escolar ---')
        print('-'*30)
        for i, opcao in enumerate(opcoes, start=1):
            print(f'{i}-{opcao}')
        print('-'*30)
        
        print('Escolha uma das opcoes:')
        try:
            choice = int(input('> '))
        
            if choice == 1:
                db.cadastro_alunos()
            elif choice == 2:
                db.atualiza_dados()
            elif choice == 3:
                db.excluir_aluno()
            elif choice == 4:
                db.buscar_aluno()
            elif choice == 5:
                db.listar_alunos()
            elif choice == 6:
                db.exportar_dados()
            elif choice == 7:
                print('Fechando sistema.')
                db.fechar_sistema()
                break
            else:
                print('Opcao invalida!')
        except ValueError:
            print('Erro... Digite o numero da opcao.')
menu()