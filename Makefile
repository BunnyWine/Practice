# Компилятор
CXX = g++
# Флаги компиляции: стандарт C++17, предупреждения, подключение include/
CXXFLAGS = -Wall -Wextra -pedantic -std=c++17 -Iinclude -g

# Пути к исходникам и сборке
SRC_DIR = src
BUILD_DIR = build

# Список исходных файлов
SOURCES = $(SRC_DIR)/main.cpp $(SRC_DIR)/hello.cpp
OBJECTS = $(patsubst $(SRC_DIR)/%.cpp, $(BUILD_DIR)/%.o, $(SOURCES))

# Имя выходного файла
TARGET = hello

# Цель по умолчанию
all: $(TARGET)

# Основная цель — собираем исполняемый файл
$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $(OBJECTS) -o $@

# Правило сборки объектных файлов
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Чистка
clean:
	rm -rf $(BUILD_DIR) $(TARGET)

# Фиктивные цели
.PHONY: all clean
