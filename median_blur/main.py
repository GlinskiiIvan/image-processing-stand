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
# image = cv2.imread('processed_image-core_neighbor_5_-1.0.png')

def singe_processed():
    # Remove noise using a median filter 
    filtered_image = cv2.medianBlur(image, 1) 
    #Save the image 
    cv2.imwrite(save_path + f'Median Blur.jpg', filtered_image) 

ksize_range = range(1, 11, 2)
def changing_ksize():
    for ksize in ksize_range:
        # Remove noise using a median filter 
        filtered_image = cv2.medianBlur(image, ksize) 
        #Save the image 
        cv2.imwrite(save_path + f'processed_image-ksize_{ksize}.png', filtered_image) 

# singe_processed()
changing_ksize()

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
