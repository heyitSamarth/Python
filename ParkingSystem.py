import datetime
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

def create_database():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS Billing(vehicle_no TEXT,vehicle_type TEXT, park_in_time TIMESTAMP NOT NULL, park_out_time TIMESTAMP NOT NULL,charges INTEGER)")
	conn.commit()
	c.execute("CREATE TABLE IF NOT EXISTS Booking(vehicle_no TEXT,vehicle_type TEXT, building integer, floor integer,row integer,column integer,park_in_time TIMESTAMP NOT NULL)")
	conn.commit()
	c.execute("CREATE TABLE IF NOT EXISTS Vehicle(vehicle_no TEXT,vehicle_type TEXT, vehicle_owner TEXT, vehicle_colour TEXT,vehicle_brand TEXT,vehicle_parked TEXT)")
	conn.commit()
	c.execute("CREATE TABLE IF NOT EXISTS all_employee(employee_name TEXT,employee_contact, employee_id TEXT, employee_password TEXT)")
	conn.commit()
	print(Back.LIGHTMAGENTA_EX+"DATABASE CONNECTED")

def picle_dump():
	f = open("test.pkl", "wb")
	dump(parking_space, f)

def view_buildings():
	for i in range(len(parking_space)):
		print(f"--------",end=" ")
	print()
	for i in range(len(parking_space)):
		print(f"| Bno  |",end=" ")
	print()
	for i in range(len(parking_space)):
		print(f"|  {i}   |",end=" ")
	print()
	for i in range(len(parking_space)):
		print(f"--------",end=" ")
	print()
	for i in range(len(parking_space)):
		print(f"floors {len(parking_space[i])}",end=" ")
	print()

def view_floors(building_no):
	print(f"------------")
	for i in reversed(range(len(parking_space[building_no]))):
		print(f"|floor no {i}|")
		print(f"------------")

def view_slots(building_no,floor_no,row="@",column="@"):
	print()
	rcount=0
	for rows in parking_space[building_no][floor_no]:
		print(f"{rcount}-> | ",end=" ")
		
		count=0
		for slot in rows:
			if(row==rcount and column==count):
				print(Back.RED+f"[{count}]",end=" ")
				print(" ",end=" ")
				count=count+1
			elif(slot==1 ):
				print(Back.MAGENTA+f"[{count}]",end=" ")
				print(" ",end=" ")
				count=count+1
			else:
				print(f"[{count}]",end=" ")
				print(" ",end=" ")
				count=count+1
		print("|")
		rcount=rcount+1
	print()	

def display_parking():
	view_buildings()
	print(Back.YELLOW +  '   Please Enter Building no :   ')
	building_no = int(input("-> "))
	view_floors(building_no)
	print(Back.YELLOW +  '   Please Enter floor no :   ')
	floor_no = int(input("-> "))
	view_slots(building_no,floor_no)
	return(building_no,floor_no)		







def find_vehicle():
	print(Back.YELLOW + "Enter Vehicle no of Vehicle u want to get location of ")
	V_no=input("-> ")
	V_no=V_no.upper()
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("Select building,floor,row,column FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	if(len(c.fetchall())==0):
		print(Back.RED + "Enter Correct Vehicle no  ")
		main()
	location=c.fetchall()
	location=location[0]
	print(Back.GREEN + f"Your Vechile is Located at Floor no {location[1]} of Buildin no {location[0]} at Red location (row {location[2]} and column {location[3]})")
	view_slots(location[0],location[1],location[2],location[3])


def vehicle_charges(V_no):
	return 100


def unpark_vehicle():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	print(Back.YELLOW + "Enter Vehicle no of Vehicle u want to Unpark")
	V_no=input("-> ")
	V_no=V_no.upper()
	c.execute("Select building,floor,row,column,vehicle_type,park_in_time FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	vehicle_details=c.fetchall()
	if(len(vehicle_details)==0):
		print(Back.RED + "Enter Correct Vehicle no  ")
		employee_functionality()
	vehicle_details=vehicle_details[0]
	building_no=vehicle_details[0]
	floor_no=vehicle_details[1]
	row=vehicle_details[2]
	column=vehicle_details[3]
	v_type=vehicle_details[4]
	park_in_time=vehicle_details[5]
	print(Back.GREEN + f"Your Vechile is Located at Floor no {vehicle_details[1]} of Buildin no {vehicle_details[0]} at Red location (row {vehicle_details[2]} and column {vehicle_details[3]})")
	view_slots(building_no,floor_no,row,column)
	parking_space[building_no][floor_no][row][column]=0
	
	print(Back.YELLOW +"Calculating Vechile Charges ")

	charges=vehicle_charges(V_no)

	print(Back.GREEN +f"Charges for vehicle no {V_no} are {charges}$")
	input("Press Enter if payment Recived")
	c.execute("INSERT INTO Billing(vehicle_no,vehicle_type , park_in_time , park_out_time, charges ) VALUES (?,?,?,?,?)", (V_no,v_type,park_in_time,datetime.datetime.now(),charges))
	conn.commit()
	c.execute("DELETE FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	conn.commit()
	c.execute("UPDATE Vehicle SET vehicle_parked = (?) WHERE vehicle_no=(?) ",("UP",V_no,))
	conn.commit()
	conn.close()
	picle_dump()
	print(Back.GREEN +"Vechile unparked ")
	print(Back.BLUE +"Thankyou for Visiting")
	employee_functionality()
	

def do_booking(V_no,V_type,building_no,floor_no,row,column):
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("INSERT INTO Booking(vehicle_no,vehicle_type , building , floor ,row ,column ,park_in_time  ) VALUES (?,?,?,?,?,?,?)", (V_no,V_type,building_no,floor_no,row,column,datetime.datetime.now()))
	conn.commit()
	conn.close()
	print(Back.GREEN + "Booking Done")


def park_vehicle():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	(building_no,floor_no)=display_parking()
	print(Back.YELLOW +  '   Please Enter row you want to select    : ')
	row = int(input("-> "))
	print(Back.YELLOW +  '   Please Enter column you want to select : ')
	column = int(input("-> "))
	if(parking_space[building_no][floor_no][row][column]==1):
		print(Back.Red + "Slot already booked ")
		park_vehicle()
	view_slots(building_no,floor_no,row,column)
	V_no=   str(input("Please Enter Vehicle no            -> "))
	V_no=V_no.upper()
	c.execute("Select count(*) From Vehicle WHERE vehicle_no=(?)",(V_no,))
	count = c.fetchall()

	if(count[0][0]==0):
		print(Back.CYAN + "+------------------------+")
		print(Back.CYAN + "|  1- Car (LMV)          |")
		print(Back.CYAN + "|  2- Truck (HMV)        |")
		print(Back.CYAN + "|  3- Bike (MC)          |")
		print(Back.CYAN + "+------------------------+")
		V_type_option=0
		while (V_type_option!='1' and  V_type_option!='2' and V_type_option!='3'):
			V_type_option=input("Please Select Vehicle type         -> ")
		if(V_type_option=='1'):
			V_type="LMV"
		if(V_type_option=='2'):
			V_type="HMV"
		if(V_type_option=='3'):
			V_type="MC"
		V_owner=str(input("Please Enter Vehicle owner         -> "))
		V_colour=   input("Please enter Vehicle colour        -> ")
		V_brand=    input("Please enter Vehical brand         -> ")
		print(Back.YELLOW + "Please Verify the Information")
		print("Vehicle no       = "+ V_no)
		print("Vehicle type     = "+ V_type)
		print("Vehicle owner    = "+ V_owner)
		print("Vehicle colour   = "+ V_colour)
		print("Vehical brand    = "+ V_brand)
		input("Press Enter to continue or CTRL+C to Break Operation")
		c = conn.cursor()
		c.execute("INSERT INTO Vehicle(vehicle_no,vehicle_type , vehicle_owner, vehicle_colour ,vehicle_brand,vehicle_parked) VALUES (?,?,?,?,?,?)", (V_no.upper(),V_type.upper(),V_owner,V_colour,V_brand,"P"))
		conn.commit()
		conn.close()
		print(Back.GREEN + "Vehicle information stored")
	
	if(count[0][0]!=0):
		print(Back.GREEN + "Vehicle Already stored")
		c.execute("Select vehicle_parked From Vehicle WHERE vehicle_no=(?)",(V_no,))
		parked = c.fetchall()[0][0]
		if(parked=="P"):
			print(Back.RED + "Vehicle Already Parked ")
			park_vehicle()
		c.execute("UPDATE Vehicle SET vehicle_parked = (?) WHERE vehicle_no=(?) ",("P",V_no))
		conn.commit()
		c.execute("Select vehicle_type From Vehicle WHERE vehicle_no=(?)",(V_no,))
		V_type=c.fetchall()
		V_type=V_type[0][0]
		conn.commit()
		conn.close()
	do_booking(V_no,V_type,building_no,floor_no,row,column)
	
	parking_space[building_no][floor_no][row][column]=1	
	picle_dump()
	employee_functionality()


def employee_functionality():
	print(Back.CYAN + "+------------------------------+")
	print(Back.CYAN + "|  1- Park a Vehicle           |")
	print(Back.CYAN + "|  2- Unpark a Vehicle         |")
	print(Back.CYAN + "|  3- Display Parking space    |")
	print(Back.CYAN + "|  4- Logout                   |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		park_vehicle()
	elif user_input == '2':
		unpark_vehicle()
	elif user_input == '3':
		display_parking()
		employee_functionality()
	elif user_input == '4':
		main()
	else:
		print(Back.RED+"    Please enter valid input    ")
		employee_functionality()


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
			parking_space.append([[]])
			picle_dump()
			view_buildings()
			change_parking_space()
		elif user_input2 == '2':
			view_buildings()
			print(Back.YELLOW +  '   Please Enter Building no :   ')
			user_input3 = int(input("-> "))
			parking_space[user_input3].append([])
			picle_dump()
			view_floors(user_input3)
			change_parking_space()
		elif user_input2 == '3':
			(building_no,floor_no)=display_parking()	
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
			view_slots(building_no,floor_no)
			change_parking_space()
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
	print(Back.CYAN + "|  4- Logout                   |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		create_employee()
	elif user_input == '2':
		change_parking_space()
	elif user_input == '3':
		display_parking()
		admin_functionality()
	elif user_input == '4':
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
	print(Back.CYAN + "|  2- Find a Vehicle          |")
	print(Back.CYAN + "|  3- Display Vehicle Charges  |")
	print(Back.CYAN + "|  4- Exit                     |")
	print(Back.CYAN + "+------------------------------+")
	user_input = input("-> ")
	if user_input == '1':
		login()
	elif user_input == '2':
		find_vehicle()
	elif user_input == '3':
		vehicle_charges()
	elif user_input == '4':
		exit()
	else:
		print(Back.RED+"    Please enter valid input    ")
		main()


if __name__ == '__main__':
	create_database()
	main()
