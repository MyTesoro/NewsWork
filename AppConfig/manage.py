from AppConfig import AppConfigSettings
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from AppConfig.AppConfigSettings import app, db


@app.route('/')
def index():
    return 'index'


manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server("127.0.0.1", port=5001), debug=True)

if __name__ == '__main__':
    manager.run()
