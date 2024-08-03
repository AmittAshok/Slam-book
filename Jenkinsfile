pipeline {
    agent any

    stages {
        stage("Code Clone") {
            steps {
                git url: "https://github.com/AmittAshok/Slam-book.git", branch: "master"
            }
        }
        stage("Code build") {
            steps {
                sh 'docker build . -t amittashok/slambook-cicd:latest'
            }
        }
        stage("login and push") {
            steps {
                echo "Building the code and pushing to Docker Hub"
                withCredentials([usernamePassword(credentialsId: 'docker-hub', passwordVariable: 'docHubPassword', usernameVariable: 'docHubUsername')]) {
                    sh "docker login -u ${env.docHubUsername} -p ${env.docHubPassword}"
                    sh "docker push amittashok/slambook-cicd:latest "
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
}
