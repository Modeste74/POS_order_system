import sys
import xml.etree.ElementTree as ET
import os
from flask import Flask
from database import db
from models import Product
from dotenv import load_dotenv

load_dotenv()


def import_products_from_xml(file_path):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for product_xml in root.findall("product"):
            name = product_xml.find("name").text.strip()
            price = float(product_xml.find("price").text)
            stock = int(product_xml.find("stock").text)

            # Upsert logic
            product = Product.query.filter_by(name=name).first()
            if product:
                if product.price != price or product.stock != stock:
                    product.price = price
                    product.stock = stock
                    print(f"Updated: {name}")
                else:
                    print(f"No change: {name}")
            else:
                product = Product(name=name, price=price, stock=stock)
                db.session.add(product)
                print(f"Inserted: {name}")

        db.session.commit()
        print("Import complete.")

    except Exception as e:
        db.session.rollback()
        print(f"Error importing XML: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python import_xml.py <filename.xml>")
        sys.exit(1)

    file_path = sys.argv[1]

    # Setup Flask app + DB connection
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        import_products_from_xml(file_path)
