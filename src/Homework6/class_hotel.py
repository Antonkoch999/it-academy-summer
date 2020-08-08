class Hotel:

    def __init__(self, name):
        self.name = name
        self.room_dct = {}
        self.__create_room()
        self.client_identification = {}

    def __create_room(self):
        self.room_dct = {'Single': {},
                         'Double': {},
                         'Lux': {},
                         }
        self.booked_a_room = {'Single': {},
                              'Double': {},
                              'Lux': {},
                              }
        self.create_single_room()
        self.create_double_room()
        self.create_lux_room()

    def create_single_room(self, quantity_single=3):
        create_single = {room_number: SingleRoom for room_number in
                         range(1, quantity_single + 1)}
        self.room_dct['Single'] = create_single

    def create_double_room(self, quantity_single=3, quantity_double=6):
        create_double = {room_number: DoubleRoom for room_number in
                         range(quantity_single + 1, quantity_double + 1)}
        self.room_dct['Double'] = create_double

    def create_lux_room(self, quantity_double=6, quantity_lux=8):
        create_lux = {room_number: LuxRoom for room_number in
                      range(quantity_double + 1, quantity_lux + 1)}
        self.room_dct['Lux'] = create_lux

    def book_a_room(self, type_room, first_name, last_name, passport_id):
        client = Client(first_name, last_name, passport_id)

        def find_free_room():
            if self.room_dct[type_room]:
                for room_number in self.room_dct[type_room].keys():
                    if room_number not in self.booked_a_room[type_room].keys():
                        self.booked_a_room[type_room][room_number] = \
                            self.room_dct[type_room][room_number], client
                        self.client_identification[passport_id] = (
                            client,
                            client.full_name,
                            room_number,
                            type_room,
                        )
                        del self.room_dct[type_room][room_number]
                        return f'Thanks, Your room number {room_number}'
            else:
                return f"Sorry, we haven't free room {type_room}"

        if passport_id in self.client_identification.keys():
            """
            Если клиент повторно обратился
            """
            instance_room = 2
            if self.client_identification[passport_id][
                    instance_room] in self.room_dct[type_room].keys():
                instance_client = 0
                client = self.client_identification[
                    passport_id][instance_client]
                yes_or_no = int(input('Do you want to '
                                      'book your last room?\n'
                                      'Enter 1 if "YES" or 2 if "NO"\n'))
                if yes_or_no == 1:
                    """Бронируем комнату с используя данные с прошлого
                    бронирования.
                    """
                    inst_room_num = self.client_identification[
                        passport_id][instance_room]
                    self.booked_a_room[type_room][inst_room_num] = \
                        self.room_dct[type_room][inst_room_num], client
                    return f'Thanks, Your room number {inst_room_num}'
                else:
                    """Просто находим свободную комнату"""
                    return find_free_room()

            else:
                return 'Sorry, Your last room is currently booked'
        else:
            """Если клиент в первый раз"""
            return find_free_room()

    def free_a_room(self, type_room, room_number):

        if room_number in self.booked_a_room[type_room].keys():
            room_without_client = 0
            self.room_dct[type_room][room_number] = \
                self.booked_a_room[type_room][room_number][room_without_client]
            del self.booked_a_room[type_room][room_number]
            return 'Goodbye'


class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price


class SingleRoom(Room):

    def __init__(self, number, price=50):
        super().__init__(number, price)
        self.type_ = 'Single'


class DoubleRoom(Room):

    def __init__(self, number, price=150):
        super().__init__(number, price)
        self.type_ = 'Double'


class LuxRoom(Room):

    def __init__(self, number, price=350):
        super().__init__(number, price)
        self.type_ = 'Lux'


class Client:
    def __init__(self, first_name, last_name, passport_id):
        self.first_name = first_name
        self.last_name = last_name
        self.passport_id = passport_id
        self.full_name = f'{self.first_name} {self.last_name}'


mariot = Hotel('Mariot')
print('Бронируем комнату', mariot.book_a_room('Single', 'Anton',
                                              'Kochnevski', 'AB1348908'))
print(mariot.booked_a_room)
print('Освобождаем комнату', mariot.free_a_room('Single', 1))
print(mariot.booked_a_room)
print('Повторное заселение', mariot.book_a_room('Single', 'Anton',
                                                'Kochnevski', 'AB1348908'))
print(mariot.booked_a_room)
print(mariot.free_a_room('Single', 1))
print(mariot.booked_a_room)
