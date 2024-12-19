To install **Portainer** on Docker, follow these steps:

### 1. **Ensure Docker is Installed**
Before installing Portainer, make sure Docker is installed and running on your machine. If you haven't already installed Docker, you can follow the official installation guides for your OS:

- [Install Docker on Linux](https://docs.docker.com/engine/install/)
- [Install Docker on Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Install Docker on Mac](https://docs.docker.com/desktop/install/mac-install/)

### 2. **Pull the Portainer Image**
To install Portainer, you need to pull the Portainer image from Docker Hub.

Open a terminal (or command prompt) and run:

```bash
docker pull portainer/portainer-ce:latest
```

This command will pull the latest version of Portainer Community Edition (Portainer CE).

### 3. **Create a Portainer Data Volume**
It’s a good practice to store Portainer data in a named Docker volume. This ensures that data is persistent, even if you remove the container.

```bash
docker volume create portainer_data
```

### 4. **Run Portainer as a Docker Container**
Now that you've pulled the Portainer image and created a volume, you can run Portainer in a Docker container. Use the following command to start Portainer:

```bash
docker run -d \
  -p 9000:9000 \
  -p 9443:9443 \
  --name portainer \
  --restart always \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest
```

### Explanation of the Command:
- `-d`: Run the container in detached mode.
- `-p 9000:9000`: Expose Portainer's web UI on port 9000.
- `-p 9443:9443`: Expose Portainer’s web UI for HTTPS access on port 9443 (optional).
- `--name portainer`: Assign the container the name `portainer`.
- `--restart always`: Ensure Portainer restarts automatically if the Docker daemon is restarted or if the container crashes.
- `-v /var/run/docker.sock:/var/run/docker.sock`: Mount the Docker socket to allow Portainer to communicate with Docker.
- `-v portainer_data:/data`: Mount the volume to persist Portainer’s configuration and data.
- `portainer/portainer-ce:latest`: The name of the Docker image to use (Portainer Community Edition).

### 5. **Access the Portainer Web UI**
Once the container is running, you can access the Portainer web UI by visiting:

- **HTTP**: `http://<IP_Addr>:9000`
- **HTTPS** (if you mapped port 9443): `https://<IP_Addr>:9443`

### 6. **Setup Portainer**
When you access Portainer for the first time, you will be prompted to create an admin user. After that, you can connect Portainer to your Docker environment.

### 7. **Managing Docker with Portainer**
Once Portainer is up and running, you can:
- View Docker containers, images, volumes, networks, etc.
- Start, stop, and manage containers.
- Access logs and console for each container.
- Manage Docker Swarm clusters (if applicable).

---

### **Stopping and Removing Portainer**

If you need to stop the Portainer container, you can run:

```bash
docker stop portainer
```

To remove the Portainer container:

```bash
docker rm portainer
```

To remove the Portainer image:

```bash
docker rmi portainer/portainer-ce:latest
```

That's it! Portainer should now be running on your Docker environment. Let me know if you need further assistance.
