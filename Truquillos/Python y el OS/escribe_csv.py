#!/usr/bin/env python
import numpy as np
import csv

#N archivos de n columnas
def escribe(N,n):
	for i in range(N):
		headers=['col_{}'.format(j) for j in range(n)]
		data=np.random.randint(0,100,(100,n))
		with open('archivo_{}.csv'.format(i),'w+',newline='') as arx:
			escritor=csv.writer(arx)
			escritor.writerow(headers)
			escritor.writerows(data)



escribe(2,3)
