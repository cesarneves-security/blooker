#importando os framework
import os#importando modulo os
import designer#importando arquivo com o designer do código
import time#importando modulo time, trabalhando com segundos
import cryptocode#cryptocoder
import cryptography#modulo para criptografia
from cryptography.fernet import Fernet #importando a função Fernet no modulo cryptography
#print ("")
#imporando a função do arquivo designer
designer.__configure__designer()#função __configure_designer
#usando while True / rodando sem parar
while True:#while True
    #imprimindo
    print ("")#imprimfo espaço
    print (" [1] USER INFO.")#imprimindo user info
    print (" [2] LISTA ARQUIVOS.")#imprimindo lista de arquivos
    #usando try e except
    try:#try
        #usando input
        escolha = input("\n [?] : ")#input
        #convertendo string para inteiro
        num_convert = int(escolha)#converting
        #usando if, elif and elif
        if (escolha == 1) or (escolha == "1"):#if
            os.system("clear")#os system
            #imporando a função do arquivo designer
            designer.__configure__designer()#função __configure_designer
            #imprimindo info
            #print ("")#imprimindo
            print ("\n [E N C R I P T A Ç Ã O] / [D E C R I P T A Ç Ã O] ?\n")
            #print (" [?] USER INFO.")#imprimindo info
            print (" [1] ENCRIPTAÇÃO.")#imprimindo ENCRIPTAÇÃO
            print (" [2] DECRIPTAÇÃO.")#imprimindo DECRIPTAÇÃO
            #criando inputs de dados
            decript_cript = input("\n [?] : ")#input
            #converter string para inteiro
            string_int = int(decript_cript)#converting
            #if, elif e else
            if (string_int == 1) or (string_int == "1"):#else
                os.system("clear")#os system
                #imporando a função do arquivo designer
                designer.__configure__designer()#função __configure_designer
                #imprimindo info
                print ("\n [E N C R I P T A Ç Ã O]\n")#i n c r i p t a ç ã o
                #criando inputs
                sms = str(input(" [!] DEGITE A INFORMAÇÃO: "))#input info sms para incriptação
                #criando chave para incriptação
                chave_key = str(input(" [!] DEGITE A KEY PARA ENCRIPTAÇÃO: "))#input para a key
                #usando if e else
                if (chave_key == "") or (chave_key == " ") or (sms == "") or (sms == " "):#if
                    #imprimindo erro
                    print ("\n [x] [E N C R I P T A Ç Ã O]: AVISO! CAMPO VAZIO / ADICIONA DADOS.\n")#imprimindo
                    #quebrando o programa
                    break#quebrando
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
                    #criando cifras
                    cifra_incriptada = crypt_format.encrypt(cifra_encoding)#encriptando
                    #CRIANDO CIFRAS
                    cifra_incriptions = cryptocode.encrypt(sms, chave_key)#criando cifras
                    #imprindo
                    print ("\n [-] ENCRIPTADO: {}".format(cifra_incriptions))#imprindo a cifra encriptada
                    #imprimindo
                    print (" [-] KEY: {}".format(chave_key))#imprindo a chave /key
                    #imprimindo
                    print ("")#espço
                    #break
                    #ICRIPTANDO INFO
            #usando elif
            elif (string_int == 2) or (string_int == "2"):#elif
                os.system("clear")#os system
                #imporando a função do arquivo designer
                designer.__configure__designer()#função __configure_designer
                #imprimindo info
                print ("\n [D E C R I P T A Ç Ã O]\n")#d e c r i p t a ç ã o
                sms2 = str(input(" [!] DEGITE O TEXTO ENCRYPTADO: "))#input info sms para incriptação
                #criando chave para incriptação
                chave_key2 = str(input(" [!] DEGITE A KEY DA ENCRIPTAÇÃO: "))#input para a key
                #CRIANDO CIFRA
                #usando if e else
                if (chave_key2 == "") or (chave_key2 == " ") or (sms2 == "") or (sms2 == " "):#if
                    #imprimindo
                    print ("\n [x] [D E C R I P T A Ç Ã O]: AVISO! CAMPO VAZIO / ADICIONA DADOS.\n")#imprimindo erro
                    #usando break ppara quebrar o programa
                    break#break
                #usando else
                else:#else
                    #cifra_coder = chave_key2+sms#concatenando
                    decrypt_cifras = cryptocode.decrypt(sms2, chave_key2) #cryptocode
                    #usando system os cler
                    os.system("clear")#system_clear
                    #imporando a função do arquivo designer
                    designer.__configure__designer__sec()#função __configure_designer
                    #imprimindo
                    #imprimindo info
                    print ("\n [D E C R I P T A N D O. . .]\n")#d e c r i p t a ç ã o
                    #usando o modulo time para dar um tempo de 2 segundos
                    time.sleep(2)#time
                    #usando if e else
                    if (decrypt_cifras == "False") or (decrypt_cifras == False):#else
                        #imprimindo
                        print ("\n [x] KEY NÃO ECONTRADO, TENTE UMA CHAVE CORRETA!\n")#imprimindo erros
                        #usando break para quebrar o código
                        break#break
                    #usando else
                    else:#else
                        #imprimindo
                        print ("\n [!] DECODIFICADO: {}".format(decrypt_cifras))#imprimindo DECODIFICADO
                        print (" [!] KEY: {}\n".format(chave_key2))#imprimindo chave
                    #if (chave_key2 == chave_key):
                    #    print ("\n [!] CODIFICADO: {}".format(res_coder))
                    #    print (" [!] KEY: {}\n".format(key_coder_))
                    #    break
                    #else:
                    #    print ("\n [x] KEY NÃO ECONTRADO, TENTE UMA CHAVE CORRETA!\n")
                    #    pass
            else:#else
                #usando system os cler
                os.system("clear")#system_clear
                #imporando a função do arquivo designer
                designer.__configure__designer()#função __configure_designer
                #imprimindo
                print ("")#imprimindo espaço
                print (" [X] ERRO - ESCOLHA INVALÍDA. TENTA NOVAMENTE!")#imprimindo erro
                print ("")#imprimindo espaço
        #linha de espaço entre escolha 1 e a escolha 2
        #usando elif
        elif (escolha == 2) or (escolha == "2"):#info
            #imprimindo
            print ("")#imprimindo espaço
            os.system("clear")#system_clear
            #imporando a função do arquivo designer
            designer.__configure__designer__sec()#função __configure_designer
            #imprimindo
            #imprimindo info
            print ("\n [1] ENCRIPTAÇÃO.")#imprimindo ENCRIPTAÇÃO
            print (" [2] DECRIPTAÇÃO.\n")#imprimindo DECRIPTAÇÃO
            incript_decript = input("\n [?]: ")
            if (incript_decript == 1) or (incript_decript == "1"):
                #imprimindo
                print ("")#imprimindo espaço
                os.system("clear")#system_clear
                #imporando a função do arquivo designer
                designer.__configure__designer__sec()#função __configure_designer
                #definindo inputs
                file_choice = input("\n [file] FILE-NAME?: ")#file_para encriptar
                file_key = input(" [key] KEY-CHAVE?: ")#chave da encriptação
                file_arquiv = input(" [file-salve] FILE-SALVE?: ")#ficheiro para salvar os dados encriptado
                #usando modulo time
                time.sleep(1)#time 1/s
                #usando with para ler o arquivo
                with open(file_choice, "r") as files:#abrind o arquivo
                    #file readline
                    file = files.readline()#lendo o arquivo
                    #usando while
                    while file:#contando cada linha do file
                        #cryptocode / encriptando
                        files_dcry = cryptocode.encrypt(file, file_key)#encryptp
                        #print (files_dcry)
                        file = files.readline()#lendo o arquivo
                        #arquivo = open(teste, 'w+')
                        #abrindo arquivo
                        arquivo = open('CRYPTOGRAFADOS/{}'.format(file_arquiv), 'a')#open arquivo
                        #escrevendo no arquivo
                        arquivo.writelines("{}\n".format(files_dcry))#escrevendo
                    #imprindo
                    print ("\n [F I L E -- E N C R I P T A D O]\n")#imprindo info - conclusão
                    #quebrando o script
                    break#quebrando break

            #usando o elif
            elif (incript_decript == 2) or (incript_decript == "2"):
                #imprimindo
                print ("")#imprimindo espaço
                os.system("clear")#system_clear
                #imporando a função do arquivo designer
                designer.__configure__designer__sec()#função __configure_designer
                #usando inputs para ler o arquivo
                file_choice2 = input("\n [file] FILE-NAME-DECRYPT?: ")#introduz o nome do arquivo
                file_key = input(" [key] KEY-CHAVE?: ")#chave do arquivo
                file_arquiv2 = input(" [file-salve] FILE-SALVE?: ")
                #usando o modulo time, pra trabalhar com o tempo
                time.sleep(1)#tempo de espera 1s
                #abrindo arquivo para decriptar
                with open(file_choice2, "r") as files:#abrindo arquivo
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
                            #usando break para quebrar o código
                            break#break
                        #usando else
                        else:#else
                            #imprindo
                            #print ("\n")#imprindo quebra de linha
                            #print (files_dcry)#imprindo arquivos decriptados
                            file = files.readline()#lendo arquivos
                            #print ("")#imprindo espaço
                            #arquivo = open("informacao_decriptada.txt", 'w+')
                            arquivo = open('DESCRYPTOGRAFADOS/{}'.format(file_arquiv2), 'a')#ler o arquivo
                            arquivo.writelines("{}\n".format(files_dcry))#salvando os dados decriptado
                    time.sleep(1)#tempo de espera 1s
                    #imprindo
                    print ("\n [F I L E -- D E C R I P T A D O]\n")#imprindo conclusão de decriptação
                    #quebrando script
                    break#quebrando / break
        #usando else
        else:#else
            #usando system os cler
            os.system("clear")#system_clear
            #imporando a função do arquivo designer
            designer.__configure__designer()#função __configure_designer
            #imprimindo
            print ("")#imprimindo espaço
            print (" [X] ERRO - ESCOLHA INVALÍDA. TENTA NOVAMENTE!")#imprimindo erro
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
#usando else com while
else:#else
    #imprimindo
    print ("")#imprimindo espaço
    print ("\n [!] ERRO DE CONFIGURAÇÃO.\n")#imprimindo erro
    print ("")#imprimindo espaço
