pipeline {

    agent any

    options{
        // Max number of build logs to keep and days to keep
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
        // Enable timestamp at each job in the pipeline
        timestamps()
    }

    environment{
        registry = 'khoav1371999/classify_toxic_text'
        registryCredential = 'dockerhub'      
    }

    stages {
        stage('Testing') {
            agent {
                docker {
                    image 'python:3.11-slim' 
                }
            }
            steps {
                echo 'Testing model correctness..'
                sh 'pip install -r requirements.txt --no-cache-dir'
                
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building image for deployment..'
                    dockerImage = docker.build registry + ":$BUILD_NUMBER" 
                    echo 'Pushing image to dockerhub..'
                    docker.withRegistry( '', registryCredential ) {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Deploy to GKE') {
            agent{
                kubernetes{
                    yaml """
                        apiVersion: v1
                        kind: Pod
                        spec:
                        containers:
                        - name: helm
                            image: fullstackdatascience/jenkins:lts
                            imagePullPolicy: Always
                    """
                }
            }
            steps{
                script{
                    container('helm'){
                        sh("helm upgrade --install classify-toxic-text \
                        ./helm/toxic_chart --namespace model-serving")
                    }
                }
            }
        }
    }
}