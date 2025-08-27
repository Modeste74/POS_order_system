<h1>🛒 POS Order System</h1>

<p>A simple <strong>Point of Sale (POS) and Order Management System</strong> built with <strong>Python (Flask)</strong>, <strong>PostgreSQL</strong>, and <strong>JavaScript frontend</strong>, with <strong>Stripe API integration</strong> for payments.</p>

<br>

<p>This project demonstrates <strong>**end-to-end software development**</strong>:</p>
<ul>
    <li>Backend with CRUD APIs.</li>
    <li>Database modeling with PostgreSQL + SQLAlchemy ORM.</li>
    <li>Frontend UI with JavaScript & XML config parsing.</li>
    <li>Third-party integration (Stripe Payment Gateway).</li>
    <li>Deployment-ready using Docker & cloud hosting.</li>
</ul>

<br>

<h2>🚀 Features</h2>
<ul>
    <li>✅ Manage Products (CRUD).</li>
    <li>✅ Create Orders (with stock validation).</li>
    <li>✅ Integrate Payments via Stripe (Test Mode).</li>
    <li>✅ Simple Frontend UI (HTML + JS + XML).</li>
    <li>✅ PostgreSQL database with SQLAlchemy ORM.</li>
    <li>✅ RESTful API design.</li>
</ul>

<br>

<h2>🏗️ Tech Stack</h2>
<ul>
    <li>**Backend**: Python, Flask, SQLAlchemy</li>
    <li>**Database**: PostgreSQL</li>
    <li>**Frontend**: HTML, CSS, JavaScript, XML</li>
    <li>**Payments**: Stripe API (test mode)</li>
    <li>**Deployment**: Docker + Render/Railway</li>
</ul>

<br>

<h2>📂 Project Structure</h2>
pos-order-system/
│── backend/
│ ├── app.py # Main Flask app
│ ├── models.py # SQLAlchemy models
│ ├── database.py # DB connection
│ ├── routes/
│ │ ├── products.py # Product CRUD
│ │ ├── orders.py # Order CRUD
│ │ ├── checkout.py # Stripe checkout
│ ├── requirements.txt # Python dependencies
│ ├── .env.example # Env variables
│
│── frontend/
│ ├── index.html # UI
│ ├── app.js # Fetch API + cart logic
│ ├── ui.xml # Mock XML layout config
│
│── Dockerfile # Containerization
│── README.md # Documentation
│── POS_Order_System.postman_collection.json # Postman tests

<br>

<h2>⚙️ Setup Instructions</h2>

<h3>1. Clone Repo</h3>
<div>
    <span>bash</span>
    <pre>
    <code>
        git clone https://github.com/Modeste74/POS_order_system.git
        cd POS_order_system/backend
    </code>
    </pre>
</div>

<div>
    <span>Install dependencies</span>
    <pre>
    <code>
        pip install -r requirements.txt
    </code>
    </pre>
</div>

Setup PostgreSQL
-> Create a database called pos_db:
   createdb pos_db
-> Update your .env file:
   DATABASE_URL=postgresql://postgres:password@localhost:5432/pos_db
    STRIPE_SECRET_KEY=sk_test_your_key
    STRIPE_PUBLIC_KEY=pk_test_your_key

Run Backend
python3 app.py
API should be running on http://localhost:5000.

Run Frontend
Open frontend/index.html in the browser.

API Endpoints
Products
* GET /products/ -> List products
* POST /products/ -> Add product

Orders
* POST /orders/ -> Create order
* GET /orders/<id>/ -> Get order details

Checkout
* POST /checkout/ -> Process payment via Stripe

🧪 Testing
* Import POS_Order_System.postman_collection.json into Postman.
* Run the pre-configured requests for /products, /orders, /checkout.

📸 Screenshots (To Add Later)
I. Products List (UI)
II. Checkout with Stripe (UI/API)
III. Database Orders Table

📦 Deployment
Build & run with Docker:
docker build -t pos-order-system .
docker run -p 5000:5000 pos-order-system

Deploy easily to Render or Railway (supports Postgres + Docker).

🎯 Learning Objectives

This project was built to demonstrate:
* Designing & building business applications (POS).
* Integrating with payment gateways.
* Building intuitive UIs with JS & XML.
* Backend optimization with PostgreSQL + ORM.
* End-to-end deployment and accountability for features.

👤 Author

Modeste Ciira
GitHub: Modeste74
LinkedIn: Modeste Ciira