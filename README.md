## Overview

I wanted to try this out as i know a lot of motorpsorts tech involves this type of enviroment of real time data so i wanted to try this out and with the help of gpt it made it easier and i know havea  good foundation of how to use docker and this tech stack so only up from here if any questions feel free to ask! 

# 📊 Kafka + InfluxDB + Grafana Pipeline

A minimal template to simulate a real-time data pipeline using:
- **Kafka**: For producing and brokering messages.
- **InfluxDB**: As a time-series database to store data.
- **Grafana**: For visualizing time-series data in real-time dashboards.

---

## 🚀 Features
- Dockerized Kafka, InfluxDB, and Grafana.
- Python producer simulating temperature sensor data.
- Python consumer storing Kafka messages to InfluxDB.
- Grafana dashboard for visualization.
- `.env`-based configuration for secure and dynamic setup.

---

## 📁 Project Structure
```
kafka-temp-project/
├── .env
├── docker-producer.yml
├── consumer.yml
├── Dockerfile.producer
├── Dockerfile.consumer
├── producer.py
├── consumer.py
├── requirements.txt
```

---

## 📦 Prerequisites
- [Docker](https://docs.docker.com/get-docker/) and Docker Compose installed.
- If Docker Desktop on Windows gives issues, **use Docker under WSL/Linux mode** for better compatibility.
- Python (for writing/editing scripts, not required to run containers).

---

## ⚙️ Configuration via `.env`

Create a `.env` file in the root directory:

```env
# InfluxDB Configuration
INFLUXDB_USERNAME=admin
INFLUXDB_PASSWORD=admin123
INFLUXDB_ORG=my-org
INFLUXDB_BUCKET=temperature
INFLUXDB_TOKEN=admin123

# Grafana Configuration
GRAFANA_ADMIN_USER=admin
GRAFANA_ADMIN_PASSWORD=admin123
```

---

## 🐳 Docker Compose

### Start Kafka + Producer
```bash
docker-compose -f docker-producer.yml --env-file .env up -d --build
```

### Start InfluxDB + Grafana + Consumer
```bash
docker-compose -f consumer.yml --env-file .env up -d --build
```

### Stop All Containers
```bash
docker-compose -f docker-producer.yml down
docker-compose -f consumer.yml down
```

### Check Container Status
```bash
docker ps
```

---

## 🔒 Setting Up InfluxDB

1. Visit: [http://localhost:8086](http://localhost:8086)
2. Login with:
   - Username: `admin` (from `.env`)
   - Password: `admin123`
3. Confirm organization and bucket names match `.env`:
   - Org: `my-org`
   - Bucket: `temperature`

---

## 📊 Setting Up Grafana

1. Visit: [http://localhost:3000](http://localhost:3000)
2. Login with:
   - Username: `admin` (from `.env`)
   - Password: `admin123`
3. Add InfluxDB as a Data Source:
   - URL: `http://influxdb:8086`
   - Token: `admin123`
   - Org: `my-org`
4. Create a new dashboard:
   - Visualize data from the `temperature` bucket.

---

## 🧪 View Logs

### Producer Logs
```bash
docker logs kafka-temp-project-producer-1
```

### Consumer Logs
```bash
docker logs kafka-temp-project-consumer-1
```

---

## 🧼 Clean Up

To stop and remove all services:
```bash
docker-compose -f docker-producer.yml down -v
docker-compose -f consumer.yml down -v
```

---

## 📝 Notes

- If running on **Windows**, prefer using Docker under **WSL or a Linux VM** if you face issues.
- You can adjust the producer delay or topic by modifying `producer.py`.
- To reset data, delete volumes or use `docker-compose down -v`.

---

## 🙌 Credits

Built by Aidan Keith Naidoo as a template to understand real-time pipelines using modern open-source tools.
