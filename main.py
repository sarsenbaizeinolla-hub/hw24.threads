import time
from concurrent.futures import ThreadPoolExecutor


# функция создания файла
def create_file(number):
    time.sleep(1)

    filename = f"file_{number}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Файл номер {number} создан!\n")

    return filename


# Однопоточный запуск
def single_thread():
    print("Однопоточный запуск...")

    start = time.time()

    for i in range(100):
        create_file(i)

    end = time.time()

    print("Однопоточно завершено!")
    print("Время:", round(end - start, 2), "секунд\n")


# Многопоточный запуск
def multi_thread():
    print("Многопоточный запуск...")

    start = time.time()

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(create_file, range(100))

    end = time.time()

    print("Многопоточно завершено!")
    print("Время:", round(end - start, 2), "секунд\n")


if __name__ == "__main__":
    single_thread()
    multi_thread()
