import sae
import os
from manage import app

application = sae.create_wsgi_app(app)