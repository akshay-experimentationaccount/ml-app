pipeline {
    agent any

    environment {
        GIT_USERNAME = "akshay-experimentationaccount"
        GIT_PAT = "******"  // Replace with actual GitHub PAT
        GIT_REPO = "https://${GIT_USERNAME}:${GIT_PAT}@github.com/${GIT_USERNAME}/ml-app.git"
        VENV_DIR = "venv"  // Virtual environment directory
    }

    stages {
        stage('Cleanup') {
            steps {
                cleanWs() // Cleans up the workspace before starting
            }
        }
        stage('Clone Repository') {
            steps {
                sh "git clone ${GIT_REPO} --branch main ml-app"
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''#!/bin/bash
                cd ml-app
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''#!/bin/bash
                cd ml-app
                source ${VENV_DIR}/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''#!/bin/bash
                cd ml-app
                source ${VENV_DIR}/bin/activate
                pytest tests/
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                cd ml-app
                docker build -t ml-app .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                docker run -d -p 5000:5000 ml-app
                '''
            }
        }
    }
}
