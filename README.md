# soa-graphql

## Доступные клиенту комманды
- addComment -- добавляет comment в комнату room_id
- scoreboard -- выводит информацию об игре в комнате room_id
- activeGames -- выводит ID комнат, где игра ещё идёт
- finishedGames -- выводит ID комнат, где игра уже завершилась
- finish -- завершает работу клиента

## Запуск клиента
`python clint.py`

## Запуск сервера
В докере необходимо пробросить порт 8000.

К примеру: `docker run -p 8000:8000  allisyonok/soa-graphql:latest`