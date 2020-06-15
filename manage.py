import AppConfigSettings
from flask import session


@AppConfigSettings.app.route('/')
def index():
    session['name'] = 'admin'
    return 'index'


if __name__ == '__main__':
    AppConfigSettings.app.run(port=5001)
