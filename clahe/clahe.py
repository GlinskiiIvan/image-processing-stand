import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

# Начало замера времени
start_time = time.time()

# Уведомление начала работы скрипта
print('Скрипт запущен')

# Указание пути для сохранения
save_path = './processed_images/'
# Создание директории, если она не существует
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Шаг 1: Загрузка изображения в градациях серого
img = cv2.imread('original.png', 0)

# Применение разных значений clipLimit
range_clipLimit = range(2, 42, 2)
for i in range_clipLimit:
    # Шаг 2: Применение CLAHE для выравнивания гистограммы
    clahe = cv2.createCLAHE(clipLimit=i, tileGridSize=(8, 8))
    equalized_img = clahe.apply(img)

    # Шаг 3: Сохранение изображения
    cv2.imwrite(save_path + f'/01_equalized_image-clipLimit_{i}.png', equalized_img)

# Применение разных значений tileGridSize
range_tileGridSize = range(2, 66, 2)
for i in range_tileGridSize:
    # Шаг 2: Применение CLAHE для выравнивания гистограммы
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(i, i))
    equalized_img = clahe.apply(img)

    # Шаг 3: Сохранение изображения
    cv2.imwrite(save_path + f'/02_equalized_image-tileGridSize_{i}x{i}.png', equalized_img)


# Применение разных значений clipLimit и tileGridSize
for i in range_clipLimit:
    for k in range_tileGridSize:
        # Шаг 2: Применение CLAHE для выравнивания гистограммы
        clahe = cv2.createCLAHE(clipLimit=i, tileGridSize=(k, k))
        equalized_img = clahe.apply(img)

        # Шаг 3: Сохранение изображения
        cv2.imwrite(save_path + f'/03_equalized_image-clipLimit_{i}-tileGridSize_{k}x{k}.png', equalized_img)

# Конец замера времени
end_time = time.time()

# Расчет времени выполнения
execution_time = end_time - start_time

# Преобразование времени в hh:mm:ss:ms
hours = int(execution_time // 3600)
minutes = int((execution_time % 3600) // 60)
seconds = int(execution_time % 60)
milliseconds = int((execution_time * 1000) % 1000)

# Вывод результата
print(f"Время выполнения скрипта: {hours:02}:{minutes:02}:{seconds:02}:{milliseconds:03}")