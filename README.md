# **Itau SRE Case - CatsAPI**

## **Overview**

### **Stack**
The solution is based on the following technology stack:

- Language and related
  - Python3 as language
  - Peewee as ORM framework
  - Flask as web framework
  - APScheduler as scheduler
  - Postman Collection for API Testing

- Infrastructure and related
  - MySQL8x as database
  - Kubernetes as container scheduler
  - Docker as container runtime
  - Prometheus as metric collector (running inside the same k8s cluster for demonstration)
  - Grafana as metric browser/dashboards (running inside the same k8s cluster for demonstration)
  - EFK stack as log centralizer and visualization (running inside the same k8s cluster for demonstration)
  - Terraform as IAC for K8S Bootstrap on DigitalOcean.
  - Bash for K8S Bootstrap on DigitalOcean (Addons Installation)

- Local Development
  - Docker Compose 

- CI/CD
  - CircleCI for app CI/CD

- Nice to Have
  - WSGI Server
  - Skaffold
  - Minikube
  - Kubectl

---
### **Application**

#### **Database**


#### **syncronizer_job**

#### **api**

