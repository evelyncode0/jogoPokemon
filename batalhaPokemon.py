# --- IMPORTAÇÕES ---
from term_image.image import from_url
import os #permite que você interaja com o sistema operacional
import sys # permite que você interaja com o interpretador Python
import random #para funções aleatorias
import pygame
from colorama import Fore, Style, init
init(autoreset=True)  #reset automático das cores após cada print
pygame.mixer.init()

def resource_path(relative_path):
    try:
        # Quando o PyInstaller cria um executável, ele armazena os dados
        # em uma pasta temporária, cujo caminho está em sys._MEIPASS.
        base_path = sys._MEIPASS
    except Exception:
        # Se não estiver rodando como executável (ou seja, está em desenvolvimento),
        # o caminho base é o diretório atual
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def tocar_som_fundo():
    pygame.mixer.music.load(resource_path("POKEMON/sons/hgss-johto-trainer.mp3"))
    pygame.mixer.music.set_volume(0.1) # Volume entre 0.0 e 1.0 (20% do volume máximo)
    pygame.mixer.music.play(-1)  # -1 para repetir em loop

# --- POKÉMONS ---

# Pokémon 1: Marowak
p1_nome = "Marowak"
p1_vida = 100
p1_ataque1_nome = "Arremesso de Osso"
p1_ataque1_dano = 30
p1_ataque2_nome = "Poder ilimitado"
p1_ataque2_dano = 45
p1_descricao = "Conhecido por empunhar um osso como arma, que pode ser envolto em fogo para causar mais dano."
url1 = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/105.png"
som1 = pygame.mixer.Sound(resource_path("POKEMON/sons/marowak.mp3"))

# Pokémon 2: Squirtle
p2_nome = "Squirtle"
p2_vida = 100
p2_ataque1_nome = "Bolha"
p2_ataque1_dano = 20
p2_ataque2_nome = "Quebra-Crânio"
p2_ataque2_dano = 35
p2_descricao = "Provando que de apenas uma gota de água, é capaz de causar um enorme tsunami!"
url2 = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png"
som2 = pygame.mixer.Sound(resource_path("POKEMON/sons/squirtle.mp3"))


# Pokémon 3: Charmander
p3_nome = "Charmander"
p3_vida = 100
p3_ataque1_nome = "Golpe de Colisão Aquecido"
p3_ataque1_dano = 30
p3_ataque2_nome = "Brasa"
p3_ataque2_dano = 40
p3_descricao = "Seu tamanho não é capaz de conter tamanho poder de fogo e de fúria!"
url3 = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/004.png"
som3 = pygame.mixer.Sound(resource_path("POKEMON/sons/charmander.mp3"))

# Pokémon 4: Pikachu
p4_nome = "Pikachu"
p4_vida = 100
p4_ataque1_nome = "Investida do Trovão"
p4_ataque1_dano = 30
p4_ataque2_nome = "Choque do Trovão"
p4_ataque2_dano = 50
p4_descricao = "Nascido da tempestade, eleito a fúria de um Trovão."
url4 = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png"    
som4 = pygame.mixer.Sound(resource_path("POKEMON/sons/pikachu.mp3"))

# Pokémon 5: Jigglypuff
p5_nome = "Jigglypuff"
p5_vida = 100
p5_ataque1_nome = "Canção"
p5_ataque1_dano = 30
p5_ataque2_nome = "Chute Lunar"
p5_ataque2_dano = 25
p5_descricao = "Parece doce, mas pode ser bastante amargo."
url5 = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/039.png"
som5 = pygame.mixer.Sound(resource_path("POKEMON/sons/Jigglypuff.mp3"))
# --- FUNÇÃO PARA EXIBIR IMAGEM NO TERMINAL ---
def mostrar_imagem_terminal(url):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpa terminal
    try:
        img = from_url(url, width=40)  # Largura da imagem
        print(img)
    except Exception as e:
        print("Erro ao carregar a imagem:", e)

# --- MENU PRINCIPAL ---

def menu_principal():
    while True:
         
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.YELLOW + Style.BRIGHT + "✨ --- MENU PRINCIPAL --- ✨" + Style.RESET_ALL)
        print(Fore.GREEN + "1. 🎮 Iniciar Jogo")
        print(Fore.CYAN + "2. 📘 Ver Pokédex")
        print(Fore.RED + "3. ❌ Sair")

        opcao_menu_principal = input(Fore.MAGENTA + "\nEscolha uma opção: ")
        

        if opcao_menu_principal == "1":
            menu_jogo()
        elif opcao_menu_principal == "2":
            exibir_pokedex()
        elif opcao_menu_principal == "3":
            print(Fore.RED + "Encerrando o jogo... Até a próxima! 👋")
            break
        else:
            print("Opção inválida, tente novamente.")

# --- POKÉDEX ---
def exibir_pokedex():
    while True:
        print("")
        print(Fore.YELLOW + Style.BRIGHT + "\n📘 --- POKÉDEX ---" + Style.RESET_ALL)
        print(Fore.CYAN + "1. 💀 Marowak")
        print(Fore.BLUE + "2. 🐢 Squirtle")
        print(Fore.RED + "3. 🔥 Charmander")
        print(Fore.YELLOW + "4. ⚡ Pikachu")
        print(Fore.MAGENTA + "5. 🎤 Jigglypuff")
        print(Fore.WHITE + "6. 🔙 Voltar ao Menu")

        escolha = input(Fore.MAGENTA + "\nEscolha um Pokémon para ver a imagem (1-6): ")

        if escolha == "1":
            mostrar_imagem_terminal(url1)
            print(Fore.CYAN + f"\n{p1_nome} - {p1_descricao}")
            som1.play()
            print(Fore.YELLOW + "Ficha Técnica: " \
            "\nVida: 100" \
            "\nAtaque 1: Arremesso de Osso (Dano: 30)" \
            "\nAtaque 2: Poder ilimitado (Dano: 45)")

        elif escolha == "2":
            mostrar_imagem_terminal(url2)
            print(Fore.CYAN + f"\n{p2_nome} - {p2_descricao}")
            som2.play()
            print( Fore.YELLOW + "Ficha Técnica: " \
            "\nVida: 100" \
            "\nAtaque 1: Bolha (Dano: 20)" \
            "\nAtaque 2: Quebra-Crânio (Dano: 35)")

        elif escolha == "3":
            mostrar_imagem_terminal(url3)
            print(Fore.CYAN + f"\n{p3_nome} - {p3_descricao}")
            som3.play()
            print(Fore.YELLOW + "Ficha Técnica: " \
            "\nVida: 100" \
            "\nAtaque 1: Golpe de Colisão Aquecido (Dano: 30)" \
            "\nAtaque 2: Brasa (Dano: 40)")

        elif escolha == "4":
            mostrar_imagem_terminal(url4)
            print(Fore.CYAN + f"\n{p4_nome} - {p4_descricao}")
            som4.play()
            print( Fore.YELLOW + "Ficha Técnica: " \
            "\nVida: 100" \
            "\nAtaque 1: Investida do Trovão (Dano: 30)" \
            "\nAtaque 2: Choque do Trovão (Dano: 50)")

        elif escolha == "5":
            mostrar_imagem_terminal(url5)
            print(Fore.CYAN + f"\n{p5_nome} - {p5_descricao}")
            som5.play() 
            print(Fore.YELLOW + "Ficha Técnica: " \
            "\nVida: 100" \
            "\nAtaque 1: Canção (Dano: 30)" \
            "\nAtaque 2: Chute Lunar (Dano: 25)")

        elif escolha == "6":
            break
        else:
            print(Fore.RED + "Opção inválida.")

        input(Fore.MAGENTA + "\nPressione Enter para continuar...")
        os.system("cls" if os.name == "nt" else "clear")

# --- MENU DE JOGO ---
def menu_jogo():

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.YELLOW + Style.BRIGHT + "⚔️ --- MODO DE JOGO ---" + Style.RESET_ALL)
    print(Fore.BLUE + "1. 🧑‍🤝‍🧑 Jogador vs Jogador")
    print(Fore.CYAN + "2. 🤖 Jogador vs Máquina")
    modo = input(Fore.MAGENTA + "\nEscolha o modo de jogo (1 ou 2): ")

    while True:  # repete até o jogador escolher certo
        if modo in ["1", "2"]:
            break   # sai do while e continua o código
        else:
            print(Fore.RED + "❌ Modo inválido. Tente novamente!\n")
            pygame.time.delay(1200)
            modo = input(Fore.MAGENTA + "\nEscolha o modo de jogo (1 ou 2): ")


    print(Fore.YELLOW + Style.BRIGHT + "\n🔽 Escolha seu Pokémon! 🔽" + Style.RESET_ALL)
    print(Fore.WHITE + f"1. 💀 {p1_nome}")
    print(Fore.BLUE + f"2. 🐢 {p2_nome}")
    print(Fore.RED + f"3. 🔥 {p3_nome}")
    print(Fore.YELLOW + f"4. ⚡ {p4_nome}")
    print(Fore.MAGENTA + f"5. 🎤 {p5_nome}")

    j1_escolha = input(Fore.MAGENTA + "Escolha um Pokémon para o Jogador 1 (1-5): ")
    while j1_escolha not in ["1", "2", "3", "4", "5"]:
        j1_escolha = input(Fore.RED + "Escolha inválida. Escolha um Pokémon para o Jogador 1 (1-5): ")

    print(Fore.GREEN + f"\n✅ Jogador 1 escolheu: {get_pokemon_name(j1_escolha)}")
    mostrar_imagem_terminal(get_pokemon_url(j1_escolha))
    get_pokemon_sound(j1_escolha).play()
    pygame.time.delay(1500) 

    if modo == "1":
        print(Fore.YELLOW + Style.BRIGHT + "\n🔽 Jogador 2, escolha seu Pokémon! 🔽" + Style.RESET_ALL)
        print(Fore.WHITE + f"1. 💀 {p1_nome}")
        print(Fore.BLUE + f"2. 🐢 {p2_nome}")
        print(Fore.RED + f"3. 🔥 {p3_nome}")
        print(Fore.YELLOW + f"4. ⚡ {p4_nome}")
        print(Fore.MAGENTA + f"5. 🎤 {p5_nome}")

        j2_escolha = input(Fore.MAGENTA + "Escolha um Pokémon para o Jogador 2 (1-5): ")

        while j2_escolha not in ["1", "2", "3", "4", "5"] or j2_escolha == j1_escolha:
            if j2_escolha == j1_escolha:
                print(Fore.RED + "Esse Pokémon já foi escolhido pelo Jogador 1.")
            j2_escolha = input(Fore.MAGENTA + "Escolha um Pokémon diferente (1-5): ")

        print(Fore.GREEN + f"\n✅ Jogador 2 escolheu: {get_pokemon_name(j2_escolha)}")
        mostrar_imagem_terminal(get_pokemon_url(j2_escolha))
        get_pokemon_sound(j2_escolha).play()
        pygame.time.delay(1500)

        ia = False

    elif modo == "2":
        opcoes_disponiveis = ["1", "2", "3", "4", "5"]
        opcoes_disponiveis.remove(j1_escolha)
        j2_escolha = random.choice(opcoes_disponiveis)
        ia = True

        print(Fore.YELLOW + f"\n🤖 A máquina está escolhendo...")
        pygame.time.delay(1000)
        print(Fore.CYAN + f"🧠 A máquina escolheu: {get_pokemon_name(j2_escolha)}")
        mostrar_imagem_terminal(get_pokemon_url(j2_escolha))
        get_pokemon_sound(j2_escolha).play()
        pygame.time.delay(1500)

    else:
        print(Fore.RED + "Modo inválido. Voltando ao menu.")
        return

    # Inicializa os Pokémon
    pokemon_j1_nome = get_pokemon_name(j1_escolha)
    pokemon_j2_nome = get_pokemon_name(j2_escolha)
    pokemon_j1_vida = get_pokemon_vida(j1_escolha)
    pokemon_j2_vida = get_pokemon_vida(j2_escolha)

    batalha(pokemon_j1_nome, pokemon_j2_nome, pokemon_j1_vida, pokemon_j2_vida, j1_escolha, j2_escolha, ia)

    print(f"\nJogador 1 escolheu: {pokemon_j1_nome}")
    print(f"Jogador 2 (ou Máquina) escolheu: {pokemon_j2_nome}")
    get_pokemon_sound(j1_escolha).play()
    pygame.time.delay(3000)  # Espera 1.5 segundos para o som tocar antes de continuar
    get_pokemon_sound(j2_escolha).play()
    pygame.time.delay(3000)

# --- FUNÇÕES AUXILIARES ---
def get_pokemon_sound(escolha):
    return {
        "1": som1,
        "2": som2,
        "3": som3,
        "4": som4,
        "5": som5
    }.get(escolha)


def get_pokemon_name(escolha):
    return {
        "1": p1_nome,
        "2": p2_nome,
        "3": p3_nome,
        "4": p4_nome,
        "5": p5_nome
    }.get(escolha, "Escolha Inválida")

def get_pokemon_vida(escolha):
    return {
        "1": p1_vida,
        "2": p2_vida,
        "3": p3_vida,
        "4": p4_vida,
        "5": p5_vida
    }.get(escolha, 0)

def get_pokemon_ataque1(escolha):
    return {
        "1": p1_ataque1_nome,
        "2": p2_ataque1_nome,
        "3": p3_ataque1_nome,
        "4": p4_ataque1_nome,
        "5": p5_ataque1_nome
    }.get(escolha)

def get_pokemon_ataque2(escolha):
    return {
        "1": p1_ataque2_nome,
        "2": p2_ataque2_nome,
        "3": p3_ataque2_nome,
        "4": p4_ataque2_nome,
        "5": p5_ataque2_nome
    }.get(escolha)

def get_pokemon_ataque1_dano(escolha):
    return {
        "1": p1_ataque1_dano,
        "2": p2_ataque1_dano,
        "3": p3_ataque1_dano,
        "4": p4_ataque1_dano,
        "5": p5_ataque1_dano
    }.get(escolha)

def get_pokemon_ataque2_dano(escolha):
    return {
        "1": p1_ataque2_dano,
        "2": p2_ataque2_dano,
        "3": p3_ataque2_dano,
        "4": p4_ataque2_dano,
        "5": p5_ataque2_dano
    }.get(escolha)

def get_pokemon_url(escolha):
    return {
        "1": url1,
        "2": url2,
        "3": url3,
        "4": url4,
        "5": url5
    }.get(escolha)

def get_ataque_dano_com_chance(ataque, escolha):
    if ataque == "1":
        dano_base = get_pokemon_ataque1_dano(escolha)
        nome_ataque = get_pokemon_ataque1(escolha)
    else:
        dano_base = get_pokemon_ataque2_dano(escolha)
        nome_ataque = get_pokemon_ataque2(escolha)

    chance_acerto = random.randint(1, 100)
    if chance_acerto > 80:
        print(Fore.LIGHTBLACK_EX + f"{nome_ataque} errou! ❌")
        return 0

    chance_critico = random.randint(1, 100)
    if chance_critico <= 20:
        dano_base = int(dano_base * 1.25)
        print(Fore.MAGENTA + "💥 Golpe Crítico!")

    print(Fore.WHITE + f"🎯 O ataque {nome_ataque} causou {dano_base} de dano!")
    return dano_base

# --- SISTEMA DE BATALHA ---
def batalha(pokemon_j1_nome, pokemon_j2_nome, pokemon_j1_vida, pokemon_j2_vida, j1_escolha, j2_escolha, ia):

    tocar_som_fundo()

    while pokemon_j1_vida > 0 and pokemon_j2_vida > 0:
        print(Fore.YELLOW + "\n⚔️ --- NOVO TURNO --- ⚔️")
        print(Fore.GREEN + f"💚 Vida de {pokemon_j1_nome}: {max(pokemon_j1_vida, 0)}")
        print(Fore.RED + f"💔 Vida de {pokemon_j2_nome}: {max(pokemon_j2_vida, 0)}")

        # --------------- jogador 1 escolhe
        print(Fore.CYAN + f"\n🎮 Jogador 1 - Escolha seu ataque:")
        print(f"1. {get_pokemon_ataque1(j1_escolha)} (Dano: {get_pokemon_ataque1_dano(j1_escolha)})")
        print(f"2. {get_pokemon_ataque2(j1_escolha)} (Dano: {get_pokemon_ataque2_dano(j1_escolha)})")
        ataque_j1 = input("👉 Escolha seu ataque (1 ou 2): ")

        if ia:
            ataque_j2 = random.choice(["1", "2"])
            print(Fore.YELLOW + f"\n🤖 A máquina escolheu o ataque {ataque_j2}.")
        else:
            print(Fore.MAGENTA + f"\n🎮 Jogador 2 - Escolha seu ataque:")
            print(f"1. {get_pokemon_ataque1(j2_escolha)} (Dano: {get_pokemon_ataque1_dano(j2_escolha)})")
            print(f"2. {get_pokemon_ataque2(j2_escolha)} (Dano: {get_pokemon_ataque2_dano(j2_escolha)})")
            ataque_j2 = input("👉 Escolha seu ataque (1 ou 2): ")

        
        print(Fore.GREEN + f"\n🗡️ {pokemon_j1_nome} está atacando...")
        dano_j1 = get_ataque_dano_com_chance(ataque_j1, j1_escolha)

        print(Fore.RED + f"\n🗡️ {pokemon_j2_nome} está atacando...")
        dano_j2 = get_ataque_dano_com_chance(ataque_j2, j2_escolha)

        pokemon_j2_vida -= dano_j1
        pygame.time.delay(150)  # Pequena pausa para melhor experiência
        pokemon_j1_vida -= dano_j2
        pygame.time.delay(150)  # Pequena pausa para melhor experiência 

        # -------------------- verificação de vitória
        if pokemon_j1_vida <= 0 and pokemon_j2_vida <= 0:
            print(Fore.YELLOW + "\n🤝 Empate! Ambos os Pokémon foram derrotados.")
            pygame.mixer.music.stop()
            break
        elif pokemon_j1_vida <= 0:
            print(Fore.RED + f"\n🏆 {pokemon_j2_nome} venceu a batalha!")
            pygame.mixer.music.stop()
            break
        elif pokemon_j2_vida <= 0:
            print(Fore.GREEN + f"\n🏆 {pokemon_j1_nome} venceu a batalha!")
            pygame.mixer.music.stop()
            break

# --- INICIAR O JOGO ---
menu_principal()
