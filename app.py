import cv2

image = cv2.imread('/photos/img.png')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

if len(faces) == 0:
    print("Лица не найдены.")
else:
    print(f"Найдено {len(faces)} лицо(лиц):")
    for (x, y, w, h) in faces:
        print(f"Лицо на позиции: x={x}, y={y}, ширина={w}, высота={h}")