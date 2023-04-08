pipeline {
	agent any;
	stages {
		stage('Code Quality') {
			steps {
				sh 'echo cheking code quality'
			}
		}
		stage('Unit tests') {
			steps {
				sh ' echo Testing the Aplications'
			}
		}
		stage('Build') {
			steps {
				sh 'echo Creando paquete de aplicaciones'
			}
		}	
		stage('Delivery') {
			steps {
				sh 'echo Actualizando el artefacto al repositorio'
			}
		}
		stage('Deploy') {
			steps {
				sh 'echo Desplegando la aplicación'
			}
		}
	}
}
