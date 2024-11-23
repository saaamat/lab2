import cv2

# Загрузка изображения
image = cv2.imread('/photos/img.png')

# Загрузка классификатора для распознавания лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Преобразуем изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Находим лица
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Печатаем результат в stdout
if len(faces) == 0:
    print("Лица не найдены.")
else:
    print(f"Найдено {len(faces)} лицо(лиц):")
    for (x, y, w, h) in faces:
        print(f"Лицо на позиции: x={x}, y={y}, ширина={w}, высота={h}")