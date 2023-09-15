import cv2

def detect_human_in_image(image_path):
    # Load the Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Unable to load the image.")
        return

    # Convert the image to grayscale for face detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Save or display the image with detected faces
    cv2.imwrite('output_image.jpg', image)  # Save the result as 'output_image.jpg'
    # Alternatively, you can display the image using cv2.imshow() if you want to show it.

if __name__ == "__main__":
    # image_path = '../assets/images/*'  # Replace with the path to your input image
    image_path = '../assets/images/image.jpg'  # Replace with the path to your input image
    detect_human_in_image(image_path)
