'''
Airline / Hotel Reservation System
Create a reservation system which books airline seats or hotel rooms. It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach. Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.
'''


class Reservation:
    def __init__(self, name, last_name, id):
        self.name = name
        self.last_name = last_name
        self.id = id


class Hotel:

    def __init__(self, customer):
        self.customer = customer
        self.hotel_rooms = {"Single": 50,
                            "Double": 50,
                            "Suite": 20,
                            "Penthouse": 3
                            }

        self.room_prices = {"Single": 80,
                            "Double": 110,
                            "Suite": 380,
                            "Penthouse": 2800
                            }

    def reserve_room(self, room):
        self.hotel_rooms[room] -= 1
        print("Room reserved")

    def free_room(self, room):
        self.hotel_rooms[room] += 1

    def available_room(self, room):

        if room in self.hotel_rooms.keys():

            if self.hotel_rooms[room] > 0:
                print("Available rooms {0}".format(self.hotel_rooms[room]))
                return True

            else:
                print("Not available rooms")
                return False

class Airline:

    def __init__(self, customer):
        self.customer = customer
        self.airline_seats = {"Economy": 150,
                              "Premium Economy": 40,
                              "Business": 80,
                              "First Class": 50
                              }

        self.seat_prices = {"Economy": 180,
                            "Premium Economy": 230,
                            "Business": 310,
                            "First Class": 490
                            }

    def reserve_seat(self, seat):
        self.airline_seats[seat] -= 1
        print("Seat reserved.")

    def free_seat(self, seat):
        self.airline_seats[seat] += 1

    def available_seats(self,seat):

        if seat in self.airline_seats.keys():

            if self.airline_seats[seat] > 0:
                print("Available seats {0}".format(self.airline_seats[seat]))
                return True
                
            else:
                print("Not available seats")
                return False
