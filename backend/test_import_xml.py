import os
import tempfile
import xml.etree.ElementTree as ET
import pytest
from flask import Flask
from database import db
from models import Product
from import_xml import import_products_from_xml


@pytest.fixture
def test_app():
    """Setup a temporary Flask app with in-memory SQLite for testing."""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # test DB
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()  # cleanup


@pytest.fixture
def sample_xml_file():
    """Create a temporary XML file for testing."""
    xml_content = """
    <products>
        <product>
            <name>Test Product A</name>
            <price>10.50</price>
            <stock>5</stock>
        </product>
        <product>
            <name>Test Product B</name>
            <price>20.00</price>
            <stock>3</stock>
        </product>
    </products>
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".xml") as f:
        f.write(xml_content.encode("utf-8"))
        return f.name


def test_import_products(test_app, sample_xml_file):
    """Test importing products from XML into DB."""
    with test_app.app_context():
        import_products_from_xml(sample_xml_file)

        products = Product.query.all()
        assert len(products) == 2

        p1 = Product.query.filter_by(name="Test Product A").first()
        assert p1.price == 10.50
        assert p1.stock == 5

        p2 = Product.query.filter_by(name="Test Product B").first()
        assert p2.price == 20.00
        assert p2.stock == 3

    os.remove(sample_xml_file)  # cleanup temp file