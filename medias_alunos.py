def adicionarTurma(turma):
    turmas = {}
    turmas[turma] = 0
    return turmas 
        
        
def adicionarAlunoNotas():
    notas = []
    turma = input('em que turma deseja adicionar o aluno? ')

    matricula = input('Informe A Matricula Do Aluno---> ')
    quant_notas = eval(input('quantidade de notas deste aluno: '))
    for repetidor in range(0, quant_notas):
        nota = eval(input('informe a nota deste aluno '))
        notas.append(nota)
        
    matricula_nota = {}
    matricula_nota[matricula] = notas
    return matricula_nota    
matricula_nota = adicionarAlunoNotas()

def calcularMedia(acessar_matri):
    acumuladora = 0
    contadora = 0
    for cada_nota in matricula_nota[acessar_matri]:
        acumuladora = cada_nota + acumuladora
        contadora = contadora + 1
    media = (acumuladora / contadora)
    print(media)
    return media


def mediaTurma():
   for acessar_matri in matricula_nota.keys():
       calcularMedia(acessar_matri)
       print(acessar_matri, '=', calcularMedia(acessar_matri))



