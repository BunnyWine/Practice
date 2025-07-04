import random
import argparse

def generate_numbers(count=10, min_val=1, max_val=100):
    """Генерирует список случайных чисел"""
    return [random.randint(min_val, max_val) for _ in range(count)]

def save_to_file(numbers, filename="data/output.txt"):
    """Сохраняет числа в файл"""
    with open(filename, "w") as f:
        for number in numbers:
            f.write(f"{number}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Генерация случайных чисел")
    parser.add_argument("--count", type=int, default=10, help="Количество чисел")
    parser.add_argument("--min", type=int, default=1, help="Минимальное значение")
    parser.add_argument("--max", type=int, default=100, help="Максимальное значение")
    parser.add_argument("--output", type=str, default="data/output.txt", help="Файл для сохранения")

    args = parser.parse_args()

    numbers = generate_numbers(args.count, args.min, args.max)
    save_to_file(numbers, args.output)

    print(f"Сгенерировано {args.count} чисел и сохранено в {args.output}")
