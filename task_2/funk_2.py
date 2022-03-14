# Написать программу, которая должна найти и вывести повторяющийся символ в слове «Hello»

random_text = input('Введите текст: - ')
bufer_sym = []
for i in random_text:
    counter_sym = random_text.count(i)
    if counter_sym > 1:
        if i not in bufer_sym:
            bufer_sym.append(i)
            print(i)