export FLASK_APP='app:create_app(config_name)'
export MAIL_USERNAME='koinangeagnes@gmail.com'
export MAIL_PASSWORD='0708042343'
# export FLASK_CONFIG='development'
# export FLASK_APP='manage.py'
export FLASK_APP = "manage.py"
export APP_SETTINGS="development"

python3 manage.py server
