clean:
	rm -f db.sqlite3

create_database:
	./manage.py syncdb --noinput
	./manage.py migrate --noinput
	./manage.py createsuperuser --username=root --email=root@goodslist.com

make_fixtures:
	DJANGO_SETTINGS_MODULE='goodslist.settings' python initialtodb.py

all: clean create_database make_fixtures