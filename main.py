import os
import designer#importando arquivo com o designer do código
import time#importando modulo time, trabalhando com segundos
import sys
from blooker_argv import __incript_info__
from blooker_argv import __decript_info__
from blooker_argv import __archive_incript__
from blooker_argv import __archive_decript__
#sys argv info

try:
    decript_info_select = sys.argv[1]#-incript-info 
    key_select = sys.argv[2] #--key=
    key_chave = sys.argv[3] 
    input_select = sys.argv[4] #--input=
    sms_input = sys.argv[5]

    output_select = sys.argv[6] #--output=
    output_file = sys.argv[7]

    #sys argv info
    #incript_decript_file_select = sys.argv[6]#-incript-file 
    #key_select = sys.argv[7]#--key=
    #chave_key_file = sys.argv[8] 
    #file_select_files = sys.argv[9] #--file= 
    #archive_file = sys.argv[10] #/tmp/teste.py
    #FINAL CONFIG VARIAVEIS ARGV[]
    if (len(sys.argv) != 5):
        #os.system('clear')
        #print ("\n SMS PARA ENCRIPTPAR: {}".format(sms_input))
        #print (" CHAVE-KEY: {}".format(key_chave))
        if (decript_info_select == "-encript-info") and (output_select == "--output-info"):
            #os.system('clear')
            #print ("\n ENCRIPTANDO INFORMAÇÃO\n")
            #print (" SMS PARA ENCRIPTPAR: {}".format(sms_input))
            #print (" CHAVE-KEY: {}".format(key_chave))(
            __incript_info__()
            #pass

        elif (decript_info_select == "-decript-info") and (output_select == "--output-info"):
            #os.system('clear')
            #print ("\n DECRIPTANDO INFORMAÇÃO\n")
            #print (" SMS PARA DECRIPTPAR: {}".format(sms_input))
            #print (" CHAVE-KEY: {}".format(key_chave))
            __decript_info__()
        #linha entre decript info e encript file

        elif (decript_info_select == "-encript-file") and (output_select == "--output-file"):
            #os.system('clear')
            #print ("\n ENCRIPTANDO FILE\n")
            #print (" FILE PARA ENCRIPTPAR: {}".format(sms_input))
            #print (" CHAVE-KEY: {}".format(key_chave))
            __archive_incript__()

        elif (decript_info_select == "-decript-file") and (output_select == "--output-file"):
            #os.system('clear')
            #print ("\n DECRIPTANDO FILE\n")
            #print (" FILE PARA DECRIPTPAR: {}".format(sms_input))
            #print (" CHAVE-KEY: {}".format(key_chave))
            __archive_decript__()
        
        else:
            os.system('clear')
            designer.__configure__designer__sec()
            print (""" [v] COMO USRA:\n
 python3 main.py
 
 info:
     python3 main.py -encript-info --key 12345 --input "eu amo python" --output-info file_para_encript.txt
     python3 main.py -decript-info --key 12345 --input "eu amo python" --output-info file_para_decript.txt
 
 file:
     python3 main.py -encript-file --key 12345 --file encript_file.txt --output-file file_para_encript.txt
     python3 main.py -decript-file --key 12345 --file decript_file.txt --output-file file_para_decript.txt


                """)
    else:
        os.system('clear')
        designer.__configure__designer__sec()
        pass

except IndexError:
        #import blooker
        pass

except ModuleNotFoundError:
    os.system("clear")#os system
    #imporando a função do arquivo designer
    designer.__configure__designer()#função __configure_designer
    print ("\n [ERRO] MODULOS NÃO INSTALADO!\n")
    time.sleep(1)
    print ("\n [INSTALL] INSTALANDO MODULOS:\n")
    time.sleep()
    os.system("pip install os")
    os.system("pip install time")
    os.system("pip install cryptocode")
    os.system("pip install cryptography")
    #import os#importando modulo os
    #import designer#importando arquivo com o designer do código
    #import time#importando modulo time, trabalhando com segundos
    #import cryptography#modulo para criptografia
    #from cryptography.fernet import Fernet #importando a função Fernet no modulo cryptography