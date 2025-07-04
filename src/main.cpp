#include <iostream>

int divide(int a, int b) {
    if (b == 0) {
        std::cerr << "Ошибка: деление на ноль!" << std::endl;
        exit(EXIT_FAILURE);
    }
    return a / b;
}

int main() {
    int x = 10;
    int y = 0;
    int result = divide(x, y);
    std::cout << "Result: " << result << std::endl;
    return 0;
}
