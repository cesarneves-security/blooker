import os
choice = input('[+] PARA INSTALAR PRESS (Y)/ PARA REMOVER PRESS (N) >> ')
run = os.system
if str(choice) =='Y' or str(choice)=='y':

    run('chmod 777 main.py')
    run('mkdir /usr/share/blooker')
    run('cp -r * /usr/share/blooker')

    cmnd=(' #! /bin/sh \n exec python3 /usr/share/blooker/main.py "$@"')
    with open('/usr/bin/blooker','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/blooker & chmod +x /usr/share/blooker/main.py')
    print('''\n\n FERRAMENTA INSTALADA COM SUCESSO...''')
if str(choice)=='N' or str(choice)=='n':
    os.system("clear")
    print(" [X] SAINDO...")
    exit()
