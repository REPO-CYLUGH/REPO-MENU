import os
os.system('sudo apt install dnsenum')
os.system('pkg install dnsenum')
os.system('pip install dnsenum')
os.system('clear')
print('''
██████╗░███╗░░██╗░██████╗███████╗███╗░░██╗██╗░░░██╗███╗░░░███╗
██╔══██╗████╗░██║██╔════╝██╔════╝████╗░██║██║░░░██║████╗░████║
██║░░██║██╔██╗██║╚█████╗░█████╗░░██╔██╗██║██║░░░██║██╔████╔██║
██║░░██║██║╚████║░╚═══██╗██╔══╝░░██║╚████║██║░░░██║██║╚██╔╝██║
██████╔╝██║░╚███║██████╔╝███████╗██║░╚███║╚██████╔╝██║░╚═╝░██║
╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝
[*]Painel made by: slayer''')
print('Feito para: Debian Linux, Linux & terminais não emulados (Ex: termux)')
a = input('Site (Ex: youtube.com): ')

b = os.system(f'dnsenum {a}')

print(b)