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
        stage("Helm install"){
            steps{
                echo "Helm install"      
                sh 'curl -o kubectl https://amazon-eks.s3.us-west-2.amazonaws.com/1.18.9/2020-11-02/bin/linux/amd64/kubectl'       
                sh 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" '
                sh 'sudo cp kubectl /usr/bin' 
                sh 'sudo chmod +x /usr/bin/kubectl'
                sh 'wget https://get.helm.sh/helm-v3.6.1-linux-amd64.tar.gz'
                sh 'ls -a'
                sh 'tar -xvzf helm-v3.6.1-linux-amd64.tar.gz'
                sh 'sudo cp linux-amd64/helm /usr/bin'
            }
        }
        stage('Deploy to GKE') {
            agent{
                kubernetes{
                    containerTemplate{
                        name 'helm' // name of the container to be used for hel, upgrade
                        image 'fullstackdatascience/jenkins:lts' // the image containing helm
                        alwaysPullImage true // Always pull image in case of using the same tag
                     }
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