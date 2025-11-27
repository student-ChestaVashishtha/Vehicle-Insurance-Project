🚗 Vehicle Insurance Prediction System
End-to-End MLOps | CI/CD | AWS | FastAPI | Docker | GitHub Actions
📌 Overview

This project predicts whether a vehicle owner is likely to purchase vehicle insurance based on demographic and historical inputs.

It is built as a full production-grade Machine Learning system, featuring:

🔹 Modular ML Pipeline

🔹 DVC-style workflow without DVC

🔹 AWS S3 Model Registry

🔹 CI/CD Deployment to AWS EC2 using GitHub Actions

🔹 Inference using FastAPI Web App

🎯 Features
Feature	Status
End-to-end ML pipeline	✔️
MongoDB Atlas as data source	✔️
Automated data ingestion → validation → transformation → training	✔️
Model evaluation and push to AWS S3	✔️
REST API using FastAPI	✔️
Production deployment via CI/CD to AWS EC2	✔️
Dockerized container support	✔️
Interactive UI (HTML + CSS + FastAPI)	✔️
🧱 Tech Stack
Category	Tools
Languages	Python, HTML, CSS
ML Libraries	Scikit-learn, Pandas, Numpy
Backend	FastAPI
Database	MongoDB Atlas
Cloud	AWS S3, EC2, IAM
DevOps	Docker, GitHub Actions
Environment	Conda
🚀 System Architecture
                    ┌──────────────────┐
                    │   MongoDB Atlas   │
                    └─────────┬────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Data Ingestion     │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Data Validation    │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Data Transformation│
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Model Training     │
                    └─────────┬─────────┘
                              │
                    ┌─────────▼─────────┐
                    │ Model Evaluation   │
                    └─────────┬─────────┘
                              │
                 ┌────────────▼─────────────┐
                 │ Model Registry (AWS S3)   │
                 └────────────┬─────────────┘
                              │
                      ┌───────▼────────┐
                      │ FastAPI Backend │
                      └───────┬────────┘
                              │
                      ┌───────▼────────┐
                      │    Web UI      │
                      └─────────────────┘

🛠 Installation & Setup
1️⃣ Clone Repository
git clone <repo_url>
cd Vehicle-Insurance-Prediction

2️⃣ Create Virtual Environment
conda create -n vehicle python=3.10 -y
conda activate vehicle

3️⃣ Install Dependencies
pip install -r requirements.txt

🏗 Project Roadmap (Completed)

✔️ Folder structure initialization
✔️ setup.py & pyproject.toml for local package imports
✔️ MongoDB integration & dataset upload
✔️ Logging and custom exception handling
✔️ Data pipeline modules
✔️ AWS S3 storage + IAM configuration
✔️ Model Registry & Prediction Pipeline
✔️ Deployment using Docker + EC2 + GitHub Actions
✔️ Web Interface using FastAPI

🌍 Deployment

📦 Dockerized application
🚀 CI/CD pipeline automatically:

Builds Docker Image

Pushes image to AWS ECR

Deploys to EC2 runner

Starts FastAPI app on port 5000

You can access the live app with:

http://<EC2-Public-IP>:5000

🧪 Running Training Pipeline
http://<EC2-Public-IP>:5000/train

🖼 UI Preview

(Optional: Add screenshots of UI & pipeline results)

📁 Repository Structure
├── src
│   ├── components
│   ├── pipeline
│   ├── configuration
│   ├── utils
│   ├── entity
│   ├── ...
├── templates/
├── static/
├── notebook/
├── Dockerfile
├── requirements.txt
├── setup.py
├── app.py

🧑‍💻 Author

Chesta Vashishtha
🚀 ML Engineer | MLOps | Cloud | AI Systems
📬 Email: vashishthachesta@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/chesta-vashishtha-a9b451318/
💻 GitHub: https://github.com/student-ChestaVashishtha

⭐ If You Like This Project

Give it a star ⭐ — it helps and motivates!
