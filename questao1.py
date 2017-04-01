dias = {}
while True:
    opçao = input('''
I)Adicionar dia
II)exibir dia

Informe a opçao desejada:
''').upper()
    def adicionarDia(posicao, dia):
        dias[posicao] = dia
    def exibirDia(dias):
        print(dias)
        return dias

    if opçao=='I':
        dia = input('informe o nome dia que deseja adicionar: ')
        posicao = input('informe a posição deste dia na semana ')
        adicionarDia(posicao, dia)
    else:
        exibirDia(dias)
        
