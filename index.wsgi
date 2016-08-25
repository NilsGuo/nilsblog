import sae
import os
import sys
absolute_path = os.path.abspath(__file__)
app_path = os.path.dirname(absolute_path)
path = os.path.join(app_path, 'site-packages')
sys.path.insert(0, path)
sys.path.insert(0, app_path)

from manage import app
application = sae.create_wsgi_app(app)