pipeline 
{
    agent any
    stages 
    {
        stage('Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Gayatri1303/Restaurant_Assignment.git'
            }
    }
        
        stage('Build') {
            steps 
            {
                sh "sudo apt-get update"
                sh "RUN apt-get update && apt-get install -y curl"
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
                sh "sudo docker run -d -p 8000:8000 fastapi:latest gayatri491/fastapi:latest"
                
                

        }
            }


             }
    }
    
