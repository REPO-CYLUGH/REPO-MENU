import youtube_dl, os
os.system('pip install youtube_dl')
os.system('clear')
print('''
██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗  
╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝  
░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░  
░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░  
░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗  
░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝  


██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░
██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝
██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝''')

print('''
█▀▀▄ █──█ 　 █▀▀ █── █▀▀█ █──█ █▀▀ █▀▀█ 
█▀▀▄ █▄▄█ 　 ▀▀█ █── █▄▄█ █▄▄█ █▀▀ █▄▄▀ 
▀▀▀─ ▄▄▄█ 　 ▀▀▀ ▀▀▀ ▀──▀ ▄▄▄█ ▀▀▀ ▀─▀▀''')

print('AVISO! ESTE DOWLOADER SO FUNCIONA EM LINUX DEBIAN!')


a = input ('coloque o link do video que voce que baixar: ')

link = [f'{a}']

with youtube_dl.YoutubeDL() as ydl:
    ydl.download(link)