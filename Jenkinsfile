pipeline 
{
    agent any

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
                sh "apt-get update"
                sh "apt-get upgrade"
                sh "apt install docker.io"
                sh "docker build -t fastapi:latest ."
                

        }
            }



            stage('Push to registry') {
            steps 
            {
                sh "docker tag fastapi:latest gayatri491/fastapi:latest"
                sh "docker push gayatri491/fastapi:latest"
                

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
    
