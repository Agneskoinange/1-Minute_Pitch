from app import create_app, db
from app.models import Comments, Pitches, UpVote, DownVote, User
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import models


#createapp instance
app = create_app('development')
# app = create_app('test')
# app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitches=Pitches, Comments=Comments, UpVote=UpVote, DownVote=DownVote)

if __name__ == '__main__':
    app.config['SECRET_KEY']="agnes12345"
    manager.run()