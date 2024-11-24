def add_parity_bit(data, parity_type="even"):
    """
    Добавляет бит четности или нечетности.
    :param data: Битовая строка (например, '1101001').
    :param parity_type: Тип бита ('even' для чётного, 'odd' для нечётного).
    :return: Битовая строка с добавленным битом четности.
    """
    num_ones = data.count('1')  # Считаем количество единиц
    if parity_type == "even":  # Чётный бит
        parity_bit = '0' if num_ones % 2 == 0 else '1'
    elif parity_type == "odd":  # Нечётный бит
        parity_bit = '1' if num_ones % 2 == 0 else '0'
    else:
        raise ValueError("Неверный тип бита: выберите 'even' или 'odd'.")
    return data + parity_bit


def check_parity(data_with_parity, parity_type="even"):
    """
    Проверяет бит четности или нечетности.
    :param data_with_parity: Битовая строка с битом четности (например, '11010011').
    :param parity_type: Тип бита ('even' для чётного, 'odd' для нечётного).
    :return: True, если ошибок нет, иначе False.
    """
    num_ones = data_with_parity.count('1')
    if parity_type == "even":  # Чётный бит
        return num_ones % 2 == 0
    elif parity_type == "odd":  # Нечётный бит
        return num_ones % 2 == 1
    else:
        raise ValueError("Неверный тип бита: выберите 'even' или 'odd'.")


if __name__ == "__main__":
    # Ввод данных
    data = input("Введите битовую строку данных (например, 1101001): ")
    parity_type = input("Выберите тип бита четности (even/odd): ").lower()

    # Добавление бита четности
    data_with_parity = add_parity_bit(data, parity_type)
    print(f"Сообщение с добавленным битом четности: {data_with_parity}")

    # Проверка битов
    received_data = input("Введите полученное сообщение (с битом четности): ")
    if check_parity(received_data, parity_type):
        print("Ошибок нет. Сообщение корректно.")
    else:
        print("Обнаружена ошибка в сообщении!")
