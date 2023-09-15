# this is the core of the CCTV parser, detects human faces and human bodies with 
# optional arguments
import cv2

def detect_human_in_video(video_path):
    # Load the haarcascades classifier for face detection
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
    #                                      'haarcascade_frontalface_default.xml')
    body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
                                         'haarcascade_fullbody.xml')

    # Initialize the video capture from the given video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    while True:
        # Capture a frame from the video
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, 
        #                                       minNeighbors=5, minSize=(30, 30))
        body = body_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                             minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in body:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame with detected faces
        cv2.imshow('Video', frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = '../assets/video/video.mp3'
    detect_human_in_video(video_path)
