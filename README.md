### Тестовое задание для cloud.ru CAMP
\
**Задания:**
1. Напишите программу на Python, которая выполняет следующие задачи:\
• Читает список чисел от пользователя и выводит только четные числа.\
• Находит и выводит максимальное и минимальное число из списка.\
• Сортирует список в порядке возрастания без использования встроенной функции sorted().\
Пример ввода: 1, 3, 4, 7, 8, 10\
Пример вывода:\
Четные числа: [4, 8, 10]\
Максимальное число: 10\
Минимальное число: 1\
Отсортированный список: [1, 3, 4, 7, 8, 10]\

2. Работа с Selenium или Playwright
• Выберите любую из указанных библиотек (Selenium или Playwright).\
• Напишите скрипт, который:\
• Открывает веб-страницу (например, https://example.com).\
• Проверяет, что заголовок страницы содержит слово "Example".\
• Находит элемент по CSS-селектору, содержащему текст "More information" и кликает по нему.\
• Проверяет, что по клику произошло перенаправление на страницу с URL "https://www.iana.org/help/example-domains".
\
---
**Решение задания №1 находится в файле main.py.** Для запуска необходимо:\
1. Запустить вашу IDE (например PyCharm).
2. Создать новый проект и виртуальное окружение.
3. Клонировать проект из публичного рипозитория git командой
> git clone https://github.com/DeadGEEK990/cloud-test-tusk

После этого в папке с вашим проектом появится папка cloud-test-tusk,
в которой хранятся все файлы.
3. Установить необходимые библиотеки
> pip install -r cloud-test-tusk/requirements.txt
4. Запустить файл main.py в терминале
> python cloud-test-tusk/main.py

После чего ввести в терминале набор чисел через пробел и нажать Enter. Например:
> 1 2 5 9 21 42 90 24

В результате получим:
>Чётные числа: [2, 42, 90, 24]\
Максимальное значение: 90\
Минимальное значение: 1\
Отсортированный массив: [1, 2, 5, 9, 21, 24, 42, 90]


**Решение задание №2 находится в файле selenium_test.py**
Для реализации была использована библиотека selenium и pytest.
Чтобы проверить работоспособность теста необходимо ввести в терминал
команду:
> pytest

По завершению тестов в терминале будет выведена надпись:
> 1 passed in 33.28s
