from pyspark.sql import SparkSession
import base64
from pymongo import MongoClient

# Create Spark session
spark = SparkSession.builder \
    .appName("ScrewQC") \
    .getOrCreate()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["quality_control"]
collection = db["defect_log"]

# Dummy defect detection function
def detect_defect(image_bytes):
    # Replace this later with YOLO/MobileNet for real detection
    if len(image_bytes) % 2 == 0:
        return ("defect", 0.85)
    else:
        return ("ok", 0.95)

# Process each micro-batch from Kafka
def process_batch(df, epoch_id):
    rows = df.collect()
    for idx, row in enumerate(rows):
        img_bytes = base64.b64decode(row.value)
        label, conf = detect_defect(img_bytes)
        doc = {
            "product_id": f"{epoch_id}_{idx}",
            "status": label,
            "confidence": conf
        }
        collection.insert_one(doc)
        print(doc)

# Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers","localhost:9092") \
    .option("subscribe","raw-sensor-images") \
    .load()

# Start streaming
query = df.writeStream.foreachBatch(process_batch).start()
query.awaitTermination()
