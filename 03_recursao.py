# Função que cumprimenta uma pessoa com outras funções dentro dela
def sauda(nome):
    print(f'Olá {nome}!')
    sauda2(nome) # Outra função de saudação
    print(f'Estou indo embora, {nome}.')
    tchau() # Função de despedida

# Função que faz outra saudação à pessoa
def sauda2(nome):
    print(f'Como vai, {nome}?')

# Função que se despede da pessoa
def tchau():
    print('Ok, tchau!')

# Função que calcula o fatorial usando a recursão
def fat(x):
    if x == 1:
        return 1 # Condição para o loop terminar
    else:
        return x * fat(x - 1) # A função "fat" chamando a ela mesma


sauda('Jéssica')
print(fat(5))
