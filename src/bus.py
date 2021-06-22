class Bus:

    def __init__(self, route_number, end_point):
        self.route_number = route_number
        self.destination = end_point
        self.passengers= []
    
    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self,passenger):
        self.passengers.append(passenger)

    def drop_off(self,passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers.clear()
    
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        

