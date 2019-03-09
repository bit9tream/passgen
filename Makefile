all: install

install:
	cp main.py /usr/bin/passgen

uninstall:
	rm /usr/bin/passgen
