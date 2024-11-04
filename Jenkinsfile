pipeline {
    agent any
    
    tools{
        maven 'mvm399'
    }

    stages {
        stage('Git clone') {
            steps {
                git credentialsId: 'github', url: 'https://github.com/anshulmb/maven-web-app.git'
            }
        }
        stage('mvn build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('docker image build') {
            steps {
                sh 'docker build -t anshulit .'
            }
        }
        stage('docker container') {
            steps {
                sh 'docker run -d -p 9092:8080 --name anshulc2 anshulit'
            }
        }
    }
}
