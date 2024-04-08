import subprocess

def install_proxybroker():
    try:
        subprocess.run(["pip", "install", "proxybroker"])
    except Exception as e:
        print(f"Erro ao instalar o ProxyBroker: {e}")

install_proxybroker()

# Agora você pode importar os módulos necessários do ProxyBroker e outros módulos
from libs.check_modules import check_modules
from sys import exit
from os import _exit

check_modules()

from os import path

from libs.logo import print_logo
from libs.utils import print_success
from libs.utils import print_error
from libs.utils import ask_question
from libs.utils import print_status
from libs.utils import parse_proxy_file
from libs.proxy_harvester import find_proxies
from libs.attack import report_profile_attack
from libs.attack import report_video_attack

from multiprocessing import Process
from colorama import Fore, Back, Style

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def profile_attack_process(username, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_profile_attack(username, None)
        return

    for proxy in proxy_list:
        report_profile_attack(username, proxy)

def video_attack_process(video_url, proxy_list):
    if (len(proxy_list) == 0):
        for _ in range(10):
            report_video_attack(video_url, None)
        return

    for proxy in proxy_list:
        report_video_attack(video_url, proxy)

def video_attack(proxies):
    video_url = ask_question("Insira o link do vídeo que deseja denunciar: ")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=video_attack_process, args=(video_url, [],))
            p.start()
            print_status(str(k + 1) + ". Processo Iniciado!")
            if (k == 5): print()
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Ataque de denúncia de vídeo iniciado!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=video_attack_process, args=(video_url, proxy_list,))
        p.start()
        print_status(str(i) + ". Processo Iniciado!")
        if (k == 5): print()
        i = i + 1

def profile_attack(proxies):
    username = ask_question("Insira o nome de usuário do perfil que deseja denunciar: ")
    print(Style.RESET_ALL)
    if (len(proxies) == 0):
        for k in range(5):
            p = Process(target=profile_attack_process, args=(username, [],))
            p.start()
            print_status(str(k + 1) + ". Processo Iniciado!")
        return

    chunk = list(chunks(proxies, 10))

    print("")
    print_status("Ataque de denúncia de perfil iniciado!\n")

    i = 1
    for proxy_list in chunk:
        p = Process(target=profile_attack_process, args=(username, proxy_list,))
        p.start()
        print_status(str(i) + ". Processo Iniciado!")
        if (k == 5): print()
        i = i + 1

def main():
    print_success("Módulos carregados!\n")

    ret = ask_question("Deseja usar proxies? [S/N]")

    proxies = []

    if (ret == "S" or ret == "s"):
        ret = ask_question("Deseja coletar proxies da internet? [S/N]")

        if (ret == "S" or ret == "s"):
            print_status("Coletando proxies da internet! Isso pode levar algum tempo.\n")
            proxies = find_proxies()
        elif (ret == "N" or ret == "n"):
            print_status("Por favor, coloque no máximo 50 proxies em um arquivo!")
            file_path = ask_question("Insira o caminho do seu arquivo de proxies: ")
            proxies = parse_proxy_file(file_path)
        else:
            print_error("Resposta não compreendida, saindo!")
            exit()

        print_success(str(len(proxies)) + " proxies encontrados!\n")
    elif (ret == "N" or ret == "n"):
        pass
    else:
        print_error("Resposta não compreendida, saindo!")
        exit()

    print("")
    print_status("1 - Denunciar perfil.")
    print_status("2 - Denunciar um vídeo.")
    report_choice = ask_question("Por favor, escolha o método de denúncia: ")
    print("")

    if (report_choice.isdigit() == False):
        print_error("Resposta não compreendida.")
        exit(0)
    
    if (int(report_choice) > 2 or int(report_choice) == 0):
        print_error("Resposta não compreendida.")
        exit(0)

    if (int(report_choice) == 1):
        profile_attack(proxies)
    elif (int(report_choice) == 2):
        video_attack(proxies)

if __name__ == "__main__":
    print_logo()
    try:
        main()
        print(Style.RESET_ALL)
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "[ * ] Programa encerrado!")
        print(Style.RESET_ALL)
        _exit(0)