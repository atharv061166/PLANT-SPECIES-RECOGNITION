import cv2
import numpy as np
import requests
import base64
import json

# Plant.id API URL and Key
API_URL = "https://api.plant.id/v2/identify"
API_KEY = "Q4g6B1DT9MwNymCrSijxdUrynLlZFhQ17YyyG2Uy6Pe7xiNOlh"  # Replace with your actual API key

# Function to send image to Plant.id API and get the prediction
def get_plant_prediction(image_path):
    with open(image_path, "rb") as image_file:
        img_data = image_file.read()
    
    # Convert the image to base64
    img_base64 = base64.b64encode(img_data).decode("utf-8")
    
    headers = {
        "Api-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {
        "images": [img_base64],
        "organs": ["leaf"]  # Optionally specify other plant parts (like "flower", "fruit", etc.)
    }
    
    # Send the request to the API
    response = requests.post(API_URL, headers=headers, json=data)
    
    # Debug: Print the raw response
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    if response.status_code == 200:
        try:
            # Try to parse the JSON response
            response_data = response.json()
            
            if response_data.get("suggestions"):
                for suggestion in response_data["suggestions"]:
                    print(f"Species: {suggestion['plant_name']}, Probability: {suggestion['probability']:.2f}")
            else:
                print("No plant found. Please try again.")
        except json.JSONDecodeError:
            print("Failed to parse JSON. Response content is not valid JSON.")
    else:
        print(f"Error: {response.status_code}. The request failed.")

# Function to capture an image from the camera
def capture_and_predict():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        
        # Display the captured frame
        cv2.imshow('Press q to Quit and Capture', frame)

        # Wait for the 'q' key to capture image
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the captured image and make a prediction
            cv2.imwrite("captured_image.jpg", frame)
            print("Image captured. Predicting plant species...")
            get_plant_prediction("captured_image.jpg")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_predict()
