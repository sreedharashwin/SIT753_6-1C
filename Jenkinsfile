pipeline {
    agent any
    
stages {
        stage('Build') {
            steps {
                script {
                    echo "Stage 1: Build - Using Maven to compile and package the code."
                    // Example: sh 'mvn clean install'
                }
            }
        }

        stage('Unit and Integration Tests') {
            steps {
                script {
                    echo "Stage 2: Unit and Integration Tests - Running tests using JUnit and Maven."
                    // Example: sh 'mvn test'
                }
            }
            post {
                always {
                    script {
                        def lFile = 'test.txt'
                        writeFile file: lFile, text: currentBuild.rawBuild.getLog(1000).join("\n")
                        archiveArtifacts artifacts: lFile, allowEmptyArchive: true
                         emailext(
                            to: 'qwertyorg2@gmail.com',
                            subject: "Tests have Succeeded: ${currentBuild.fullDisplayName}",
                            body: "The tests stage has succeeded. Logs are attached.",
                            attachmentsPattern: lFile
                        )
                    }
                }
            }
        }

        stage('Code Analysis') {
            steps {
                script {
                    echo "Stage 3: Code Analysis - Analyzing code with SonarQube."
                    // Example: sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    echo "Stage 4: Security Scan - Performing security scan with OWASP Dependency-Check."
                    // Example: sh 'dependency-check.sh --project myApp --scan ./'
                }
            }
            post {
                always {
                    script {
                        def logFile = 'scan.txt'
                        writeFile file: logFile, text: currentBuild.rawBuild.getLog(1000).join("\n")
                        archiveArtifacts artifacts: logFile, allowEmptyArchive: true
                        emailext(
                            to: 'qwertyorg2@gmail.com',
                            subject: "Security Scan Succeeded: ${currentBuild.fullDisplayName}",
                            body: "The Security Scan stage has succeeded. Logs are attached.",
                            attachmentsPattern: logFile
                        )
                    }
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                script {
                    echo "Stage 5: Deploy to Staging - Deploying to AWS EC2 instance."
                    // Example: sh 'scp target/myapp.jar ec2-user@staging-instance:/path/to/deploy'
                }
            }
        }

        stage('Integration Tests on Staging') {
            steps {
                script {
                    echo "Stage 6: Integration Tests on Staging - Running tests in the staging environment."
                    // Example: sh 'mvn verify -Pstaging'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    echo "Stage 7: Deploy to Production - Deploying to production server."
                    // Example: sh 'scp target/myapp.jar ec2-user@production-instance:/path/to/deploy'
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
            mail to: 'qwertyorg2@gmail.com',
                 subject: "Pipeline : ${currentBuild.result}: ${currentBuild.fullDisplayName}",
                 body: "The pipeline status is ${currentBuild.result}. Attached the Jenkins console for details.\n.\n. ${currentBuild.rawBuild.getLog(1000).join("\n")}"
        }
    }
}

