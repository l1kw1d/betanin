# betanin
from betanin import paths


SQLALCHEMY_DATABASE_URI = f'sqlite:///{paths.DB_PATH}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = "GUYSILOVEIT"
PROPAGATE_EXCEPTIONS = True
CORS_ORIGIN_WHITELIST = [
    'http://0.0.0.0:5000',
    'http://localhost:5000',
    'http://0.0.0.0:8081',
    'http://localhost:8081',
]
