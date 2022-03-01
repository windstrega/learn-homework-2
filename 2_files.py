"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass

if __name__ == "__main__":
    main()

def main():
    
    with open('referat.txt', 'r', encoding='utf-8') as tekst:
        tasktext = tekst.read() 
        print(f'Оригинальный текст: {tasktext}')
    
        str_lenght = len(tasktext)
        print(f'Длина строки {str_lenght}')
        words = len(tasktext.split())
        print(f'Количество слов {words}')

        wow = tasktext.replace('.', '!')
        print(wow)

    with open('referat2.txt', 'a', encoding='utf-8') as newtext:
        newtext.write(wow)

        pass

if __name__ == "__main__":
    main()