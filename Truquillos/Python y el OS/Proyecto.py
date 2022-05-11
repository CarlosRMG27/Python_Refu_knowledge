#!/usr/bin/env python3

import operator
import re
import sys
import csv

error={}#Number of errors
per_user={}#Number of entries of each user

#Aquí decimos que el logfile que se lee 
#es el que se dé como un argumento en la command line
logfile = sys.argv[1]

#Abrimos el lofgile como file
#e iteramos sobre cada línea
with open(logfile) as file:
        for line in file:
                username = re.search(r"\((.*)\)",line).group(1)
                user_count = {'INFO': 0, 'ERROR': 0}
                #print(username)
                #Si el username no existe, creamos una
                #nueva entrada en el diccionario
                #e inicializamos su cuenta de errores y éxitos
                if username not in per_user.keys():
                        per_user[username] = user_count


                U=re.search(r"ticky: INFO: ([\w ]*) ", line)
                E=re.search(r"ticky: ERROR: ([\w ]*) ", line)
                if 'INFO' in line:
                        per_user[username]['INFO']+=1
                elif 'ERROR' in line:
                    #Si hay un error, el tipo de error se busca y se le suma uno
                    
                        per_user[username]['ERROR']+=1
                        ms=re.search(r'ERROR (.*) ',line).group(1)
                        if ms not in error:
                                error[ms]=0
                        error[ms]+=1

print('Diccionario acabado')
print(per_user)

#Ordenamos según cantidad de errores
error=sorted(error.items(), key = operator.itemgetter(1), reverse=True)
#Ordenamos alfabéticamente
per_user=sorted(per_user.items(),key=operator.itemgetter(0))

print('Diccionario ordenado')
print(per_user)
#Insertamos los headers
error.insert(0,('ERROR','Count'))

#Aquí escribimos los csv
with open('error_message.csv','w') as file:
        escritor=csv.writer(file)
        escritor.writerows(error)
        file.close()

per_user_list=[]
for item in per_user:
        tup=(item[0],item[1]['INFO'],item[1]['ERROR'])
        per_user_list.append(tup)


per_user_list.insert(0,("Username","INFO","ERROR"))



with open('user_statistics.csv','w') as file:
        escritor=csv.writer(file)
        escritor.writerows(per_user_list)
        file.close()

print('Diccionario final')
print(per_user_list)
