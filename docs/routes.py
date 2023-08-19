from docs import app, Flask, redirect, url_for, request, render_template, flash

@app.route("/announcements", methods=['POST', 'GET'])
def announcements_page():
    
    if request.method == 'POST':
        announcementText = request.form['chatBox']
        
    return render_template("announcements.html")


@app.route("/dashboard", methods=['POST', 'GET'])
def announcements_page():
    
        
    return render_template("dashboard.html")


@app.route("/tasks", methods=['POST', 'GET'])
def tasks_page():
        
    return render_template("tasks.html")

@app.route("/checkin", methods=['POST', 'GET'])
def checkin_page():
    
    return render_template("checkin.html")