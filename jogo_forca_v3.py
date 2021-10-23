import random

# Banco de palavras no formato {palavra:dica}
banco_palavras = {'banana': 'fruta', 'brasil': 'país', 'salto em distancia': 'esporte'}


def bemVindo():
   nome = input('Qual o seu nome? ')
   print(f'Bem-vindo(a) {nome}!')
   

def jogarForca(banco_palavras=banco_palavras):
   figuras_forca = ["""
                    _______
                    |      |
                    |      
                    |     
                    |     
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     
                    |     
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     /
                    |     
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     /|
                    |     
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     /|\\
                    |     
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     /|\\
                    |     / 
                   _|__
                """, """
                    _______
                    |      |
                    |      O
                    |     /|\\
                    |     / \\
                   _|__
                """]

   
   # INICIO DO JOGO
   quant_erros = 0
   quant_acertos = 0

   # Sorteia uma palavra do banco de palavras e mostra uma dica
   palavra_sorteada = random.choice(list(banco_palavras.keys()))
   print('Vamos começar o jogo!')
   print(f'A dica é: {banco_palavras[palavra_sorteada]}')
   # Monta os "traços" que representam a palavra
   tracos = ''
   for letra in palavra_sorteada:
      if letra == ' ':
         tracos += ' '
      else:
         tracos += '-'
   print(f'{figuras_forca[quant_erros]} Resposta: {tracos}')
   print(palavra_sorteada)

   # Recebe uma letra do usuário
   letras_escolhidas = []

   # Continuar pedindo uma letra enquanto ainda permitir erros e se o usuário já não tiver acertado a palavra
   while quant_erros < len(figuras_forca)-1 and '-' in tracos : 
      letra_usuario = input(f'Escolha uma letra! As letras que já foram escolhidas são {letras_escolhidas}. ').lower()

      # Valida a entrada do usuário
      while letra_usuario not in 'abcdefghijklmnopqrstuvwxyz' or letra_usuario in letras_escolhidas or len(letra_usuario) != 1:
         if letra_usuario not in 'abcdefghijklmnopqrstuvwxyz': # Casos em que o usuário não digitou uma letra do alfabeto
            letra_usuario = input(f'Ops! Você não digitou uma letra do alfabeto. Tente novamente, por favor. As letras que já foram escolhidas são {letras_escolhidas}').lower()
         elif len(letra_usuario) != 1:
            letra_usuario = input(f'Ops! Você digitou mais de uma letra. Digite apenas uma letra, por favor. As letras que já foram escolhidas são {letras_escolhidas}').lower()
         else: # Casos em que o usuário digitou uma letra que já saiu
            letra_usuario = input(f'Ops! Você já escolheu essa letra! Escolha uma outra, por favor. As letras que já foram escolhidas são {letras_escolhidas} ').lower()

      letras_escolhidas.append(letra_usuario)

      # Verifica se o usuário acertou a letra ou não
      if letra_usuario in palavra_sorteada:
         tracos = list(tracos) # Transformar a string de traços em uma lista para poder alterá-la
         print('Você acertou uma letra!')
         for i in range(len(palavra_sorteada)):
            if palavra_sorteada[i] == letra_usuario: # Onde estiver a letra correta, substituir o traço pela letra
               tracos[i] = letra_usuario 
         tracos = ''.join(tracos) # Transformando de volta os traços para string
      else:
         quant_erros += 1
         print('Você errou a letra :(')
      print(f'{figuras_forca[quant_erros]} Resposta: {tracos}')

   # Se saiu do while, é porque o usuário ganhou o jogo ou perdeu. Abaixo, verificamos a vitória/derrota:
   if quant_erros == len(figuras_forca)-1:
      print('Você perdeu o jogo :(')
   else:
      print('Parabéns! Você ganhou o jogo!!!')


def continua_jogo():
   # Verificar se o usuário quer continuar o jogo
   continuar_jogo = input('Você quer jogar novamente? (S/N) ').upper()
   while continuar_jogo != 'S' and continuar_jogo != 'N':
      print('Digite uma opção válida.')
      continuar_jogo = input('Você quer jogar novamente? (S/N) ').upper()
   return continuar_jogo 

bemVindo()
jogarForca()
continuar = continua_jogo()
while continuar == 'S':
   jogarForca()
   continuar = continua_jogo()
   
# Finalizar
print('Obrigada por jogar! :)')
