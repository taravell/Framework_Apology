#Apology Framework v.01

#!/usr/bin/python3
# - * - codificação utf-8 - * -

#blibliotecas
import sys
import os

def main():
	try:
		print("Apology Framework")
		def inicio1():
			while True:
				print("[1] instalar [2]sair")
				repo = input("selecione as opções")    
				while opc == "1":
                                        print("[1]instalar [2]sair ")
				if repo == "1":
					cmd1 = os.system("apt-get install nmap")
				elif repo  "2":
					cmd1 = os.system("exit")
