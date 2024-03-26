from flask import render_template
from app.main import bp
from app.models.post import Post
from app.models.question import Question
from app import db

@bp.route('/')
def index():
    db.create_all()
    return render_template('index.html')