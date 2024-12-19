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

### 2. **Install `doctl` (DigitalOcean CLI)**
`doctl` is the DigitalOcean command-line tool used to manage DigitalOcean resources from the terminal.

1. **Install `doctl`**:
   - For **macOS** using Homebrew:

     ```bash
     brew install doctl
     ```

   - For **Linux**, you can install using the following command:

     ```bash
     snap install doctl
     ```

   - For **Windows**, you can use `choco`:

     ```bash
     choco install doctl
     ```

2. **Authenticate `doctl`**:
   - Run the following command to authenticate:

     ```bash
     doctl auth init
     ```

   - This will prompt you to enter your DigitalOcean API token. You can find or create your API token from [here](https://cloud.digitalocean.com/account/api/tokens).

### 3. **Get Kubernetes Cluster Config File**
After the cluster is created, you need to retrieve the **kubeconfig** file to access and manage the cluster.

1. **Get kubeconfig for your cluster**:
   Run the following command to download the kubeconfig file for your cluster:

   ```bash
   doctl kubernetes cluster kubeconfig save <cluster-name>
   ```

   Replace `<cluster-name>` with the name of your Kubernetes cluster. This will configure your `kubectl` to interact with your Kubernetes cluster.

2. **Verify the kubeconfig**:
   After running the command, your kubeconfig file is automatically saved, and you can check it using:

   ```bash
   cat ~/.kube/config
   ```

   Make sure the file contains the context for your DigitalOcean Kubernetes cluster.

### 4. **Install `kubectl`**
`kubectl` is the command-line tool to interact with Kubernetes clusters.

- **Install `kubectl`**:
   - For **macOS**:

     ```bash
     brew install kubectl
     ```

   - For **Linux**:

     ```bash
     curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
     chmod +x ./kubectl
     sudo mv ./kubectl /usr/local/bin/kubectl
     ```

   - For **Windows**, use `choco`:

     ```bash
     choco install kubernetes-cli
     ```

### 5. **Verify Access to the Kubernetes Cluster**
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

### 6. **Access the Kubernetes Dashboard (Optional)**
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

### 7. **Deploy Applications to the Cluster**
You can now deploy applications to the DigitalOcean Kubernetes cluster using `kubectl` or Helm.

Example for deploying an application (e.g., NGINX):

1. Create a deployment YAML file `nginx-deployment.yaml`:

   ```yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx
   spec:
     replicas: 2
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

2. Apply the YAML file to your cluster:

   ```bash
   kubectl apply -f nginx-deployment.yaml
   ```

3. Expose the deployment as a service:

   ```bash
   kubectl expose deployment nginx --port=80 --type=LoadBalancer
   ```

   Once exposed, you can find the external IP with:

   ```bash
   kubectl get svc
   ```

### 8. **Monitor and Manage Your Cluster**
You can manage and monitor your Kubernetes cluster directly via `kubectl`, Portainer, or using the DigitalOcean Dashboard. The Kubernetes Dashboard provides a UI for managing applications, viewing cluster health, and accessing logs.

---

### Summary:
By following these steps, you'll be able to access and manage your Kubernetes cluster on DigitalOcean:
1. Create a cluster on DigitalOcean.
2. Install and configure `doctl` and `kubectl`.
3. Get the kubeconfig and test the cluster access.
4. Optionally, set up the Kubernetes Dashboard for easier cluster management.
5. Deploy applications and services using `kubectl`.

Let me know if you need further details on any step!
