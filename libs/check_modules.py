# coding=utf-8
#!/usr/bin/env python3

import sys

def check_modules():
    try:
        import requests
    except:
        print("[-] 'requests' pacote não instalado!")
        print("[*] Digite 'pip install requests' Para instalar ,digite: r")
        sys.exit(0)

    try:
        import colorama
    except Exception as e:
        print("[-] 'colorama' pacote não instalado")
        print("[*] Para instalar ,digite: pip install colorama' ")
        print(e)
        sys.exit(0)

    try:
        import asyncio
    except:
        print("[-] 'asyncio' pacote não instalado")
        print("[*] Para instalar ,digite: pip install asyncio' ")
        sys.exit(0)

    try:
        import proxybroker
    except:
        print("[-] 'proxybroker' pacote não instalado")
        print("[*] Para instalar ,digite: pip install proxybroker' ")
        sys.exit(0)

    try:
        import warnings
    except:
        print("[-] 'warnings' pacote não instalado")
        print("[*] Para instalar ,digite: pip install warnings' ")
        sys.exit(0)

    import warnings
    warnings.filterwarnings("ignore")

    from colorama import init
    init()
