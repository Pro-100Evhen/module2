def print_array(array):
    print(" ".join(map(str, array)))


def is_sorted_ascending(array):
    for index in range(len(array) - 1):
        if array[index] > array[index + 1]:
            return False

    return True


def main():
    numbers = [2, 9, 12, 13, 15, 12, 2, 0, 6, 6, 3, 2]

    print(f"Масив {len(numbers)} елементів:")
    print_array(numbers)

    element_number = int(input("Введіть номер елемента масиву: "))

    if element_number < 0 or element_number >= len(numbers):
        print("Помилка: номер елемента має бути від 0 до 11")
        return

    selected_numbers = numbers[:element_number + 1]

    print(f"Масив {element_number} елементів:")
    print_array(selected_numbers)

    if is_sorted_ascending(selected_numbers):
        print("Впорядковано за зростанням")
    else:
        print("НЕ впорядковано за зростанням")


if __name__ == "__main__":
    main()