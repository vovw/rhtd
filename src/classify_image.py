import cv2
import numpy as np
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input, decode_predictions

def get_image_info():
    # Load pre-trained EfficientNet model
    model = EfficientNetB0(weights='imagenet')

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()
        
        # Display the frame in a window
        cv2.imshow('Camera', frame)
        
        # Check for user input (press 'q' to quit or 's' to save and classify the image)
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
            print(f"Top Prediction: {top_prediction[1]} ({top_prediction[2]:.2f})")
    
    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# i dont know what to do here HALP
if __name__ == "__main__":
    get_image_info()
