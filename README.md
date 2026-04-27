# YOLOv5 Object Detection — From Research to Production

![Docker](https://img.shields.io/badge/Docker-djjoel%2Fyolov5--detection-blue?logo=docker)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Deployed-326CE5?logo=kubernetes)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions)
![Python](https://img.shields.io/badge/Python-3.9-yellow?logo=python)

I built this object detection system during my undergraduate research, trained it on the YOLOv5 pretrained model, and published the work in a Springer conference paper. After getting hands-on with DevOps and cloud infrastructure, I came back to this project and took it further — packaged it into a Docker container, set up a GitHub Actions pipeline to automate builds and pushes to Docker Hub, and deployed it on a Kubernetes cluster running on AWS EC2.

The goal was simple: take something I built as a researcher and show what it looks like when you treat it as a real product that needs to be deployed, maintained, and scaled.

> Published Paper: [Springer — Object Detection Using YOLOv5](https://link.springer.com/chapter/10.1007/978-981-99-7137-4_60)

---

## What It Does

<img width="1911" height="890" alt="image" src="https://github.com/user-attachments/assets/99a89346-820c-4bf6-b0c3-45d36f4de74b" />
<img width="1860" height="693" alt="image" src="https://github.com/user-attachments/assets/ea36d64f-2b5d-40d4-bcf4-fdf3dbeafefd" />



---

## Architecture
```
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
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| YOLOv5 | Pretrained object detection model |
| Streamlit | Web interface for uploads and results |
| Docker | Packages the app and all dependencies |
| Docker Hub | Hosts the published container image |
| Kubernetes | Runs and manages the app on AWS EC2 |
| kubeadm | Used to bootstrap the cluster from scratch |
| AWS EC2 | Cloud servers for master and worker nodes |
| GitHub Actions | Automates build and push on every commit |

---

## Run It Locally

If you want to try it without setting up Kubernetes, just pull the image and run:

```bash
docker pull djjoel/yolov5-detection:latest
docker run -p 8501:8501 djjoel/yolov5-detection:latest
```

Then open `http://localhost:8501` in your browser.

---

## Deploy on Kubernetes

```bash
# Create the namespace
kubectl create namespace prod

# Apply the manifests
kubectl apply -f https://raw.githubusercontent.com/joeldepuri/Object-detection-using-yolov5-devops/main/k8s/deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/joeldepuri/Object-detection-using-yolov5-devops/main/k8s/service.yaml

# Check that the pod is running
kubectl get pods -n prod
kubectl get svc -n prod
```

Once the pod is running, open `http://<worker-node-public-ip>:30001` in your browser.

---

## CI/CD Pipeline

Every push to `main` triggers the GitHub Actions workflow which:

1. Pulls the latest code
2. Logs into Docker Hub
3. Builds a fresh Docker image
4. Tags it with both `latest` and the commit SHA
5. Pushes it to `djjoel/yolov5-detection` on Docker Hub

No manual build steps — every commit ships automatically.

---

## Project Structure

```
Object-detection-using-yolov5-devops/
├── app.py                        # Streamlit web application
├── Dockerfile                    # How the container is built
├── .dockerignore                 # What to leave out of the build
├── k8s/
│   ├── deployment.yaml           # Kubernetes Deployment
│   └── service.yaml              # NodePort Service on port 30001
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # GitHub Actions pipeline
└── README.md
```

## About Me

I'm Joel, a graduate student in Information Technology Management at Webster University, San Antonio. My core focus is on DevOps and Cloud Engineering — working hands-on with Docker, Kubernetes, AWS, CI/CD pipelines, and infrastructure tooling.

Beyond the traditional DevOps stack, I'm actively exploring where AI fits into modern infrastructure. I'm currently learning MCP (Model Context Protocol), RAG (Retrieval-Augmented Generation), and AI agents — with a specific interest in integrating them into DevOps pipelines to automate workflows, reduce manual operations, and build smarter infrastructure. The way I see it, the next evolution of DevOps isn't just automation — it's intelligent automation.

[GitHub](https://github.com/joeldepuri) | [LinkedIn](https://www.linkedin.com/in/joeldepuri)
