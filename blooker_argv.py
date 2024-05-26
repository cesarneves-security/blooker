#importando os framework
import os#importando modulo os
import designer#importando arquivo com o designer do código
import time#importando modulo time, trabalhando com segundos
import cryptocode#cryptocoder
import cryptography#modulo para criptografia
from cryptography.fernet import Fernet #importando a função Fernet no modulo cryptography
import sys #importando sys
#print ("")
#imporando a função do arquivo designer
designer.__configure__designer()#função __configure_designer


#arquivos#ARCHIVES - DECRIPTANDO

#usando try e except
try:#try
    #importando modulo com variaveis
    def __incript_info__():
        from main import sms_input
        from main import key_chave
        from main import output_file
        #VARIAVEIS
        chave_key = key_chave
        sms = sms_input
        guardar_info = output_file
        #usando os
        os.system("clear")#os system
        #imporando a função do arquivo designer
        designer.__configure__designer()#função __configure_designer
        #imprimindo info
        print ("\n [I N C R I P T A Ç Ã O - I N F O]\n")#i n c r i p t a ç ã o
        if (chave_key == "") or (chave_key == " ") or (sms == "") or (sms == " "):#if
            #imprimindo erro
            print ("\n [x] [I N C R I P T A Ç Ã O]: AVISO! CAMPO VAZIO / ADICIONA DADOS.\n")#imprimindo
            #quebrando o programa
            exit()#exit
        #usando else
        else:#else
            #CRIANDO CIFRA
            cifra = chave_key+sms#concatenando
            #usando o modulo time para dar uma pausa de 2 segundo
            time.sleep(2)#time
            #criando codificação
            codefic_cifra = cifra[-1::-1]#codificando
            clave_crypt = Fernet.generate_key()#claver
            crypt_format = Fernet(clave_crypt)#fernet claver
            cifra_encoding = codefic_cifra.encode()#encoding
            #incript
            cifra_incriptions = cryptocode.encrypt(sms, chave_key)#criando cifras
            #if
            if (cifra_incriptions == "False") or (cifra_incriptions == False):#if
                #imprimindo
                print ("\n [x] KEY NÃO ECONTRADO, TENTE UMA CHAVE CORRETA!\n")#imprimindo erros
                #usando exit para quebrar o código
                exit()#exit
            else:#else
                arquivo_local_info = '{}'.format(guardar_info)
                #abrindo arquivo
                arquivo_info = open('{}'.format(guardar_info), 'a')#open arquivo
                #criando variavel geral
                global_all = "KEY: {}; SMS: {}; CRIPTOGRAFIA: {}".format(chave_key,sms,cifra_incriptions)
                #escrevendo no arquivo
                arquivo_info.writelines("{}\n".format(global_all))#escrevendo
                #imprindo
                print ("\n [-] ENCRIPTADO: {}".format(cifra_incriptions))#imprindo a cifra encriptada
                #imprimindo
                print (" [-] KEY: {}".format(chave_key))#imprindo a chave /key
                print (" [s] {}\n".format(arquivo_local_info))
                #imprimindo
                print ("")#espço
                #break
                #ICRIPTANDO INFO
                #__incript_info__()

    def __decript_info__():
        #DECRIPTAÇÃO
        from main import sms_input
        from main import key_chave
        from main import output_file
        #VARIAVEIS
        chave_key = key_chave
        sms = sms_input
        guardar_info2 = output_file
        #usando os
        os.system("clear")#os system
        #imporando a função do arquivo designer
        designer.__configure__designer()#função __configure_designer
        #imprimindo info
        print ("\n [D E C R I P T A Ç Ã O - I N F O]\n")#d e c r i p t a ç ã o
        if (chave_key == "") or (chave_key == " ") or (sms == "") or (sms == " "):#if
            #imprimindo
            print ("\n [x] [D E C R I P T A Ç Ã O]: AVISO! CAMPO VAZIO / ADICIONA DADOS.\n")#imprimindo erro
            #usando exit ppara quebrar o programa
            exit()#exit
        #usando else
        else:#else
            #cifra_coder = chave_key2+sms#concatenando
            decrypt_cifras = cryptocode.decrypt(sms, chave_key) #cryptocode
            #usando o modulo time para dar um tempo de 2 segundos
            time.sleep(2)#time
            #usando if e else
            if (decrypt_cifras == "False") or (decrypt_cifras == False):#if
                #imprimindo
                print ("\n [x] KEY NÃO ECONTRADO, TENTE UMA CHAVE CORRETA!\n")#imprimindo erros
                #usando exit para quebrar o código
                exit()#exit
            #usando else
            else:#else
                arquivo_local = '{}'.format(guardar_info2)#cool
                #criando arquivos
                arquivo_info = open('{}'.format(guardar_info2), 'a')#open arquivo
                #criando variavel geral
                global_all = "KEY: {}; DECRIPTOGRAFADO: {}".format(chave_key,decrypt_cifras)
                #escrevendo no arquivo
                arquivo_info.write("{}\n".format(global_all))#escrevendo
                #imprimindo
                print ("\n [!] DECODIFICADO: {}".format(decrypt_cifras))#imprimindo DECODIFICADO
                print (" [!] KEY: {}".format(chave_key))#imprimindo chave
                print (" [s] {}\n".format(arquivo_local))

    #TRABALHANDO COM ARQUIVOS
    #incriptando arquivo
    #usando elif
    def __archive_incript__():
        #arquivos#ARCHIVES - INCRIPTANDO
        from main import sms_input
        from main import key_chave
        from main import output_file
        file_choice2 = sms_input
        file_key2 = key_chave
        file_arquiv2 = output_file
        #imprimindo
        print ("")#imprimindo espaço
        os.system("clear")#system_clear
        #imporando a função do arquivo designer
        designer.__configure__designer__sec()#função __configure_designer
        #imprimindo
        print ("")#imprimindo espaço
        os.system("clear")#system_clear
        #imporando a função do arquivo designer
        designer.__configure__designer__sec()#função __configure_designer
        #usando modulo time
        time.sleep(1)#time 1/s
        #usando with para ler o arquivo
        with open(file_choice2, "r") as files:#abrind o arquivo
            #file readline
            file = files.readline()#lendo o arquivo
            #usando while
            while file:#contando cada linha do file
                dir_salv = '{}'.format(file_arquiv2)
                #cryptocode / encriptando
                files_dcry = cryptocode.encrypt(file, file_key2)#encryptp
                #print (files_dcry)
                file = files.readline()#lendo o arquivo
                #arquivo = open(teste, 'w+')
                #abrindo arquivo
                arquivo = open('{}'.format(file_arquiv2), 'a')#open arquivo
                #escrevendo no arquivo
                arquivo.writelines("{}\n".format(files_dcry))#escrevendo
            #imprindo
            print ("\n [F I L E -- E N C R I P T A D O]\n")#imprindo info - conclusão
            print (" [-] KEY: {}".format(file_key2))
            print (" [S] {}\n".format(dir_salv))
            #quebrando o script
            exit()#quebrando exit


        #decriptando arquivos
        #usando o elif
    def __archive_decript__():
        from main import sms_input
        from main import key_chave
        from main import output_file
        file_choice = sms_input
        file_key = key_chave
        file_arquiv = output_file
        #imprimindo
        print ("")#imprimindo espaço
        os.system("clear")#system_clear
        #imporando a função do arquivo designer
        designer.__configure__designer__sec()#função __configure_designer
        #usando o modulo time, pra trabalhar com o tempo
        time.sleep(1)#tempo de espera 1s
        #abrindo arquivo para decriptar
        try:
            with open(file_choice, "r") as files:#abrindo arquivo
                #lendo arquivos para conf
                file = files.readline()#lendo o arquivo
                #usando while para contar cada linha do arquivo
                while file:#lendo cada linha do arquivo e contando
                    #encryptando
                    files_dcry = cryptocode.decrypt(file, file_key)#file_dcry / encriptando
                    #usando o if para selecionar erro FALSE
                    if (files_dcry == "False") or (files_dcry == False):#if
                        #imprimindo
                        print ("\n [x] KEY NÃO ECONTRADO, TENTE UMA CHAVE CORRETA!\n")#imprimindo erros
                        #usando exit para quebrar o código
                        exit()#exit
                    #usando else
                    else:#else
                        #criando caminho de andamento
                        caminho_file = '{}'.format(file_arquiv)
                        #print (files_dcry)#imprindo arquivos decriptados
                        file = files.readline()#lendo arquivos
                        #arquivo = open("informacao_decriptada.txt", 'w+')
                        arquivo = open('{}'.format(file_arquiv), 'a')#ler o arquivo
                        arquivo.writelines("{}".format(files_dcry))#salvando os dados decriptado
                        #imprindo
                        #print ("\n")#imprindo quebra de linha
                        #print ("")#imprindo espaço
                #time.sleep(1)#tempo de espera 1s
                #imprindo
                print ("\n [F I L E -- D E C R I P T A D O]\n")#imprindo conclusão de decriptação
                print (" [-] KEY: {}".format(file_key))
                print (" [S] {}\n".format(caminho_file))
                #quebrando script
                exit()#quebrando / exit
        except FileNotFoundError:
            os.system("clear")#os system
            #imporando a função do arquivo designer
            designer.__configure__designer()#função __configure_designer
            #imprimindo
            print ("")#imprimindo espaço
            print (" [X] ERRO - ARQUIVO: {} NÃO ENCONTRADO!".format(file_choice))##imprimindo erro
            print ("")#imprimindo espaço
#tratando erros
except ValueError:#except
    os.system("clear")#os system
    #imporando a função do arquivo designer
    designer.__configure__designer()#função __configure_designer
    #imprimindo
    print ("")#imprimindo espaço
    print (" [X] ERRO - ESCOLHA INVALÍDA. TENTA NOVAMENTE!")##imprimindo erro
    print ("")#imprimindo espaço

