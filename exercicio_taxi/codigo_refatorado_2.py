from datetime import datetime, timedelta

class Client:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    
    def get_id(self):
        return self._id
    
    def get_name(self):
        return self._name

class Race:
    def __init__(self, id):
        self._id = id
    
    def get_id(self):
        return self._id

    def start_race(self):
        self._start_date_time = datetime.now()

    def get_start_date_time(self):
        return self._start_date_time
    
    def end_race(self):
        # self._stop_date_time = stop_date_time

        # mock
        delta_tempo_mock = timedelta(hours=0, minutes=15, seconds=0)
        self._stop_date_time = self.get_start_date_time() + delta_tempo_mock
    
    def get_stop_date_time(self):
        return self._stop_date_time

    def get_duration_race(self):
        self._duration_race = ((self.get_stop_date_time() - self.get_start_date_time()).seconds)/60
        return self._duration_race
    
    def is_flag_01(self):
        if ((self.get_start_date_time().hour<6) or (self.get_start_date_time().hour>22)):
            return False
        else:
            return True
            
class Bill:
    def __init__(self, id, client_obj, race_obj):
        self._id = id
        self._client = client_obj
        self._race = race_obj

    def close_bill(self):
        if self._race.is_flag_01():
            self._race_value = 5.50 + (0.50*self._race.get_duration_race())
        else:
            self._race_value = 5.50 + (0.50*1.10*self._race.get_duration_race())
        self.print_bill()
    
    def print_header(self):
        print('***********************')
        print('Extrato da Corrida')
        print('***********************')
        print('Cód. cliente: {}'.format(self._client.get_id()))
        print('Nome cliente: {}'.format(self._client.get_name()))
        print('***********************')
    
    def print_footer(self):
        print('***********************')
        print(datetime.now())
        print('Cód. Corrida: {}'.format(self._id))
        print('***********************')

    def print_race_info(self):
        print('Início da corrida: {}'.format(self._race.get_start_date_time()))
        print('Término da corrida: {}'.format(self._race.get_stop_date_time()))
        print('Duração da corrida: {}'.format(self._race.get_duration_race()))
        print('Valor da corrida: {}'.format(self._race_value))

    def print_bill(self):
        self.print_header()
        self.print_race_info()
        self.print_footer()

if __name__ == "__main__":
    client_1 = Client(1, 'Client 1')
    race_1 = Race(1)
    race_1.start_race()
    race_1.end_race()
    bill_1 = Bill(1, client_1, race_1)
    bill_1.close_bill()