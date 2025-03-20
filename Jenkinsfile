pipeline {
    agent any
    
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm  // מבצע את ה-checkout מה-repository
            }
        }
        
        // תוכל להוסיף כאן עוד שלבים, לדוגמה:
        stage('Build') {
            steps {
                echo 'Building the project'
                // הוספת פקודות בניית קוד כאן אם צריך
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the project'
                // הוספת פקודות פריסת הקוד אם צריך
            }
        }
    }
    
    post {
        always {
            cleanWs()  // מנקה את סביבת העבודה בסוף
        }
    }
}
