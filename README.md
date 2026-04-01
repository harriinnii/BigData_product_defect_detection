🔧 Real-Time Defective Screw Detection using Kafka, Spark, MongoDB & Docker
📌 Project Overview

This project implements a real-time quality control analytics pipeline to detect defective screws in a manufacturing environment. The system streams inspection data, processes it using Spark analytics, stores results in MongoDB, and visualizes the analytics using Python and Matplotlib.

🏗️ System Architecture

Producer → Kafka → Consumer → MongoDB → Spark Analytics → Visualization

⚙️ Technologies Used
Apache Kafka – Real-time data streaming
Apache Spark (MLlib) – Analytics & defect detection
MongoDB – Data storage
Python – Data processing & visualization
Matplotlib & Pandas – Charts & analytics
Docker – Containerized MongoDB deployment
WSL Ubuntu – Development environment
🔄 Workflow
Producer sends screw inspection data to Kafka
Kafka streams data in real-time
Consumer reads data and stores into MongoDB
Spark performs analytics to detect defective screws
Python visualization generates charts
Real-time insights displayed using plots
📊 Analytics Performed
Count of Good vs Defective screws
Defect distribution analysis
Product-wise inspection results
Real-time quality monitoring
Spark MLlib defect prediction
📈 Visualizations

The system generates:

Bar chart: Count of Good vs Defective screws
Pie chart: Defect distribution
Product-wise inspection chart

Example output files:

plot1_status.png
plot2_confidence.png
plot3_product.png
🐳 Docker Deployment

MongoDB is deployed using Docker container:

docker run -d --name mongodb -p 27017:27017 mongo

Benefits:

Containerized database
Easy setup
Portable deployment
Isolated environment
▶️ How to Run the Project
Step 1: Start Zookeeper
bin/zookeeper-server-start.sh config/zookeeper.properties
Step 2: Start Kafka Broker
bin/kafka-server-start.sh config/server.properties
Step 3: Start MongoDB Docker
docker start mongodb
Step 4: Run Producer
python3 producer.py
Step 5: Run Consumer
python3 consumer.py
Step 6: Run Spark Analytics
spark-submit spark_analytics.py
Step 7: Run Visualization
python3 visualization.py
📁 Project Structure
project/
│
├── producer.py
├── consumer.py
├── spark_analytics.py
├── visualization.py
├── requirements.txt
├── Dockerfile
├── README.md
└── plots/
🎯 Features
Real-time defect detection
Scalable streaming architecture
Spark MLlib analytics
Docker-based deployment
Automated visualization
Modular pipeline design
🚀 Future Improvements
Real-time dashboard (Streamlit)
Spark Structured Streaming
Deep learning defect detection
Cloud deployment (AWS/Azure)
Kafka Connect integration
👩‍💻 Author

Harini – Real-Time Quality Control Analytics Project
