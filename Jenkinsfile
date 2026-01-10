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
                // Unga laptop-la Docker path sariya irukka nu paarunga
                bat 'docker build -t e-learning-monitor .'
            }
        }

        stage('Run Container (CD)') {
            steps {
                echo 'Starting Containerized Monitoring...'
                // Palaiya container irundha delete panni fresh-aa run pannum
                bat 'docker rm -f my-monitor-app || true'
                bat 'docker run -d --name my-monitor-app e-learning-monitor'
            }
        }
    }
}