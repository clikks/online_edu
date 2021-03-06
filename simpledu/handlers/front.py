from flask import Blueprint, render_template, url_for, flash, redirect, request, current_app
from flask_login import login_user, logout_user, login_required

from simpledu.models import User, Course
from simpledu.forms import LoginForm, RegisterForm

front = Blueprint('front', __name__)


@front.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    pagination = Course.query.paginate(
            page=page,
            per_page=current_app.config['INDEX_PER_PAGE'],
            error_out=False
            )
#    courses = Course.query.all()
    return render_template('index.html', pagination=pagination)

@front.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        login_user(user, form.remeber_me.data)
        return redirect(url_for('.index'))
    return render_template('login.html', form=form)

@front.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        form.create_user()
        flash('Success,Please login!', 'success')
        return redirect(url_for('.login'))
    return render_template('register.html', form=form)

@front.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You are logout', 'success')
    return redirect(url_for('.index'))

