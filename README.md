# FABRIKA TEST TASK
# Ссылка на бота https://t.me/fabrika_test_task_bot
## нужно нажать на start, затем на кнопку /token, бот будет ждать от вас токена сгенерированного по адресу http://85.198.91.34:8000/api/generate-token/

#инструкция
## Регистрация по адресу http://85.198.91.34:8000/api/users/create/

curl --request POST \
  --url http://85.198.91.34:8000/api/users/create/ \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "username",
	"password": "password"
}'

## Авторизация по адресу http://85.198.91.34:8000/api/token/
Авторизация работает с помощью jwt токенов
curl --request POST \
  --url http://85.198.91.34:8000/api/token/ \
  --header 'Content-Type: application/json' \
  --data '{"username": "username",
"password": "password"}'

## Первичная генерация токена по адресу http://85.198.91.34:8000/api/generate-token/ (в хэдер добавить jwt acess токен который генерировали ранее)
curl --request PATCH \
  --url http://85.198.91.34:8000/api/generate-token/ \
  --header 'Authorization: Bearer your acess token'

ответ придет в виде токена

## Получение токена по адресу http://85.198.91.34:8000/api/telegram-token/ (в хэдер добавить jwt acess токен который генерировали ранее)

curl --request GET \
  --url http://85.198.91.34:8000/api/telegram-token/ \
  --header 'Authorization: Bearer your acess token'
  
## Отправка сообщения в бота по адресу http://85.198.91.34:8000/api/send-message/ (в хэдер добавить jwt acess токен который генерировали ранее)

curl --request POST \
  --url http://85.198.91.34:8000/api/send-message/ \
  --header 'Authorization: Bearer your acess token' \
  --header 'Content-Type: application/json' \
  --data '{"text": "TEST"
}'

##Просмотр ваших сообщений http://85.198.91.34:8000/api/my-messages/ (в хэдер добавить jwt acess токен который генерировали ранее)

curl --request GET \
  --url http://85.198.91.34:8000/api/my-messages/ \
  --header 'Authorization: Bearer your acess token'


  

