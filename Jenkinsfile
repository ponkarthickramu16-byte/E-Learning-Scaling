pipeline {
    agent any
    triggers {
        pollSCM('* * * * *') // 1 min-ku oru vaati check pannum
    }
    stages {
        stage('Build Docker Image') {
            steps {
             // Docker image-ah build panrom
                bat 'docker build -t e-learning-monitor .'
            }
        }
        stage('Run Container') {
            steps {
            // Palaiya container irundha stop panni thirumba run panrom
                bat 'docker run --name monitoring-app e-learning-monitor'
            }
        }
        stage('Checkout') {
            steps {
                echo 'Fetching Code from GitHub...'
                git 'https://github.com/ponkarthickramu16-byte/E-Learning-Scaling.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing psutil...'
                bat '"C:\\Users\\ponka\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pip install psutil'
            }
        }
        stage('Run Monitoring') {
            steps {
                echo 'Starting Scaling Monitor...'
                bat '"C:\\Users\\ponka\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" app.py'
            }
        }
    }
}
