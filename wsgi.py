import web
from main import app

web.config.debug = False
application = app.wsgifunc()
