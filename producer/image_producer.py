import os
import base64
import time
from kafka import KafkaProducer

# Path to your screw test images
IMAGE_FOLDER = r"/mnt/d/BDM_MINI/screw/test"

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

# Recursively send all images from subfolders
for root, dirs, files in os.walk(IMAGE_FOLDER):
    for img in files:
        if img.lower().endswith((".jpg", ".png")):
            path = os.path.join(root, img)
            with open(path, "rb") as image_file:
                encoded = base64.b64encode(image_file.read())
                producer.send("raw-sensor-images", encoded)
                print(f"Sent: {path}")
            time.sleep(0.2)  # optional delay

producer.close()
print("All images sent!")
