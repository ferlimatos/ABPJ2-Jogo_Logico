pontuacao = 0 # Variável para armazenar a pontuação do usuário
pontuacao_mínima = 80 # Pontuação mínima necessária para aprovação

# Estrutura de perguntas e respostas
# Pergunta 1
print('O que é Python?')
print('A) Uma linguagem de marcação\n'
      'B) Uma linguagem de programação interpretada\n'
      'C) Um sistema operacional\n'
      'D) Um tipo de banco de dados')
resposta_1 = input('Digite a letra correspondente à resposta correta: ') # Recebe a resposta do usuário
if resposta_1.upper() == "B":
  print('Resposta correta!')
  print('Você ganhou 20 pontos!')
  pontuacao += 20
else:    
  print('Resposta incorreta.\n'
        'A resposta correta é: B) Uma linguagem de programação interpretada.')
  
# Pergunta 2
print('\nQual das opções abaixo cria corretamente uma variável inteira em Python?')
print('A) int numero = 5\n'
      'B) numero = 5\n'
      'C) numero := int(5)\n'
      'D) let numero = 5')
resposta_2 = input('Digite a letra correspondente à resposta correta: ') # Recebe a resposta do usuário
if resposta_2.upper() == "B":
  print('Resposta correta!')
  print('Você ganhou 20 pontos!')
  pontuacao += 20
else:    
  print('Resposta incorreta.\n'
        'A resposta correta é: B) numero = 5.')
  
# Pergunta 3
print('\nQual é o tipo da variável "x" no código: x = 3.14?')
print('A) int\n'
      'B) float\n'
      'C) string\n'
      'D) boolean')
resposta_3 = input('Digite a letra correspondente à resposta correta: ') # Recebe a resposta do usuário
if resposta_3.upper() == "B":
  print('Resposta correta!')
  print('Você ganhou 20 pontos!')
  pontuacao += 20
else:    
  print('Resposta incorreta.\n'
        'A resposta correta é: B) float.')

# Pergunta 4
print('\nQuando usamos o operador ">=", o que estamos verificando?')
print('A) Se um valor é maior que outro\n'
      'B) Se um valor é menor que outro\n'
      'C) Se um valor é maior ou igual a outro\n'
      'D) Se dois valores são diferentes')
resposta_4 = input('Digite a letra correspondente à resposta correta: ') # Recebe a resposta do usuário
if resposta_4.upper() == "C":
  print('Resposta correta!')
  print('Você ganhou 20 pontos!')
  pontuacao += 20
else:    
  print('Resposta incorreta.\n'
        'A resposta correta é: C) Se um valor é maior ou igual a outro.')
  
# Pergunta 5
print('\nO operador lógico "or" retorna verdadeiro quando:')
print('A) Todas as condições são verdadeiras\n'
      'B) Pelo menos uma condição é verdadeira\n'
      'C) Todas as condições são falsas\n'
      'D) Nenhuma condição é avaliada')
resposta_5 = input('Digite a letra correspondente à resposta correta: ') # Recebe a resposta do usuário
if resposta_5.upper() == "B":
  print('Resposta correta!')
  print('Você ganhou 20 pontos!')
  pontuacao += 20
else:    
  print('Resposta incorreta.\n'
        'A resposta correta é: Pelo menos uma condição é verdadeira.')

# Total de pontos
print(f'\nSua pontuação final é: {pontuacao}')

# Verificação de aprovação
if pontuacao >= pontuacao_mínima:
  print("Parabéns! Você foi aprovado no teste!")
elif pontuacao >= 60:
  print("Você está de recuperação.")
else:
  print("Infelizmente, você foi reprovado.")
