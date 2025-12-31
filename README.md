# 📊 Raspberry Pi Dashboard

A lightweight web application based on **Flask** that allows you to monitor the resource status of your server or Raspberry Pi in real-time. The project includes a login system and displays key system metrics.

## ✨ Features

* **Resource Monitoring:**
* **CPU:** Average processor load percentage.
* **RAM:** Percentage of memory usage.
* **Disk:** Total, used, and free space (in GB), plus usage percentage.
* **Network:** Real-time incoming and outgoing traffic in MB.


* **Network Info:** Displays the server's external IP address.
* **Remote Access:** Generates a ready-to-use SSH connection string for the current user.
* **Security:** Simple password protection for the dashboard.
* **Auto-refresh:** The dashboard automatically updates every 10 seconds.

---

## 🚀 How to Run

### 1. Prerequisites

Ensure you have Python installed. It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

### 2. Install Dependencies

Install the required Python libraries using pip:

```bash
pip install flask psutil requests

```

### 3. Project Structure

Ensure your files are organized as follows:

```text
.
├── app.py              # Main application file
├── templates/
│   ├── login.html      # Login page
│   └── dashboard.html  # Dashboard page
└── static/
    └── css/
        └── css.css     # Stylesheets

```

### 4. Start the Application

Run the script:

```bash
python app.py

```

Open your browser and navigate to: `http://127.0.0.1:5000`

---

## 🔑 Access Credentials

* **Default Password:** `Alex09`

> **Note:** You can modify the password in `app.py` within the `submit()` function.

---

## 🛠 Tech Stack

* **Backend:** Python 3, Flask
* **System Metrics:** `psutil`
* **Frontend:** HTML5, CSS3 (Jinja2 Templates)
* **API:** ipify (for external IP detection)

---

## 📋 Dashboard Overview

The application is divided into several information blocks:

1. **Disk Usage:** Shows total capacity and currently occupied space.
2. **SSH Connection:** Provides the command for remote terminal access.
3. **RAM Usage:** Visualizes current memory consumption.
4. **Network & IP:** Displays external connectivity details and data throughput.
5. **CPU Load:** Real-time processor utilization.

---

## ⚠️ Security Notice

This project is intended for local network use or educational purposes. For production environments, ensure you implement password hashing and run the app behind a production-grade WSGI server like Gunicorn.





---
JL с нами малина становится вкуснее