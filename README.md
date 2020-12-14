# Book shop forms

## Разворачивание проекта:

1. Клонировать репозиторий командой
    
    ```
    git clone https://github.com/relax-man/SF-ModuleD5 *folder_name*
    ```

2. Создать виртуальное окружение и установить пакеты из **requirements.txt**

    ```
    python -m venv env
    
    ./env/scripts/activate

    pip install -r requirements.txt
    ```

3. Провести миграции и загрузить данные в базу из фикстуры

    ```
    python src/manage.py migrate

    python src/manage.py loaddata src/data.json
    ```

4. Запустить сервер по адресу localhost:8000

    ```
    python src/manage.py runserver
    ```

## Результат на выходе:

![Screen 1](https://user-images.githubusercontent.com/63586837/97419306-7e24b880-193c-11eb-9a48-8a9d93126376.png)
#
![Screen 2](https://user-images.githubusercontent.com/63586837/97418857-eb841980-193b-11eb-9e7f-5695efdd6187.png)
#
![Screen 3](https://user-images.githubusercontent.com/63586837/97419024-21290280-193c-11eb-95dc-37c2cc90749a.png)

## Дополнительно

Минимальная версия Python - 3.7.9

