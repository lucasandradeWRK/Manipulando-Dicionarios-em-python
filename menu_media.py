def menu():
  print('''
I) Adicionar Turma
II) Adicionar Alunos E Notas
III) Calcular Média De Um Aluno
IV) Calcular Média De Uma Turma
  ''')
 

  opçao_menu = input('Informe A Opção Desejada\n').upper()
  import medias_alunos
  if (opçao_menu=='I'):
    turma = input('informe o nome da turma' )
    medias_alunos.adicionarTurma(turma)
    menu()
  elif (opçao_menu=='II'):
    medias_alunos.adicionarAlunoNotas()
    menu()
  elif (opçao_menu=='III'):
    acessar_matri = input('informe a matricula do aluno ')
    medias_alunos.calcularMedia(acessar_matri)
    menu()
  elif (opçao_menu=='IV'):
    medias_alunos.mediaTurma()
    menu()
    
menu()


