pipeline {
	agent any;
	stages {
		stage('Preparando entorno') {
			steps {
				sh 'python -m pip install -r requeriments.txt'
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
			steps {
				sh 'exit 1'
			}
		}	
		stage('Delivery') {
			steps {
				sh 'exit 1'
			}
		}
		stage('Deploy') {
			steps {
				sh 'exit 1'
			}
		}
	}
}
