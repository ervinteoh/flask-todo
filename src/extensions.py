"""Extensions initialization.

This module initializes all the Flask extensions used in the
application. The extension is initialized in the application instance
in the application factory method `register_extensions`.

Notes
-----
Do not define any functions in this module. This module's only purpose
is initializing the extensions required for the application.
"""

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login_manager = LoginManager()
db = SQLAlchemy()
migrate = Migrate()
