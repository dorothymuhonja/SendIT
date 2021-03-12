from  app import create_app, db
from app.models import User, Parcel, Role
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('productions')
manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Parcel=Parcel, Role=Role)


manager.add_command('server', Server)
@manager.command
def test():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

if __name__ == '__main__':
    manager.run()
