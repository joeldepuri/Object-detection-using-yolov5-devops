# YOLOv5 Object Detection — DevOps Edition

![Docker](https://img.shields.io/badge/Docker-djjoel%2Fyolov5--detection-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?logo=kubernetes)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.9-yellow?logo=python)

A production-style DevOps upgrade of a YOLOv5-based object detection application. The app detects objects in images and videos using a pretrained YOLOv5 model via a Streamlit web interface — containerized with Docker, deployed on a multi-node Kubernetes cluster on AWS EC2, and automated with a GitHub Actions CI/CD pipeline.

> Research paper: [Springer — Object Detection Using YOLOv5](https://link.springer.com/chapter/10.1007/978-981-99-7137-4_60)

---

## Architecture
Developer pushes code to GitHub (main branch)
|
v
GitHub Actions CI/CD Pipeline
- Builds Docker image
- Pushes to Docker Hub (djjoel/yolov5-detection:latest)
|
v
AWS EC2 Kubernetes Cluster (kubeadm)
+----------------+   +-----------------+   +-----------------+
| Master Node    |   | Worker Node 1   |   | Worker Node 2   |
| t2.medium      |   | t3.small        |   | t3.small        |
| Control Plane  |   | Runs Pods       |   | Runs Pods       |
+----------------+   +-----------------+   +-----------------+
|
YOLOv5 Detection Pod
Streamlit UI on port 8501
Exposed via NodePort 30001

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| YOLOv5 | Pretrained object detection model |
| Streamlit | Web UI for image and video detection |
| Docker | Containerization |
| Docker Hub | Container image registry |
| Kubernetes | Container orchestration on AWS EC2 |
| kubeadm | Kubernetes cluster bootstrap |
| AWS EC2 | Cloud infrastructure |
| GitHub Actions | CI/CD pipeline automation |

---

## Run with Docker

```bash
docker pull djjoel/yolov5-detection:latest
docker run -p 8501:8501 djjoel/yolov5-detection:latest
```

Open browser at `http://localhost:8501`

---

## Deploy on Kubernetes

```bash
# Create namespace
kubectl create namespace prod

# Apply manifests
kubectl apply -f https://raw.githubusercontent.com/joeldepuri/Object-detection-using-yolov5-devops/main/k8s/deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/joeldepuri/Object-detection-using-yolov5-devops/main/k8s/service.yaml

# Check pod status
kubectl get pods -n prod

# Check service
kubectl get svc -n prod
```

Access the app at `http://<worker-node-public-ip>:30001`

---

## CI/CD Pipeline

Every push to `main` branch automatically triggers:

1. Checkout code from GitHub
2. Login to Docker Hub
3. Build Docker image
4. Tag with `latest` and commit SHA
5. Push image to Docker Hub (`djjoel/yolov5-detection:latest`)

---

## Project Structure
Object-detection-using-yolov5-devops/
├── app.py                        # Streamlit application
├── Dockerfile                    # Container build instructions
├── .dockerignore                 # Files excluded from Docker build
├── k8s/
│   ├── deployment.yaml           # Kubernetes Deployment manifest
│   └── service.yaml              # Kubernetes NodePort Service
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions CI/CD pipeline
└── README.md                     # Project documentation

---

## Author

**Jedeediah Joel Depuri**  
MS in Information Technology Management — Webster University, San Antonio  
[GitHub](https://github.com/joeldepuri) | [LinkedIn](https://www.linkedin.com/in/joeldepuri)
