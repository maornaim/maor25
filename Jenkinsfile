pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'maorn132/maor25:latest' // שנה לשם המשתמש שלך ב-Docker Hub
    }
    stages {
        stage('Clone from GitHub') {
            steps {
                script {
                    git branch: 'main', url: 'https://github.com/maornaim/maor25.git'
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withDockerRegistry([credentialsId: 'docker-hub-credentials']) {
                    script {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
