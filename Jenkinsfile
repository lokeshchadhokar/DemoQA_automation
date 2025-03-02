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
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh "pytest -m ${params.TEST_TYPE} -v --html=report.html"
            }
        }
//         stage('Generate Report') {
//             steps {
//                 archiveArtifacts artifacts: 'report.html', fingerprint: true
//             }
        }
    }
}