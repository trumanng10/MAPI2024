To access a Kubernetes cluster on **DigitalOcean**, follow these steps:

### 1. **Create a Kubernetes Cluster on DigitalOcean**
If you haven’t already created a Kubernetes cluster on DigitalOcean, follow these steps:

1. **Log in to DigitalOcean**: Sign in to your DigitalOcean account. If you don’t have one, [create a DigitalOcean account](https://www.digitalocean.com/).
2. **Navigate to Kubernetes**: Once logged in, go to the **Kubernetes** section from the DigitalOcean dashboard.
3. **Create a Cluster**:
   - Click **Create Cluster**.
   - Choose the **Kubernetes version** (the latest stable version is recommended).
   - Select the **Region** for your cluster.
   - Choose the **Cluster size** based on your use case.
   - Specify any additional settings like enabling backups or monitoring.
   - Click **Create Cluster**.

Once the cluster is created, you will be able to manage it through the DigitalOcean dashboard or using `kubectl`.

### 2. **Download `kubectl` (DigitalOcean CLI)**
`doctl` is the DigitalOcean command-line tool used to manage DigitalOcean resources from the terminal.

1. **Verify the kubeconfig**:
   After running the command, your kubeconfig file is automatically saved, and you can check it using:

   ```bash
   cat ~/.kube/config
   ```

   Make sure the file contains the context for your DigitalOcean Kubernetes cluster.


### 3. **Verify Access to the Kubernetes Cluster**
Once the `kubectl` is installed and configured, you can verify if you're able to connect to the Kubernetes cluster.

1. Run the following command to check the cluster status:

   ```bash
   kubectl get nodes
   ```

   This should display the nodes in your Kubernetes cluster.

2. You can also check the Kubernetes context to confirm that you're connected to the right cluster:

   ```bash
   kubectl config current-context
   ```

### 4. **Access the Kubernetes Dashboard (Optional)**
To access the Kubernetes Dashboard, which provides a web-based user interface for managing your cluster, follow these steps:

1. **Enable the Kubernetes Dashboard**:
   If the Kubernetes Dashboard is not installed, you can install it by running the following:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/recommended.yaml
   ```

2. **Create a Service Account**:

   Create a `dashboard-admin-user` for access:

   ```bash
   kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/master/aio/deploy/alternative.yaml
   ```

   Then, create the necessary `ClusterRoleBinding`:

   ```bash
   kubectl create clusterrolebinding dashboard-admin-user \
     --clusterrole=cluster-admin \
     --serviceaccount=kubernetes-dashboard:kubernetes-dashboard
   ```

3. **Access the Dashboard via `kubectl proxy`**:

   To access the dashboard locally, run:

   ```bash
   kubectl proxy
   ```

   This will allow you to access the dashboard via:

   ```bash
   http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/
   ```

### 5. **Deploy Applications to the Cluster**
You can now deploy applications to the DigitalOcean Kubernetes cluster using `kubectl` or Helm.

Example for deploying an application (e.g., NGINX):

1. Create Namespace:
     ```bash
   kubectl create namespace <your_name>
   kubectl get pods --namespace=<your_name>
     ```
2. Access to the Namespace:
     ```bash
   kubectl config set-context --current --namespace=<your_name>
      ```
     
3. Create a deployment YAML file `nginx-deployment.yaml`:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx
   spec:
     replicas: 3
     selector:
       matchLabels:
         app: nginx
     template:
       metadata:
         labels:
           app: nginx
       spec:
         containers:
         - name: nginx
           image: nginx
           ports:
           - containerPort: 80
   ```

5. Apply the YAML file to your cluster:

   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

6. Expose the deployment as a service:

   ```bash
   kubectl expose deployment nginx --port=80 --type=LoadBalancer
   ```

   Once exposed, you can find the external IP with:

   ```bash
   kubectl get svc
   ```
      ```bash
   kubectl describe svc nginx
   ```
      ```bash
   kubectl get deploy
   ```
         ```bash
   kubectl get pod
   ```

### 7. **Monitor and Manage Your Cluster**
You can manage and monitor your Kubernetes cluster directly via `kubectl`, Portainer, or using the DigitalOcean Dashboard. The Kubernetes Dashboard provides a UI for managing applications, viewing cluster health, and accessing logs.


