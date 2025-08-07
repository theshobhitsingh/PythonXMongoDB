# PythonXMongoDB

PythonXMongoDB is a command-line based YouTube video manager built with **Python** and **MongoDB**. It allows users to **add**, **view**, **update**, and **delete** video entries stored in a MongoDB collection.

This project demonstrates CRUD operations using the official `pymongo` library, secure environment variable handling using `python-dotenv`, and modular CLI-based interaction.

---

## 🚀 Features

- 📝 Add a new YouTube video with title and duration.
- 📜 List all stored videos with indexes.
- ✏️ Update any existing video details.
- ❌ Delete a video by selecting from the list.
- 🔐 Uses `.env` file to secure sensitive credentials.

---

## 📦 Tech Stack

- **Language:** Python 3  
- **Database:** MongoDB Atlas (NoSQL)  
- **Libraries:**  
  - `pymongo` - MongoDB client  
  - `python-dotenv` - For loading environment variables  

---

## 📁 Project Structure

```plaintext
PythonXMongoDB/
├── main.py
├── .env
├── .gitignore
└── README.md
```

## 🔧 Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/PythonXMongoDB.git
cd PythonXMongoDB
```

2. Install Required Packages
Ensure you have Python 3.7 or later installed.
```bash
pip install pymongo python-dotenv
```

3. Create a .env File
In the project root, create a .env file and add your MongoDB URI:

```
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-address>.mongodb.net/
```
Note: Replace with your actual MongoDB Atlas connection string.

4. Run the Application
   ```
   python main.py
   ```

## 🧪 Usage Guide

Upon running, you'll see a simple menu:

```text
YouTube Manager || Choose an Option
1. List All Favourite Videos
2. Add a YouTube Video
3. Update a YouTube Video
4. Delete a YouTube Video
5. Exit the Application
```

## 🙏 Acknowledgements

- MongoDB Atlas – for providing a free, scalable cloud database.  
- PyMongo – the official MongoDB driver for Python.  
- python-dotenv – for secure environment variable handling.  
- GitHub Gitignore Templates – for the Python `.gitignore` base.  
- The Python community – for extensive resources and support.  
