# Сайт посещения хранилища банка с записями в базу данных.

## Данный сайт обрабатывает базу данных с картами доступа в хранилище банка, записывая посещения и вычисляя время нахождения в хранилище

### Как установить:

для подключения к базе данных нужно ввести данные самой базы в файле .env формате
'ENGINE': '',
'HOST': '',
'PORT': '',
'NAME': '',
'USER': '',
'PASSWORD': ''
Так же потребуется версия Django 3.2
Python3 должен быть уже установлен. 

### Затем нужно создать папку виртуального окружения:

 python -m venv venv
 
### После запустить виртуальное окружение:

venv\Scripts\activate.bat

### Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

pip install -r requirements.txt

### Далее запустить проект командой:

python manage.py

## Цель проекта:
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
