import cv2

image = cv2.imread("day8_photo.jpg")
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped = image[10:600, 200:500]
cv2.imshow("Image", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()

x1, y1 = 100, 100
x2, y2 = 200, 200
image_with_rectangle = cv2.rectangle(cropped, (x1, y1),(x2, y2), (0, 255, 0), 3)
cv2.imshow("Image", image_with_rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_with_text = cv2.putText(image_with_rectangle, "Valkov Ivan Vladimirovich", (50, 75), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
cv2.imshow("Image", image_with_text)
cv2.waitKey(0)
cv2.destroyAllWindows()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor= 1.1,
    minNeighbors= 5,
    minSize=(10, 10)
)
faces_detected = "Лиц обнаружено: " + format(len(faces))
print(faces_detected)
# Рисуем квадраты вокруг лиц
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
viewImage(image,faces_detected)
