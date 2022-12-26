class Notebook:# TODO Написать 3 класса с документацией и аннотацией типов
    def __init__(self,count_pages: int,written_pages: int, color: str):
        if not isinstance(count_pages, int):
            raise TypeError('Количество страниц должны быть типа int')
        self.count_pages = count_pages
        if written_pages < 0:
            raise ValueError('Исписанных страниц не модет быть меньше 0')
        self.written_pages = written_pages
        if not isinstance(color,str):
            raise TypeError('Название цвета должно быть типа str')
        self.color = color

    def torn(self):
        print('Тетрадь порвалась')
        self.profit = 0

class Pans_packaging:
    def __init__(self,color: str, pens_per_pack: int):
        if not isinstance(color,str):
            raise TypeError('Цвет ручки должен быть типа str')
        self.color = color
        if pens_per_pack < 0:
            raise ValueError('Ручек в упаковке должно быть больше 0')
        self.pens_per_pack = pens_per_pack

    def lost(self):
        print('Ручки потерялись')
        self.pens = 0

class Car:
    def __init__(self, color: str,number: str, count_door: int ):
        if not  isinstance(color, str):
            raise TypeError('Цвет должен содержать только буквы')
        self.color = color
        if not isinstance(number,str):
            raise TypeError('Номер машины должен содержать цифры и буквы')
        self.number = number
        if count_door <= 0:
            raise ValueError('Машины без дверей быть не может')
        self.count_door = count_door

if __name__ == "__main__":
    notebook1 = Notebook(18, 11, 'синий')
    notebook2 = Notebook(36, 20, 'зелёный')
    pans = Pans_packaging('синий', 10)
    car1 = Car('белый', 'BP2121ER', 5)
    import doctest
    doctest.testmod()
    pass
