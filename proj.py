#PROGRAMA PARA CADASTRAR FUNCIONÁRIOS GERANDO UM 'ID' PARA CADA FUNCIONÁRIO NOVO CADASTRADO .
#NO CADASTRO FICAM DADOS BÁSICO COMO: ID, NOME, FUNÇÃO E SALARIO.
#NO MENU DE PESQUISA E POSSIVEL FAZER A BUSCA POR TODOS FUNCIONARIOS CADASTRADOS , BUSCA POR SETOR OU
#BUSCA POR 'ID'.
#E POR ULTIMO E POSSIVEL EXCLUIR FUNCIONÁRIO.

lista_funcionarios = []                                                             
codigo_ID = 0
# .......... fim das variaveis globais ..........

# .......... inicio de cadastrar_funcionario.() ..........
def cadastrar_funcionario(codigo):
  print(40*'-'+'   '+'Menu Cadastrar funcionario'+'   '+40*'-') # nome do menu
  print('Codigo (ID) do Funcionario : {}'.format(codigo)) # print do codigo do funcionario a ser cadastrado
  nome = input('Digite o nome do funcionario(a): ')         # entrada com o nome do funcionario a ser cadastrado
  setor  = input('Digite o setor do funcionario(a): ')      # entrada com o setor do funcionario a ser cadastrado
  salario  = int(input('Digite o salario (R$) do funcionario(a): '))   # entrada com o salario do funcionario a ser cadastrado
  print(50*'-')
  dicionario_funcionario = {'codigo'  : codigo,
                            'nome'    : nome,
                            'setor'   : setor,
                            'salario' : salario}
  lista_funcionarios.append(dicionario_funcionario.copy()) # inclui uma copia do dicionario do funcionario com suas informaçoes na variavel global lista_funcionarios
#.......... Fim de cadastrar funcionario  ..........

# .......... inicio de consultar_funcionario() ..........
def consultar_funcionario():
  print(40*'-'+'   '+'Menu consultar funcionario'+'   '+40*'-') # nome do menu
  while True:  # laço de repetição
    menu_consultar = input('Escolha a Opção desejada:\n'+            #entrada da escolha do menu consultar funcionarios
                       '1 - Consultar TODOS  Funcionarios \n'+       #consultar todos os funcionarios
                       '2 - Consultar Funcionario por CODIGO(ID)\n'+ #consultar funcionario por codigo (ID)
                       '3 - Consultar Funcionario por SETOR\n'+      #consultar funcionario por setor
                       '4 - Retornar\n'+                             #retorna ao menu principal
                       '>>> ')
    if menu_consultar == '1':
      print('Você escolheu Consultar TODOS  Funcionarios')
      for funcionario in lista_funcionarios:                         #varredura em lista de funcionarios com print de todos funcionarios encontrados
        print(50*'-')
        for key, value in funcionario.items():
          print('{} : {}'.format(key, value))
        print(50*'-')

    elif  menu_consultar == '2':
      print('Você escolheu Consultar Funcionario por CODIGO(ID)')
      codigo_selecionado = int(input('Digite o CODIGO(ID) desejado : ')) #entrada com o codigo do funcionario a ser consultado
      for funcionario in lista_funcionarios:                       #varredura em lista de funcionarios com print do funcionario consultado pelo codigo(ID)
        if funcionario['codigo'] == codigo_selecionado:
           print(50*'-')
           for key, value in funcionario.items():
              print('{} : {}'.format(key, value))
           print(50*'-')

    elif  menu_consultar == '3':
      print('Você escolheu Consultar Funcionario por SETOR')
      codigo_selecionado = input('Digite o SETOR desejado : ')     ##entrada com o setor do funcionario a ser consultado
      for funcionario in lista_funcionarios:                       #varredura em lista de funcionarios com print do funcionario consultado pelo setor
        if funcionario['setor'] == codigo_selecionado:
           print(50*'-')
           for key, value in funcionario.items():
              print('{} : {}'.format(key, value))
           print(50*'-')

    elif  menu_consultar == '4':
      return # sai do menu consultar para o menu principal

    else:
      print('***** O P Ç Ã O -- I N V A L I D A *****')
      continue  # volta para o inicio do laço.

#.......... Fim de consultar funcionario  ..........

# .......... inicio de remover_funcionario() ..........
def  remover_funcionario():
  print(40*'-'+'   '+'Menu  remover funcionario'+'   '+40*'-')
  codigo_selecionado = int(input('Digite o CODIGO(ID) do funcionario que deseja remover: '))
  for funcionario in lista_funcionarios:
    if funcionario['codigo'] == codigo_selecionado:
      lista_funcionarios.remove(funcionario)
      print('* FUNCIONARIO REMOVIDO COM SUCESSO **')

#.......... Fim de  remover funcionario  ..........

#........... Inicio do Main .............
print(33*'-'+'   '+'Bem vindo ao RH de Cristian De Oliveira'+'   '+33*'-')   #titulo do programa
while True: # laço do programa principal
  menu_principal = input('Escolha a Opção desejada:\n'+                      #  escolha da opçao desejada
                       '1 - Cadastrar Funcionario\n'+                        #cadastrar funcionario
                       '2 - Consultar Funcionario(s)\n'+                     #consultar funcionario
                       '3 - Remover Funcionario\n'+                          #remover funcionario
                       '4 - Sair\n'+                                         #sair
                       '>>> ')
  if menu_principal == '1':
    codigo_ID = codigo_ID + 1                            #acrescenta  +1 no codigo do funcionario gerado em relaçao ao anterior
    cadastrar_funcionario(codigo_ID)                     #1 = novo cadastro

  elif menu_principal == '2':                            #2 = consulta funcionario
    consultar_funcionario()

  elif menu_principal == '3':                            #3 = remove funcionario
    remover_funcionario()

  elif menu_principal == '4':
    break                                                #4  = encerra o programa.

  else:
    print('***** O P Ç Ã O -- I N V A L I D A *****')
    continue  # volta para o inicio do laço.
