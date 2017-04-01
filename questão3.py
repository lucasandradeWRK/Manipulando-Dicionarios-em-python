produtos = {}
while True:
    opçao = input('''
I)Cadastrar Produto
II)Exibir Produtos
III)Excluir Produtos
IV)Produto Mais Caro
V)Produto Mais Barato

Informe A Letra Da Opção Desejada:
''').upper()




    def cadastrarProduto(produtos, produto_cad, preço_cad):
        produtos[produto_cad] = preço_cad
    def exibirProdutos(produtos):
        for produto in produtos:
            cadaProduto = produtos[produto]
            print(produto, '=', cadaProduto)
    def removerProduto(produtos, excluir_prod):
        del produtos[excluir_prod]
    def exibirCaroProduto(produtos):
        produto_caro = max(produtos, key=produtos.get)
        preço_caro = produtos[produto_caro]
        print('o produto mais caro:', produto_caro, 'com valor de', preço_caro)
    def exibirBaratoProduto(produtos):
        produto_caro = min(produtos, key=produtos.get)
        preço_caro = produtos[produto_caro]
        print('o produto mais barato:', produto_caro, 'com valor de', preço_caro)
        
    if opçao=='I':
        produto_cad = input('informe o produto que deseja cadastrar ')
        preço_cad = eval(input('informe o preço deste produto '))
        cadastrarProduto(produtos, produto_cad, preço_cad)
    elif opçao=='II':
        exibirProdutos(produtos)
    elif opçao=='III':
        excluir_prod = input('informe o produto a ser excluido ')
        removerProduto(produtos, excluir_prod)
    elif opçao=='IV':
        exibirCaroProduto(produtos)
    else:
        exibirBaratoProduto(produtos)
