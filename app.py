from simple_chalk import chalk
import random

print('********************')
print('Jogo da Adivinhação!')
print('********************')

numero_secreto = random.randint(1,6)
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print('Você tem {} tentativas para adivinhar o número secreto!'.format(chalk.red(total_de_tentativas)))
    print('rodada {} de {}'.format(chalk.green(rodada), chalk.red(total_de_tentativas)))
    chute_str = input('Digite um número de 1 a 6: ')
    chute = int(chute_str)

    acerto = chute == numero_secreto
    maior  = chute >  numero_secreto
    menor  = chute <  numero_secreto

    if(acerto):
        print(chalk.green('Parabéns você mandou bem!'))
        print('O número secreto era: {}'.format(chalk.green(numero_secreto)))
        total_de_tentativas = 0
    else:
        print(chalk.red('Você errou, tente outra vez!'))
        if(menor):
            print('O seu chute foi {} que o número secreto'.format(chalk.yellow('menor')))
        elif(maior):
            print('O seu chute foi {} que o número secreto'.format(chalk.yellow('maior')))
    rodada = rodada + 1