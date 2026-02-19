pontuacao = 0 # Variável para armazenar a pontuação do usuário
pontuacao_mínima = 80 # Pontuação mínima necessária para aprovação

print("Olá, seja bem-vindo!\n\n"
      "O Quiz de Python foi criado para que você possa testar seus conhecimentos sobre os conceitos básicos da linguagem por meio de 5 perguntas de múltipla escolha.\n\n"
      "Cada questão vale 20 pontos, totalizando 100 pontos possíveis.\n\n"
      "- Se você obtiver 80 pontos ou mais, estará APROVADO!\n"
      "- Se fizer entre 40 e 79 pontos, ficará de RECUPERAÇÃO. Nesse caso será necessário realizar atividades extras para melhorar sua nota.\n"
      "- Se obtiver 20 pontos ou menos, infelizmente estará REPROVADO e precisará refazer o quiz.\n\n"
      "Boa sorte!")

# Estrutura de perguntas e respostas
perguntas = [
    {
        "enunciado": "O que é Python?",
        "alternativas": [
            "A) Uma linguagem de marcação",
            "B) Uma linguagem de programação interpretada",
            "C) Um sistema operacional",
            "D) Um tipo de banco de dados"
        ],
        "resposta": "B",
        "pontos": 20
    },
    {
       "enunciado": "Qual das opções abaixo cria corretamente uma variável inteira em Python?",
       "alternativas": [
            "A) int numero = 5",
            "B) numero = 5",
            "C) numero := int(5)",
            "D) let numero = 5"
       ],
       "resposta": "B",
       "pontos": 20
    },
    {
        "enunciado": "Qual é o tipo da variável x = 3.14?",
        "alternativas": [
            "A) int",
            "B) float",
            "C) string",
            "D) boolean"
        ],
        "resposta": "B",
        "pontos": 20
    },
    {
        "enunciado": "Quando usamos o operador >=, o que estamos verificando?",
        "alternativas": [
            "A) Se um valor é maior que outro",
            "B) Se um valor é menor que outro",
            "C) Se um valor é maior ou igual a outro",
            "D) Se dois valores são diferentes"
        ],
        "resposta": "C",
        "pontos": 20
    },
    {
        "enunciado": "O operador lógico OR retorna verdadeiro quando:",
        "alternativas": [
            "A) Todas as condições são verdadeiras",
            "B) Pelo menos uma condição é verdadeira",
            "C) Todas as condições são falsas",
            "D) Nenhuma condição é avaliada"
        ],
        "resposta": "B",
        "pontos": 20
    }
]

for pergunta in perguntas:
    print("\n" + pergunta["enunciado"])
    
    for alternativa in pergunta["alternativas"]:
        print(alternativa)
        # print(pergunta["alternativas")
    
    resposta_usuario = input("Digite a resposta: ").upper()
    
    if resposta_usuario == pergunta["resposta"]:
        print("Resposta correta!")
        pontuacao_enunciado = pergunta["pontos"]
        print(f'Você ganhou {pontuacao_enunciado} pontos!')
        pontuacao += pontuacao_enunciado
        
    else:
        print(f"Resposta incorreta. A resposta correta é {pergunta['resposta']}.")

# Total de pontos
print(f'\nSua pontuação final é: {pontuacao} pontos!')

# Verificação de aprovação
if pontuacao >= pontuacao_mínima:
  print("Parabéns! Você foi aprovado no teste!")
elif pontuacao < pontuacao_mínima and pontuacao >= 40:
  print("Você está de recuperação.")
else:
  print("Infelizmente, você foi reprovado.")

print("Obrigado por participar do quiz!")
