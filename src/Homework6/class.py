"""
Создайте  модель из жизни. Это может быть бронирование комнаты
в отеле, покупка билета в транспортной компании, или простая РПГ.
Создайте несколько объектов классов, которые описывают
ситуацию Объекты должны содержать как атрибуты так и методы
класса для симуляции различных действий. Программа должна
инстанцировать объекты и эмулировать какую-либо ситуацию -
вызывать методы, взаимодействие объектов и т.д
"""


class Hotel:

    def __init__(self, name):
        self.single_dct = {}
        self.double_dct = {}
        self.lux_dct = {}

        self.room_dct = self.__create_rooms()
        self.booked_room_count = {'Single': 0,
                                  'Double': 0,
                                  'Lux': 0}
        self.booked_room_client = {'Single': {},
                                   'Double': {},
                                   'Lux': {}}
        self.client_information = {}
        self.client_identification = {}
        self.name = name

    def book_a_room(self, type_room, first_name, last_name, passport_id):
        client = Client(first_name, last_name, passport_id)

        def find_free_room():
            for key_room_dct_type_room in self.room_dct[type_room].keys():
                if key_room_dct_type_room in \
                        self.booked_room_client[type_room].keys():
                    continue
                else:
                    self.booked_room_client[
                        type_room][key_room_dct_type_room] = client
                    self.client_information[client] = first_name, \
                        last_name, \
                        passport_id, \
                        key_room_dct_type_room
                    self.client_identification[passport_id] = client
                    break

        if passport_id in self.client_identification.keys():
            client = self.client_identification[passport_id]
            client_room_number = 3
            if self.client_information[client][client_room_number] not in \
                    self.booked_room_client[type_room]:
                decision = int(input('Want to check in again? 1-Yes, 2-No'))
                if decision == 1:
                    self.booked_room_client[type_room][
                        self.client_information[client][
                            client_room_number]] = client
                else:
                    return f'Ok, we find free room. {find_free_room()}'
            else:
                return f'Sorry, your room is booking, ' \
                       f'we find free room. {find_free_room()}'

        if type_room in self.booked_room_count:
            if self.booked_room_count[
                            type_room] < len(self.room_dct[type_room]):
                find_free_room()
                self.booked_room_count[type_room] += 1
                return 'Your room is booked'
            else:
                return 'Sorry, free rooms is not'
        else:
            return 'Sorry, this type rooms in no'

    def free_a_room(self, type_room, passport_id):

        if type_room in self.booked_room_count:
            if self.booked_room_count[type_room]:
                client = self.client_identification[passport_id]
                for key, value_booker_room_count in self.booked_room_client[
                                                    type_room].items():
                    if value_booker_room_count == client:
                        self.booked_room_client[type_room].pop(key)
                        # del self.client_identification[passport_id]
                        break
                    else:
                        return 'Your room not found'
                self.booked_room_count[type_room] -= 1
                return 'Thanks you, goodbye'
            else:
                return 'Your room not found'
        else:
            return 'Your type room not found'

    def __create_rooms(self):
        self.room_dct = {'Single': self.create_single_room(),
                         'Double': self.create_double_room(),
                         'Lux': self.create_lux_room()}
        return self.room_dct

    def create_single_room(self, quantity_single=5):
        for number_room in range(1, quantity_single + 1):
            self.single_dct[number_room] = SingleRoom(number_room)
        return self.single_dct

    def create_double_room(self, quantity_single=5, quantity_double=5):
        start = quantity_single + 1
        quantity_double = quantity_single + quantity_double + 1
        for number_room in range(start, quantity_double):
            self.double_dct[number_room] = DoubleRoom(number_room)
        return self.double_dct

    def create_lux_room(self, quantity_single=5, quantity_double=5,
                        quantity_lux=3):
        start = quantity_single + quantity_double + 1
        quantity_lux = quantity_single + quantity_double + quantity_lux + 1
        for number_room in range(start, quantity_lux):
            self.lux_dct[number_room] = LuxRoom(number_room)
        return self.lux_dct

    def show_spare_rooms(self):
        pass


class Room:

    def __init__(self, number, price=50):
        self.price = price
        self.number = number


class SingleRoom(Room):

    def __init__(self, number, price=100):
        super().__init__(number, price)
        self.type_ = 'Single'
        self.bed = 1
        self.place = 1


class DoubleRoom(Room):

    def __init__(self, number, price=200):
        super().__init__(number, price)
        self.type_ = 'Double'
        self.bed = 1
        self.place = 2


class LuxRoom(Room):

    def __init__(self, number, price=400):
        super().__init__(number, price)
        self.type_ = 'Lux'
        self.bed = 3
        self.place = 5


class Client:

    def __init__(self, first_name, last_name, passport_id):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_id = passport_id
        self.fullname = f'{self.first_name} {self.last_name}'


mariot = Hotel('Mariot')
print(mariot.book_a_room('Single', 'Tom', 'Smith', 'AD1231281'))
print(mariot.book_a_room('Single', 'Will', 'Smith', 'AB123'))
print(mariot.book_a_room('Single', 'Katy', 'Smith', 'AR123'))
print(mariot.booked_room_client)
print(mariot.free_a_room('Single', 'AD1231281'))
print(mariot.free_a_room('Single', 'AB123'))
print(mariot.free_a_room('Single', 'AR123'))
print(mariot.booked_room_client)
print(mariot.booked_room_count)
print(mariot.book_a_room('Single', 'Tom', 'Smith', 'AD1231281'))
print(mariot.booked_room_client)
print(mariot.client_identification)
print(mariot.client_information)
print(mariot.room_dct)