# Трассировка автономных систем

Эта программа позволяет осуществлять трассировку до указанного узла (доменное имя или IP адрес) и определять к какой автономной системе относятся IP адреса маршрутизаторов, через которые проходит пакет. Для определения номеров автономных систем используются базы данных региональных интернет регистраторов.

## Автор
Асбапов Рустам Русланович, Группа КН-202

## Инструкция по запуску
Для запуска приложения необходимо выполнить команду:

   ```
  py tracer.py <ip\domain_name>
   ```

   Здесь `<ip\domain_name>` может быть доменным именем или IP адресом, до которого требуется осуществить трассировку.
   

## Используемые технологии

- **Python**: Язык программирования, на котором написана программа.
- **sys**: Модуль Python для работы с системными параметрами и функциями.
- **re**: Модуль Python для работы с регулярными выражениями.
- **subprocess**: Модуль Python для выполнения внешних команд и процессов.
- **json**: Модуль Python для работы с JSON-данными.
- **urllib**: Модуль Python для работы с URL-запросами.
  
Программа использует команду `tracert` для выполнения трассировки маршрута, модуль `re` для поиска IP-адресов в выводе `tracert`, модуль `subprocess` для запуска внешних команд, модуль `json` и `urllib` для получения информации об IP-адресах из внешнего API сервиса.


## Результат

После выполнения программы выводится таблица с ip адресами пройденных маршрутизаторов, страной/городом, номером автономной системы и провайдером.

Пример запуска:
```
py tracer.py 104.98.238.167
```

Пример вывода:

![image](https://github.com/rustutam/Tracer_AS/assets/113977718/544b13af-6cd5-48d1-8619-d191e3044b5b)
