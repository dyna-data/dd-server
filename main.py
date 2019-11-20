from flask import Flask, escape, request
from app.shared import create_app, db
from app.models.usuario import Usuario
import datetime

app = create_app()
app.app_context().push()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    
    admin = Usuario(username=f'admin{datetime.datetime.now()}', email=f'admin{datetime.datetime.now()}@example.com')
    db.session.add(admin)
    db.session.commit()
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":    
    db.create_all()
    app.run()
