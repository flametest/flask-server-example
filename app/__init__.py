import os
import yaml
from flask import Flask as BaseFlask, Config as BaseConfig
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Config(BaseConfig):

    def from_yaml(self, config_file):
        env = os.environ.get('FLASK_ENV', 'development')
        self['ENVIRONMENT'] = env.lower()

        with open(config_file) as f:
            c = yaml.load(f, yaml.Loader)

        c = c.get(env, c)
        for key in c.keys():
            if key.isupper():
                self[key] = c[key]


class Flask(BaseFlask):

    def make_config(self, instance_relative=False):
        root_path = self.root_path
        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)


def register_blueprints(app: Flask):
    from .handler import user
    from .handler import node
    app.register_blueprint(user.user_bp)
    app.register_blueprint(node.node_bp)


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_yaml(os.path.join(app.root_path, 'config.yml'))
    register_blueprints(app)
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    return app
