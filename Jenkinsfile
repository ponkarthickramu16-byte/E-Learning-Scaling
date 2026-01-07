pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Fetching Code from GitHub...'
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
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
