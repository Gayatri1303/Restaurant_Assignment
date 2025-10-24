pipeline 
{
    agent any
    options {
            skipDefaultCheckout true
        }
    stages 
    {
        stage(' Code') {
            steps 
            {
               sh "git clone https://github.com/Gayatri1303/Restaurant_Assignment"
                }
            }
        
        stage('Build') {
            steps 
            {
                sh "sudo apt-get update"
                sh "sudo apt-get upgrade"
                sh "sudo apt install docker.io"
                sh "sudo docker build -t fastapi:latest ."
                

        }
            }



            stage('Push to registry') {
            steps 
            {
                sh "sudo docker tag fastapi:latest gayatri491/fastapi:latest"
                sh "sudo docker push gayatri491/fastapi:latest"
                

        }
            }



             stage('Deploy') {
            steps 
            {
                sh "docker run -d -p 8000:8000 fastapi:latest gayatri491/fastapi:latest"
                
                

        }
            }


             }
    }
    
