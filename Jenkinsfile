pipeline {
    agent any

    stages {
        stage("create docker image") {
            steps {
                echo "========== start building image =========="
                sh "sudo docker build -t rodionova_test ."
                sh "sudo docker run rodionova_test pytest -s -v tests/web_test.py"
            }
        }
    }
}