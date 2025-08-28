📒 Flask Notes Saver

A simple Flask-based Notes Web Application to add, delete, and search notes.
Data is stored in a local JSON file, and the project includes HTML, CSS, and Docker support.

🚀 Features

Add new notes 📝

Delete existing notes ❌

Search notes 🔍

JSON file-based storage

Simple HTML & CSS frontend (templates + static files)

Dockerized for easy deployment

📂 Project Structure
week6/
│── app.py               # Main Flask application  
│── requirements.txt     # Python dependencies  
│── Dockerfile           # Docker setup file  
│── notes.json           # Notes data (auto-created)  
│── static/              # CSS and static files  
│   └── style.css  
│── templates/           # HTML templates  
│   ├── index.html  
│   └── search.html  

⚙️ Installation & Run
🔧 Run Locally

Clone repo:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name/week6


Create virtual environment & install requirements:

pip install -r requirements.txt


Run Flask app:

python app.py


Open in browser:

http://127.0.0.1:5000

🐳 Run with Docker

Build Docker image:

docker build -t flask-notes .


Run container:

docker run -p 5000:5000 flask-notes


Visit:

http://localhost:5000

📌 Technologies Used

Python (Flask)

HTML & CSS (templates + static files)

JSON (data storage)

Docker

✨ Author

Developed by Ahsan Sajid
