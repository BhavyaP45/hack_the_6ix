from docs import app, render_template, redirect, db, url_for, flash, login_user, logout_user, bcrypt, current_user
from docs.forms import RegisterForm, LoginForm
from docs.models import User

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST", "GET"])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user_to_create = User(username = form.username.data, email_address = form.email_address.data, password = form.password.data, is_manager = False)
            with app.app_context():
                db.session.add(user_to_create)
                db.session.commit()
                login_user(user_to_create)
        
            return redirect(url_for("dashboard_page"))
        
        except:
            flash(f'There was an error with creating a user: {err_msg}', category = "error")
    
    elif form.errors != {}: #.errors Stores all the errors from the form (If there are no errors from the validations)
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category = "error")

    return render_template("register.html", form = form)

@app.route("/dashboard", methods = ["POST", "GET"])
def dashboard_page():
    
    return render_template("dashboard.html")

@app.route('/login', methods = ["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            attempted_user = User.query.filter_by(username = form.username.data).first() 

            #Check if the user is already stored in the database and check password with password hash
            if attempted_user and attempted_user.check_password_correction(form.password.data):
                login_user(attempted_user)
                flash(f'Welcome Back {attempted_user.username}', category="success")

                return redirect(url_for("dashboard_page"))
            else:
                flash("User name and password are not matched!", category= "error")
        except:
            flash("Something Went Wrong", category = "error")

    return render_template('login.html', form = form)

@app.route('/logout', methods = ["POST","GET"])
def logout_page():
    logout_user()
    flash("Success", category= "success")
    return redirect(url_for("index"))
