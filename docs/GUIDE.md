# Getting Started with Docker: A Complete Beginner's Guide

## Table of Contents

1. [Introduction](#introduction)
2. [What is Docker?](#what-is-docker)
3. [System Requirements](#system-requirements)
4. [Installation](#installation)
5. [Your First Container](#your-first-container)
6. [Building Your Own Container](#building-your-own-container)
7. [Common Issues & Solutions](#common-issues--solutions)
8. [AI Learning Journey](#ai-learning-journey)
9. [Next Steps](#next-steps)
10. [References](#references)

---

## Introduction

### What Technology Did I Choose?

Docker - a containerization platform that packages applications with all their dependencies into portable, isolated containers.

### Why Did I Choose Docker?

After reviewing job postings in the software development field, I noticed Docker appeared in over 70% of DevOps and backend engineer positions. I was tired of the "it works on my machine" problem and wanted to understand how modern companies deploy applications consistently across different environments. Docker is the industry standard for containerization and a foundational skill for cloud-native development.

### What's the End Goal?

By the end of this guide, you'll be able to:
- Understand what Docker is and why developers use it
- Install Docker on Ubuntu Linux
- Run pre-built containers from Docker Hub
- Create your own Python Flask application
- Write a Dockerfile to containerize your app
- Build Docker images and run containers
- Troubleshoot common Docker errors
- Deploy a working web application in a container

**Estimated time to complete:** 2-3 hours

**Difficulty level:** Beginner-friendly (basic command line knowledge required)

---

## What is Docker?

### The Simple Explanation

Docker is like a shipping container for software. Just as shipping containers revolutionized global trade by standardizing how goods are transported (any container can go on any ship, truck, or train), Docker standardizes how software is packaged and deployed.

A Docker container packages your application code, runtime environment, system tools, libraries, and settings into a single, portable unit. This container runs identically on your laptop, your colleague's computer, a testing server, and production servers in the cloud.

### The Problem Docker Solves

#### The "Works On My Machine" Nightmare

Every developer has experienced this:

**Scenario without Docker:**
```
You (Developer): "My Python app works perfectly on my laptop!"
Colleague: "It crashes on my machine... missing dependencies"
QA Team: "Tests fail - different Python version"
Production Server: "Application won't start - library conflict"
```

**Why this happens:**
- You have Python 3.11, production has Python 3.8
- Different versions of Flask, NumPy, or other libraries
- Missing system packages (libpq-dev, gcc, etc.)
- Different operating systems (you use Ubuntu, server uses CentOS)
- Environment variables configured differently
- File paths that don't exist on other systems

**Hours (or days) wasted debugging environmental differences instead of writing code.**

#### Docker's Solution

**With Docker:**
```
You: "Here's my Docker container"
Colleague: *runs container* "Works perfectly!"
QA Team: *runs same container* "All tests pass!"
Production: *runs same container* "Running smoothly!"
```

Docker guarantees that your application runs the same way everywhere because:
- The exact Python version is in the container
- All libraries and dependencies are included
- System packages are pre-installed
- Configuration is baked in
- File structure is standardized

**"Build once, run anywhere"** - This is Docker's core promise.

### Real-World Examples

#### Netflix
- **Challenge:** 1000+ microservices deployed thousands of times daily
- **Docker Solution:** Each service runs in containers, ensuring consistent behavior
- **Result:** Rapid deployment with zero environmental surprises

#### Uber
- **Challenge:** Code works in staging but fails in production
- **Docker Solution:** Same container runs in all environments
- **Result:** Reliable deployments, faster time-to-market

#### PayPal
- **Challenge:** Deployment process took hours, high failure rate
- **Docker Solution:** Containerized applications with automated deployment
- **Result:** Deployment time reduced from hours to minutes

#### Spotify
- **Challenge:** Managing infrastructure for millions of users
- **Docker Solution:** Runs millions of containers across global data centers
- **Result:** Seamless scaling and consistent user experience

### Key Docker Concepts

#### 1. Docker Image (The Recipe)

A Docker image is a **blueprint** or **template** - a read-only package containing:
- Base operating system (usually minimal Linux)
- Your application code
- Runtime environment (Python, Node.js, Java, etc.)
- Libraries and dependencies
- Configuration files
- Commands to run

**Analogy:** Like a recipe card for baking a cake - it has all the instructions and ingredient lists, but it's not the actual cake.

**Example:** The `python:3.11-slim` image contains:
- Debian Linux (minimal)
- Python 3.11 pre-installed
- pip package manager
- Basic system utilities

#### 2. Docker Container (The Running Application)

A Docker container is a **running instance** of an image - it's your actual application executing in an isolated environment.

**Analogy:** The actual cake you baked from the recipe. You can bake multiple cakes from one recipe (run multiple containers from one image).

**Key properties:**
- Isolated from host system and other containers
- Has its own filesystem, network, and processes
- Lightweight (shares host OS kernel)
- Can be started, stopped, deleted, and recreated instantly

**Example:** Running `docker run python:3.11-slim` creates a container where you can execute Python code.

#### 3. Dockerfile (The Build Instructions)

A Dockerfile is a **text file with instructions** for building a Docker image. It's like a recipe written in a standardized format that Docker understands.

**Simple example:**
```dockerfile
FROM python:3.11-slim          # Start with Python image
WORKDIR /app                   # Create /app directory
COPY requirements.txt .        # Copy dependency list
RUN pip install -r requirements.txt  # Install dependencies
COPY app.py .                  # Copy application code
CMD ["python", "app.py"]       # Run the app
```

**Think of it as:** IKEA furniture assembly instructions - step-by-step commands to build your container.

#### 4. Docker Hub (The Image Library)

Docker Hub is a **public registry** where people share Docker images - like GitHub for containers.

**What you can find:**
- Official images (Python, Node.js, PostgreSQL, Redis, Nginx)
- Community images (thousands of pre-built applications)
- Your own private images

**Example:** Instead of manually installing Python, just use:
```bash
docker pull python:3.11
```

#### 5. The Docker Workflow
```
1. WRITE CODE
   ├── app.py (your Python application)
   └── requirements.txt (dependencies)

2. WRITE DOCKERFILE
   └── Instructions to package your app

3. BUILD IMAGE
   └── docker build -t my-app .
   └── Creates reusable template

4. RUN CONTAINER
   └── docker run my-app
   └── Your app is now running in isolation

5. DISTRIBUTE (optional)
   └── docker push my-app
   └── Share via Docker Hub or private registry
```

### Why Docker Matters for Your Career

**Job Market Impact:**
- 70%+ of DevOps positions require Docker
- Cloud platforms (AWS, Google Cloud, Azure) heavily use containers
- Kubernetes (container orchestration) requires Docker knowledge
- Modern development workflows assume containerization

**Skills Docker Teaches:**
- Understanding of networking and ports
- Linux system administration basics
- Application deployment strategies
- Infrastructure as Code concepts
- Microservices architecture

**The Bottom Line:** Docker is no longer optional - it's a fundamental skill for modern software development.

---

## System Requirements

### Operating System

**Supported (what this guide covers):**
- **Ubuntu 20.04 LTS or later** (recommended)
- Ubuntu 22.04 LTS
- Debian 11+
- Linux Mint 20+

**Also compatible (not covered in detail):**
- macOS 10.15 (Catalina) or later
- Windows 10/11 Pro, Enterprise, or Education (with WSL2)
- Fedora 36+
- CentOS/RHEL 8+

**Not supported:**
- Windows 10 Home (requires WSL2 setup)
- 32-bit operating systems
- macOS older than 10.15

### Hardware Requirements

**Minimum:**
- 4GB RAM (8GB recommended)
- 10GB free disk space
- 64-bit processor
- Virtualization support enabled in BIOS

**Recommended:**
- 8GB+ RAM (for running multiple containers)
- 20GB+ free disk space (images can be large)
- SSD for better performance
- Stable internet connection (for downloading images)

### Software Prerequisites

**Required:**
- Terminal/command line access
- Text editor (VS Code, nano, vim, or gedit)
- Basic command line knowledge
- `curl` (usually pre-installed on Ubuntu)

**For this guide specifically:**
- Python 3.8+ (for testing locally before Docker)
- pip (Python package manager)
- Git (for version control)

### Check Your System

Before installing Docker, verify your system meets requirements:

#### 1. Check Ubuntu Version
```bash
lsb_release -a
```

**Expected output:**
```
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

#### 2. Check Architecture (Must be 64-bit)
```bash
uname -m
```

**Expected output:**
```
x86_64   # This is 64-bit
```

**If you see `i686` or `i386`, your system is 32-bit and Docker won't work.**

#### 3. Check Available Disk Space
```bash
df -h /
```

**Expected output:**
```
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /
```

**You need at least 10GB in the "Avail" column.**

#### 4. Check RAM
```bash
free -h
```

**Expected output:**
```
              total        used        free
Mem:           7.7G        2.1G        3.2G
```

**Total should be 4GB or more.**

#### 5. Check if Virtualization is Enabled
```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```

**Expected output:**
```
4   # Any number greater than 0 is good
```

**If you get `0`:** Virtualization is disabled in BIOS. You'll need to:
1. Restart computer
2. Enter BIOS/UEFI settings (usually F2, F10, or Del key during boot)
3. Find "Virtualization Technology" or "VT-x" setting
4. Enable it
5. Save and reboot

---

## Installation

### Installation Steps for Ubuntu

Follow these steps carefully. Each command is explained so you understand what's happening.

#### Step 1: Update Package Index
```bash
sudo apt-get update
```

**What this does:** Updates the list of available packages and their versions. Always do this before installing new software.

**Expected output:**
```
Hit:1 http://us.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://us.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
...
Fetched 1,234 kB in 2s (567 kB/s)
Reading package lists... Done
```

#### Step 2: Install Prerequisites
```bash
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

**What this does:**
- `ca-certificates` - SSL certificates for secure downloads
- `curl` - Tool for downloading files from the internet
- `gnupg` - Encryption tool for verifying downloads
- `lsb-release` - Utility to identify your Ubuntu version

**The `-y` flag** automatically answers "yes" to installation prompts.

**Expected output:**
```
Reading package lists... Done
Building dependency tree... Done
ca-certificates is already the newest version
curl is already the newest version
...
```

#### Step 3: Add Docker's GPG Key
```bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```

**What this does:** Downloads Docker's security key to verify that packages actually come from Docker (not malicious sources).

**Breaking down the command:**
- `mkdir -p /etc/apt/keyrings` - Creates directory for storing keys
- `curl -fsSL` - Downloads the key silently
- `gpg --dearmor` - Converts the key to a format Ubuntu understands
- `> /etc/apt/keyrings/docker.gpg` - Saves it to the keyring directory

**No output means success!**

#### Step 4: Add Docker Repository
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**What this does:** Tells Ubuntu where to download Docker packages from.

**Breaking it down:**
- `dpkg --print-architecture` - Detects your system architecture (amd64, arm64, etc.)
- `lsb_release -cs` - Gets your Ubuntu codename (jammy, focal, etc.)
- `tee` - Writes to the Docker repository list file

**Expected output:**
```
(no output, but file is created)
```

**Verify it worked:**
```bash
cat /etc/apt/sources.list.d/docker.list
```

**You should see:**
```
deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu jammy stable
```

#### Step 5: Update Package Index Again
```bash
sudo apt-get update
```

**Why again?** Now that we've added Docker's repository, we need to fetch the list of Docker packages available.

**Expected output:**
```
Get:1 https://download.docker.com/linux/ubuntu jammy InRelease [48.9 kB]
Get:2 https://download.docker.com/linux/ubuntu jammy/stable amd64 Packages [24.8 kB]
...
```

#### Step 6: Install Docker Engine
```bash
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**What this installs:**
- `docker-ce` - Docker Community Edition (the main engine)
- `docker-ce-cli` - Command-line interface for Docker
- `containerd.io` - Container runtime (runs the containers)
- `docker-buildx-plugin` - Advanced build features
- `docker-compose-plugin` - Tool for multi-container apps

**Expected output:**
```
Reading package lists... Done
Building dependency tree... Done
The following NEW packages will be installed:
  containerd.io docker-buildx-plugin docker-ce docker-ce-cli docker-compose-plugin
...
Setting up docker-ce (5:24.0.7-1~ubuntu.22.04~jammy) ...
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service
```

**This will take 1-3 minutes to download and install.**

#### Step 7: Add Your User to Docker Group
```bash
sudo usermod -aG docker $USER
```

**What this does:** Adds your user account to the "docker" group, allowing you to run Docker commands without `sudo`.

**Why this matters:** 
- Without this: `sudo docker run hello-world` (tedious!)
- With this: `docker run hello-world` (convenient!)

**Breaking it down:**
- `usermod` - Modify user account
- `-aG` - Add to group (don't remove from other groups)
- `docker` - The group name
- `$USER` - Your current username

**No output means success!**

#### Step 8: Apply Group Changes

**Option 1: Quick method (works immediately)**
```bash
newgrp docker
```

**What this does:** Logs you into the docker group in the current session.

**Option 2: Complete method (recommended)**
```bash
# Log out and log back in
# Or restart your terminal
```

**Why?** Group changes don't take effect until you start a new session.

### Verify Installation

Now let's confirm everything works!

#### Test 1: Check Docker Version
```bash
docker --version
```

**Expected output:**
```
Docker version 24.0.7, build afdd53b
```

**If you see this, Docker is installed!**

#### Test 2: Check Docker Service Status
```bash
sudo systemctl status docker
```

**Expected output:**
```
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled; vendor preset: enabled)
     Active: active (running) since Tue 2024-12-17 10:30:15 EAT; 5min ago
TriggeredBy: ● docker.socket
       Docs: https://docs.docker.com
   Main PID: 12345 (dockerd)
      Tasks: 8
     Memory: 45.2M
        CPU: 234ms
     CGroup: /system.slice/docker.service
             └─12345 /usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock
```

**Key thing to look for:** `Active: active (running)` in green text.

**If it says "inactive" or "failed":**
```bash
sudo systemctl start docker
sudo systemctl enable docker
```

#### Test 3: Run Hello World Container
```bash
docker run hello-world
```

**What this does:**
1. Looks for "hello-world" image locally
2. Doesn't find it, so downloads from Docker Hub
3. Creates a container from the image
4. Runs the container (which prints a message)
5. Container exits

**Expected output:**
```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:4bd78111b6914a99dbc560e6a20eab57ff6655aea4a80c50b0c5491968cbc2e6
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

**If you see "Hello from Docker!" - your installation is complete!**

#### Test 4: Verify Permissions (No Sudo Needed)
```bash
docker ps
```

**Expected output:**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**Empty list is fine!** The important part is that the command worked without `sudo`.

**If you get "permission denied":**
```bash
sudo usermod -aG docker $USER
newgrp docker
# Or log out and log back in
```

### Installation Troubleshooting

#### Issue 1: "Cannot connect to the Docker daemon"

**Full error:**
```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

**Cause:** Docker service isn't started.

**Solution:**
```bash
# Start Docker
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Verify it's running
sudo systemctl status docker
```

**Check the output shows `active (running)`.**

#### Issue 2: "Got permission denied"

**Full error:**
```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
```

**Cause:** Your user isn't in the docker group, or group changes haven't taken effect.

**Solution:**
```bash
# Add user to docker group
sudo usermod -aG docker $USER

# Method 1: Quick (apply in current shell)
newgrp docker

# Method 2: Complete (log out and back in)
# Close terminal and open new one
# OR logout of your desktop session and login again
```

**Verify it worked:**
```bash
groups
# Should show "docker" in the list
```

**Test:**
```bash
docker run hello-world
# Should work without sudo
```

#### Issue 3: "Package 'docker-ce' has no installation candidate"

**Cause:** Docker repository wasn't added correctly or Ubuntu version is too old.

**Solution 1: Re-add repository**
```bash
# Remove old repo file if exists
sudo rm /etc/apt/sources.list.d/docker.list

# Re-add repository (run Steps 3-5 again)
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```

**Solution 2: Check Ubuntu version**
```bash
lsb_release -a
# Docker supports Ubuntu 20.04+
```

#### Issue 4: "E: Unable to locate package docker-ce"

**Cause:** Package list wasn't updated after adding Docker repository.

**Solution:**
```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io
```

#### Issue 5: "curl: command not found"

**Cause:** curl isn't installed (rare on modern Ubuntu).

**Solution:**
```bash
sudo apt-get update
sudo apt-get install -y curl

# Then re-run Step 3
```

#### Issue 6: Firewall Blocking Docker

**Symptom:** Docker installed but can't pull images.

**Check firewall:**
```bash
sudo ufw status
```

**If active, allow Docker:**
```bash
sudo ufw allow 2375/tcp
sudo ufw allow 2376/tcp
sudo ufw reload
```

#### Issue 7: Old Docker Installation Conflicts

**Symptom:** Errors about conflicting packages.

**Solution: Remove old Docker first**
```bash
# Remove old Docker versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Remove old configuration
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd

# Now install fresh (run Steps 1-6 again)
```

### Post-Installation Configuration

#### Optional: Configure Docker to Start on Boot
```bash
sudo systemctl enable docker
sudo systemctl enable containerd
```

#### Optional: Set Docker to Use Different Storage Location

**If /var/lib/docker doesn't have enough space:**
```bash
# Stop Docker
sudo systemctl stop docker

# Create new location
sudo mkdir -p /home/docker-data

# Edit Docker configuration
sudo nano /etc/docker/daemon.json
```

**Add this content:**
```json
{
  "data-root": "/home/docker-data"
}
```

**Save (Ctrl+X, Y, Enter)**
```bash
# Restart Docker
sudo systemctl start docker

# Verify new location
docker info | grep "Docker Root Dir"
```

### Installation Complete! 

**You now have:**
- Docker Engine installed
- Docker CLI working
- Permissions configured correctly
- hello-world container tested successfully

**Next step:** Let's run some pre-built containers to understand how Docker works before building our own!

---

## Your First Container

Now that Docker is installed, let's run some containers to understand how they work!

### Understanding docker run

The `docker run` command is your primary tool for starting containers. Here's the basic syntax:
```bash
docker run [OPTIONS] IMAGE [COMMAND]
```

**Key options you'll use:**
- `-d` - Run in detached mode (background)
- `-p` - Publish ports (map container port to host port)
- `--name` - Give container a friendly name
- `-e` - Set environment variables
- `-v` - Mount volumes (persistent storage)
- `--rm` - Automatically remove container when it stops
- `-it` - Interactive terminal (for shells)

### Example 1: Run Nginx Web Server

Nginx is a popular web server. Let's run it in a container!
```bash
docker run -d -p 8080:80 --name my-nginx nginx
```

**Breaking down this command:**
- `docker run` - Create and start a container
- `-d` - Detached mode (runs in background)
- `-p 8080:80` - Map port 80 in container to port 8080 on your machine
- `--name my-nginx` - Name the container "my-nginx"
- `nginx` - The image to use (downloads from Docker Hub if needed)

**What happens:**
1. Docker looks for nginx image locally
2. Doesn't find it, downloads from Docker Hub
3. Creates a container from the image
4. Starts nginx web server inside
5. Maps port 80 (inside) to 8080 (outside)
6. Returns container ID and goes to background

**Expected output:**
```
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
a2abf6c4d29d: Pull complete 
...
Digest: sha256:4c0fdaa8b6341bfdeca5f18f7837462c80cff90527ee35ef185571e1c327beac
Status: Downloaded newer image for nginx:latest
9a8c3f5d6b2e4f1a7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
```

**Test it:**
Open your browser and go to: **http://localhost:8080**

You should see the **"Welcome to nginx!"** page! 

### Check Running Containers

docker ps


**Expected output:**
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                  NAMES
9a8c3f5d6b2e   nginx     "/docker-entrypoint.…"   30 seconds ago   Up 29 seconds   0.0.0.0:8080->80/tcp   my-nginx

**Understanding this output:**
- **CONTAINER ID** - Short ID for this container
- **IMAGE** - Image used to create it
- **COMMAND** - Command running inside container
CREATED - When container was created
STATUS - Current state (Up = running)
PORTS - Port mapping (0.0.0.0:8080->80/tcp means all interfaces on port 8080 map to container port 80)
NAMES - Container name

Stop the Container
- docker stop my-nginx
```

**Expected output:**
```
my-nginx
Verify it stopped:
- docker ps
# Shows nothing (no running containers)

docker ps -a
# Shows all containers (including stopped ones)
Start it Again
- docker start my-nginx
Container is now running again! Check browser: http://localhost:8080
View Container Logs
docker logs my-nginx
```

**Expected output:**
```
/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
...
2024/12/17 10:45:23 [notice] 1#1: nginx/1.25.3
2024/12/17 10:45:23 [notice] 1#1: start worker processes
View logs in real-time:
- docker logs -f my-nginx
# Press Ctrl+C to stop following
Execute Commands Inside Container
docker exec -it my-nginx bash
```

**What this does:** Opens an interactive bash shell inside the running container!

**You're now INSIDE the container! Your prompt changes to:**
```
root@9a8c3f5d6b2e:/#
Try some commands:
# See what's running
ps aux

# Check nginx configuration
cat /etc/nginx/nginx.conf

# See web files
ls /usr/share/nginx/html/

# Exit container
exit
Remove the Container
# Stop first
docker stop my-nginx

# Remove
docker rm my-nginx
Verify it's gone:
docker ps -a
# Should not show my-nginx
Example 2: Run Ubuntu Container
Let's run an Ubuntu container with an interactive shell:

docker run -it --rm ubuntu bash

Breaking it down:

-it - Interactive terminal (keep STDIN open + allocate TTY)
--rm - Automatically remove container when it exits
ubuntu - Official Ubuntu image
- Command to run (open bash shell)

You're now in an Ubuntu environment!
# Check Ubuntu version
cat /etc/os-release

# Update package list
apt-get update

# Install something
apt-get install -y curl

# Use it
curl https://httpbin.org/ip

# Exit (container will be auto-removed due to --rm)
exit
Example 3: Run Python Container
docker run -it --rm python:3.11 python
Opens Python REPL inside container:
python>>> print("Hello from Docker!")
Hello from Docker!

>>> import sys
>>> sys.version
'3.11.7 (main, Dec  8 2023, 14:22:46) [GCC 12.2.0]'

>>> exit()
Useful Docker Commands
- List all containers (including stopped)
docker ps -a
- List all images
docker images
- Remove an image
docker rmi nginx
- Remove all stopped containers
docker container prune
- Remove all unused images
docker image prune -a
- Get detailed info about container
docker inspect my-nginx
- View container resource usage
docker stats
- Copy file from container to host
docker cp my-nginx:/etc/nginx/nginx.conf ./nginx.conf
- Copy file from host to container
docker cp ./myfile.txt my-nginx:/tmp/
- Understanding Port Mapping
Port mapping is critical for accessing containerized applications.
Format: -p HOST_PORT:CONTAINER_PORT
Examples:
# Map container port 80 to host port 8080
docker run -d -p 8080:80 nginx
# Access at: http://localhost:8080

# Map container port 5000 to host port 5000
docker run -d -p 5000:5000 my-flask-app
# Access at: http://localhost:5000

# Map to random available port
docker run -d -P nginx
# Docker chooses available port (check with docker ps)

# Map multiple ports
docker run -d -p 8080:80 -p 4443:443 nginx
# HTTP on 8080, HTTPS on 4443
```

**Why port mapping matters:**
- Containers have their own network namespace
- Without mapping, container ports aren't accessible from host
- Multiple containers can use same internal port (80) mapped to different host ports (8080, 8081, 8082)

### Key Takeaways

**You've learned:**
- How to run containers with `docker run`
- Detached mode (`-d`) vs interactive (`-it`)
- Port mapping with `-p`
- Viewing running containers with `docker ps`
- Stopping, starting, and removing containers
- Viewing logs with `docker logs`
- Executing commands inside containers with `docker exec`
- Auto-cleanup with `--rm`

**Next:** Let's build our own container!

---

## Building Your Own Container

Now for the exciting part - creating your own Dockerized application!

### The Application: Flask Web App

We'll build a simple but visually appealing Flask web application that demonstrates Docker's power.

### Project Structure
```
example-app/
├── app.py           # Flask application
├── requirements.txt # Python dependencies
├── Dockerfile       # Docker build instructions
└── README.md        # Documentation
Step 1: Create the Flask Application
File: example-app/app.py
pythonfrom flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    hostname = os.uname().nodename
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Docker Demo</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }}
            .container {{
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }}
            h1 {{ font-size: 3em; margin: 0; }}
            .emoji {{ font-size: 4em; }}
            .info {{ 
                background: rgba(0, 0, 0, 0.2);
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🐳</div>
            <h1>Hello from Docker!</h1>
            <p style="font-size: 1.2em;">This Flask app is running inside a Docker container</p>
            <div class="info">
                <p><strong>Time:</strong> {current_time}</p>
                <p><strong>Hostname:</strong> {hostname}</p>
                <p><strong>Status:</strong> Container is running successfully!</p>
            </div>
            <p style="margin-top: 30px; font-size: 0.9em;">
                If you can see this, you've successfully Dockerized your first app!
            </p>
        </div>
    </body>
    </html>
    """
    return html

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Docker container is running!'}, 200

if __name__ == '__main__':
    # CRITICAL: host='0.0.0.0' makes app accessible outside container
    app.run(host='0.0.0.0', port=5000, debug=True)
```

**Key points about this code:**

1. **`host='0.0.0.0'`** - CRITICAL for Docker!
   - `127.0.0.1` = Only accessible inside container
   - `0.0.0.0` = Accessible from outside container (your browser)

2. **`os.uname().nodename`** - Shows container ID
   - Proves you're running in a container!

3. **`/health` endpoint** - For monitoring container status
   - Returns JSON: `{"status": "healthy"}`

4. **Beautiful UI** - Makes it obvious when it works!

### Step 2: Create Requirements File

**File: example-app/requirements.txt**
```
Flask==3.0.0
Werkzeug==3.0.1
What these are:

Flask - Web framework
Werkzeug - WSGI utility library (Flask dependency)

Step 3: Create the Dockerfile
File: example-app/Dockerfile
dockerfile# Use official Python runtime as base image
FROM python:3.11-slim

# Set metadata (optional but professional)
LABEL maintainer="your.email@example.com"
LABEL description="Docker beginner's toolkit - Flask demo app"

# Set working directory in container
WORKDIR /app

# Copy requirements first (Docker layer caching optimization)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000 to the outside world
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py

# Command to run when container starts
CMD ["python", "app.py"]
Let's break down EVERY line:
FROM python:3.11-slim
What it does: Starts with official Python 3.11 image (slim variant = smaller size)
Why this line is first: Every Dockerfile must start with FROM - it's the foundation.
Alternatives:

python:3.11 - Full version (larger, includes more tools)
python:3.11-alpine - Tiny version (harder to use, some packages don't work)
python:3.11-slim - Goldilocks (just right!)

LABEL maintainer="your.email@example.com"
What it does: Adds metadata to the image
Why include it: Professional practice, helps others know who maintains the image
Not required: You can delete these lines, image will still work
WORKDIR /app
What it does: Creates /app directory in container and sets it as working directory
Equivalent to:
mkdir /app
cd /app
Why /app? Convention. You could use /code, /application, etc.
All subsequent commands (COPY, RUN, CMD) execute from this directory.
COPY requirements.txt .
What it does: Copies requirements.txt from your computer into the container's /app directory
Syntax: COPY [source on host] [destination in container]
The . means: Current directory (which is /app because of WORKDIR)
Why copy requirements first? Docker layer caching! If requirements don't change, Docker reuses cached layer instead of re-installing packages.
RUN pip install --no-cache-dir -r requirements.txt
What it does: Installs Python packages inside the container
Breaking it down:

RUN - Executes command during build (not at runtime)
pip install - Python package installer
--no-cache-dir - Don't save pip cache (reduces image size)
-r requirements.txt - Install from requirements file

This creates a new layer with Flask installed.
COPY app.py .
What it does: Copies application code into container
Why separate from requirements? Layer caching! If you change app.py, only this layer and later ones rebuild. Requirements layer is reused.
Best practice order:

Copy requirements
Install dependencies
Copy application code

EXPOSE 5000
What it does: Documents that container listens on port 5000
IMPORTANT: This is documentation only! It doesn't actually publish the port.
To actually access: You must use -p 5000:5000 when running container.
Why include it?

Documents intent
Some tools (like Docker Compose) use this
Good practice

ENV FLASK_APP=app.py
What it does: Sets environment variable inside container
Format: ENV KEY=VALUE
Multiple variables:
dockerfileENV FLASK_APP=app.py \
    FLASK_ENV=development \
    PORT=5000
Use in code:
pythonimport os
app_name = os.getenv('FLASK_APP')
CMD ["python", "app.py"]
What it does: Command to run when container starts
Syntax: CMD ["executable", "param1", "param2"]
This is what happens when you docker run the image!
Alternatives:
dockerfile# Shell form (simpler, but less efficient)
CMD python app.py

# Exec form (recommended, more efficient)
CMD ["python", "app.py"]

# With gunicorn (production)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
CMD vs RUN:

RUN - Executes during build (install packages, create files)
CMD - Executes when container starts (run application)

Step 4: Build the Docker Image
- Navigate to your project:
- Verify files are present:
ls
# Should show: app.py  Dockerfile  requirements.txt  README.md
Build the image:
docker build -t flask-docker-app .
```

**Breaking down this command:**
- `docker build` - Build an image from Dockerfile
- `-t flask-docker-app` - Tag (name) the image "flask-docker-app"
- `.` - Build context (current directory - where Dockerfile is)

**Expected output:**
```
[+] Building 15.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                    0.0s
 => => transferring dockerfile: 623B                                    0.0s
 => [internal] load .dockerignore                                       0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim     1.2s
 => [auth] library/python:pull token for registry-1.docker.io          0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:abc123...     5.3s
 => => resolve docker.io/library/python:3.11-slim@sha256:abc123...     0.0s
 => => sha256:abc123... 1.65kB / 1.65kB                                 0.0s
 => => sha256:def456... 1.37kB / 1.37kB                                 0.0s
 => => sha256:ghi789... 7.53kB / 7.53kB                                 0.0s
 => => sha256:jkl012... 29.15MB / 29.15MB                               2.1s
 => [internal] load build context                                       0.0s
 => => transferring context: 1.23kB                                     0.0s
 => [2/5] WORKDIR /app                                                  0.1s
 => [3/5] COPY requirements.txt .                                       0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt            7.2s
 => [5/5] COPY app.py .                                                 0.0s
 => exporting to image                                                  0.2s
 => => exporting layers                                                 0.2s
 => => writing image sha256:xyz789...                                   0.0s
 => => naming to docker.io/library/flask-docker-app                    0.0s
Understanding the output:

Each => represents a step
Numbers in brackets [1/5], [2/5] match Dockerfile lines
Time shown for each step
Layer caching - If you rebuild, cached layers show CACHED

First build takes 10-30 seconds (downloading base image + installing packages)
Subsequent builds take 1-3 seconds (cached layers)
Verify image was created:
docker images | grep flask-docker-app
```

**Expected output:**
```
flask-docker-app   latest    xyz789abc123   30 seconds ago   187MB
Understanding this output:

Repository - Image name
Tag - Version (default is "latest")
Image ID - Unique identifier
Created - When built
Size - Total image size

Step 5: Run the Container
docker run -p 5000:5000 flask-docker-app
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 123-456-789
Open your browser: http://localhost:5000
You should see:

Purple gradient background
🐳 Whale emoji
"Hello from Docker!" heading
Current time
Container hostname (weird alphanumeric string - that's the container ID!)
Success message

- YOU DID IT! Your Flask app is running in Docker!
Test the health endpoint:
**Open new terminal:**
curl http://localhost:5000/health
Expected output:
json{"message":"Docker container is running!","status":"healthy"}
Stop the container:
Press Ctrl+C in the terminal running Docker
Step 6: Run in Background (Detached Mode)
docker run -d -p 5000:5000 --name my-flask-container flask-docker-app
```

**Breaking it down:**
- `-d` - Detached mode (runs in background)
- `-p 5000:5000` - Port mapping
- `--name my-flask-container` - Friendly name
- `flask-docker-app` - Image to use

**Returns container ID:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
Container now runs in background!
Check it's running:
bashdocker ps
View logs:
docker logs my-flask-container

# Follow logs in real-time:
docker logs -f my-flask-container
Stop it:
docker stop my-flask-container
Start it again:
docker start my-flask-container
Remove it:
docker stop my-flask-container
docker rm my-flask-container
Advanced: Run with Environment Variables
docker run -d -p 5000:5000 \
  --name my-app \
  -e APP_MESSAGE="Hello from Nairobi!" \
  -e APP_DEBUG=true \
  flask-docker-app
Use in app.py:
pythonmessage = os.getenv('APP_MESSAGE', 'Hello from Docker!')
```

### Docker Image Layers Explained

When you build an image, Docker creates **layers**:
```
Layer 1: Base Python image (FROM)
Layer 2: Create /app directory (WORKDIR)
Layer 3: Add requirements.txt (COPY)
Layer 4: Install packages (RUN pip install)
Layer 5: Add app.py (COPY)
Layer 6: Metadata (EXPOSE, ENV, CMD)
Each layer is cached!
Example: If you change only app.py:

Layers 1-4 are reused from cache (instant)
Only layer 5-6 rebuild (fast)

This is why order matters in Dockerfile!
**Best Practices You've Learned**

- Use official base images (python:3.11-slim)
- Copy requirements before code (layer caching)
- Use --no-cache-dir with pip (smaller images)
- Set WORKDIR (organized filesystem)
- Use EXPOSE (documentation)
- Use host='0.0.0.0' in Flask (accessibility)
- Include health check endpoint (monitoring)
- Use -d for background services (convenience)
- Name containers with --name (easier management)

Quick Reference: Complete Workflow
# 1. Navigate to project
cd ~/Development/code/Personal-Projects/docker-beginner-toolkit/example-app

# 2. Build image
docker build -t flask-docker-app .

# 3. Run container
docker run -d -p 5000:5000 --name my-app flask-docker-app

# 4. Check it's running
docker ps

# 5. View logs
docker logs my-app

# 6. Test in browser
# Open http://localhost:5000

# 7. Stop and remove
docker stop my-app
docker rm my-app
```

---

## Common Issues & Solutions

This section documents **real errors** I encountered and how I solved them.

### Build Errors

#### Error 1: "failed to solve: failed to compute cache key"

**Full error:**
```
failed to solve with frontend dockerfile.v0: failed to create LLB definition: 
failed to compute cache key: "/app.py" not found: not found
What I was doing: Running docker build from wrong directory
Root cause: I was in project root (docker-beginner-toolkit/) instead of example-app/
How I diagnosed it:
bashpwd  # Checked my location
ls   # Looked for Dockerfile - it wasn't there!
Solution:
cd example-app  # Navigate to correct directory
ls              # Verify: app.py, Dockerfile, requirements.txt present
docker build -t flask-docker-app .
```

**Prevention:** Always check `pwd` and `ls` before building. Dockerfile must be in current directory.

---

#### Error 2: "ERROR [4/5] RUN pip install --no-cache-dir -r requirements.txt"

**Full error:**
```
ERROR [4/5] RUN pip install --no-cache-dir -r requirements.txt
------
 > [4/5] RUN pip install --no-cache-dir -r requirements.txt:
#8 1.234 ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
Root cause: COPY command failed silently, requirements.txt wasn't in build context
How I diagnosed it:
ls example-app/
# Checked if requirements.txt actually exists
Solution: requirements.txt was missing - I created it:
bashcd example-app
cat > requirements.txt << EOF
Flask==3.0.0
Werkzeug==3.0.1
EOF
```

**Then rebuilt successfully.**

**Prevention:** Verify all files exist before building. Use `ls` to check.

---

#### Error 3: "Cannot connect to the Docker daemon"

**Full error:**
```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. 
Is the docker daemon running?
What I was doing: Trying to build image
Root cause: Docker service wasn't running
How I diagnosed it:
bashsudo systemctl status docker
# Output showed: inactive (dead)
Solution:
sudo systemctl start docker
sudo systemctl enable docker  # Start on boot
sudo systemctl status docker  # Verify: active (running)
```

**Then `docker build` worked!**

**Prevention:** After reboot, Docker should start automatically if enabled.

---

### Runtime Errors

#### Error 4: "port is already allocated"

**Full error:**
```
Error response from daemon: driver failed programming external connectivity 
on endpoint my-flask-container: Bind for 0.0.0.0:5000 failed: port is already allocated.
What I was doing: Running docker run -p 5000:5000
Root cause: Port 5000 already in use (Flask running locally or another container)
How I diagnosed it:
bashsudo lsof -i :5000
# Output showed python3 process using port 5000
Solution 1: Stop the conflicting process
# Kill the process (replace PID with actual number from lsof output)
kill -9 [PID]

# Now docker run works
docker run -p 5000:5000 flask-docker-app
Solution 2: Use different port
# Map to port 8080 instead
docker run -p 8080:5000 flask-docker-app

# Access at http://localhost:8080
Prevention: Stop local Flask before running container, or use different ports.

Error 5: "Container runs but browser shows 'can't connect'"
Symptom: docker ps shows container running, but http://localhost:5000 doesn't load
What I was doing: Accessing Flask app in browser
Root cause: Flask was binding to 127.0.0.1 instead of 0.0.0.0
How I diagnosed it:
docker logs my-flask-container
# Output showed: "Running on http://127.0.0.1:5000"
# Should be: "Running on all addresses (0.0.0.0)"
Solution: Fixed app.py:
Wrong:
pythonapp.run(host='127.0.0.1', port=5000)  # Only accessible inside container
Correct:
pythonapp.run(host='0.0.0.0', port=5000)    # Accessible from outside
Rebuilt and ran:
bashdocker build -t flask-docker-app .
docker run -p 5000:5000 flask-docker-app
```

**Now browser worked!**

**Prevention:** ALWAYS use `host='0.0.0.0'` for containerized web apps.

---

#### Error 6: "Permission denied" accessing Docker

**Full error:**
```
Got permission denied while trying to connect to the Docker daemon socket at 
unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json": 
dial unix /var/run/docker.sock: connect: permission denied
What I was doing: Running docker ps without sudo
Root cause: My user wasn't in the docker group
How I diagnosed it:
bashgroups
# Output didn't include "docker"
Solution:
sudo usermod -aG docker $USER
newgrp docker  # Apply changes immediately

# Test
docker ps  # Works without sudo!
```

**Prevention:** Add user to docker group during installation (Step 7 of installation).

---

#### Error 7: "exec format error"

**Full error:**
```
standard_init_linux.go:228: exec user process caused: exec format error
What I was doing: Running container on ARM Mac/Raspberry Pi
Root cause: Built image on x86 machine, trying to run on ARM architecture
Solution: Build for correct architecture:
docker build --platform linux/amd64 -t flask-docker-app .
Or use buildx for multi-arch:
docker buildx build --platform linux/amd64,linux/arm64 -t flask-docker-app .
```

---

### Image Management Errors

#### Error 8: "no space left on device"

**Full error:**
```
Error processing tar file(exit status 1): write /usr/local/lib/python3.11/site-packages/...: 
no space left on device
What I was doing: Building image
Root cause: Too many Docker images/containers filling disk
How I diagnosed it:
bashdf -h /var/lib/docker
# Output showed 100% usage

docker system df
# Showed size of images, containers, volumes
Solution:
# Clean up stopped containers
docker container prune

# Clean up unused images
docker image prune -a

# Clean up everything (CAREFUL!)
docker system prune -a --volumes

# Verify space recovered
df -h /var/lib/docker
```

**Prevention:**
Regular cleanup, especially during learning/testing.

---

#### Error 9: "repository name must be lowercase"

**Full error**

invalid reference format: repository name must be lowercase
What I was doing: docker build -t Flask-Docker-App .
Root cause: Image names must be lowercase
Solution:
bashdocker build -t flask-docker-app .  # All lowercase
Prevention: Use lowercase and hyphens for image names.

Troubleshooting Checklist
When something goes wrong, follow this checklist:
For Build Errors:
# 1. Verify you're in correct directory
pwd
ls  # Should see Dockerfile

# 2. Check all files exist
ls -la

# 3. Verify Docker is running
docker ps

# 4. Check Dockerfile syntax
cat Dockerfile  # Look for typos

# 5. Try building with --no-cache
docker build --no-cache -t flask-docker-app .
For Runtime Errors:
# 1. Check container is running
docker ps

# 2. View container logs
docker logs [container-name]

# 3. Check port isn't in use
sudo lsof -i :5000

# 4. Verify port mapping
docker ps  # Look at PORTS column

# 5. Try accessing with curl first
curl http://localhost:5000

# 6. Execute shell inside container
docker exec -it [container-name] bash
For "Can't Access" Issues:
# 1. Verify container is actually running
docker ps

# 2. Check logs for errors
docker logs [container-name]

# 3. Test with curl before browser
curl -v http://localhost:5000

# 4. Verify app binds to 0.0.0.0
docker logs [container-name] | grep "Running on"
# Should see: "Running on all addresses (0.0.0.0)"

# 5. Check firewall isn't blocking
sudo ufw status

AI Learning Journey
How I Used AI to Learn Docker
Throughout this project, I used Claude as my AI learning assistant. This section documents my complete prompt strategy and lessons learned.

**My Prompting Strategy**
**What worked well:**

Specific context - "I'm on Ubuntu 22.04" vs "I'm on Linux"
Structured requests - Numbered lists (1, 2, 3, 4) got better responses
Including errors - Pasting full error messages yielded specific solutions
Asking for explanations - "Explain each line like I'm a beginner" was invaluable
Follow-up questions - Digging deeper when something wasn't clear

**What didn't work:**

Vague questions - "Docker isn't working" got generic responses
Too broad - "Teach me everything about Docker" was overwhelming
Assuming knowledge - Not mentioning my OS caused problems
No examples - AI couldn't gauge my level