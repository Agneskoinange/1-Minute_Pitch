export FLASK_APP="app:create_app(config_name)"
export MAIL_USERNAME="koinangeagnes@gmail.com"
export MAIL_PASSWORD="0708042343"

# # export FLASK_CONFIG='development'

export FLASK_APP="manage.py"

# # export FLASK_APP = "manage.py"
# # export APP_SETTINGS="development"
# # export SQLALCHEMY_DATABASE_URL=os.getenv('DATABASE_URL')

export SQLALCHEMY_TRACK_MODIFICATIONS="False"
export SECRET_KEY="agnes12345"

# # export PYTHONHOME="/home/nessie/.local/lib/python3.8"
# # export PYTHONPATH="${PYTHONHOME}/bin"
# # ./configure --prefix='/home/nessie/.local'

python3 manage.py server
