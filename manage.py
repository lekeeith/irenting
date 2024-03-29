from ihome import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(1)

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/index")
def index():
    return "index page"


if __name__ == "__main__":
    manager.run
