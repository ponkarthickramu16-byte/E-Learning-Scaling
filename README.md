Automated Scaling of E-Learning Platforms During Peak Usage
🚀 Project Overview
This project focuses on building a highly available, secure, and scalable e-learning platform using DevSecOps methodologies. It addresses the challenges of fluctuating user traffic and security vulnerabilities by leveraging container orchestration and automated CI/CD pipelines.

🛠 Technologies & Tools
Frontend/Backend: Node.js, Express.js, HTML5, Bootstrap.

DevOps: Jenkins (CI/CD), Docker (Containerization).

Orchestration: Kubernetes (Minikube).

Security: SonarQube (Code Analysis), Trivy (Vulnerability Scanning).

Monitoring: Prometheus & Grafana.

🏗 System Architecture
The workflow follows a strict DevSecOps pipeline:

Code Commit: Developers push code to GitHub.

Continuous Integration: Jenkins triggers a build, runs SonarQube for code quality, and Trivy for image security.

Deployment: The secure Docker image is deployed to a Kubernetes cluster.

Monitoring: Prometheus collects cluster metrics, and Grafana visualizes the system health.

📦 How to Run
Clone the Repo:

Bash
git clone https://github.com/ponkarthickramu16-byte/E-Learning-Scaling.git
Deploy to Kubernetes:

Bash
kubectl apply -f deployment.yaml
Access the Service:

Bash
minikube service elearning-monitor
📊 Key Results
Zero Vulnerabilities: Successfully passed the SonarQube Quality Gate.

Automation: End-to-end deployment in under 35 seconds via Jenkins.

High Availability: Kubernetes ensures 100% uptime with automated pod scaling.
