from PIL import Image
import numpy as np
import io
import cv2

def detect_image(file):
    try:
        image_bytes = file.file.read()

        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        img = np.array(image)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()

        if laplacian_var < 100:
            return "Real Image"
        else:
            return "AI Generated Image"

    except Exception as e:
        return f"Image Detection Error: {str(e)}"


