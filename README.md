# Quiz Python

## Descrição do projeto

O Quiz Python é um programa de perguntas e respostas sobre conceitos básicos da linguagem Python. É um programa executado no terminal que testa conhecimentos iniciais sobre Python por meio de 5 perguntas de múltipla escolha. Cada questão vale 20 pontos, totalizando 100 pontos possíveis. Após as 5 perguntas, o programa mostra a pontuação final.

### 🎯 Sistema de Pontuação

- 80 pontos ou mais → Aprovado
- 40 a 79 pontos → Recuperação
- 20 pontos ou menos → Reprovado
- Pontuação máxima: 100 pontos

Este projeto foi desenvolvido como prática de lógica de programação e fundamentos da linguagem Python.

## Funcionalidades

- Escalabilidade: Perguntas armazenadas em estruturas de dicionários.
- Automação: Processamento automático de perguntas e alternativas via loops.
- Feedback em Tempo Real: Informa se o usuário acertou ou errou imediatamente após cada resposta.
- Normalização de Dados: Tratamento de entradas (maiusculas/minusculas) para evitar erros de digitação.

## Lógica e Variáveis

O sistema foi otimizado para não utilizar variáveis isoladas para cada resposta. Agora, utilizamos:
| Variável | Descrição | Tipo de Dado |
| :--- | :--- | :--- |
| `perguntas` | Lista contendo dicionários com enunciado, opções e resposta correta | `list[dict]` |
| `pontuacao_mínima` | Define a pontuação mínima necessária para aprovação | `int` |
| `pontuacao` | Acumulador de pontos do usuário | `int` |
| `pergunta` | Variável de controle do laço que representa a questão atual | `iterator` |

## Fluxograma do Projeto:

O fluxo agora conta com uma estrutura de repetição que valida cada pergunta antes de seguir para o resultado final:

![Fluxograma](Fluxograma-Quiz-Python.drawio.png)

## Aprendizados

Nesta versão refatorada, os principais conceitos aplicados foram:

- Estruturas de Dados Compostas: Uso de listas e dicionários para organizar informações.
- Laços de Repetição (for loops): Automação da exibição de perguntas e validação de respostas.
- Clean Code: Redução de repetição de código (substituindo múltiplos inputs por um único laço).
- F-strings: Formatação moderna de strings para exibição de resultados e variáveis.

## Como Executar o Projeto

1.  Certifique-se de ter o **Python 3.x** instalado.
2.  Faça o download ou clone este repositório.
3.  Navegue até a pasta do projeto.
4.  Execute o comando: `python main.py`.

## Tecnologias Utilizadas

- Linguagem: Python 3.x
- Ferramentas: VS Code
- Versionamento: Git (Estratégia de Branches para histórico de evolução)
- Modelagem: Draw.io (para o fluxograma)

## Autores

**Fernanda Matos** – Desenvolvimento Web e Mobile – Python Iniciante.
