# Retail Store Microservices Application

## Overview
A cloud-native e-commerce platform built with 5 containerized microservices, orchestrated using Kubernetes. Demonstrates modern DevOps practices including CI/CD readiness, horizontal autoscaling, and centralized configuration.

## Architecture
### Microservices
| Service           | Tech Stack      | Port | Description                          | Docker Image                     |
|-------------------|----------------|------|--------------------------------------|----------------------------------|
| Product           | Python/Flask   | 5001 | Product catalog management           | yourprofilename/product-service:latest   |
| Order             | Python/Flask   | 5002 | Order processing system              | yourprofilename/order-service:latest     |
| User              | Python/Flask   | 5003 | Customer account management          | yourprofilename/user-service:latest      |
| Inventory         | Python/Flask   | 5005 | Real-time stock tracking             | yourprofilename/inventory-service:latest |
| Recommendation    | Python/Flask   | 5003 | Personalized suggestions             | yourprofilename/recommendation-service:latest |

### Kubernetes Components
- **Ingress**: Routes traffic to services via `retail.algonquin.com`
- **Horizontal Pod Autoscaler**: Auto-scales Product and Order services
- **Health Checks**: Readiness probes on `/health` endpoint
- **Service Discovery**: Internal DNS-based communication

## Prerequisites
- Docker 20.10+
- Kubernetes cluster (Minikube v1.25+ or cloud provider)
- kubectl 1.24+
- Python 3.9+ (for Flask services)

## Deployment
### 1. Build and Push Images
```bash
docker build -t yourprofilename/product-service:latest ./product-service
docker push yourprofilename/product-service:latest
# Repeat for other services
```

### 2. Apply Kubernetes Manifests
```bash
kubectl apply -f product-service.yaml
kubectl apply -f order-service.yaml
kubectl apply -f user-service.yaml
kubectl apply -f inventory-service.yaml
kubectl apply -f recommendation-service.yaml
kubectl apply -f ingress.yaml
kubectl apply -f product-hpa.yaml
kubectl apply -f order-hpa.yaml
```

### 3. Verify Deployment
```bash
kubectl get all -n retail
kubectl get ingress -n retail
```

## API Endpoints
| Service       | Path               | Method | Description                  |
|---------------|--------------------|--------|------------------------------|
| Product       | /product           | GET    | Get product catalog          |
| Order         | /order             | POST   | Create new order             |
| User          | /user/{id}         | GET    | Get user details             |
| Inventory     | /inventory/{id}    | GET    | Check product stock          |
| Recommendation| /recommendation    | GET    | Get product recommendations  |

## Health Checks
All services expose a health endpoint:
```bash
curl http://retail.algonquin.com/product/health
```

## Troubleshooting
1. **CrashLoopBackOff**:
   ```bash
   kubectl logs <pod-name> -n retail --previous
   ```

2. **Ingress 404 Errors**:
   - Verify hostname resolution
   - Check rewrite-target annotation

3. **HPA Not Scaling**:
   ```bash
   kubectl describe hpa -n retail
   kubectl top pods -n retail
   ```
## License
MIT License - See LICENSE file for details

**Note**: For local development, add to your `/etc/hosts`:
```
<minikube-ip> retail.algonquin.com
```
