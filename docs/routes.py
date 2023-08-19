from docs import app

@app.route("/")
def home_page():
    return "Hello World"