pipeline {
    agent any

    environment {
        GIT_USERNAME = "akshay-experimentationaccount"
        GIT_PAT = "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"
        GIT_REPO = "https://akshay-experimentationaccount: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@github.com/akshay-experimentationaccount/ml-app.git"
    }

    stages {
        stage('Clone Repository') {
            steps {
                sh "git clone ${GIT_REPO} --branch main ml-app"
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd ml-app
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                cd ml-app
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
