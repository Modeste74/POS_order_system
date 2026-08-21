from flask_migrate import Migrate
from backend.database import db
from backend.app import create_app
from backend import models

app = create_app()

# attach flask-migrate
migrate = Migrate(app, db)

# @app.shell_context_processor
# def make_shell_context():
#     return {"db": db, "app": app}

if __name__ == "__main__":
	app.run()