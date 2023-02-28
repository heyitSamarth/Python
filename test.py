import time
import getpass
import warnings
import sqlite3
import os
from tqdm.auto import tqdm
import numpy
import colorama
from colorama import Back, Style
from pickle import load,dump
warnings.filterwarnings("ignore")
colorama.init(autoreset=True)

parking_data = open("test.pkl", "rb")
parking_space=load(parking_data)
avail_spaces = 0
total_spaces = 0
def picle_dump():
	f = open("test.pkl", "wb")
	dump(parking_space, f)
	

# def change_parking_space():
# 	print(Back.CYAN + "+------------------------------+")
# 	print(Back.CYAN + "|  1- Add Parking Space        |")
# 	print(Back.CYAN + "|  2- Remove Parking space     |")
# 	print(Back.CYAN + "|  3- Previous Menu            |")
# 	print(Back.CYAN + "+------------------------------+")
# 	user_input = input("-> ")
# 	if user_input == '1':
# 		print(Back.CYAN + "+------------------------------+")
# 		print(Back.CYAN + "|  1- Add Building             |")
# 		print(Back.CYAN + "|  2- Add floor in building    |")
# 		print(Back.CYAN + "|  3- Add Slot in building     |")
# 		print(Back.CYAN + "|  4- Previous Menu            |")
# 		print(Back.CYAN + "+------------------------------+")
# 		user_input2 = input("-> ")
# 		if user_input2 == '1':
# 			global parking_space
# 			parking_space.append([[]])
# 			picle_dump()
# 		elif user_input2 == '2':
# 			for i in range(len(parking_space)):
# 				print(f"Building no {i}")
# 			print(Back.YELLOW +  '   Please Enter Building no :   ')
# 			user_input3 = int(input("-> "))
# 			parking_space[user_input3].append([])
# 			picle_dump()
# 		elif user_input2 == '3':
# 			for i in range(len(parking_space)):
# 				print(f"Building no {i}")
# 			print(Back.YELLOW +  '   Please Enter Building no :   ')
# 			building_no = int(input("-> "))
# 			for i in range(len(parking_space[building_no-1])):
# 				print(f"floor no {i}")
# 			print(Back.YELLOW +  '   Please Enter floor no :   ')
# 			floor_no = int(input("-> "))
# 			print(Back.YELLOW +  '   Please Enter no of rows :    ')
# 			no_of_rows = int(input("-> "))
# 			print(Back.YELLOW +  '   Please Enter no of columns : ')
# 			no_of_columns = int(input("-> "))
# 			existing_slot=len(parking_space[building_no][floor_no])
# 			for i in range( no_of_rows):
# 				parking_space[building_no][floor_no].append([])
# 				for j in range(no_of_columns):
# 					parking_space[building_no][floor_no][i+existing_slot].append(0)
# 			picle_dump()
# 		elif user_input2 == '4':
# 			change_parking_space()
# 		else :
# 			print(Back.RED+"    Please enter valid input    ")
# 			change_parking_space()
		
# 	elif user_input == '2':
# 		pass
# 	elif user_input == '3':
# 		pass
# 	else:
# 		print(Back.RED+"    Please enter valid input    ")
# 		change_parking_space()

def employee_functionality():
	pass


employee_functionality()