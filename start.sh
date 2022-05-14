export FLASK_APP="app:create_app(config_name)"
export MAIL_USERNAME="koinangeagnes@gmail.com"
export MAIL_PASSWORD="0708042343"
export FLASK_APP="manage.py"
export SQLALCHEMY_TRACK_MODIFICATIONS="False"
export SECRET_KEY="agnes12345"
export DATABASE_URL='postgres://ujtnrslaktjpyi:b52d078974eb49e0830d8e14804be58c80ed4f68ec138480c2d769067adcfe11@ec2-3-229-11-55.compute-1.amazonaws.com:5432/ddg1ec44crtdea'

python3 manage.py server
