import cv2

cap = cv2.VideoCapture(0)

# Capture frame
ret, frame = cap.read()
frame = cv2.rotate(frame, cv2.ROTATE_180)
if ret:
	cv2.imwrite('image.jpg', frame)

cap.release()
