# API-FLASK\
User Management REST API (Flask)
📌 Project Overview
This project is a simple User Management REST API built using Python Flask. It allows basic CRUD (Create, Read, Update, Delete) operations on user data through HTTP requests.

🚀 Features
✅ Get all users

🔍 Get a user by ID

➕ Add (create) a new user

📝 Update an existing user

❌ Delete a user by ID

🛠️ Technologies Used
Python 3.x

Flask

Postman / curl (for testing)

(Optional: Anaconda or virtual environment for isolation)

📁 Project Structure
bash
Copy
Edit
user-api-flask/
│
├── app.py              # Main Flask app with REST routes
└── README.md           # Project documentation
▶️ How to Run the API
1. Clone the Repository or Copy Code
bash
Copy
Edit
git clone https://github.com/yourusername/user-api-flask.git
cd user-api-flask
2. Create & Activate Environment (Optional but Recommended)
bash
Copy
Edit
conda create -n flaskenv python=3.10
conda activate flaskenv
3. Install Dependencies
bash
Copy
Edit
pip install flask
Or use a requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Application
bash
Copy
Edit
python app.py
The API will run on:

cpp
Copy
Edit
http://127.0.0.1:5000
🔗 API Endpoints
Method	Endpoint	Description
GET	/users	Get list of all users
GET	/users/<id>	Get user by ID
POST	/users	Add new user
PUT	/users/<id>	Update existing user
DELETE	/users/<id>	Delete user by ID

🧪 Example JSON for POST/PUT
json
Copy
Edit
{
  "name": "Alice",
  "email": "alice@example.com"
}
