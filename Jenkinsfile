pipeline {
    agent any
    parameters {
        choice(name: 'TEST_TYPE', choices: ['smoke', 'regression', 'sanity'], description: 'Select test type')
    }
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://lokeshchadhokar@github.com/lokeshchadhokar/DemoQA_automation.git'
            }
        }
        stage('Run Tests - CMD') {
            steps {
                bat '''
                    cd tests
                    pytest -m %TEST_TYPE% -v"
                '''
            }
        }
    }
}