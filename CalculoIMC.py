from time import sleep
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'vermelhoSub':'\033[4;31m'}

print('Ola! Estou aqui para te ajudar a calcular seu IMC.')
nome = input('Antes de começarmos, digite seu nome: ')
print('Ola, {}! Prazer em te conhecer! :)'.format(nome))
print('Vamos prosseguir...')
sleep(1)
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
print('Calculando seu IMC...')
sleep(2)
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Voce esta abaixo do peso ideal!')
elif imc >= 18.5 and imc <= 24.9:
    print('{}Voce esta no peso ideal!{}\nParabens {}!'.format(cores['verde'], cores['limpa'], nome))
    print('Seu IMC é {}{:.2f}{}'.format(cores['verde'], imc, cores['limpa']))
elif imc >= 25 and imc <= 29.9:
    print('{}Voce esta com sobrepeso!{} Recomendo que melhore seus habitors alimentares e pratique mais atividades fisicas {}!'.format(cores['amarelo'], cores['limpa'], nome))
    print('Seu IMC é de {}{:.2f}{}'.format(cores['amarelo'], imc, cores['limpa']))
elif imc >= 30 and imc <= 39.9:
    print('{}Voce esta com obesidade!!{} {}Procure um médico {}!!!{}'.format(cores['vermelho'], cores['limpa'], cores['vermelhoSub'], cores['limpa'], nome))
    print('Seu IMC é de {}{:.2f}{}'.format(cores['vermelho'], imc, cores['limpa']))
else:
    print('{}Voce esta com obesidade grave!! Procure um médico URGENTE!!!{}'.format(cores['vermelhoSub'], cores['limpa']))
    print('Seu IMC é de {}{:.2f}{}'.format(cores['vermelhoSub'], imc, cores['limpa']))