#Import the necessary libraries 
import cv2 
import matplotlib.pyplot as plt 
import numpy as np 
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

# Шаг 1: Загрузка изображения
image = cv2.imread('original.png')

def singeProcessed():
    # Шаг 2: установка яркости и контрастности
    brightness = 10
    contrast = 2.3

    # Шаг 3: применение изменения яркости и контрастности
    image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

    # Шаг 4: сохранение изображения
    cv2.imwrite(save_path + f'/processed_images.png', image2)

brightness_range = range(0, 101, 10)
contrast_range = range(0, 11, 1)

def changing_brightness():
    for brightness in brightness_range:
        contrast = 2.3

        # Шаг 3: применение изменения яркости и контрастности
        image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

        # Шаг 4: сохранение изображения
        cv2.imwrite(save_path + f'/01_processed_images-brightness_{brightness}.png', image2)

def changing_contrast():
    for contrast in contrast_range:
        brightness = 10

        # Шаг 3: применение изменения яркости и контрастности
        image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

        # Шаг 4: сохранение изображения
        cv2.imwrite(save_path + f'/02_processed_images-contrast_{contrast}.png', image2)

def changing_everything():
    for brightness in brightness_range:
        for contrast in contrast_range:
            # Шаг 3: применение изменения яркости и контрастности
            image2 = cv2.addWeighted(image, contrast, np.zeros(image.shape, image.dtype), 0, brightness) 

            # Шаг 4: сохранение изображения
            cv2.imwrite(save_path + f'/03_processed_images-brightness_contrast_{brightness}_{contrast}.png', image2)

# singeProcessed()
changing_brightness()
changing_contrast()
changing_everything()

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