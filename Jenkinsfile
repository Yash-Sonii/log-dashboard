pipeline {
  agent any
  stages {
    stage('Build') {
      steps { sh 'docker build -t log-dashboard:1.0 .' }
    }
    stage('Run') {
      steps { sh 'docker run -d -p 5000:5000 --name test-container log-dashboard:1.0' }
    }

    stage ('wait'){
        steps { sh 'sleep 10' }
    }

    stage('Verify') {
      steps { sh 'curl --fail http://localhost:5000/health' }
    }
    stage('Cleanup') {
      steps { sh 'docker stop test-container && docker rm test-container' }
    }
  }
}