import random

# Banco de palavras no formato {palavra:dica}
banco_palavras = {'banana': 'fruta', 'brasil': 'país', 'salto em distancia': 'esporte'}

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

# Sorteia uma palavra do banco de palavras e mostra uma dica
palavra_sorteada = random.choice(list(banco_palavras.keys()))
print(f'A dica é: {banco_palavras[palavra_sorteada]}')
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
letra_usuario = input(f'Escolha uma letra! As letras que já foram escolhidas são {letras_escolhidas} ').lower()

# Valida a entrada do usuário
while letra_usuario not in 'abcdefghijklmnopqrstuvwxyz' or letra_usuario in letras_escolhidas:
   if letra_usuario not in 'abcdefghijklmnopqrstuvwxyz': # Casos em que o usuário não digitou uma letra do alfabeto
      letra_usuario = input(f'Ops! Você não digitou uma letra do alfabeto. Tente novamente, por favor. As letras que já foram escolhidas são {letras_escolhidas}').lower()
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