import os
os.system('clear')
#banner
print('''
░█████╗░██████╗░███████╗  
██╔══██╗██╔══██╗██╔════╝  
██║░░╚═╝██████╔╝█████╗░░  
██║░░██╗██╔═══╝░██╔══╝░░  
╚█████╔╝██║░░░░░██║░░░░░  
░╚════╝░╚═╝░░░░░╚═╝░░░░░  

░██████╗░███████╗██████╗░░█████╗░██████╗░░█████╗░██████╗░
██╔════╝░██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██████╔╝███████║██║░░██║██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██╔══██╗██╔══██║██║░░██║██║░░██║██╔══██╗
╚██████╔╝███████╗██║░░██║██║░░██║██████╔╝╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝''')
#by
print('''
█▀▀▄ █──█ 　 █▀▀ █── █▀▀█ █──█ █▀▀ █▀▀█ █ 
█▀▀▄ █▄▄█ 　 ▀▀█ █── █▄▄█ █▄▄█ █▀▀ █▄▄▀ ▀ 
▀▀▀─ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀──▀ ▄▄▄█ ▀▀▀ ▀─▀▀ ▄''')

escolha = -1

#escolhas

while escolha < 1 or escolha > 2:
    escolha = int(input("""\033[1;0m

[ 1 ] gerar cpf
[SAIR] ENTER
\033[1;34m---> """))
    print(''' ''')
    print('')
    print('')
    
# escolha
if escolha == 1:
    exec(open('genCpf.py', encoding="utf-8").read(), globals())