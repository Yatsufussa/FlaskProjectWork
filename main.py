from flask import Flask
from flask_restx import Api
from database.models import db

from comment.comment_api import comment_bp
from photo.photo_api import photo_bp
from user.user_api import user_bp
from posts.post_api import post_bp

# объект swagger
api = Api()
# объект Flask
app = Flask(__name__)
# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)
# Регистрация сайта к swagger
api.init_app(app)


# Для тестов
# @app.route('/')
# def test_api():
#     html_dexkan = '<h1>Test my api</h1><br><input type="file">'
#
#     return render_template('test.html')


# Зарегистрируем компоненты
app.register_blueprint(comment_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# Swagger