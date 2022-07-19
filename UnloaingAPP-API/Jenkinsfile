
pipeline{
	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub')
		REMOTE_IP=credentials('unloading-app-server-ip')
		ANSIBLE_HOST_KEY_CHECKING="False"
		DJANGO_DEBUG="FALSE"
		DATABASE_CREDENTIALS=credentials('unloading-app-database')
	}

	stages {
		stage('Build') {
			steps {
				sh 'docker build -t jenneron/unloading-app:latest .'
			}
		}

		stage('Login to Docker Hub') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {
			steps {
				sh 'docker push jenneron/unloading-app:latest'
			}
		}

		stage('Deploy with ansible') {
			steps {
				withCredentials([sshUserPrivateKey(credentialsId: "unloading-app-server-key", usernameVariable: "REMOTE_USER", keyFileVariable: 'REMOTE_KEY_FILE')]) {
					sh 'echo "[unloading-app]\nserver ansible_host=$REMOTE_IP ansible_user=$REMOTE_USER django_debug=$DJANGO_DEBUG database_user=$DATABASE_CREDENTIALS_USR database_password=$DATABASE_CREDENTIALS_PSW" > hosts.ini'
					sh 'ansible-playbook -i hosts.ini --private-key $REMOTE_KEY_FILE deploy.yml'
				}
			}
		}
	}

	post {
		always {
			sh 'rm hosts.ini'
			sh 'docker logout'
		}
	}
}
