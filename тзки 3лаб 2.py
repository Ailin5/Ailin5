def create_matrix(text, rows, cols):
    """Создает матрицу для текста."""
    matrix = [[""] * cols for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                matrix[r][c] = text[index]
                index += 1
    return matrix

def encrypt(text, row_order, col_order):
    """Шифрование текста методом двойной перестановки."""
    rows, cols = len(row_order), len(col_order)
    if len(text) > rows * cols:
        raise ValueError("Текст слишком длинный для заданных размеров матрицы!")

    text = text.ljust(rows * cols, "_")  # Дополнение символами "_", чтобы матрица была полной
    matrix = create_matrix(text, rows, cols)

    # Перестановка строк
    matrix = [matrix[i] for i in row_order]
    # Перестановка столбцов
    matrix = [[row[i] for i in col_order] for row in matrix]

    # Преобразование обратно в строку
    return "".join("".join(row) for row in matrix)

def decrypt(text, row_order, col_order):
    """Дешифрование текста методом двойной перестановки."""
    rows, cols = len(row_order), len(col_order)
    if len(text) > rows * cols:
        raise ValueError("Зашифрованный текст слишком длинный для заданных размеров матрицы!")

    matrix = create_matrix(text, rows, cols)

    # Обратная перестановка столбцов
    reverse_col_order = [col_order.index(i) for i in range(len(col_order))]
    matrix = [[row[i] for i in reverse_col_order] for row in matrix]
    # Обратная перестановка строк
    reverse_row_order = [row_order.index(i) for i in range(len(row_order))]
    matrix = [matrix[i] for i in reverse_row_order]

    # Преобразование обратно в строку
    return "".join("".join(row) for row in matrix).rstrip("_")

if __name__ == "__main__":
    # Ввод текста
    text = input("Введите текст для шифрования: ")

    # Ввод порядка строк
    row_order = list(map(int, input("Введите порядок строк (через пробел, начиная с 1): ").split()))
    row_order = [x - 1 for x in row_order]  # Преобразование в нумерацию Python (с 0)

    # Ввод порядка столбцов
    col_order = list(map(int, input("Введите порядок столбцов (через пробел, начиная с 1): ").split()))
    col_order = [x - 1 for x in col_order]  # Преобразование в нумерацию Python (с 0)

    # Проверка на соответствие размеров
    rows, cols = len(row_order), len(col_order)
    if rows * cols < len(text):
        print("Ошибка: Размеры матрицы не подходят для заданного текста!")
    else:
        # Шифрование
        encrypted = encrypt(text, row_order, col_order)
        print(f"Зашифрованный текст: {encrypted}")

        # Дешифрование
        decrypted = decrypt(encrypted, row_order, col_order)
        print(f"Расшифрованный текст: {decrypted}")
