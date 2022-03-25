import os
import yaml
from flask import Flask as BaseFlask, Config as BaseConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_yaml(os.path.join(app.root_path, 'config.yml'))
    from .handlers import user
    app.register_blueprint(user.user_bp)
    db.init_app(app)
    return app
