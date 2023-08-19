from docs import app, Flask, redirect, url_for, request, render_template, flash, sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/announcements", methods=['POST', 'GET'])
def announcements_page():

    conn = get_db_connection()
    announcements = conn.execute('SELECT * FROM announcements').fetchall()
    conn.close()   
        
    return render_template("announcements.html", announcements = announcements)

@app.route("/announcements-create", methods=['POST', 'GET'])

def announcements_create_page():

    if request.method == "POST":
        title = request.form["titleBox"]
        announcementText = request.form["chatBox"]
        conn = get_db_connection()
        conn.execute('INSERT INTO announcements (title, announcementText) VALUES (?,?)',
                        (title, announcementText))
        conn.commit()
        conn.close()
        return redirect(url_for('announcements_page'))
        
    return render_template("createAnnouncement.html")


@app.route("/dashboard", methods=['POST', 'GET'])
def dashboard_page():
    return render_template("dashboard.html")


@app.route("/tasks", methods=['POST', 'GET'])
def tasks_page():

    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()           
    return render_template("tasks.html",tasks = tasks)

@app.route("/checkin", methods=['POST', 'GET'])
def checkin_page():
    
    return render_template("checkin.html")