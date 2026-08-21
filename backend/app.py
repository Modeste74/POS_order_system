from flask import Flask
# from flask import send_from_directory
from flask_cors import CORS
from backend.database import db
from backend.routes.products import product_bp
from backend.routes.orders import order_bp
from backend.routes.checkout import checkout_bp
from backend.routes.auth import auth_bp
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Get credentials from environment variables
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    stripe_sk = os.getenv("STRIPE_SECRET_KEY")
    stripe_pk = os.getenv("STRIPE_PUBLIC_KEY")

    # Config - To be adjusted later for Railway/Render later
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Stripe config
    app.config['STRIPE_SECRET_KEY'] = stripe_sk
    app.config['STRIPE_PUBLIC_KEY'] = stripe_pk

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(product_bp, url_prefix="/products") 
    app.register_blueprint(order_bp, url_prefix="/orders") 
    app.register_blueprint(checkout_bp, url_prefix="/checkout")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Serve frontend files
    # @app.route("/")
    # def serve_fronend():
    #     return send_from_directory(os.path.join(app.root_path, "frontend"), "index.html")
    
    # @app.route("/<path:path>")
    # def static_proxy(path):
    #     return send_from_directory(os.path.join(app.root_path, ""))

    @app.route("/ping")
    def ping():
        return {"message": "pong"}
    return app


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()

        # Seed only if no products exist
        # from models import Product
        # if not db.session.query(Product).first():
        #     sample_products = [
        #         Product(name="Coffee", price=2.5, stock=20),
        #         Product(name="Coffee", price=1.2, stock=50),
        #         Product(name="Pen", price=0.5, stock=100),
        #     ]
        #     db.session.bulk_save_objects(sample_products)
        #     db.session.commit()
    app.run(debug=True)
