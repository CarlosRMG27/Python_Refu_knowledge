#!/bin/bash

touch oldFiles.txt

#Aquí leemos todos los documentos que tienen Jane en ellos desde el archivo list.txt
#Nos quedamos solo con sus nombres

files=$(grep "jane " ../data/list.txt | cut -d' ' -f3)
#Probamos si los documentos guardados en la variable files están en
#el file system

for f in $files; do
 if [ -e $HOME$f ];then
    echo $HOME$f >> oldFiles.txt;
 fi
 done

