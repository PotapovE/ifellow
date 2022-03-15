class BaseConverter():
    """Конвертер градусов из C в K, F"""

    def __init__(self, degrees_c):
        self.degrees_c = degrees_c

    def convert(self):
        return f'Градусы K: {round((273.15 + self.degrees_c), 2)}\nГрадусы F: {round((self.degrees_c * 9 / 5 + 32), 2)}'

print(BaseConverter(float(input('Введите градусы С: '))).convert())