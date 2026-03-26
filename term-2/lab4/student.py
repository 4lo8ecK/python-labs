import random as rnd
import time as tm

class StConst:
    ID_MAX_LEN = 10000000

    GRANT_MIN = 1500
    GRANT_MAX = 80000

    SNAMES_BANK = ['Иванов', 'Петров', 'Васильев', 'Кузнецов', 'Иванова', 'Петрова', 'Васильева', 'Кузнецова']
    ADDRESSES_BANK = ['Москва', 'Чебоксары', 'Нижний Новгород', 'Казань', 'Санкт-Петербург']
    MARITAL_STATUS = ['состоит в браке', 'не состоит в браке']


class Student:
    def __init__(self, grade_id: int = None, surname: str = None,
        grant: int = None, address: str = None, marital_status: str = None
        ) -> None:

        if isinstance(grade_id, str):
            grade_id = int(grade_id)
        elif not(isinstance(grade_id, int)):
            raise ValueError('grade_id принимает значения типа int, а на вход даётся', type(grade_id))

        if not(isinstance(surname, str)):
            raise ValueError('surname принимает значения типа str, а на вход даётся', type(surname))

        if isinstance(grant, str):
            grant = int(grant)
        elif not(isinstance(grant, int)):
            raise ValueError('grant принимает значения типа int, а на вход даётся', type(grant))

        if not(isinstance(address, str)):
            raise ValueError('address принимает значения типа str, а на вход даётся', type(address))
        
        if not(isinstance(marital_status, str)):
            raise ValueError('marital_status принимает значения типа str, а на вход даётся', type(marital_status))
        
        self.grade_id: int = grade_id
        self.surname: str = surname
        self.grant: int = grant
        self.address: str = address
        self.marital_status: str = marital_status        

    def __str__(self) -> str:
        return f'Студент(ID: {self.grade_id}, \'{self.surname}\', стипендия: {self.grant} руб., место жительства: {self.address}, семейное положение: {self.marital_status})'

    def to_tuple(self) -> tuple:
        return (self.grade_id, self.surname, self.grant, self.address, self.marital_status)

    @staticmethod
    def rnd_seed() -> None:
        rnd.seed(int(tm.time()*1000))

    @staticmethod
    def __get_random_elem(lst: list = None):
        return lst[rnd.randint(0, len(lst)-1)]

    @staticmethod
    def get_random(id_lst: list[int] = None) -> Student:
        if id_lst == None:
            tmp_id = rnd.randint(1, StConst.ID_MAX_LEN)
        elif isinstance(id_lst, list):
            while tmp_id in id_lst:
                tmp_id = rnd.randint(1, StConst.ID_MAX_LEN)
        else:
            raise TypeError()
        
        rand = Student.__get_random_elem
        return Student(
            tmp_id, rand(StConst.SNAMES_BANK),
            int(rnd.randint(StConst.GRANT_MIN, StConst.GRANT_MAX)),
            rand(StConst.ADDRESSES_BANK),
            rand(StConst.MARITAL_STATUS))

if __name__ == "__main__":
    a = Student.get_random().to_tuple()
    
    for i in a:
        print(i)