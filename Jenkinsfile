pipeline {
	agent any;
	stages {
		stage('Preparando entorno') {
			steps {
				sh 'python -m pip install -r requirements.txt'
			}
		}	
		stage('Calidad de código') {
			steps {
				sh 'python -m pylint app.py'
			}
		}
		stage('test unitario') {
			steps {
				sh 'python -m pytest'
			}
		}
		stage('Build') {
			agent {
				node {
					label "dcokerserver";
				}
			}	
			steps {
				sh 'docker build https://github.com/AlissonMMenezes/Chapter10.git -t chapter10:latest'
			}
		}	
		stage('Deploy') {
			agent {
				node {
					label "dcokerserver";
				}
			}	
			steps {
				sh 'docker run -tdi -p 5000:5000 chapter10:latest'
			}
		}
	}
}
