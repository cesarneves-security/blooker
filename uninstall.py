import os
choice = "y"
run = os.system
if str(choice)=='Y' or str(choice)=='y':
    run('rm -r /usr/share/blooker ')
    run('rm /usr/bin/blooker ')
    print('[!] FERRAMENTA REMOVIDA COM SUCESSO!')

