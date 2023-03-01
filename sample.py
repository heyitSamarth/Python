    # ParkingLot Class: This class represents the overall parking lot and contains information about the number of parking spaces available, the number of parking spaces reserved, the number of parking spaces occupied, etc.

    # ParkingSpace Class: This class represents a single parking space within the parking lot. It contains information about the parking space, such as its location, size, availability, etc.

    # Vehicle Class: This class represents a vehicle that enters the parking lot. It contains information about the vehicle, such as its type, license plate number, etc.

    # Reservation Class: This class represents a reservation made by a customer for a specific parking space at a specific time. It contains information about the reservation, such as the customer's name, the parking space reserved, the start and end times of the reservation, etc.

    # Payment Class: This class represents a payment made by a customer for their parking reservation. It contains information about the payment, such as the payment amount, payment method, etc.

    # Customer Class: This class represents a customer who uses the parking lot. It contains information about the customer, such as their name, contact information, payment history, etc.

    # ParkingTicket Class: This class represents a ticket issued to a customer when they enter the parking lot. It contains information about the ticket, such as the ticket number, entry time, etc.

    # ParkingSystem Class: This class represents the overall parking system and contains methods for managing the parking lot, parking spaces, vehicles, reservations, payments, customers, and parking tickets. It serves as the main interface for the parking lot management system.
    
    
    
class ParkingLot:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.reserved_spaces = 0
        self.occupied_spaces = 0
    
    def get_available_spaces(self):
        return self.total_spaces - self.reserved_spaces - self.occupied_spaces

class ParkingSpace:
    def __init__(self, space_id, location, size):
        self.space_id = space_id
        self.location = location
        self.size = size
        self.is_reserved = False
        self.is_occupied = False
    
    def reserve(self):
        self.is_reserved = True
    
    def unreserve(self):
        self.is_reserved = False
    
    def occupy(self):
        self.is_occupied = True
    
    def release(self):
        self.is_occupied = False

class Vehicle:
    def __init__(self, vehicle_type, license_plate):
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate

class Reservation:
    def __init__(self, customer_name, parking_space, start_time, end_time):
        self.customer_name = customer_name
        self.parking_space = parking_space
        self.start_time = start_time
        self.end_time = end_time

class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.payment_history = []

    def add_payment(self, payment):
        self.payment_history.append(payment)

class ParkingTicket:
    def __init__(self, ticket_number, entry_time):
        self.ticket_number = ticket_number
        self.entry_time = entry_time

class ParkingSystem:
    def __init__(self):
        self.parking_lots = []
        self.parking_spaces = []
        self.customers = []
        self.tickets = []

    def add_parking_lot(self, total_spaces):
        parking_lot = ParkingLot(total_spaces)
        self.parking_lots.append(parking_lot)

    def add_parking_space(self, space_id, location, size, lot_index):
        parking_lot = self.parking_lots[lot_index]
        space = ParkingSpace(space_id, location, size)
        parking_lot.reserved_spaces += 1
        self.parking_spaces.append((space, parking_lot))

    def reserve_parking_space(self, customer_name, space_id, start_time, end_time):
        pass
        # make a arr or a dictionary that can store the reserved parking slot and every time assigning a parking space to a vehicle check in
        # the dictionary that this parking space is reserved or not for a specific vehicle registered
    
    # def occupy_parking_space(self, space_id):
    #     space, parking_lot = next(((s, l) for s, l in self.parking_spaces if


# this is a rough idea dekh le 
# agar sahi lage toh
