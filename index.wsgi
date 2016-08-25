import sae
import os
from manage import app

sae.add_vendor_dir('venv/lib/site-packages')
application = sae.create_wsgi_app(app)