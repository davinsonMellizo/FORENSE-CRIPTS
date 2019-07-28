#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import time
def obtenerHash():
	insInicial=time.time()
	print("Procesando...")
	ComandoHash="md5sum "+sys.argv[2]
	print("HASH:")
	os.system(ComandoHash)
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def compararHash():
	insInicial=time.time()
	print("Procesando...")
	f = open (sys.argv[3],'r')
	hashVerificacion = f.read()
	f.close()
	ComandoHash="md5sum "+sys.argv[2]+">result.txt"
	os.system(ComandoHash)
	f = open ("result.txt",'r')
	hashObtenido = f.read()
	f.close()
	hashObtenido=hashObtenido.split(" ")[0]
	print("HASH verificación:"+hashVerificacion)
	print("HASH obtenido    :"+hashObtenido)
	if(hashObtenido==hashVerificacion):
		print("!!!IGUALES!!!")
	else:
		print("!!!DIFIERENTES!!!")
	insFinal=time.time()
	tiempo=insFinal- insInicial
	print("Tiempo de Ejecucion", tiempo)
def buscarCadenas():
	archivo = open(sys.argv[2], "r")
	for linea in archivo.readlines():
		ComandoGrep='grep -ir '+"'"+linea+"' "+sys.argv[3]
		os.system(ComandoGrep)
	archivo.close()

	

def buscarArchivos():
	ComandoGrep='grep -ir '+sys.argv[2]
	print(ComandoGrep)
	os.system(ComandoGrep)

if __name__ == "__main__":
	if(sys.argv[1]=="-o"):
		obtenerHash()
	if(sys.argv[1]=="-c"):
		compararHash()
	if(sys.argv[1]=="-b"):
		buscarCadenas()
	
	#os.system("fdisk -l /root/Documents/FORENSE/PARCIAL3/SCHARDT.img|grep SCHARDT.img>result.txt")
	#f = open ("result.txt",'r')
	#hashObtenido = f.read()
	#f.close()
	#print(hashObtenido.split(" "))
	#dd if=/dev/mmcblk0p1 of=imgenCd.img mount -o ro,loop imgenCd.img ensayo
	os.system("mount -o ro,loop /root/Documents/PARCIAL2/SCHARDT.img /root/Documents/FORENSE/PARCIAL3/mount")