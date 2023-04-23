from .models import User
from flask import Blueprint, render_template, request, current_app

blueprint = Blueprint('simple_pages', __name__)


@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')


@blueprint.route('/users')
def users():
    page_number = request.args.get('page', 1, type=int)
    users_pagination = User.query.paginate(
        page=page_number, per_page=current_app.config['USERS_PER_PAGE'])
    return render_template('simple_pages/users.html', users_pagination=users_pagination)


@blueprint.route('/run-seed')
def run_seed():
    if not User.query.filter_by(last_name='Müller').first():
        import app.scripts.seed
        return 'Database seed completed!'
    else:
        return 'Nothing to run.'
