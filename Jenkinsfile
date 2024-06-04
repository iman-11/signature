pipeline {
    agent any

    // environment {
    //     // Variables d'environnement
    //     DOCKER_IMAGE = '
    //     DOCKER_TAG = 'latest'
    // }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/iman-11/signature.git']]])
            }
        }
        stage('Build') {
            steps {
                script {
                    // Construire l'image Docker
                    bat 'docker build -t model_signature_based .'
                    
                }
            }
        }
        stage('push') {
            steps {
                script {
                    // Construire l'image Docker
                    // withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhub-pwd')]) {
                    bat 'docker login'
                    bat 'docker push imanhrt/model_signature_based'
                    // }
                    
                }
            }
        }
    }
}