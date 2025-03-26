pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'maorn132/maor25:latest' // שנה לשם המשתמש שלך ב-Docker Hub
        DOCKER_HUB_CREDENTIALS = 'docker-hub' // שם הקרדנציאלס ל-Docker Hub ב-Jenkins
        GITHUB_CREDENTIALS = 'git-hub' // שם הקרדנציאלס ל-GitHub ב-Jenkins
    }
    stages {
        stage('Clone from GitHub') {
            steps {
                script {
                    // clone the repository using the GitHub credentials
                    git branch: 'main', url: 'https://github.com/maornaim/maor25.git', credentialsId: "${GITHUB_CREDENTIALS}"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    // Push Docker image to Docker Hub using the Docker credentials
                    withDockerRegistry([credentialsId: "${DOCKER_HUB_CREDENTIALS}"]) {
                        sh "docker push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy the application to Kubernetes (ensure you have a valid deployment.yaml)
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
}
