# gigachat

Данный проект создан на базе интеграции с Gigachat и предназначен для проверки написанных дата-инженерами строк на их соответствие указанным классам.

Для проверки строк необходимо иметь 2 эксель файла, где:
- первый - файл с заголовками столбцов в ячейке А1 - 'ID', в ячейке В1 - 'Тема' или 'Пример'
- второй файл - сама работа с написанными строками, где А1 - это указанный ID, а B1 - написанная строка.
После завершения работы программы ячейка с несоответствующей по содержанию строкой будет закрашена красным цветом.

## Запуск

## TODO: 

- дописать тесты - done
- 
- компоуз запуск (docker compose build- строим образ, docker compose up -d gigachat - создаем и запускаем конт
, docker compose run gigachat -c classes2.xlsx -s example2.xlxs(их нет в srv. мы их туда не кладем. что делать??))
, аналогично - docker run gigachat python main.py classes2.xlsx example2.xlxs - нет файлов, что логично
- вопросы : если мы хотим, чтобы юзер вводил пути к файлам в баше, то что писать в команде компоуз файла.

- https://github.com/getumbrel/llama-gpt - запустить локально модель
  - запустить образ просто (Nous Hermes Llama 2 7B Chat (GGML q4_0))
  - добавить образ в свой docker-compose  
  - обратиться в апи к модели ламы 
  