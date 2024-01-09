2# Определяем класс Точка, который отвечает за хранение координат на поле
class Tochka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Дополнительная функция, проверяющая, равны ли две точки
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Определяем класс Корабль, в котором хранятся все точки, связанные с каждым кораблем
class Korabl:
    def __init__(self, tochki):
        self.tochki = tochki
        self.razrushen = False  # по умолчанию корабль не разрушен

    # Функция, которая определяет, поражена ли точка на корабле
    def popadanie(self, tochka):
        for tochka_korablya in self.tochki:
            if tochka == tochka_korablya:
                self.tochki.remove(tochka_korablya)
                if not self.tochki:
                    self.razrushen = True
                return True
        return False

# Определяем класс Поле, где будут создаваться корабли и игровое поле   
class Pole:
    def __init__(self):
        self.igrovoye_pole = [['О' for _ in range(6)] for _ in range(6)]
        self.korabli = self.sozdat_korabli()

    def sozdat_korabli(self):
        tochki1 = [Tochka(0, 0), Tochka(0, 1), Tochka(0, 2)] 
        tochki2 = [Tochka(2, 2), Tochka(2, 3)]

        korabl1 = Korabl(tochki1)
        korabl2 = Korabl(tochki2) 

        return [korabl1, korabl2]

    def vistrel(self, tochka):
        for korabl in self.korabli:
            if korabl.popadanie(tochka):
                if korabl.razrushen:
                    print("Корабль разрушен!")
                else:
                    print()
                    print("Попал... :-( ")
                    print()
                self.igrovoye_pole[tochka.x][tochka.y] = "Х"
                return

        self.igrovoye_pole[tochka.x][tochka.y] = "-"
        print()
        print("МИМО! :-))")
        print()

    def otobrazit(self):
        print('  | 1 | 2 | 3 | 4 | 5 | 6 |')
        for i in range(6):
            ryad = str(i + 1) + ' | ' + ' | '.join(self.igrovoye_pole[i]) + ' |'
            print(ryad)
        print()

        

print("Добро пожаловать в игру Морской Бой!")
print("""
Игра происходит на квадратном поле 6x6. 
Каждый игрок имеет свой набор кораблей: один 3-палубный и один 2-палубный.  
Корабли представляют собой ряд из 2 или 3 клеток, расположенных вертикально или горизонтально.
Ваша цель - уничтожить корабли противника- за которого будет играть компьютер.
""")


pole = Pole()

while True:
    print("Ваш ход!")

    pole.otobrazit()

    while True:  # Бесконечный цикл для повторного ввода, если введены неправильные данные
        try:
            x = int(input("Введи X координату по вертикали для выстрела (цифру от 1 до 6): ")) - 1 
            y = int(input("Введи Y координату по горизонтали для выстрела (цифру от 1 до 6): ")) - 1
            if x < 0 or x > 5 or y < 0 or y > 5:
                print("Координаты должны быть в диапазоне от 1 до 6. Попробуйте снова.")
                continue  # Возвращает нас на начало цикла для нового ввода
            break  # Выходим из цикла, если данные корректны
        except ValueError:  # Ошибку ValueError вызывает int() при попытке преобразовать не числовой ввод
            print("Введены некорректные данные. Попробуйте снова.")
    
    tochka = Tochka(x, y)
    pole.vistrel(tochka)

    if all(korabl.razrushen for korabl in pole.korabli):
        print("Поздравляю! Все корабли противника разрушены!")
        break
    
    
