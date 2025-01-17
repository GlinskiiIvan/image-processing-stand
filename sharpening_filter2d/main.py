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
# image = cv2.imread('original.png')
image = cv2.imread('taj_bilateral.jpg')

def singe_processed():
    # Create the sharpening kernel 
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
    # Sharpen the image 
    sharpened_image = cv2.filter2D(image, -1, kernel) 
    #Save the image 
    cv2.imwrite('sharpened_image.jpg', sharpened_image) 

core_range = range(1, 21, 1)
neighbors_range = np.arange(-0.5, -5, -0.5)
# neighbors_range = range(-0.5, -5, 0.5)

def changing_core():
    for core in core_range:
        # Create the sharpening kernel 
        kernel = np.array([[0, -1, 0], [-1, core, -1], [0, -1, 0]]) 
        # Sharpen the image 
        sharpened_image = cv2.filter2D(image, -1, kernel) 
        #Save the image 
        cv2.imwrite('sharpened_image.jpg', sharpened_image) 

def changing_neighbors():
    for neighbor in neighbors_range:
        # Create the sharpening kernel 
        kernel = np.array([[0, neighbor, 0], [neighbor, 5, neighbor], [0, neighbor, 0]]) 
        # Sharpen the image 
        sharpened_image = cv2.filter2D(image, -1, kernel) 
        #Save the image 
        cv2.imwrite('sharpened_image.jpg', sharpened_image) 

def changing_everything():
    for core in core_range:
        for neighbor in neighbors_range:
            # Create the sharpening kernel 
            kernel = np.array([[0, neighbor, 0], [neighbor, core, neighbor], [0, neighbor, 0]]) 
            # Sharpen the image 
            sharpened_image = cv2.filter2D(image, -1, kernel) 
            #Save the image 
            cv2.imwrite(save_path + f'processed_image-core_neighbor_{core}_{neighbor}.jpg', sharpened_image) 

# changing_everything()
singe_processed()

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