pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "maorn132/maor25"  // שם ה-repository ב-Docker Hub
        DOCKER_TAG = "latest"  // הגרסה של ה-image
    }

    stages {
        stage('Checkout') {
            steps {
                // קוד למשיכת קבצים מה-repository ב-GitHub
                git 'https://github.com/maornaim/maor25.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    // בניית ה-Docker image מתוך ה-Dockerfile
                    sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // עליך להתחבר ל-Docker Hub לפני שאתה מבצע push
                    sh "docker login -u your-username -p your-password"  // חשוב לשים את פרטי ההתחברות שלך

                    // Push של ה-image ל-Docker Hub
                    sh "docker push ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
        stage('Deploy Docker Image') {
            steps {
                script {
                    // הרצת הקונטיינר מה-image החדש ב-Docker Hub
                    sh "docker run -d --name my_container -p 8080:8080 ${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }
    }

    post {
        always {
            // כל פעולה שתתבצע בסיום, לדוגמה סיום המבחן או בניית קונטיינר
            cleanWs()  // מנקה את המרחב של העבודה
        }
    }
}
