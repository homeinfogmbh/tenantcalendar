FILE_LIST = ./.installed_files.txt

.PHONY: pull push clean install uninstall

default: | pull clean generate-bindings install

install:
	@ ./setup.py install --record $(FILE_LIST)

uninstall:
	@ while read FILE; do echo "Removing: $$FILE"; rm "$$FILE"; done < $(FILE_LIST)

clean:
	@ rm -Rf ./build

pull:
	@ git pull

push:
	@ git push

generate-bindings:
	@ pyxbgen -u tenantcalendar.xsd -m dom --module-prefix=tenantcalendar
