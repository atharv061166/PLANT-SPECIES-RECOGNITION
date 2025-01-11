# Plant Recognition System

## Overview

This project is a Python-based Plant Recognition System that uses the Plant.id API to identify plant species from images. The system captures images using a webcam and sends them to the Plant.id API for analysis. The API responds with plant species predictions along with their probabilities. This project showcases the integration of computer vision and API usage for real-world applications.

## Features

- Captures images using a webcam.
- Identifies plant species by analyzing the captured images via the Plant.id API.
- Displays the species name and probability of identification.
- Simple and interactive interface using OpenCV.

## Requirements

To run this project, ensure you have the following dependencies installed:

- Python 3.6+
- OpenCV
- NumPy
- Requests

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/plant-recognition-system.git
   cd plant-recognition-system
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace the placeholder API key in the `API_KEY` variable with your actual API key from [Plant.id](https://web.plant.id/).

## Usage

1. Run the script:

   ```bash
   python plant_recognition.py
   ```

2. The webcam feed will appear. Press `q` to capture an image and get the plant species prediction.

3. The species name and probability will be displayed in the terminal.

## Example

- Capture an image of a plant's leaf using the webcam.
- The system will identify the plant species, such as:

  ```
  Species: Rosa chinensis, Probability: 0.95
  ```

## Limitations

- Requires an active internet connection to communicate with the Plant.id API.
- Limited to the features provided by the Plant.id API.

## Future Enhancements

- Add support for analyzing images of flowers, fruits, and other plant parts.
- Build a graphical user interface for a more user-friendly experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
