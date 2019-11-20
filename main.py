from flask import Flask, escape, request
from app.shared import create_app, db
from app.models.usuario import Usuario

app = create_app()
app.app_context().push()

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    print(Usuario.query.all())
    return f'Hello, {escape(name)}!'

if __name__ == "__main__":    
    db.create_all()
    app.run()
