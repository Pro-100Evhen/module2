import os


VARIABLE_NAME = "STUDENT_SURNAME"


def main():
    surname = os.getenv(VARIABLE_NAME)

    if surname:
        print(f"Значення змінної {VARIABLE_NAME}: {surname}")
    else:
        print(f"Змінна {VARIABLE_NAME} відсутня")


if __name__ == "__main__":
    main()