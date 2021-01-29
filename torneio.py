import random

tournaments = []
fighters = []


class Fighter():
    def __init__(self, name, age, weight, strength, belt, style, code):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__strength = strength
        self.__belt = belt
        self.__style = style
        self.__code = code
        self.__fight_power = round((self.__strength/self.__weight)*1000)

    def __repr__(self):
        sep = '-'*34
        out = f'''{sep}
\033[1m-=-=-=-  FICHA DE INSCRIÇÃO  -=-=-=-
Lutador:\033[0m {self.__name}
\033[1mIdade:\033[0m {self.__age}
\033[1mPeso(kg):\033[0m {self.__weight}
\033[1mForça:\033[0m {self.__strength}
\033[1mPoder de luta:\033[0m {self.__fight_power}
\033[1mFaixa:\033[0m {self.__belt}
\033[1mEstilo de luta:\033[0m {self.__style}
\033[1mCódigo de inscrição:\033[0m {self.__code}\n{sep}'''
        return out

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def weight(self):
        return self.__weight

    @property
    def strength(self):
        return self.__strength

    @property
    def fight_power(self):
        return self.__fight_power

    @property
    def belt(self):
        return self.__belt

    @property
    def style(self):
        return self.__style

    @property
    def code(self):
        return self.__code


class Tournament():
    def __init__(self, t_name, t_weight, t_belt, t_style, t_code):
        self.__t_name = t_name
        self.__t_weight = t_weight
        self.__t_belt = t_belt
        self.__t_style = t_style
        self.__t_code = t_code
        self.__t_fighters = []
        self.__t_ranking = {}
        self.__t_fights = {}
        self.__t_weight_range = {}
        for i in t_belt:
            self.__t_weight_range[i] = {}
            self.__t_ranking[i] = {}
            self.__t_fights[i] = {}
            for j in range(len(t_weight)):
                self.__t_weight_range[i][j] = []
                self.__t_ranking[i][j] = {}
                self.__t_fights[i][j] = []

    def __repr__(self):
        sep = '-'*34
        out = f'''{sep}
\033[1m-=-=-=-  FICHA DE TORNEIO  -=-=-=-
Torneio:\033[0m {self.__t_name}
\033[1mCategorias de peso:\033[0m {self.__t_weight}
\033[1mFaixas:\033[0m {self.__t_belt}
\033[1mModalidade de luta:\033[0m {self.__t_style}
\033[1mCódigo de torneio:\033[0m {self.__t_code}\n{sep}'''
        return out

    @property
    def t_name(self):
        return self.__t_name

    @property
    def t_style(self):
        return self.__t_style

    @property
    def t_weight(self):
        return self.__t_weight

    @property
    def t_belt(self):
        return self.__t_belt

    @property
    def t_code(self):
        return self.__t_code

    @property
    def t_fighters(self):
        return self.__t_fighters

    @property
    def t_ranking(self):
        return self.__t_ranking

    @property
    def t_fights(self):
        return self.__t_fights

    @property
    def t_weight_range(self):
        return self.__t_weight_range

    def fight(self, competitor_1, competitor_2):
        if competitor_1.fight_power > competitor_2.fight_power:
            return competitor_1, competitor_2
        else:
            return competitor_2, competitor_1

    def ranking_update(self, winner, loser, i, j):
        self.__t_ranking[i][j][loser][1] += 1  # +1 LOSS
        self.__t_ranking[i][j][winner][0] += 1  # +1 WIN

    def enroll_fighter(self, fighter, i, j):
        self.__t_fighters.append(fighter)
        k = self.__t_weight.index(j)
        self.__t_weight_range[i][k].append(fighter)
        self.__t_ranking[i][k][fighter] = [0, 0]  # WIN/LOSS


def error():
    sep = "_"*20
    print(f'\n{sep}')
    print("A informação inserida não é válida\nPor favor, tente novamente.")
    print(f'{sep}\n')


def no_tournaments():
    sep = "_"*20
    print(f'\n{sep}')
    print("Ainda não foi criado nenhum torneio\nPor favor, retorne ao menu e crie um torneio.")
    print(f'{sep}\n')
    menu_start()


def no_fighters():
    sep = "_"*20
    print(f'\n{sep}')
    print("Ainda não foi cadastrado nenhum lutador\nPor favor, retorne ao menu e registre um lutador.")
    print(f'{sep}\n')
    menu_start()


def menu_start():
    sep = "-=-"*20
    sep2 = "-"*45
    options = ['1', '2', '3', '4']
    print(f'\n{sep}')
    print(f'''\033[1mOlá usuário, bem-vindo ao menu principal!
Para escolher alguma das opções abaixo,
basta digitar o número correspondente.\033[0m
{sep2}
Menu de Torneio (1)
Menu de Lutador (2)
Criar um torneio aleatório (3)
Sair (4)
{sep2}''')
    print(f'{sep}\n')
    choice = input("Por favor, escolha uma opção. ")
    if choice not in options:
        error()
        menu_start()
    elif int(choice) == 1:
        menu_tournament()
    elif int(choice) == 2:
        menu_fighter()
    elif int(choice) == 3:
        random_tournament()
    elif int(choice) == 4:
        quit()


def menu_tournament():
    sep = "-=-"*20
    sep2 = "-"*45
    options = ['1', '2', '3', '4', '5', '6', '7', '8']
    print(f'\n{sep}')
    print(f'''\033[1mMenu de Torneio\033[0m
{sep2}
Criar torneio (1)
Inscrever lutador (2)
Torneios existentes (3)
Ranking de torneio (4)
Lutadores inscritos (5)
Realizar luta (6)
Voltar ao Menu Principal (7)
Sair (8)
{sep2}''')
    print(f'{sep}\n')
    choice = input("Por favor, escolha uma opção. ")
    if choice not in options:
        error()
        menu_tournament()
    elif int(choice) == 1:
        tournament_create()
    elif int(choice) == 2:
        enroll_fighter()
    elif int(choice) == 3:
        show_tournaments()
    elif int(choice) == 4:
        tournament_ranking()
    elif int(choice) == 5:
        show_enrolled_fighters()
    elif int(choice) == 6:
        perform_fight()
    elif int(choice) == 7:
        menu_start()
    elif int(choice) == 8:
        quit()


def menu_fighter():
    sep = "-=-"*20
    sep2 = "-"*45
    options = ['1', '2', '3', '4', '5']
    print(f'\n{sep}')
    print(f'''\033[1m  Menu de Lutador  \033[0m
{sep2}
Cadastro de lutador (1)
Lutadores cadastrados (2)
Informação de lutador (3)
Voltar ao Menu Principal (4)
Sair (5)
{sep2}''')
    print(f'{sep}\n')
    choice = input("Por favor, escolha uma opção. ")
    if choice not in options:
        error()
        menu_fighter()
    elif int(choice) == 1:
        register_fighter()
    elif int(choice) == 2:
        registered_fighters()
    elif int(choice) == 3:
        fighter_info()
    elif int(choice) == 4:
        menu_start()
    elif int(choice) == 5:
        quit()


def register_fighter():
    name = input("Digite o nome do lutador. ").capitalize()
    age = input("Digite a idade do lutador. ")
    belt = input("Digite a cor de faixa do lutador. ").capitalize()
    fight_style = input("Digite o estilo do luta do lutador. ").capitalize()
    check = True
    while check:
        try:
            weight = round(float(input('Digite o peso do lutador. ')))
            check = False
        except:
            error()
    check = True
    while check:
        try:
            strength = int(input("Digite a força do lutador(1 a 100)."))
            check = False
        except:
            error()
        if strength not in range(1, 101):
            check = True
            error()
    code = len(fighters)
    fighter = Fighter(name, age, weight, strength, belt, fight_style, code)
    fighters.append(fighter)
    menu_fighter()


def registered_fighters():
    sep = "-="*20
    sep2 = "-"*45
    if len(fighters) < 1:
        no_fighters()
    else:
        print(f'''\n{sep}\n\033[1m-=-=-=-  LUTADORES CADASTRADOS  -=-=-=-
NOME \t           CÓDIGO DE INSCRIÇÃO\033[0m''')
        for fighter in fighters:
            print(f'''{fighter.name} \t\t\t{fighter.code}
{sep2}''')
    print(f"{sep}")
    menu_fighter()


def fighter_info():
    if len(fighters) < 1:
        no_fighters()
    sep = "-="*20
    sep2 = "-"*45
    print(f'''\n{sep}\n\033[1m-=-=-=-  LUTADORES CADASTRADOS  -=-=-=-
NOME \t           CÓDIGO DE INSCRIÇÃO\033[0m''')
    for fighter in fighters:
        print(f'''{fighter.name} \t\t\t{fighter.code}
{sep2}''')
    print(f"{sep}")
    option = int(input(
        'Digite o código do lutador que deseja ter mais detalhes. O código de inscrição pode ser encontrado na tabela acima. '))
    for fighter in fighters:
        if fighter.code == option:
            print(fighter)
    menu_fighter()


def tournament_create():
    check = True
    name = input('Escolha um nome para seu torneio. ')
    style = (
        input('Agora, defimna a modalidade de luta para seu torneio. ')).capitalize()
    weight_list, belt_list = [], []
    weight_qtd = int(
        input("Escolha quantas categorias de peso o torneio possuirá. "))
    for i in range(weight_qtd):
        while check:
            try:
                weight_min = round(
                    float(input(f'Categoria de peso {i+1}:\nEscolha o peso mínimo para essa categoria (kg). ')))
                weight_max = round(
                    float(input('Escolha o peso máximo para essa categoria (kg). ')))
                break
            except:
                error()
        if weight_min > weight_max:
            weight = [weight_max, weight_min]
        else:
            weight = [weight_min, weight_max]
        weight_list.append(weight)
    while check:
        try:
            belt_qtd = int(
                input('Defina quantas faixas podem participar do torneio. '))
            check = False
        except:
            error()
    for i in range(belt_qtd):
        belt = (input("Defina a cor da faixa. ")).capitalize()
        belt_list.append(belt)
    t_code = len(tournaments)
    tournament = Tournament(name, weight_list, belt_list, style, t_code)
    tournaments.append(tournament)
    menu_tournament()


def enroll_fighter():
    sep = "-="*20
    sep2 = "-"*45
    if len(tournaments) < 1:
        no_tournaments()
    if len(fighters) < 1:
        no_fighters()
    check = True
    while check:
        print(
            f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-\nNOME \t           CÓDIGO DE TORNEIO\033[0m''')
        for tournament in tournaments:
            print(
                f'''{tournament.t_name} \t\t\t{tournament.t_code}\n{sep2}\n{sep}''')
        t_code = int(input(
            'Insira o código do torneio em que deseja fazer a inscrição. Os códigos de torneio podem ser encontrados na tabela acima. '))

        if t_code > (len(tournaments))-1:
            error()
            menu_tournament()

        check = False
    check = True
    while check:
        print(
            f'''\n{sep}\n\033[1m-=-=-=-  LUTADORES CADASTRADOS  -=-=-=-\nNOME \t           CÓDIGO DE INSCRIÇÃO\033[0m''')
        for fighter in fighters:
            print(f'''{fighter.name} \t\t\t{fighter.code}\n{sep2}\n{sep}''')
        code = int(input(
            'Insira o código do lutador que deseja fazer a inscrição. Os códigos de lutador podem ser encontrados na tabela acima. '))

        if code > (len(fighters))-1:
            error()
            menu_tournament()

        check = False
    check = True
    fighter = fighters[code]
    tournament = tournaments[t_code]
    if fighter in tournament.t_fighters:
        print("O lutador em questão já foi inscrito nesse torneio.")
        menu_tournament()

    if fighter.belt not in tournament.t_belt:
        print('Lamento, mas o lutador não possui os requisitos de faixa para participar desse torneio. ')
        menu_tournament()
    else:
        belt = fighter.belt

    weight_l = []
    for i in tournament.t_weight:
        if i[1] > fighter.weight and i[0] <= fighter.weight:
            weight_l.append(i)

    if len(weight_l) > 1:
        for i in range(len(weight_l)):
            print(f'Categoria {i+1}: {weight_l[i][0]}Kg - {weight_l[i][1]}Kg')
        while check:
            try:
                option = int(
                    input("Digite o número da categoria de peso que deseja. "))
                if len(weight_l) >= option:
                    weight = weight_l[option-1]
                    check = False
            except:
                error()
    elif len(weight_l) == 1:
        weight = weight_l[0]
        print(
            f'Inscrito na categoria de peso {weight_l[0][0]} - {weight_l[0][1]}')
    else:
        print('O lutador não possui os requisitos de peso.')
        menu_tournament()
    tournament.enroll_fighter(fighter, belt, weight)
    menu_tournament()


def show_tournaments():
    sep = "-="*20
    sep2 = "-"*45

    if len(tournaments) < 1:
        no_tournaments()
    else:
        print(f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-
NOME \t           CÓDIGO DE TORNEIO\033[0m''')
        for tournament in tournaments:
            print(f'''{tournament.t_name} \t\t\t{tournament.t_code}
{sep2}''')
    print(f"{sep}")
    menu_tournament()


def show_enrolled_fighters():
    sep = "-="*20
    sep2 = "-"*45
    if len(tournaments) < 1:
        no_tournaments()
    else:
        check = True
    while check:
        print(
            f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-\nNOME \t      CÓDIGO DE TORNEIO\033[0m''')
        for tournament in tournaments:
            print(
                f'''{tournament.t_name} \t\t\t\t\t{tournament.t_code}\n{sep2}\n{sep}''')
        t_code = int(input(
            'Insira o código do torneio para ver os lutadores inscritos. Os códigos de torneio podem ser encontrados na tabela acima. '))
        if t_code > (len(tournaments))-1:
            error()
            menu_tournament()
        check = False
    check = True
    tournament = tournaments[t_code]
    print(
        f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-\nNOME DO LUTADOR \t  CÓDIGO DE INSCRIÇÃO\033[0m''')
    for fighter in tournament.t_fighters:
        print(
            f'''{fighter.name} \t\t\t{fighter.code}\n{sep2}\n{sep}''')
    menu_tournament()


def perform_fight():
    sep = "-="*20
    sep2 = "-"*45
    if len(tournaments) < 1:
        no_tournaments()
    else:
        check = True
    while check:
        print(
            f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-\nNOME \t      CÓDIGO DE TORNEIO\033[0m''')
        for tournament in tournaments:
            print(
                f'''{tournament.t_name} \t\t\t   {tournament.t_code}\n{sep2}\n{sep}''')
        t_code = int(input(
            'Insira o código do torneio para ver os lutadores inscritos. Os códigos de torneio podem ser encontrados na tabela acima. '))

        if t_code > (len(tournaments))-1:
            error()
            menu_tournament()
        check = False
    check = True

    tournament = tournaments[t_code]
    print(
        f'''\n{sep}\n\033[1m-=-=-=-  TORNEIO  -=-=-=-\nCOR DA FAIXA \t  CÓDIGO DE FAIXA\033[0m''')
    print(
        f'''033[1m\nCATEGORIA DE PESO\tCÓDIGO DE CATEGORIA\033[0m\n{sep}''')
    for i in range(len(tournament.t_belt)):
        print(f"{i + 1} \t\t\t{tournament.t_belt[i]} ")
    for i in range(len(tournament.t_weight)):
        print(
            f"{i + 1} \t\t\t{tournament.t_weight[i][0]}kg - {tournament.t_weight[i][1]}kg")
    while check:
        try:
            choice_belt = int(
                input("Defina a cor da faixa para a luta digitando o código de faixa")) - 1
            if len(tournament.t_belt) > choice_belt and choice_belt >= 0:
                belt = tournament.t_belt[choice_belt]
                check = False
        except:
            error()

    check = True
    while check:
        try:
            choice_weight = int(
                input("Defina a categoria de peso para a luta digitando o código de categoria. ")) - 1
            if 0 <= choice_weight < len(tournament.t_weight):
                check = False
        except:
            error()
    if len(tournament.t_weight_range[belt][choice_weight]) < 2:
        print(
            "Não foram encontrados competidores suficientes que atendessem os requisitos. ")
        menu_tournament()
    check = True
    print("Os lutadores que atendem os requisitos e podem realizar essa luta são:")
    for i in range(len(tournament.t_weight_range[belt][choice_weight])):
        print(
            f"{i + 1} - {tournament.t_weight_range[belt][choice_weight][i].name}")
    while check:
        try:
            comp1 = abs(int(
                input("Digite o número correspondente ao primeiro lutador: ")) - 1)
            comp2 = abs(int(
                input("Digite o número correspondente ao segundo lutador: ")) - 1)
            if comp1 < len(tournament.t_weight_range[belt][choice_weight]) and comp2 < len(tournament.t_weight_range[belt][choice_weight]):
                competitor_1 = tournament.t_weight_range[belt][choice_weight][comp1]
                competitor_2 = tournament.t_weight_range[belt][choice_weight][comp2]
                check = False
        except:
            error()
    check = True

    print(
        f"Competidores escolhidos!\nA luta já vai começar, aguarde por favor...\nFIGHT: {competitor_1.name} vs {competitor_2.name}")

    winner, loser = tournament.fight(competitor_1, competitor_2)
    print(f"O vencedor do duelo foi {winner.name}\nParabéns pela vitória. ")
    tournament.ranking_update(
        winner, loser, belt, choice_weight)

    menu_tournament()


def tournament_ranking():
    sep = "-="*20
    sep2 = "-"*45
    if len(tournaments) < 1:
        no_tournaments()
    else:
        check = True
    while check:
        print(
            f'''\n{sep}\n\033[1m-=-=-=-  TORNEIOS  -=-=-=-\nNOME \t      CÓDIGO DE TORNEIO\033[0m''')
        for tournament in tournaments:
            print(
                f'''{tournament.t_name} \t\t\t   {tournament.t_code}\n{sep2}\n{sep}''')
        t_code = int(input(
            'Insira o código do torneio para ver os lutadores inscritos. Os códigos de torneio podem ser encontrados na tabela acima. '))

        if t_code > (len(tournaments))-1:
            error()
            menu_tournament()
        check = False
    check = True
    tournament = tournaments[t_code]
    print(
        f'''\n{sep}\n\033[1m-=-=-=-  TORNEIO  -=-=-=-\nCOR DA FAIXA \t  CÓDIGO DE FAIXA\033[0m''')
    print(
        f'''\033[1m\nCATEGORIA DE PESO\tCÓDIGO DE CATEGORIA\033[0m\n{sep}''')
    for i in range(len(tournament.t_belt)):
        print(f"{i + 1} \t\t\t {tournament.t_belt[i]} ")
    for i in range(len(tournament.t_weight)):
        print(
            f"{i + 1} \t\t\t\{tournament.t_weight[i][0]}kg - {tournament.t_weight[i][1]}kg")
    while check:
        try:
            choice_belt = int(
                input("Defina a cor da faixa para visualizar ranking que deseja digitando o código de faixa. ")) - 1
            if choice_belt in range(len(tournament.t_belt)):
                belt = tournament.t_belt[choice_belt]
                check = False
        except:
            error()

    check = True
    while check:
        try:
            choice_weight = int(
                input("Defina a categoria de peso para a luta digitando o código de categoria. ")) - 1
            if choice_weight in range(len(tournament.t_weight)):
                check = False
        except:
            error()
    print(
        f'''\n{sep}\n\033[1m-=-=-=-  RANKING {tournament.t_name.capitalize()}  -=-=-=-\nNOME \t  VITÓRIAS \t DERROTAS \t CÓDIGO DE INSCRIÇÃO\033[0m''')
    for i in range(len(tournament.t_ranking[belt][choice_weight])):
        fighter = tournament.t_weight_range[belt][choice_weight][i]
        print(
            f"{(fighter.name)}\t\t{tournament.t_ranking[faixa][choice_weight][fighter][0]}\t\t{tournament.t_ranking[belt][choice_weight][fighter][1]}\t\t{fighter.code}\n{sep2}\n{sep}")
    menu_tournament()


def random_tournament():

    belts = ["branca", "amarela", "verde", "laranja", "azul",
             "preta", "marrom", "vermelha", "roxa", "coral"]
    martial = ["jiu jitsu", "muay thai", "judo",
               "krav maga", "kung fu", "taekwondo", "karate"]
    names = ['Acacio', 'Jordán'
             'Adriano', 'Cintra'
             'Alicia', 'Franco'
             'Anacleto', 'Valle'
             'Anacleto', 'Velásquez'
             'Anhangüera', 'Martinho'
             'Antônia', 'Carrasco'
             'Arminda', 'Cayado'
             'Branca', 'Cabral'
             'Capitolino', 'Paredes'
             'Caubi', 'Castanheira'
             'Celestina', 'Salgado'
             'Celso', 'Cartaxo'
             'Cláudio', 'Malheiros'
             'César', 'Dâmaso'
             'Delfina', 'Veloso'
             'Duarte', 'Belchior'
             'Dália', 'Grilo'
             'Eduarda', 'Fortunato'
             'Eliseu', 'Grillo'
             'Ema', 'Betancour'
             'Emanuel', 'Javier'
             'Epifânia', 'Rivero'
             'Ernesto', 'Lousã'
             'Esmeralda', 'Bentes'
             'Eunice', 'Franco'
             'Eusébio', 'Barrios'
             'Eva', 'Tristão'
             'Ezequiel', 'Butantã'
             'Fabíola', 'Ruela'
             'Fausto', 'Carvalheira'
             'Felicidade', 'Onofre'
             'Felícia', 'Bautista'
             'Filena', 'Nieto'
             'Firmino', 'Nunes'
             'Flor', 'Ramalho'
             'Flávio', 'Baranda'
             'Frederico', 'Marcondes'
             'Frutuoso', 'Carvalheira'
             'Félix', 'Quadros'
             'Garibaldo', 'Escobar'
             'Gastão', 'Brandán'
             'Gil', 'Curado'
             'Gilberto', 'Antúnez'
             'Godo', 'Penteado'
             'Guilhermina', 'Regalado'
             'Heloísa', 'Grande'
             'Heloana', 'Herrera'
             'Honório', 'Piragibe'
             'Humberto', 'Barrios'
             'Irani', 'Fernández'
             'Itiberê', 'Melgaço'
             'Jordão', 'Eanes'
             'João', 'Carvajal'
             'Juliano', 'Villas'
             'Jónatas', 'Cuaresma'
             'Liliana', 'Espartero'
             'Lorena', 'Correia'
             'Luciano', 'Foquiço'
             'Luciano', 'Jaguaribe'
             'Manuela', 'Betancour'
             'Marli', 'Vega'
             'Martim', 'Carrilho'
             'Matias', 'Hierro'
             'Mauro', 'Tomé'
             'Micaela', 'Amorín'
             'Micaela', 'Igrejas'
             'Moema', 'Gomes'
             'Odilia', 'Varanda'
             'Olga', 'Naves'
             'Otávio', 'Guedes'
             'Palmira', 'Lira'
             'Piedade', 'Simões'
             'Querubim', 'Lacerda'
             'Querubina', 'Estrada'
             'Regina', 'Ferraz'
             'Rita', 'Quintana'
             'Rogério', 'Baldaia'
             'Roquita', 'Quadros'
             'Rosalina', 'Pajares'
             'Salomé', 'Querino'
             'Sancho', 'Batista'
             'Sara', 'Lagos'
             'Serafim', 'Coito'
             'Solano', 'Ipanema'
             'Soraia', 'Athayde'
             'Susana', 'Sabala'
             'Sérgio', 'Rosmaninho'
             'Trajano', 'Ruela'
             'Tália', 'Malta'
             'Ubiratã', 'Torrado'
             'Ulrico', 'Lucena'
             'Vanda', 'Linares'
             'Veridiano', 'Amarante'
             'Veríssimo', 'Frota'
             'Ximeno', 'Freire'
             'Xénia', 'Sobreira'
             'Zara', 'Clementino'
             'Zeferino', 'Pádua'
             'Zita', 'Silveira']

    fighter_qtd = random.randint(0, 180)

    for i in range(fighter_qtd):
        r_fighter = random.choice(names).capitalize()
        r_age = random.randint(15, 70)
        r_weight = round(random.randint(50, 120))
        r_strength = random.randint(1, 100)
        r_belt = random.choice(belts).capitalize()
        r_style = random.choice(martial).capitalize()
        r_code = i
        fighter = Fighter(r_fighter, r_age, r_weight,
                          r_strength, r_belt, r_style, r_code)
        fighters.append(fighter)

    name_t = 'Torneio Aleatório'
    style_t = random.choice(martial)
    weight_list, belt_list = [], []
    weight_qtd = random.randint(1, 8)
    code_t = 0
    for i in range(weight_qtd):
        weight_min = round(
            float(random.randint(50, 120)))
        weight_max = round(
            float(random.randint(50, 120)))
        if weight_min > weight_max:
            weight = [weight_max, weight_min]
        else:
            weight = [weight_min, weight_max]
        weight_list.append(weight)
        belt_t = random.choice(belts).capitalize()
        belt_list.append(belt_t)
    tournament = Tournament(name_t, weight_list, belt_list, style_t, code_t)
    tournaments.append(tournament)
    tournament_r = tournaments[code_t]
    fighter_r = fighters[r_code]

    for i in range(len(r_fighter)):
        fighter_r = fighters[i]
        if fighters[i].style == tournament_r.t_style and fighter[i].belt in tournament_r.t_belt and i[1] > fighter.weight and i[0] <= fighter.weight:
            belt_final = fighter_r.belt
            weight_l.append(i)
            weight_final = weight_l[0]
            tournament_r.enroll_fighter(fighters[i], belt_final, weight_final)

    print('Torneio aleatório criado!')
    menu_start()


if __name__ == "__main__":
    menu_start()
