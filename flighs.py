import self as self


class Flights:
  def __init__(self,capacity):
        self.capacity = capacity
        self.passenger=[]

  def add_passenger(self,names):
    if not self.open_seats():
            return False
    self.passenger.append(names)
    return True
  def open_seats(self):
      return self.capacity - len(self.passenger)



flight= Flights(3)

people=["shahzad","ahsan","sajjad","mullan"]

for person in people:
    if flight.add_passenger(person):
        print(f"Addes {person} to flight successfully")
    else:
        print(f"No Available seats for {person}")