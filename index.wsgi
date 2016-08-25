import sae
from manage import app

sae.add_vendor_dir('/venv')
application = sae.create_wsgi_app(app)