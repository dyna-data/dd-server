from app.shared import db
from .base import BaseModel

class Usuario(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    _default_fields = [
        "username",
        "email",
    ]

    def __repr__(self):
        return '<User %r>' % self.username