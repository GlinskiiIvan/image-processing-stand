import cv2 
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

def single():
    bilateral = cv2.bilateralFilter(image, 15, 75, 75)   
    cv2.imwrite(f'processed_image.png', bilateral)


d_range = range(0, 31, 5)
sigmaColor_range = range(0, 151, 10)
sigmaSpace_range = range(0, 151, 10)
def changing_everything():
    for d in d_range:
        for sigmaColor in sigmaColor_range:
            for sigmaSpace in sigmaSpace_range:
                bilateral = cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)   
                cv2.imwrite(save_path + f'processed_images-d_{d}-sigmaColor_{sigmaColor}-sigmaSpace_{sigmaSpace}.png', bilateral)

# changing_everything()
single()

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
