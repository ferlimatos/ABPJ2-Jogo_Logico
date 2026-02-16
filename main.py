pontuacao = 0 # Variável para armazenar a pontuação do usuário
pontuacao_mínima = 80 # Pontuação mínima necessária para aprovação

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
        "resposta": "B"
    },
    {
       "enunciado": "Qual das opções abaixo cria corretamente uma variável inteira em Python?",
       "alternativas": [
            "A) int numero = 5",
            "B) numero = 5",
            "C) numero := int(5)",
            "D) let numero = 5"
       ],
       "resposta": "B"
    },
    {
        "enunciado": "Qual é o tipo da variável x = 3.14?",
        "alternativas": [
            "A) int",
            "B) float",
            "C) string",
            "D) boolean"
        ],
        "resposta": "B"
    },
    {
        "enunciado": "Quando usamos o operador >=, o que estamos verificando?",
        "alternativas": [
            "A) Se um valor é maior que outro",
            "B) Se um valor é menor que outro",
            "C) Se um valor é maior ou igual a outro",
            "D) Se dois valores são diferentes"
        ],
        "resposta": "C"
    },
    {
        "enunciado": "O operador lógico OR retorna verdadeiro quando:",
        "alternativas": [
            "A) Todas as condições são verdadeiras",
            "B) Pelo menos uma condição é verdadeira",
            "C) Todas as condições são falsas",
            "D) Nenhuma condição é avaliada"
        ],
        "resposta": "B"
    }
]

for pergunta in perguntas:
    print("\n" + pergunta["enunciado"])
    
    for alternativa in pergunta["alternativas"]:
        print(alternativa)
    
    resposta_usuario = input("Digite a resposta: ").upper()
    
    if resposta_usuario == pergunta["resposta"]:
        print("Resposta correta!")
        print('Você ganhou 20 pontos!')
        pontuacao += 20
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