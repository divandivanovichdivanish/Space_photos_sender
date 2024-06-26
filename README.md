# Публикация фото в телеграм канал

Данный проект может быть использован для публикации и скачивания фото.

### Как установить

Необходимо задать ключ телеграм бота и API ключ nasa. Создаете файл `.env`, в нем переменную `NASA_API`, а в значение пишете свой API ключ nasa. В этом же файле создаем переменную `TG_TOKEN` и в ней пишете свой токен Telegram бота.
Так-же требуется задать имя канала. Для этого в файле `.env` создаем переменную `TG_CHAT_ID` и в значение пишем имя телеграм канала в формате: `@abcdefg`

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как использовать

Для работы основного скрипта нужны изображения в папке `images`.
Для их скачивания можно запустить дополнительные скрипты (`download_a_lot_of_APODs`, `download_spacex_images`, `download_some_really_EPIC_photos`).
После их выполнения можно запускать основной скрипт.
Второй скрипт для публикации фото в телеграм канал - `publish_photo_to_telegram`. Он публикует указанное фото из папки `images` с помощью аргумента `--photo_name`(`-phn`)(Если не указан публикует случайную фотографию).

### Примеры запуска скрипта

Для дополнительных скриптов:
```
>>>python download_spacex_images.py

>>>
```

```
>>>python download_a_lot_of_APODs.py

>>>
```

```
>>>python download_some_really_EPIC_phootos.py

>>>
```

Скрипт, публикующий одно фото:
```
>>>python publish_photo_to_telegram.py

>>>
```

Основной скрипт запускает бесконечный цикл:
```
>>>python bot.py

```
Его корректное выполнение - это отсутствие ошибок и публикация фото в телеграм канал.

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).