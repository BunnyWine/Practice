import os
import sys
import subprocess

def is_root():
    return os.geteuid() == 0

def extract_hash(line):
    parts = line.strip().split(':')
    if len(parts) >= 2:
        username = parts[0]
        hashed = parts[1]
        if hashed not in ['*', '!', 'x', ''] and hashed.startswith('$'):
            return username, hashed
    return None, None

def verify_password(password, stored_hash):
    """Проверяет, совпадает ли пароль с хэшем через mkpasswd"""
    try:
        # Определяем тип хэша
        if stored_hash.startswith('$6$'):  # SHA-512
            cmd = ['mkpasswd', '--method=sha-512', password, '--salt', stored_hash.split('$')[2]]
        elif stored_hash.startswith('$5$'):  # SHA-256
            cmd = ['mkpasswd', '--method=sha-256', password, '--salt', stored_hash.split('$')[2]]
        elif stored_hash.startswith('$1$'):  # MD5
            cmd = ['mkpasswd', '--method=md5', password, '--salt', stored_hash.split('$')[2]]
        else:
            # Для других типов хэшей — попробуем просто передать хэш как соль
            cmd = ['mkpasswd', password, '--salt', stored_hash]

        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
        generated_hash = result.stdout.strip()
        return generated_hash == stored_hash
    except Exception as e:
        print(f"[!] Ошибка при проверке: {e}")
        return False

def load_passwords(file_path):
    """Загружает список паролей из файла"""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    if not is_root():
        print("[!] Для чтения /etc/shadow нужны права root")
        sys.exit(1)

    passwords_file = "passwords.txt"
    if not os.path.isfile(passwords_file):
        print(f"[!] Файл '{passwords_file}' не найден")
        sys.exit(1)

    print(f"[*] Загрузка паролей из '{passwords_file}'...")
    passwords = load_passwords(passwords_file)

    weak_users = []

    print("[*] Проверяем /etc/shadow на наличие слабых паролей...")
    with open('/etc/shadow', 'r') as f:
        for line in f:
            username, stored_hash = extract_hash(line)
            if not username:
                continue

            # Проверка: имя пользователя как пароль
            if verify_password(username, stored_hash):
                print(f"[+] Найден слабый пароль: {username} : {username}")
                weak_users.append((username, "username"))
                continue

            # Проверка по словарю
            for pwd in passwords:
                if verify_password(pwd, stored_hash):
                    print(f"[+] Найден слабый пароль: {username} : {pwd}")
                    weak_users.append((username, pwd))
                    break

    # Сохранение результата
    output_file = "weak_passwords.txt"
    if weak_users:
        with open(output_file, 'w') as f:
            for user, pwd in weak_users:
                f.write(f"{user}:{pwd}\n")
        print(f"\n[+] Результаты сохранены в файл: {output_file}")
    else:
        print("\n[-] Слабых паролей не найдено.")

if __name__ == '__main__':
    main()