
#!/usr/bin/env python3

import sys
import subprocess


#Leemos el command line argument con el módulo de sys
F=sys.argv[1]
#F es un archivo que trae nombres de archivos

with open(F) as files:
    #Cada línea de F es un nombre
        for name in files.readlines():
            #Quitamos los espacios blancos de cada nombre
                data=name.strip()
                output=data.replace('jane','jdoe')
                subprocess.run(['mv',data,output])
                #En el subproceso es que se renombran los archivos
        files.close()






