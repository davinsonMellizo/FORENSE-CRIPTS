#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

def esterilizar():	
	vuelta=0
	print("====running the process for disinfecting hard disks====")
	while vuelta<int(sys.argv[8]):
		porcentaje=vuelta+1
		print("==========Completed "+str(porcentaje)+"/"+sys.argv[8])
		ValorIF="if=/dev/zero"
		ValorOF=" of="+sys.argv[2]
		ValorBS=" bs="+sys.argv[4]
		ComandoDDZERO="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDZERO)
		ValorIF="if=/dev/urandom"
		ComandoDDRANDOM="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDRANDOM)
		ValorIF="if=/dev/zero"
		ComandoDDZERO="dd "+ValorIF+ValorOF+ValorBS
		os.system(ComandoDDZERO)
		vuelta=vuelta+1
	print("====End of the disinfection process of hard disks====")
	print("")
	print("======checking the disinfection with grep command=====")
	CoGrep="dd if="+sys.argv[2]+" | xxd | grep -v "+"'0000 0000 0000 0000 0000 0000 0000 0000'"
	os.system(CoGrep)
def formatear():
	print("====Formatting====")
	UNMOUNT="umount "+sys.argv[2]
	os.system(UNMOUNT)
	FORMATEAR="sudo mkfs.vfat -F 32 -n "+sys.argv[6]+" "+sys.argv[2]
	os.system(FORMATEAR)
	print("====End...====")
def menu():
	print("================================================MENU=================================================")
	print("| Sintaxis:                                                                                          |")
	print("| python main.py -of Dispositivo -bs tamañoBloque -n Nombre -v Iteraciones                           |")
	print("|                                                                                                    |")
	print("| Dispositivo: Dirección donde esta montada el Dispositivo, df -h para obtenerla                     |")
	print("| tamañoBloque: tamaño de los bloques, fdisk -l 'ruta' para obtenerlo o 512 por defecto              |")
	print("| Nombre: nombre que se le asignara al Dispositivo despues de formatear                              |")
	print("| Iteraciones: Numero de iteraciones para rellenar con ceros y numeros aleatorios el Dispositivo     |")
	print("|====================================================================================================|")
	print("| Ejemplo:                                                                                           |")
	print("| python main.py -of /dev/sdb1 -bs 512 -n Mi-USB -v 99                                               |")	
	print("|====================================================================================================|")
	print("| Creado por: Davinson Mellizo                                                                       |")
	print("| Correo: davinsonmellizo@unicauca.edu.co                                                            |")
	print("| Profesor: Siler Amador Donado                                                                      |")
	print("| Fecha: 21/05/2019                                                                                  |")
	print("| Repositorio: https://github.com/davinsonMellizo/Esterilizacion.git                                 |")
	print("=====================================================================================================")
if __name__ == "__main__":
	if len(sys.argv)>8:
		if sys.argv[1]=="-of" and sys.argv[3]=="-bs" and sys.argv[5]=="-n" and sys.argv[7]=="-v":
			esterilizar()
			formatear()		
		else:
			menu()
	else:
			menu()
		