import pyctuator
from flask import current_app, _app_ctx_stack


class Pyctuator(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('PYCTUATOR')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        return pyctuator.connect(current_app.config['PYCTUATOR'])

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'pyctuator'):
            ctx.pyctuator.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'pyctuator'):
                ctx.pyctuator = self.connect()
            return ctx.pyctuator