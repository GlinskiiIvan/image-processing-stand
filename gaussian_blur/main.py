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
    denoised_img = cv2.GaussianBlur(img, (5, 5), 0) # Используем ядро 5x5 и стандартное отклонение по умолчанию (0)
    cv2.imwrite(f'processed_image.png', denoised_img)

kernel_size_range = range(3, 22, 2)
sigmaX_range = range(0, 11, 1)
def changing_everything():
    for kernel_size in kernel_size_range:
        for sigmaX in sigmaX_range:
            denoised_img = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX)
            cv2.imwrite(save_path + f'processed_image-kernel_size_{kernel_size}-sigmaX_{sigmaX}.png', denoised_img)


# single()
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