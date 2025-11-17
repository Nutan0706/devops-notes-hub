# 🚀 **KUBECTL CHEATSHEET (50+ Commands)**

---

# 🔹 **1. Basic Cluster Info**

```sh
kubectl version
kubectl cluster-info
kubectl get nodes
kubectl describe node <node>
kubectl top nodes
```

---

# 🔹 **2. Get Resources (Most Used)**

```sh
kubectl get pods
kubectl get pods -o wide
kubectl get deployments
kubectl get rs
kubectl get svc
kubectl get ing
kubectl get configmaps
kubectl get secrets
kubectl get pv
kubectl get pvc
kubectl get ns
kubectl get all
```

---

# 🔹 **3. Describe Resources**

```sh
kubectl describe pod <pod>
kubectl describe deployment <deploy>
kubectl describe svc <svc>
kubectl describe node <node>
```

---

# 🔹 **4. Logs (Debugging)**

```sh
kubectl logs <pod>
kubectl logs <pod> -f
kubectl logs <pod> -c <container>
kubectl logs --previous <pod>
```

---

# 🔹 **5. Exec (Enter Pod)**

```sh
kubectl exec -it <pod> -- bash
kubectl exec -it <pod> -- sh
kubectl exec <pod> -- ls /
```

---

# 🔹 **6. Apply / Create**

```sh
kubectl apply -f <file>.yaml
kubectl apply -f k8s/

kubectl create -f <file>.yaml
kubectl create namespace my-namespace
kubectl create deployment nginx --image=nginx
```

---

# 🔹 **7. Edit Resources**

```sh
kubectl edit deployment <deploy>
kubectl edit svc <svc>
kubectl edit configmap <cm>
```

---

# 🔹 **8. Delete Resources**

```sh
kubectl delete pod <pod>
kubectl delete deployment <deploy>
kubectl delete svc <svc>
kubectl delete ns <namespace>
kubectl delete -f <file>.yaml
kubectl delete all --all   # Delete all resources
```

---

# 🔹 **9. Namespace Commands**

```sh
kubectl get ns
kubectl create ns dev
kubectl delete ns dev
kubectl config set-context --current --namespace=dev
```

---

# 🔹 **10. Resource Usage**

```sh
kubectl top pods
kubectl top nodes
```

---

# 🔹 **11. Rollout (Deployment Management)**

```sh
kubectl rollout status deployment <deploy>
kubectl rollout history deployment <deploy>
kubectl rollout undo deployment <deploy>
kubectl rollout restart deployment <deploy>
```

---

# 🔹 **12. Scale**

```sh
kubectl scale deployment <deploy> --replicas=5
kubectl scale rs <rs> --replicas=2
```

---

# 🔹 **13. Port Forwarding**

```sh
kubectl port-forward <pod> 8080:80
kubectl port-forward svc/my-svc 3000:80
```

---

# 🔹 **14. Expose Resources**

```sh
kubectl expose deployment nginx --port=80 --type=NodePort
kubectl expose pod mypod --port=8080
```

---

# 🔹 **15. Restart / Refresh**

```sh
kubectl rollout restart deployment <deploy>
kubectl delete pod <pod>   # force recreate
```

---

# 🔹 **16. Copy Files**

```sh
kubectl cp <pod>:/path/to/file /local/path
kubectl cp /local/file <pod>:/path/
```

---

# 🔹 **17. Config & Context Management**

```sh
kubectl config view
kubectl config get-contexts
kubectl config current-context
kubectl config use-context <context>
kubectl config set-context --current --namespace=dev
```

---

# 🔹 **18. Dry Run (Preview Changes)**

```sh
kubectl apply -f deploy.yaml --dry-run=client -o yaml
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml
```

---

# 🔹 **19. Labels & Annotations**

```sh
kubectl get pods --show-labels
kubectl label pod <pod> env=dev
kubectl annotate pod <pod> description="test pod"
```

---

# 🔹 **20. Taints & Tolerations**

```sh
kubectl taint nodes node1 key=value:NoSchedule
kubectl taint nodes node1 key=value:NoSchedule-
```

---

# 🔹 **21. Events (Debug)**

```sh
kubectl get events --sort-by=.metadata.creationTimestamp
```

---

# 🔹 **22. Apply Kustomize**

```sh
kubectl apply -k ./kustomize-dir/
```

---

# 🔹 **23. Autoscaling**

```sh
kubectl autoscale deployment <deploy> --min=2 --max=10 --cpu-percent=80
```

---

# 🔹 **24. Resource YAML Output**

```sh
kubectl get pod <pod> -o yaml
kubectl get deploy <deploy> -o json
```

---

# 🔹 **25. Debug Pod (Ephemeral Container)**

```sh
kubectl debug <pod> -it --image=busybox
```

