# sms-reg.com API [Python]
  Python API для [сервиса активации симкарт](https://sms-reg.com).
  
  Оригинальный [REST](http://sms-reg.com/docs/API.html)
***
### Установка:

    pip install sms-reg
***
### Документация:
* Авторизация клиента
```python
sms = Sms(client_key)  # str: client_key
```
Метод             | Описание
------------------|----------------------
balance()         | Возвращает баланс аккаунта
set_rate(rate)    | Ставит дополнительную ставку в размере rate (**int**)
get_list(extended=None)    | Возвращает список сервисов, с extended(**int**) только доступные
get_num(service, country=None)| Запрашивает офер на номер, service(**str**) - сервис, с country(**str**) номер страны, возвращает tzid
get_num_repeat(tzid)      | Запрашивает офер на использование номера повторно, tzid ключ(**str**)
set_ready(tzid)   | Активирует офер
wait_number(tzid)       | Ожидает пока не выдан номер
wait_answer(tzid)      | Ожмдает пока не придет смс, возвращает либо его содержимое, либо False(**bool**)
get_operations(opstate=None, count=None, output=None):        | Возвращает операции, [подробнее](http://sms-reg.com/docs/APImethods.html?getOperations)
set_ok(tzid)        | Подтверждает, что операция прошла успешно, закрывает офер
set_used(tzid)        | Сообщает, что номер был использован ранее, закрывает офер

### Пример:
Покупка номера телеграм:
```python
sms = Sms('2d08p37k6bkwjpj1pqgwdsbg9nuy2g1y')
print(sms.balance())
tzid = sms.get_num('telegram', country='all')
if sms.wait_number(tzid):
	***
	На telegram.org используется номер
	***
	print(sms.wait_answer(tzid))  # Выводит сообщение с предположительно кодом
	sms.set_ok(tzid)
else:
	print('Что-то пошло не так')
```
** Требуются тестировщики, по всем вопросам linkedin.com/in/vbxx3
