from flask import Flask
from api.route.home import home_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
