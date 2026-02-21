from __future__ import annotations

import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///sdg4.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    JSON_AS_ASCII = False


class DevConfig(Config):
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False

