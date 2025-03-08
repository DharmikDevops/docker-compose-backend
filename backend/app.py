from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

@app.route('/db')
def db_check():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="password",
            database="mydb"
        )
        return "Connected to MySQL!"
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
