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

def employee_functionality():
	pass

def employee_login():
	conn = sqlite3.connect('Database.db')
	print(Back.YELLOW +'   Please Enter Employee id :   ')
	employee_id=input("-> ")
	c = conn.cursor()
	c.execute("SELECT employee_password FROM all_employee WHERE employee_id=(?)",(employee_id,))
	rows = c.fetchall()
	if(len(rows)==0):
		employee_login()
	else:
		print(Back.YELLOW +'   Please Enter Password :      ')
		employee_password = getpass.getpass()
	if(employee_password==rows[0][0]):
		return True
	else:
		print(Back.RED+"      Invalid Password          ")
		login()


def create_employee():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS employee_record(employee_name TEXT,employee_contact, employee_id TEXT, employee_password TEXT)")
	E_name=str(input("Please Enter Employee Name         -> "))
	E_contact= input("Please enter Employee Contact No   -> ")
	E_id=str(input  ("Please Enter Employee Id           -> "))
	E_password=input("Please enter Employee password     -> ")
	print(Back.YELLOW + "Please Verify the Information")
	print("Employee Name       = "+ E_name)
	print("Employee Contact    = "+ E_contact)
	print("Employee ID         = "+ E_id)
	print("Employee Password   = "+ E_password)
	input("Press Enter to continue or CTRL+C to Break Operation")
	c = conn.cursor()
	c.execute("INSERT INTO all_record(employee_name, employee_contact, employee_id ,employee_password) VALUES (?,?,?,?)", (E_name,E_contact,E_id,E_password))
	conn.commit()
	print(Back.GREEN + "Employee information stored")
	conn.close()


def change_parking_space():
	print(Back.CYAN + "+------------------------------+")
	print(Back.CYAN + "|  1- Add Parking Space        |")
	print(Back.CYAN + "|  2- Remove Parking space     |")
	print(Back.CYAN + "|  3- Previous Menu            |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		print(Back.CYAN + "+------------------------------+")
		print(Back.CYAN + "|  1- Add Building             |")
		print(Back.CYAN + "|  2- Add floor in building    |")
		print(Back.CYAN + "|  3- Add Slot in building     |")
		print(Back.CYAN + "|  4- Previous Menu            |")
		print(Back.CYAN + "+------------------------------+")
		user_input2 = input("-> ")
		if user_input2 == '1':
			global parking_space
			parking_space.append([[]])
			picle_dump()
		elif user_input2 == '2':
			for i in range(len(parking_space)):
				print(f"Building no {i}")
			print(Back.YELLOW +  '   Please Enter Building no :   ')
			user_input3 = int(input("-> "))
			parking_space[user_input3].append([])
			picle_dump()
		elif user_input2 == '3':
			for i in range(len(parking_space)):
				print(f"Building no {i}")
			print(Back.YELLOW +  '   Please Enter Building no :   ')
			building_no = int(input("-> "))
			for i in range(len(parking_space[building_no-1])):
				print(f"floor no {i}")
			print(Back.YELLOW +  '   Please Enter floor no :   ')
			floor_no = int(input("-> "))
			print(Back.YELLOW +  '   Please Enter no of rows :    ')
			no_of_rows = int(input("-> "))
			print(Back.YELLOW +  '   Please Enter no of columns : ')
			no_of_columns = int(input("-> "))
			existing_slot=len(parking_space[building_no][floor_no])
			for i in range( no_of_rows):
				parking_space[building_no][floor_no].append([])
				for j in range(no_of_columns):
					parking_space[building_no][floor_no][i+existing_slot].append(0)
			picle_dump()
		elif user_input2 == '4':
			change_parking_space()
		else :
			print(Back.RED+"    Please enter valid input    ")
			change_parking_space()
		
	elif user_input == '2':
		main()
	elif user_input == '3':
		admin_functionality()
	else:
		print(Back.RED+"    Please enter valid input    ")
		change_parking_space()


def admin_functionality():
	print(Back.CYAN + "+------------------------------+")
	print(Back.CYAN + "|  1- Create Employee          |")
	print(Back.CYAN + "|  2- Change Parking space     |")
	print(Back.CYAN + "|  3- Display Parking space    |")
	print(Back.CYAN + "|  4- Change Parking price     |")
	print(Back.CYAN + "|  5- Exit                     |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		create_employee()
	elif user_input == '2':
		change_parking_space()
	elif user_input == '3':
		pass
	elif user_input == '4':
		pass
	elif user_input == '5':
		main()
	else:
		print(Back.RED+"    Please enter valid input    ")
		admin_functionality()


def login():
	print(Back.CYAN + "+------------------------------+")
	print(Back.CYAN + "|  1- Admin                    |")
	print(Back.CYAN + "|  2- Employee                 |")
	print(Back.CYAN + "|  3- Main Menu                |")
	print(Back.CYAN + "+------------------------------+")
	user_input2 = input("-> ")
	if user_input2 == '1':
		print(Back.YELLOW +  'Please Enter Password : ')
		password = getpass.getpass()
		if password =='aka':
			for i in tqdm(range(4000)):
				print("",end='\r')
			print("------------------------------------------------------------------------------------------------------------------------")
			print(Back.BLUE+"Hello Admin")
			admin_functionality()
		if password != 'aka':
			print(Back.RED+"      Invalid Password          ")
			login()
	elif user_input2 == '2':
		if(employee_login()):
			employee_functionality()
	elif user_input2=='3':
		main()
	else:
		print(Back.RED+"    Please enter valid input    ")
		login()

#-------MainPage----------------------------
def main():
	print(Back.CYAN + "+------------------------------+")
	print(Back.CYAN + "|  1- Login                    |")
	print(Back.CYAN + "|  2- Find a Vehicale          |")
	print(Back.CYAN + "|  3- Display Vehicle Charges  |")
	print(Back.CYAN + "|  4- Exit                     |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		login()
	elif user_input == '2':
		pass
	elif user_input == '3':
		pass
	elif user_input == '4':
		exit()
	else:
		print(Back.RED+"    Please enter valid input    ")
		main()


if __name__ == '__main__':
    main()
