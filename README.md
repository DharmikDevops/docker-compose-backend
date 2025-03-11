# 🚀 Flask + MySQL + Nginx with Docker Compose  

This project sets up a **Flask application** with a **MySQL database**, routed through, **Nginx** as a reverse proxy, using **Docker Compose** for container orchestration.  

---

## 🛠 **Technologies and Tools**  
- 🐍 **Flask** – Backend framework  
- 🐬 **MySQL** – Database  
- 🌐 **Nginx** – Reverse proxy  
- 🐳 **Docker Compose** – Manages multi-container applications  

---

## 🌟 **Key Features**  
✅ Containerized Flask backend and MySQL database using Docker  
✅ Configured Nginx as a reverse proxy to route traffic to the Flask app  
✅ Managed multi-container setup using Docker Compose  
✅ Environment variables used to configure database connection  

---

## 🏗 **Steps Implemented**  

### 1️⃣ **Flask App Setup:**  
- Created a Flask application with basic endpoints.  
- Configured the app to connect to the MySQL database.  

### 2️⃣ **Docker Setup:**  
- Created Dockerfiles for Flask and Nginx.  
- Built and managed containers using Docker Compose.  

### 3️⃣ **MySQL Setup:**  
- Created a MySQL container with environment variables for user and database creation.  
- Configured Flask to connect to the MySQL database.  

### 4️⃣ **Nginx Configuration:**  
- Configured Nginx as a reverse proxy for the Flask app.  
- Set up Docker Compose to expose the Nginx container on port *8080*.  

---

## 🚀 **How to Run**  
1. **Clone the repository:**  
```bash
git clone https://github.com/DharmikDevops/docker-compose-backend.git
cd docker-compose-backend
```

2. **Start the containers:**
```bash
docker-compose up -d
```

3. **Access the Flask app at:**

   🌐 `http://localhost:8080`

5. **Stop the containers:**
```bash
docker_compose down
```

---

## 🎯 **What I Learned**

✅ Setting up multi-container apps with Docker Compose <br>
✅ Configuring Nginx as a reverse proxy <br>
✅ Docker container networking <br>

---

## 🎯 **Next Steps**

➡️ Integrate Jenkins for CI/CD

---

## 📞 **Contact**

Feel free to reach out on www.linkedin.com/in/dharmik1904 for any question!

---

