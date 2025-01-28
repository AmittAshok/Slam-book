pipeline {
    agent any

    stages {
        stage("Code Clone") {
            steps {
                git url: "https://github.com/AmittAshok/Slam-book.git", branch: "master"
            }
        }

        stage("Filesystem Scan with Trivy") {
            steps {
                echo "Scanning the filesystem with Trivy"
                sh 'trivy fs . --exit-code 1 || true' // Scans the current directory
            }
        }

        stage("Code Build") {
            steps {
                sh 'docker build . -t amittashok/slambook-cicd:latest'
            }
        }

        stage("Image Scan with Trivy") {
            steps {
                echo "Scanning the Docker image with Trivy"
                sh 'trivy image amittashok/slambook-cicd:latest --exit-code 1 || true' // Scans the built Docker image
            }
        }

        stage("Dependency Analysis with OWASP Dependency-Check") {
            steps {
                echo "Performing OWASP Dependency Analysis"
                sh '''
                    dependency-check --scan . \
                    --out owasp-report \
                    --format HTML
                '''
                archiveArtifacts artifacts: 'owasp-report/dependency-check-report.html', allowEmptyArchive: true
            }
        }

        stage("Login and Push") {
            steps {
                echo "Building the code and pushing to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'docHubPassword', usernameVariable: 'docHubUsername')]) {
                    sh "docker login -u ${env.docHubUsername} -p ${env.docHubPassword}"
                    sh "docker push amittashok/slambook-cicd:latest"
                }
            }
        }

        stage("Code Run") {
            steps {
                sh 'docker compose down'  // Use 'docker-compose' if using Docker Compose v1
                sh 'docker compose up -d'  // Use 'docker-compose' if using Docker Compose v1
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
            mail to: 'amittashok@gmail.com',
                 subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Good news! The pipeline ${env.JOB_NAME} completed successfully.\nCheck the details at ${env.BUILD_URL}"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
            mail to: 'amittashok@gmail.com',
                 subject: "Jenkins Pipeline Failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 body: "Unfortunately, the pipeline ${env.JOB_NAME} failed.\nCheck the logs at ${env.BUILD_URL}"
        }
        always {
            echo "Cleaning up workspace"
            cleanWs() // Cleans up the workspace after every build
        }
    }
}

