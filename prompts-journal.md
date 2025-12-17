# AI Prompts Journal - Docker Learning Journey

## Project Information

- **Technology:** Docker
- **Learning Platform:** moringaschool.com
- **Start Date:** [Today's date]
- **Goal:** Master Docker basics in 5 days using AI-assisted learning

---

## Day 1: Monday - Foundation & Planning

### Session 1.1 - Understanding Docker Basics

**Date:** [Dec 16 2025]

**Context:** Preparing a toolkit for Docker from beginners in their POV for easier understanding and streamlined projects
**Prompt Used:**
```
I'm a software developer who knows Python but has never used Docker. 
Explain what Docker is, what problem it solves, and give me a real-world 
scenario where Docker would be essential. Use simple language and avoid 
jargon where possible.
```

**AI Platform:** claude.ai

**Response Summary:**
Docker packages applications and dependencies into portable containers.
Solves "works on my machine" by ensuring identical environments everywhere.
Used by Netflix, Uber, PayPal for microservices and consistent deployments.

**Key Takeaways:**
- Docker = shipping container for software
- Eliminates environment inconsistencies
- "Build once, run anywhere"
- Production standard for modern apps

**Helpfulness:** ⭐⭐⭐⭐⭐ (5/5)

### Session 1.2 - Core Docker Concepts


**Prompt Used:**
Explain Docker Image vs Container, Dockerfile, Docker Hub, and basic workflow...

**Response Summary:**
- Image = recipe/blueprint, Container = running meal/instance
- Dockerfile = instructions file to build images
- Docker Hub = public registry of pre-built images
- Workflow: Write code → Dockerfile → Build image → Run container

**Key Takeaways:**
- Images are templates, containers are running instances
- Dockerfile is like a recipe card with build steps
- Can use existing images from Docker Hub (don't reinvent wheel)
- Clear workflow from code to deployment

**Helpfulness:** ⭐⭐⭐⭐⭐ (4/5)

### Session 1.3 - Docker Installation on Ubuntu

**Date:** [Today's date]

**Prompt Used:**
Give me step-by-step instructions to install Docker on Ubuntu 22.04...

**Response Summary:**
Complete installation guide with prerequisites, exact commands, verification steps, 
and 5 common errors with solutions.

# Update system
sudo apt-get update

# Install prerequisites
sudo apt-get install -y ca-certificates curl gnupg lsb-release

# Add Docker's GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add user to docker group
sudo usermod -aG docker $USER

# Apply changes
newgrp docker

# Verify installation
docker --version
docker run hello-world

**Installation Result:**
- [✅] Completed installation (mark when done)
- [✅] Docker version: [fill in after install]
- [✅] hello-world test

**Issues Encountered:**
- initial no hello-world image error but it auto solved it

**Helpfulness:** ⭐⭐⭐⭐⭐ (5/5)

### Session 1.5-1.10 - Building & Running Docker Container

**Prompts Covered:**
**1. Prompt #5: Created Dockerfile**
# Use official Python runtime as base image
FROM python:3.11-slim

# Set metadata
LABEL maintainer="your.email@example.com"
LABEL description="Docker beginner's toolkit - Flask demo app"

# Set working directory in container
WORKDIR /app

# Copy requirements first (for layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py

# Run the application
CMD ["python", "app.py"]
**Prompt #6: Build and run commands**
# Make sure you're in example-app directory
cd ~/Development/code/Personal-Projects/docker-beginner-toolkit/example-app

# Build the image
docker build -t flask-docker-app .
```

**What this does:**
- `docker build` = Build an image from Dockerfile
- `-t flask-docker-app` = Tag (name) the image "flask-docker-app"
- `.` = Look for Dockerfile in current directory

**Expected output:**
```
[+] Building 15.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [internal] load metadata for docker.io/library/python:3.11-slim
 => [1/4] FROM docker.io/library/python:3.11-slim
 => [2/4] WORKDIR /app
 => [3/4] COPY requirements.txt .
 => [4/4] RUN pip install --no-cache-dir -r requirements.txt
 => [5/4] COPY app.py .
 => exporting to image
 => => naming to docker.io/library/flask-docker-app

- Run the container: docker run -p 5000:5000 flask-docker-app


### Session 7 - Common Docker Build Errors


**Prompt Used:**
What are the 5 most common errors beginners encounter when building Docker images, and how do I fix each one? Format as:
Error: [exact error message]
Cause: [why it happens]
Solution: [how to fix it]
Prevention: [how to avoid it]

**Response Summary:**
Received 5 common errors with detailed solutions:
1. COPY failed - file not found
2. Cannot connect to Docker daemon
3. Port already allocated
4. Permission denied
5. No space left on device

**Key Takeaways:**
- Always run docker build from directory containing Dockerfile
- Ensure Docker service is running before building
- Check for port conflicts before running containers
- User must be in docker group for permissions
- Regular cleanup prevents disk space issues

**Errors I Actually Encountered:**
- I could not access app.py because i was the the root directory


---

### Session 8 - Troubleshooting Container Access


**Prompt Used:**
I successfully built and ran my Docker container, but I can't access it in my browser at localhost:5000. The container is running (confirmed with 'docker ps'). What could be wrong and how do I troubleshoot this?

**Response Summary:**
Comprehensive troubleshooting checklist:
- Verify container is running (docker ps)
- Check port mapping is correct
- Ensure Flask binds to 0.0.0.0 not 127.0.0.1
- Review container logs for errors
- Test with curl first before browser

**Key Takeaways:**
- host='0.0.0.0' is CRITICAL for Docker networking
- Port mapping format: -p HOST_PORT:CONTAINER_PORT
- Container logs show what's happening inside
- Health check endpoints are useful for debugging

**Issues I Faced:**
Addressed the directory error

**Helpfulness:** ⭐⭐⭐⭐⭐ (5/5)

---

### Session 9 - Adding Environment Variables


**Prompt Used:**
Show me how to add environment variables to my Dockerized Flask app. I want to pass a custom message through an environment variable and display it on the webpage. Include:
1. How to modify the Dockerfile
2. How to modify app.py
3. How to pass the variable when running the container

**Response Summary:**
Learned three ways to use environment variables:
1. Set default in Dockerfile with ENV
2. Read in Python with os.getenv()
3. Override at runtime with -e flag

**Key Takeaways:**
- ENV in Dockerfile sets defaults
- os.getenv() provides fallback values
- Runtime -e flag overrides Dockerfile ENV
- Useful for configuration without rebuilding

**Implementation Status:**
- [ ] Added ENV to Dockerfile
- [ ] Modified app.py to read variables
- [ ] Tested with custom values
- [ ] Documented in GUIDE.md

**Helpfulness:** ⭐⭐⭐⭐☆ (4/5)
Note: Basic example, could explore more advanced config patterns

---

### Session 10 - Complete Testing Checklist


**Prompt Used:**
Give me a complete testing checklist to verify my Dockerized Flask application is working correctly from build to browser access.

**Response Summary:**
Comprehensive 8-step verification process:
1. Verify image exists
2. Run container
3. Check container status
4. Test HTTP endpoint with curl
5. Test health endpoint
6. Review container logs
7. Verify in browser
8. Clean up properly

**Key Takeaways:**
- Test incrementally (don't skip to browser)
- curl is faster than browser for quick tests
- docker logs reveals runtime issues
- Always clean up test containers

**Test Results:**
- [ ] All 8 steps completed successfully
- [ ] Documented any failures
- [ ] Took screenshots of working app

**Helpfulness:** ⭐⭐⭐⭐⭐ (5/5)

---

## Summary Statistics

**Total Prompts Used:** 10
**Successful First Answers:** 8/10 (80%)
**Required Follow-ups:** 2 (app.py formatting error, directory navigation)
**Most Helpful Prompt:** Installation guide (Session 1.3)
**Most Challenging:** Dockerfile syntax understanding

**Overall AI Learning Experience:**
Claude provided clear, actionable responses with exact commands and code.
The structured prompt format (1, 2, 3, 4 lists) yielded best results.
Follow-up questions were handled well with specific debugging steps.

**Recommendation for Future Learners:**
- Be specific about your OS and versions
- Include error messages in full
- Ask for explanations, not just solutions
- Test each step before moving forward
- Prompt #8: Troubleshooting access
- Prompt #9: Environment variables
- Prompt #10: Testing checklist

**Build Result:**
- Dockerfile created
- Image built successfully: flask-docker-app
- Container runs without errors
- Accessible in browser at localhost:5000
- Health check endpoint working

**Errors Encountered:**
Always ensure you're at the right location for lack of a better word to avoid annoying status code errors

**Final Status:** WORKING DOCKER CONTAINER!

