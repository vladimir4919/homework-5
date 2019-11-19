import os
import platform
import version
from victory import conduct_quiz
from bank_account import bank_account_run

while True:
    print('1. создать папку')
    print('2. удалить(файл / папку)')
    print('3. копировать(файл / папку)')
    print('4. просмотр содержимого  рабочей директории')
    print('5. посмотреть только папки)')
    print('6. посмотреть только файлы)')
    print('7. просмотр информации об операционной системе)')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский  счет')
    print('11.смена рабочей директории')
    print('12.выход')

    choice = input('Выберите пункт меню:')
    if choice == '1':#после выбора пользователь вводит название папки, создаем её в рабочей директории
        print("*"*40)
        print()
        version.create_dir()
        print()
        print("*"*40)

    elif choice == '2':#после выбора пользователь вводит название папки или файла,
        # удаляем из рабочей директории если такой есть
        print("*" * 40)
        print()
        version.del_file_or_dir()
        print()
        print("*" * 40)
    elif choice == '3':#после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем
        print("*" * 40)
        print()
        version.copy_file_or_dir()
        print()
        print("*" * 40)

    elif choice == '4':#просмотр содержимого рабочей директории вывод всех объектов в рабочей папке
        print("*" * 40)
        print()
        version.viewing_all_in_working_dir()
        print()
        print("*" * 40)
    elif choice == '5':#  вывод только папок,которые находятся в рабочей папке
        print("*" * 40)
        print()
        version.get_dir_in_working_dir()
        print()
        print("*" * 40)
    elif choice == '6':  # вывод только файлов, которые находятся в рабочей папке
        print("*" * 40)
        print()
     #   version.get_dir_in_working_dir()
        print("Список файлов в рабочей директории:")
        print("\n".join(list(filter(lambda x: os.path.isfile(x), os.listdir(".")))))
        print()
        print("*" * 40)
    elif choice == '7':#просмотр информации об операционной системе
        print(platform.system())
        print(platform.release())
        print("*" * 40)
        print()
    elif choice == '8':#создатель программы вывод информации о создателе программы
        print("*" * 40)
        print()
        print("Создатель программы Воробьев Владимир")
        print()
        print("*" * 40)
    elif choice == '9':#играть в викторину запуск игры викторина из предыдущего дз
        print("*" * 40)
        print("Введите количество вопросов викторины")
        n_st = int(input(f'Количество вопросов викторины'))
        conduct_quiz(n_st)
        print("*" * 40)
        print()
    elif choice == '10':#мой банковский счет
        print("*" * 40)
       # print("Введите количество денежных средств на счету")
        history = []
        account = int(input(f'Введите количество денег на счету первоначально'))
        bank_account_run(account,history)
        print(10)

#запуск программы для работы с банковским счетом из предыдущего дз (задание учебное, после выхода из программы
#управлением счетом в главной программе сумму и историю покупок можно не запоминать)
    elif choice == '11':#смена рабочей директории (*необязательный пункт)
        version.change_working_dir()


#усложненное задание пользователь вводит полный /home/user/... или относительный user/my/... путь.
# Меняем рабочую директорию на ту что ввели и работаем уже в ней
    elif choice == '12':#выход из программы
        print(12)
        break
    else:
        print('Неверный пункт меню')
