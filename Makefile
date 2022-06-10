################################## BUILD ################################## 

################################## CREATE INFRA ################################## 

create-ecr:
	aws cloudformation deploy \
              --template-file deployment/cfn/ecr.yml \
              --tags project=flaskServer_k8s \
              --region us-east-2 \
              --stack-name "flaskServer" \
              --parameter-overrides RegistryName="flask-server"
    
connect-eks:
	aws --version
	
################################## DEPLOY################################## 	
create-deployment: 
	kubectl apply -f deployment/k8s/flaskServer.yml
create-service:
	kubectl apply -f deployment/k8s/service.yml
	
create-all-resources: create-deployment create-service

get-backend-service-dns:
	API_URL=${kubectl get service -o=jsonpath='{.items[?(@.metadata.name=="capstone-backend")].status.loadBalancer.ingress[0].hostname}'}
	export API_URL