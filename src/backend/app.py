from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Database connection parameters
DB_HOST = "your_db_host"
DB_NAME = "your_db_name"
DB_USER = "your_db_user"
DB_PASS = "your_db_password"

def get_db_connection():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
    return conn

@app.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    job_title = data['job_title']
    company_name = data['company_name']
    location = data['location']
    description = data['description']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO jobs (job_title, company_name, location, description) VALUES (%s, %s, %s, %s)',
                (job_title, company_name, location, description))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'message': 'Job created successfully'}), 201

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM jobs')
    jobs = cur.fetchall()
    cur.close()
    conn.close()

    job_list = []
    for job in jobs:
        job_dict = {
            'id': job[0],
            'job_title': job[1],
            'company_name': job[2],
            'location': job[3],
            'description': job[4]
        }
        job_list.append(job_dict)

    return jsonify(job_list), 200

if __name__ == '__main__':
    app.run(debug=True)
```

Please replace `your_db_host`, `your_db_name`, `your_db_user`, and `your_db_password` with your actual database connection details. This Flask application includes two API endpoints: one for creating a new job listing (`/api/jobs POST`) and another for retrieving all job listings (`/api/jobs GET`). The data is stored in a PostgreSQL database using the psycopg2 library.