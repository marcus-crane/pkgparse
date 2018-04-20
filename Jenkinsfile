pipeline {
    agent 'any'
    stages {
        stage('Branch Check') {
            when {
                not {
                    anyOf {
                        branch 'PR-*'
                        branch 'master'
                    }
                }
            }
            steps {
                script {
                    currentBuild.result = 'ABORTED'
                    error('Stopping early...')
                }
            }
        }
        stage('Installing dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Checking code quality') {
            when {
                anyOf {
                    branch 'PR-*'
                    branch 'master'
                }
            }
            steps {
                parallel(
                    lint: {
                        script {
                            env.STEP = 'Linting'
                            sh 'inv test.flake8'
                        }
                    },
                    unit: {
                        script {
                            env.STEP = 'Unit Tests'
                            sh 'inv test.unit'
                        }
                    },
                    integration: {
                        script {
                            env.STEP = 'Integration Tests'
                            sh 'inv test.integration'
                        }
                    }
                )
            }
        }
    }
}