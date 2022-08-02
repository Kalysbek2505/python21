# Slash commands
* `\c` - показывает в какой бд мы находимся и через какого юзера
* `\c name_of_database` - переключаемся к этой бд
* `\l` - показывает все базы данных
* `\dt` - показывает все таблицы в бд, к которой мы подключились
* `\du` - показывает всех юзеров
* `\q` - выход

# Создание бд и таблиц
```sql
CREATE DATABASE name_of_db;
-- создает базу данных
```
```sql
CREATE TABLE name_of_table (
    name_of_column1 data_type constraint,
    name_of_column2 data_type constraint,
    ...
);
-- создает таблицу с полями
```

# Заполнение таблиц
```sql
INSERT INTO name_of_table (name_of_column1, name_of_column2) VALUES (val1, val2);
-- добавляет запись в таблицу
```

# Вывод данных из таблиц
```sql
SELECT * FROM name_of_table;
-- достает все поля и все записи из таблицы
```
```sql
SELECT name_of_column1, name_of_column2 FROM name_of_table
-- достает только указанные столбцы из таблицы (все записи)
```

```sql
SELECT * FROM name_of_table WHERE name_of_column2 = 'hello';
--достет все записи из таблицы у которых name_of_column2 со значением 'hello'
```

# Связи 
## pk fk
> primary key (pk) - первичный ключ
> это ограничение, которое мы указываем на те поля которые должны быть уникальными для того, чтобы их использовать в связях


> foreign key (fk) - внешний ключ 
> это ограничение которое мы указываем на те поляёё

```sql
CREATE TABLE author (
    id serial primary key,
    first_name varchar(50),
    last_name varchar(50)
);

CREATE TABLE book (
    id serial,
    title varchar(100),
    published year,
    author_id int,
    CONSTRAINT fk_author_book
    FOREIGN KEY (author_id)
    REFERENCES author (id)
);
```