print("Введите фамилию, имя, отчество и год рождения")
def isint(m):
    try:
        int(m)
        return True
    except ValueError:
        return False
while True:
    try:
        file = open('fio.txt', 'a', encoding='utf8')
        try:
            surname, name, patronymic, year = (i for i in input().split(' '))
            if surname == '-' and name == '-' and patronymic == '-' and year == '-':
                break
            elif isint(year) and len(year) == 4:
                file.write(str(surname) + ' ' + str(name) + ' ' + str(patronymic) + ' ' + str(year) + ' ' + '\n')
            else:
                print('Год рождения должен состоять из четырех цифр !')
        except ValueError:
            print('Корректно введите данные, для праильной работы  !')
        finally:
            file.close()
    except:
        print('Произошла ошибка при открытии файла !')

print('Фамилия Имя Отчество Год рождения')
try:
    file = open('fio.txt', 'r', encoding='utf8')
    while True:
        line = file.readline()
        if not line:
            break
        print('Фамилия ' + ' Имя ' + ' Отчество ' + ' Год рождения ' + '\n')
        print(str(line))
except:
    print('Произошла ошибка при открытии файла')
finally:
    file.close()

