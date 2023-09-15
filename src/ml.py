import cv2
import numpy as np
# import tensorflow as tf
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input
from tensorflow.keras.applications.efficientnet import decode_predictions
import tkinter as tk
from tkinter import Label

def get_image_info():
    # Load pre-trained EfficientNet model
    model = EfficientNetB0(weights='imagenet')

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Create a Tkinter window
    root = tk.Tk()
    root.title("Image Info")

    label = Label(root, text="", font=("Helvetica", 16))
    label.pack()

    def update_label(text):
        label.config(text=text)

    def close_window():
        root.destroy()

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        
        # Display the frame in a window
        cv2.imshow('Camera', frame)
        
        # Check for user input ('q' to quit and 's' to give image context)
        key = cv2.waitKey(1)
        
        if key == ord('q'):
            break
        elif key == ord('s'):
            # Save the captured frame as 'input_image.jpg'
            cv2.imwrite('input_image.jpg', frame)
            
            # Load and preprocess the image for inference
            img = cv2.imread('input_image.jpg')
            img = cv2.resize(img, (224, 224))  # Resize to match EfficientNet input size
            img = preprocess_input(img)
            img = np.expand_dims(img, axis=0)  # Add batch dimension
            
            # Perform inference
            predictions = model.predict(img)
            
            # Decode predictions (you may need to adjust this for your specific task)
            decoded_predictions = decode_predictions(predictions)
            
            # Display the top prediction
            top_prediction = decoded_predictions[0][0]
            result_text = f"Top Prediction: {top_prediction[1]} ({top_prediction[2]:.2f})"
            print(result_text)
            print(top_prediction)

            # Update the Tkinter label
            update_label(result_text)

            # Set a timer to close the Tkinter window after 10 seconds
            root.after(10000, close_window)
    
    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Start the Tkinter main loop
    root.mainloop()
