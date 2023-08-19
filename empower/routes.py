from empower import app

@app.route("/index")
def home_page():
    return "Hello World"