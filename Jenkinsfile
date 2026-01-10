pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching Code from GitHub...'
                git branch: 'master', url: 'https://github.com/ponkarthickramu16-byte/E-Learning-Scaling.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                // Docker image-ah build panrom. Idhu unga Dockerfile-ah use pannum.
                bat 'docker build -t e-learning-monitor .'
            }
        }

        stage('Run Deployment (CD)') {
            steps {
                echo 'Deploying Container...'
                // Palaiya container irundha thookittu fresh-aa run pannuvom
                // -d potta background-la run aagum, Jenkins wait pannaadhu.
                bat 'docker rm -f my-monitor-app || true'
                bat 'docker run -d --name my-monitor-app e-learning-monitor'
            }
        }
    }
}
