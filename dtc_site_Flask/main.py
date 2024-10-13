from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_login.mixins import AnonymousUserMixin

from models import User, ImageFeed, DetectedObject
from utils import is_logged_in, check_login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///detection_site.db'
app.config['SECRET_KEY'] = 'xRsytXzlPwPAJnX9y0VGl6kwu1Yia90E'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def get_home_page():
    print(current_user, )
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def get_login_page():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = User.query.filter_by(name=request.form.get('username'), password=request.form.get('password')).first()
        if user:
            login_user(user)
            return redirect('/dashboard')
        else:
            return render_template('/login.html',
                                   message='Wrong login or password!')


@app.route('/register', methods=['GET', 'POST'])
def get_register_page():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        if not check_login(username):
            return render_template('register.html',
                                   message='Forbidden symbols in username!')

        if password != password_confirmation:
            return render_template('register.html',
                                   message='Entered passwords ane not equal!')

        if User.query.filter_by(name=username).first():
            return render_template('register.html',
                                   message='User already exist!')

        try:
            user = User(name=username, password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect('/dashboard')

        except:
            return render_template('register.html',
                                   message='Couldn`t create user!')


@app.route('/dashboard')
def get_dashboard_page():
    return render_template('home.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
