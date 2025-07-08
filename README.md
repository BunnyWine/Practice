# Practice
Это репозиторий для практики Мухиной Полины Ивановны

### Использование скриптов

В папке `scripts/` есть полезный Python-скрипт `generate_data.py`, который генерирует случайные числа и сохраняет их в файл.

### Как использовать:
python3 scripts/generate_data.py [--count N] [--min X] [--max Y] [--output FILE]


---

### 1. Установка зависимостей (один раз)

Для работы скрипта нужна утилита `mkpasswd` из пакета `whois`:

```bash
sudo apt update
sudo apt install -y whois
```

### 2. Как запустить скрипт

### a) Сохраните скрипт как `passaudit.py`

Скопируйте содержимое скрипта в файл:

```bash
nano passaudit.py
```

Затем сохраните (`Ctrl+O`, `Enter`, `Ctrl+X`).

### b) Добавьте права на исполнение (не обязательно):

```bash
chmod +x passaudit.py
```

### c) Запустите скрипт от root:

```bash
sudo python3 passaudit.py
```

---

### 3. Файл `passwords.txt`

Создайте файл со списком популярных паролей:

```bash
nano passwords.txt
```

Пример содержимого:

```
password
admin
test
root
user
qwerty
123456
```

Сохраните файл и продолжите.

---

### 4. Пример вывода при наличии слабых паролей

```
[*] Загрузка паролей из 'passwords.txt'...
[*] Проверяем /etc/shadow на наличие слабых паролей...
[+] Найден слабый пароль: alice : password
[+] Найден слабый пароль: bob : 123456

[+] Результаты сохранены в файл: weak_passwords.txt
```

---

### 5. Содержимое файла `weak_passwords.txt` (пример)

```
alice:password
bob:123456
```

---







