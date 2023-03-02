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
avail_spaces = 0
total_spaces = 0
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
		print(f"{rcount}| ",end=" ")
		
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


	# for i in parking_space[building_no][floor_no]:
	# 	if(row!='@'  and i==parking_space[building_no][floor_no][row]):
	# 		print('[',end=" ")
	# 		for col in range(len(i)):
	# 			if(col==column):
	# 				print(Back.WHITE+"1" ,end=" ")
	# 			else:
	# 				print(parking_space[building_no][floor_no][row][col],end=" ")
	# 				print("," ,end=" ")
	# 		print(' ]')	
	# 	print(i)
	# print()	

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

def display_parking():
	view_buildings()
	print(Back.YELLOW +  '   Please Enter Building no :   ')
	building_no = int(input("-> "))
	view_floors(building_no)
	print(Back.YELLOW +  '   Please Enter floor no :   ')
	floor_no = int(input("-> "))
	view_slots(building_no,floor_no)
	return(building_no,floor_no)	


def do_booking(V_no,V_type,building_no,floor_no,row,column):
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS Booking(vehicle_no TEXT,slot_type TEXT, building integer, floor integer,row integer,column integer,park_in_time TIMESTAMP NOT NULL)")
	c = conn.cursor()
	c.execute("INSERT INTO Booking(vehicle_no,slot_type , building , floor ,row ,column ,park_in_time  ) VALUES (?,?,?,?,?,?,?)", (V_no,V_type,building_no,floor_no,row,column,datetime.datetime.now()))
	conn.commit()
	conn.close()
	print(Back.GREEN + "Booking Done")


# def park_vehicle():
# 	conn = sqlite3.connect('Database.db')
# 	c = conn.cursor()
# 	c.execute("ALTER TABLE Booking RENAME COLUMN slot_type TO vehicle_type;")
# 	conn.commit()
# 	conn.close()
# 	(building_no,floor_no)=display_parking()
# 	print(Back.YELLOW +  '   Please Enter row you want to select    : ')
# 	row = int(input("-> "))
# 	print(Back.YELLOW +  '   Please Enter column you want to select : ')
# 	column = int(input("-> "))
# 	if(parking_space[building_no][floor_no][row][column]==1):
# 		print(Back.Red + "Slot already booked ")
# 		park_vehicle()
# 	view_slots(building_no,floor_no,row,column)
# 	V_no=   str(input("Please Enter Vehicle no            -> "))
# 	V_no=V_no.upper()
# 	c.execute("Select count(*) From Vehicle WHERE vehicle_no=(?)",(V_no,))
# 	count = c.fetchall()

# 	if(count[0][0]==0):
# 		print(Back.CYAN + "+------------------------+")
# 		print(Back.CYAN + "|  1- Car (LMV)          |")
# 		print(Back.CYAN + "|  2- Truck (HMV)        |")
# 		print(Back.CYAN + "|  3- Bike (MC)          |")
# 		print(Back.CYAN + "+------------------------+")
# 		V_type_option=0
# 		while (V_type_option!='1' and  V_type_option!='2' and V_type_option!='3'):
# 			V_type_option=input("Please Select Vehicle type         -> ")
# 		if(V_type_option=='1'):
# 			V_type="LMV"
# 		if(V_type_option=='2'):
# 			V_type="HMV"
# 		if(V_type_option=='3'):
# 			V_type="MC"
# 		V_owner=str(input("Please Enter Vehicle owner         -> "))
# 		V_colour=   input("Please enter Vehicle colour        -> ")
# 		V_brand=    input("Please enter Vehical brand         -> ")
# 		print(Back.YELLOW + "Please Verify the Information")
# 		print("Vehicle no       = "+ V_no)
# 		print("Vehicle type     = "+ V_type)
# 		print("Vehicle owner    = "+ V_owner)
# 		print("Vehicle colour   = "+ V_colour)
# 		print("Vehical brand    = "+ V_brand)
# 		input("Press Enter to continue or CTRL+C to Break Operation")
# 		c = conn.cursor()
# 		c.execute("INSERT INTO Vehicle(vehicle_no,vehicle_type , vehicle_owner, vehicle_colour ,vehicle_brand,vehicle_parked) VALUES (?,?,?,?,?,?)", (V_no.upper(),V_type.upper(),V_owner,V_colour,V_brand,"P"))
# 		conn.commit()
# 		conn.close()
# 		print(Back.GREEN + "Vehicle information stored")
	
# 	if(count[0][0]!=0):
# 		print(Back.GREEN + "Vehicle Already stored")
# 		c.execute("Select vehicle_parked From Vehicle WHERE vehicle_no=(?)",(V_no,))
# 		parked = c.fetchall()[0][0]
# 		if(parked=="P"):
# 			print(Back.RED + "Vehicle Already Parked ")
# 			park_vehicle()
# 		c.execute("UPDATE Vehicle SET vehicle_parked = (?) WHERE vehicle_no=(?) ",("P",V_no))
# 		c.execute("Select vehicle_type From Vehicle WHERE vehicle_no=(?)",(V_no,))
# 		V_type=c.fetchall()
# 		V_type=V_type[0][0]
# 		conn.commit()
# 		conn.close()
# 	do_booking(V_no,V_type,building_no,floor_no,row,column)
# 	parking_space[building_no][floor_no][row][column]=1	
# 	picle_dump()
	

# display_parking()
def vehicle_charges():
	pass

def unpark_vehicle():
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS Billing(vehicle_no TEXT,vehicle_type TEXT, park_in_time TIMESTAMP NOT NULL, park_out_time TIMESTAMP NOT NULL,charges INTEGER)")
	conn.commit()
	print(Back.YELLOW + "Enter Vehicle no of Vehicle u want to Unpark")
	V_no=input("-> ")
	V_no=V_no.upper()
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("Select building,floor,row,column,vehicle_type,park_in_time FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	vehicle_details=c.fetchall()
	if(len(vehicle_details)==0):
		print(Back.RED + "Enter Correct Vehicle no  ")
		exit()
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
	print(Back.GREEN +"Vechile unparked ")
	print(Back.YELLOW +"Calculating Vechile Charges ")
	charges=vehicle_charges(V_no)
	print(Back.GREEN +f"Charges for vehicle no {V_no} are {charges}$")
	input("Press Enter if payment Recived")
	c.execute("INSERT INTO Billing(vehicle_no,vehicle_type , park_in_time , park_out_time ) VALUES (?,?,?,?)", (V_no,v_type,park_in_time,datetime.datetime.now(),charges))
	conn.commit()
	
	c.execute("DELETE FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	conn.commit()
	c.execute("UPDATE Vehicle SET vehicle_parked = (?) WHERE vehicle_no=(?) ",("UP",V_no,))
	conn.commit()
	conn.close()
	picle_dump()

def vehicle_charges(V_no):
	conn = sqlite3.connect('Database.db')
	c = conn.cursor()
	c.execute("Select vehicle_type,park_in_time FROM Booking WHERE vehicle_no=(?) ",(V_no,))
	vehicle_details=c.fetchall()
	if(len(vehicle_details)==0):
		print(Back.RED + "Enter Correct Vehicle no  ")
		exit()
	vehicle_details=vehicle_details[0]
	v_type=vehicle_details[0]
	park_in_time=vehicle_details[1]
	duration=-datetime.datetime.now()-datetime.datetime.strptime(park_in_time,'%Y-%m-%d %H:%M:%S.%f')
	duration=divmod(duration.total_seconds(),3600)[0]
	if(v_type=="LMV"):
		if(duration<2):
			return 20
		elif(duration<12):
			return 40
		else:
			return 100
	elif(v_type=="HMV"):
		if(duration<2):
			return 50
		elif(duration<12):
			return 150
		else:
			return 500
	elif(v_type=="MC"):
		if(duration<2):
			return 10
		elif(duration<12):
			return 30
		else:
			return 70


# vehicle_charges("MP07FL7890")

# unpark_vehicle()

for building in parking_space:
	for floor in building:
		for slot in floor:
			print(slot)
		print("\n")
	print("\n\n")