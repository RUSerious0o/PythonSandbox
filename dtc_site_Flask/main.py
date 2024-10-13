from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_login.mixins import AnonymousUserMixin

from utils import is_logged_in, check_login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///detection_site.db'
app.config['SECRET_KEY'] = 'xRsytXzlPwPAJnX9y0VGl6kwu1Yia90E'

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)

    rel_image_feed_user = db.relationship('ImageFeed', back_populates='rel_image_feed_feed')


class ImageFeed(db.Model):
    __tablename__ = 'imagefeeds'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    image = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True, nullable=False)
    processed_image = db.Column(db.String(100), nullable=True)

    rel_image_feed_feed = db.relationship('User', back_populates='rel_image_feed_user')
    rel_detected_object_feed = db.relationship('DetectedObject', back_populates='rel_detected_object_obj')


class DetectedObject(db.Model):
    __tablename__ = 'detectedobjects'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    object_type = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    image_feed_id = db.Column(db.BigInteger, db.ForeignKey('imagefeeds.id'), nullable=False)

    rel_detected_object_obj = db.relationship('ImageFeed', back_populates='rel_detected_object_feed')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def get_home_page():
    return render_template(
        'home.html',
        user=is_logged_in()
    )


@app.route('/login', methods=['GET', 'POST'])
def get_login_page():
    if request.method == 'GET':
        return render_template(
            'login.html',
            user=is_logged_in()
        )

    else:
        user = User.query.filter_by(name=request.form.get('username'), password=request.form.get('password')).first()
        if user:
            login_user(user)
            return redirect('/dashboard')
        else:
            return render_template(
                '/login.html',
                message='Wrong login or password!',
                user=is_logged_in()
            )


@app.route('/register', methods=['GET', 'POST'])
def get_register_page():
    if request.method == 'GET':
        return render_template(
            'register.html',
            user=is_logged_in()
        )

    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        if not check_login(username):
            return render_template(
                'register.html',
                message='Forbidden symbols in username!',
                user=is_logged_in()
            )

        if password != password_confirmation:
            return render_template(
                'register.html',
                message='Entered passwords ane not equal!',
                user=is_logged_in()
            )

        if User.query.filter_by(name=username).first():
            return render_template(
                'register.html',
                message='User already exist!',
                user=is_logged_in()
            )

        try:
            user = User(name=username, password=password)
            db.session.add(user)
            db.session.commit()
            login_user(user)

            return redirect('/dashboard')

        except:
            return render_template(
                'register.html',
                message='Couldn`t create user!',
                user=is_logged_in()
            )


@app.route('/dashboard')
def get_dashboard_page():
    return render_template(
        'dashboard.html',
        user=is_logged_in()
    )


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
