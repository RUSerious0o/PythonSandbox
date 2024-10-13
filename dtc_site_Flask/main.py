import os

from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, logout_user, current_user, LoginManager
from flask_login.mixins import AnonymousUserMixin

from utils import is_logged_in, check_login, generate_filepath, process_image as utils_process_image

UPLOAD_FOLDER_PATH = 'static/media/images'
PROCESSED_IMAGE_DIR = 'static/media/processed_images'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///detection_site.db'
app.config['SECRET_KEY'] = 'xRsytXzlPwPAJnX9y0VGl6kwu1Yia90E'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PATH

os.makedirs(UPLOAD_FOLDER_PATH, exist_ok=True)
os.makedirs(PROCESSED_IMAGE_DIR, exist_ok=True)

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
    rel_detected_object_feed = db.relationship('DetectedObject',
                                               back_populates='rel_detected_object_obj',
                                               cascade='all, delete-orphan',
                                               passive_deletes=True)


class DetectedObject(db.Model):
    __tablename__ = 'detectedobjects'

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    object_type = db.Column(db.String(100), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(255), nullable=False)
    image_feed_id = db.Column(db.BigInteger, db.ForeignKey('imagefeeds.id', ondelete='CASCADE'), nullable=False)

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
    if is_logged_in():
        return render_template(
            'dashboard.html',
            user=is_logged_in(),
            image_feeds=ImageFeed.query.filter_by(user_id=current_user.id)
        )
    else:
        return redirect('/login')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/add_image', methods=['GET', 'POST'])
def get_add_image_page():
    if not is_logged_in():
        return redirect('/login')

    return render_template(
        'add_image_feed.html',
        user=is_logged_in()
    )


@app.route('/upload_image', methods=['POST'])
def upload_image():
    if not is_logged_in():
        return redirect('/login')

    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']
    if image.filename == '':
        return redirect(request.url)

    if image:
        image_path = generate_filepath(UPLOAD_FOLDER_PATH, image.filename)
        image.save(image_path)
        image_feed = ImageFeed(image=image_path, user_id=current_user.id)
        db.session.add(image_feed)
        db.session.commit()

        return redirect('/dashboard')

    return redirect('/')


@app.route('/process_image/<image_id>', methods=['GET'])
def process_image(image_id: int):
    image_feed = ImageFeed.query.get(int(image_id))
    if image_feed.processed_image:
        return redirect('/dashboard')

    detected_object = DetectedObject(image_feed_id=image_id, object_type=None, location='', confidence=0)
    processed_image_path = utils_process_image(
        image_id,
        ImageFeed.query.get(int(image_id)).image,
        PROCESSED_IMAGE_DIR,
        db,
        detected_object
    )

    image_feed.processed_image = processed_image_path
    db.session.commit()

    return redirect('/dashboard')


@app.route('/delete_image/<image_id>', methods=['POST'])
def delete_image(image_id):
    image = ImageFeed.query.get(int(image_id))
    db.session.delete(image)
    db.session.commit()
    os.remove(image.image)
    os.remove(image.processed_image)

    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()
