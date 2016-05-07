# flask_exploration
specify
DATABASE_URL
APP_SETTINGS
example
export APP_SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='postgresql://localhost/discover_flask_dev'

autoenv (directory specific environment control)
flask-migrate

woah woah woah, sqlalchemy writes migrations for you?
Alembic is the bones under flask-migrate

sudo ln -s /Library/PostgreSQL/9.2/lib/libssl.1.0.0.dylib /usr/lib && sudo ln -s /Library/PostgreSQL/9.2/lib/libcrypto.1.0.0.dylib /usr/lib

http://stackoverflow.com/questions/16407995/psycopg2-image-not-found
got to part 17, postgres being obnoxious

if psycopg2 error re-emerges, try deactivating anaconda from bashprofile

which python : informs which environment python is being pulled from, homebrew python (/usr/local/bin/python) is important.

