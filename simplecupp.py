# Cupp (Common User Passwords Profiler) simples feito por caiorodrgues [https://github.com/caiorodrgues]

GREEN = "\033[0;32m"
RED = "\033[1;31m"
BLUE  = "\033[1;34m"
BOLD = "\033[;1m"
RESET = "\033[0;0m"

print("")
print(GREEN + "░░██▓▓██" + RESET)
print(GREEN + "░██▓▓██" + RESET)
print(GREEN + "░░██▓▓██" + RESET)
print(GREEN + "░░░██▓▓███" + RESET)
print(GREEN + "░░░░██▓▓████" + RESET + "           # Common User Profile Password")
print(GREEN + "░░░░░██▓▓█████" + RESET)
print(GREEN + "░░░░░░██▓▓▓▓██████" + RESET + "     [-- caiorodrgues -- [https://github.com/caiorodrgues] --] ")
print(GREEN + "░░░░░░███▓▓███████" + RESET + "     [-- Obrigado por usar! --]")
print(GREEN + "░░░░░████▓▓████████" + RESET)
print(GREEN + "░░░░█████▓▓█████████" + RESET)
print(GREEN + "░░░█████░░░█████" + RED + "●" + GREEN + "███" + RESET)
print(GREEN + "░░████░░░░░░░███████" + RESET)
print(GREEN + "░░███░░░░░░░░░██████" + RESET)
print(GREEN + "░░██░░░░░░░░░░░████" + RESET)
print(GREEN + "░░░░░░░░░░░░░░░░██" + RESET)
print("")

print(GREEN + "[" + RESET + "!" + GREEN + "]" + RESET + ' Se você não tiver a resposta para alguma das perguntas abaixo, apenas tecle "enter"')

nome = input(GREEN + ">>>" + RESET + " Primeiro nome: ")
if nome == '':
    print(GREEN + "[" + RESET + "!" + GREEN + "]" + RESET + ' Obs: sem o nome, as senhas geradas serão menores e menos efetivas')

# não sabemos quantos sobrenomes serão inseridos <-- separar pelos espaços e armazenar em uma lista
sobrenome = input(GREEN + ">>>" + RESET + " Sobrenome: ").split(' ')

ultsobrenome = sobrenome[len(sobrenome) - 1]
ultimosobrenome = ultsobrenome.lower()

primeirosobrenome = ''
if len(sobrenome) >= 0:
    primeirosobrenome = sobrenome[0]
    primeirosobrenome = sobrenome[0].lower()

if nome != '':
    nome = nome.lower()

# declarando as variáveis como vazias para não dar problema caso a data inteira não seja especificada
ano = ''
dia = ''
mes = ''
nascimento = ''
datanascimento = ''

datanascimento = input(GREEN + ">>>" + RESET + " Data de nascimento ou só o ano (DDMMAAAA) ou (AAAA): ")
if len(datanascimento) == 4:
    ano = datanascimento

elif len(datanascimento) == 8:
    nascimento = datanascimento
    ano = datanascimento[4] + datanascimento[5] + datanascimento[6] + datanascimento[7]
    dia = datanascimento[0] + datanascimento[1]
    mes = datanascimento[2] + datanascimento[3]

if len(nascimento) != 8 and len(datanascimento) != 4 and datanascimento != '':
    print(RED + "[" + RESET + "!" + RED + "]" + RESET + " Data de nascimento não registrada, é aceito apenas 4 ou 8 dígitos")
    # atribuindo um valor "vazio" à variavel para que ela não apareça nas concatenações dos loops mais a frente
    nascimento = ''

apelido = input(GREEN + ">>>" + RESET + " Apelido: ")
if apelido != '':
    apelido = apelido.lower()

pai = input(GREEN + ">>>" + RESET + " Pai: ")
if pai != '':
    pai = pai.lower()

mae = input(GREEN + ">>>" + RESET + " Mãe: ")
if mae != '':
    mae = mae.lower()

filho = input(GREEN + ">>>" + RESET + " Nome do filho: ")
if filho != '':
    filho = filho.lower()

numero = input(GREEN + ">>>" + RESET + " Celular ou telefone (Sem DDD): ")

# declarando as variáveis como vazias para não dar problema caso a data inteira não seja especificada
celular = ''
telefone = ''

if len(str(numero)) == 9:
    telefone = ''
    celular = numero

elif len(str(numero)) == 8:
    celular = ''
    telefone = numero

pet = input(GREEN + ">>>" + RESET + " Nome do pet: ")
if pet != '':
    pet = pet.lower()

time = input(GREEN + ">>>" + RESET + " Time preferido: ")
if time != '':
    time = time.lower()

extra = input(GREEN + "[" + BLUE + "+" + GREEN + "]" + RESET + " Gostaria de adicionar alguma palavra chave extra? Y/[N]: ")
extralower = extra.lower()
if extralower in ['y', 'yes', 'sim', 's', 'yep', 'ye']:
    extra = input(GREEN + ">>>" + RESET + " Palavra chave extra: ")
elif extralower == '' or extralower in ['n', 'no', 'nah', 'nao', 'nao']:
    extra = ''
else:
    print(RED + "[" + RESET + "!" + RED + "]" + RESET + " Opção não válida, palavra chave extra não foi registrado")
    extra = ''

nomearquivo = input(GREEN + "[" + BLUE + "+" + GREEN + "]" + RESET + " Gostaria de dar um nome específico ao arquivo? Y/[N]: ")
nomearquivolower = nomearquivo.lower()
if nomearquivolower in ['y', 'yes', 'sim', 's', 'yep', 'ye']:
    nomearquivo = input(GREEN + ">>>" + RESET + " Digite o nome do arquivo sem espaço/caracteres especiais: ")
elif nomearquivolower in ['n', 'no', 'nah', 'nao', 'nop']:
    nomearquivo = nome

# Daqui pra baixo é as parte que o programa pega as informações e escreve no arquivo de texto

arquivo = open(nomearquivo if nomearquivo != '' else nome if nome != '' else 'cupp', 'w')

arquivo.write(celular + "\n" if celular != '' else '')
if celular != '':
    arquivo.write(celular + nome + "\n")
    arquivo.write(nome + celular + "\n")
    arquivo.write(nome + celular[0] + celular[1] + celular[2] + celular[3] + "\n")
    arquivo.write(nome + celular[0] + celular[1] + celular[2] + celular[3] + celular[4] + "\n")
    arquivo.write(nome + celular[4] + celular[5] + celular[6] + celular[7] + celular[8] + "\n")
    if ano != '':
        arquivo.write(celular + ano + "\n")
    if nascimento != '':
        arquivo.write(celular + nascimento + "\n")
arquivo.write(nome + nascimento + "\n")
if telefone != '':
    arquivo.write(telefone + nome + "\n")
    arquivo.write(nome + telefone + "\n")
    arquivo.write(nome + telefone[0] + telefone[1] + telefone[2] + telefone[3] + "\n")
    arquivo.write(nome + telefone[3] + telefone[4] + telefone[5] + telefone[6] + telefone[7] + "\n")

if nome != '':
    arquivo.write(nome + pet + "\n")
    arquivo.write(nome + dia + mes + "\n")
    arquivo.write(nome + ano + "\n")
    if extra != '':
        arquivo.write(nome + extra + "\n")
        arquivo.write(nome + extra + nascimento + "\n")
        arquivo.write(nome + extra + ano + "\n")
if primeirosobrenome != '' and ano != '':
    arquivo.write(nome + primeirosobrenome + ano + "\n")
    arquivo.write(nome + primeirosobrenome + nascimento + "\n")
    if dia != '' and mes != '' and ano != '':
        arquivo.write(nome + primeirosobrenome + dia + mes + "\n")
        arquivo.write(nome + primeirosobrenome + ano + dia + mes + "\n")
        arquivo.write(nome + primeirosobrenome + ano + mes + dia + "\n")
    if extra != '':
        if dia != '' and mes != '':
            arquivo.write(nome + extra + dia + mes + "\n")
            arquivo.write(nome + extra + ano + dia + mes + "\n")
        if dia != '' and mes != '' and ano != '':
            arquivo.write(nome + extra + ano + mes + dia + "\n")
if apelido != '':
    arquivo.write(apelido + ano + "\n")
    arquivo.write(apelido + nascimento + "\n")
    if dia != '' and mes != '':
        arquivo.write(apelido + dia + mes + "\n")
    arquivo.write(nome + apelido + ano + "\n")
if pai != '':
    arquivo.write(nome + pai + "\n")
    arquivo.write(nome + pai + ano + "\n")
    if dia != '' and mes != '':
        arquivo.write(nome + pai + dia + mes + "\n")
if mae != '':
    arquivo.write(nome + mae + "\n")
    arquivo.write(nome + mae + ano + "\n")
    if dia != '' and mes != '':
        arquivo.write(nome + mae + dia + mes + "\n")
if pai != '' and mae != '':
    arquivo.write(pai + mae + ano + "\n")
    arquivo.write(nome + pai + mae + ano + "\n")
    arquivo.write(mae + pai + ano + "\n")
    arquivo.write(nome + mae + pai + ano + "\n")
if pet != '':
    arquivo.write(nome + pet + "\n")
    arquivo.write(nome + pet + ano + "\n")
    arquivo.write(pet + ano + "\n")
    if nascimento != '':
        arquivo.write(pet + nascimento + "\n")
if time != '':
    arquivo.write(time + ano + "\n")
    arquivo.write(time + nascimento + "\n")
    arquivo.write(nome + time + "\n")
    arquivo.write(nome + time + ano + "\n")
    arquivo.write(nome + time + nascimento + "\n")
if ultimosobrenome != '':
    arquivo.write(nome + ultimosobrenome + nascimento + "\n")
    arquivo.write(nome + ultimosobrenome + ano + "\n")
    arquivo.write(nome + ultimosobrenome + dia + mes + "\n")
    if numero != '':
        arquivo.write(nome + ultimosobrenome + numero + "\n")
        arquivo.write(nome + ultimosobrenome + numero[0] + numero[1] + numero[2] + numero[3] + "\n")
    arquivo.write(ultimosobrenome + nascimento + "\n")
    arquivo.write(ultimosobrenome + ano + "\n")
    arquivo.write(ultimosobrenome + dia + "\n")
    if extra != '':
        if nome != '':
            arquivo.write(nome + ultimosobrenome + extra + "\n")

# leet (1337)
if nome != '':
    # leet simples
    nomeleet = nome
    nomeleet = nomeleet.replace('a', '4')
    nomeleet = nomeleet.replace('o', '0')
    nomeleet = nomeleet.replace('e', '3')
    if ano != '':
        arquivo.write(nomeleet + ano + "\n")
        if nascimento != '':
            arquivo.write(nomeleet + nascimento + "\n")
    if primeirosobrenome != '':
        primeirosobrenomeleet = primeirosobrenome
        primeirosobrenomeleet = primeirosobrenomeleet.replace('a', '4')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('o', '0')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('e', '3')
        if ano != '':
            arquivo.write(primeirosobrenomeleet + ano + "\n")
            arquivo.write(primeirosobrenomeleet + nomeleet + ano + "\n")
        if nome != '':
            arquivo.write(nomeleet + primeirosobrenomeleet + "\n")
            arquivo.write(nomeleet + primeirosobrenomeleet + ano + "\n")

if nome != '':
    # leet mais complexo
    nomeleet = nome
    nomeleet = nomeleet.replace('a', '4')
    nomeleet = nomeleet.replace('o', '0')
    nomeleet = nomeleet.replace('e', '3')
    nomeleet = nomeleet.replace('z', '2')
    nomeleet = nomeleet.replace('t', '7')
    nomeleet = nomeleet.replace('s', '5')
    nomeleet = nomeleet.replace('i', 'l')
    nomeleet = nomeleet.replace('l', '1')

    if ano != '':
        arquivo.write(nomeleet + ano + "\n")
        if nascimento != '':
            arquivo.write(nomeleet + nascimento + "\n")
            
    if primeirosobrenome != '':
        primeirosobrenomeleet = primeirosobrenome
        primeirosobrenomeleet = primeirosobrenomeleet.replace('a', '4')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('o', '0')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('e', '3')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('z', '2')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('t', '7')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('s', '5')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('i', 'l')
        primeirosobrenomeleet = primeirosobrenomeleet.replace('l', '1')

        arquivo.write(nomeleet + primeirosobrenomeleet + "\n")
        if ano != '':
            arquivo.write(nomeleet + primeirosobrenomeleet + ano + "\n")
        if nascimento != '':
            arquivo.write(nomeleet + primeirosobrenomeleet + nascimento + "\n")
        if ultimosobrenome != '':
            arquivo.write(primeirosobrenome + ultimosobrenome + nome + "\n")
            arquivo.write(primeirosobrenome + ultimosobrenome + ano + "\n")
            arquivo.write(primeirosobrenome + ano + "\n")
            arquivo.write(primeirosobrenome + nascimento + "\n")
            arquivo.write(primeirosobrenome + primeirosobrenome + "\n")

if filho != '':
    if nome != '':
        arquivo.write(nome + filho + "\n")
        if ano != '':
            arquivo.write(nome + filho + ano + "\n")
        arquivo.write(filho + ano + "\n")
        arquivo.write(ano + filho + "\n")
    if pet != '':
        arquivo.write(filho + pet + "\n")
        if ano != '':
            arquivo.write(filho + pet + ano + "\n")
            if nascimento != '':
                arquivo.write(filho + pet + nascimento + "\n")
    if mae != '':
        arquivo.write(mae + filho + "\n")

# Invertendo o nome
nomeinvertido = ''
if nome != '':
    for i in range(len(nome)):
        i += 1
        nomeinvertido = nomeinvertido + nome[len(nome) - i]

if nomeinvertido != '':
    if ano != '':
        arquivo.write(nomeinvertido + ano + "\n")
    if nascimento != '':
        arquivo.write(nomeinvertido + nascimento + "\n")
    if sobrenome != '':
        arquivo.write(nomeinvertido + primeirosobrenome + "\n")
        if ano != '':
            arquivo.write(nomeinvertido + primeirosobrenome + ano + "\n")
    