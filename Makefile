runserver:
	. venv/bin/activate; python manage.py runserver 0.0.0.0:8000

migrate:
	. venv/bin/activate; python manage.py migrate --all

test:
	. venv/bin/activate; python manage.py test ieis --color --nologcapture --liveserver=127.0.0.1:8001-8010

ci_test:
	python manage.py test ieis --color --nologcapture --liveserver=127.0.0.1:8001-8010

pep8:
	pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  ieis/

pyflakes:
	pylama --skip=*migrations* -l pyflakes ieis/

pipinstall:
	. venv/bin/activate; pip install -r requirements.txt
