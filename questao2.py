funcionarios = {}
while True:
    opção = input(''' I)Adicionar Funcionário
                  II)Buscar Funcionário
                  III)Exibir Funcionários
                Informe A opção Desejada:  
                  ''').upper()
    def adicionarFuncionario(matricula, nome):
        funcionarios[matricula] = nome
    def buscarFuncionario(matricula):
        print(funcionarios[matricula])
    def exibirFuncionários(funcionarios):
        print(funcionarios.values())

        
    if opção=='I':
        nome = input('informe o nome do funcionario ')
        matricula = input('informe a matricula : ')
        adicionarFuncionario(matricula, nome)
        
    elif opção=='II':
        matricula = input('informe a matricula : ')
        buscarFuncionario(matricula)
        
    else:
        exibirFuncionários(funcionarios)
    
