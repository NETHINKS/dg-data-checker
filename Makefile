# set environment variables
BIN_PYINSTALLER = pyinstaller
BIN_PIP = pip
BIN_RPMBUILD = rpmbuild
DIR_BUILD = $(CURDIR)/target
DIR_BIN_BUILD = ${DIR_BUILD}/bin
DIR_TEMP= ${DIR_BUILD}/temp
DIR_RPM_BUILD = ${DIR_BUILD}/rpm
DIR_DOCKER_BUILD = ${DIR_BUILD}/docker

# set default goal
.DEFAULT_GOAL := all

# build whole application
.PHONY: all
all: bin docker


# install Python requirements
.PHONY: requirements
requirements:
	${BIN_PIP} install -r requirements.txt

# create onefile binary of dg-data-checker
.PHONY: bin
bin: requirements
	${BIN_PYINSTALLER} --name dg-data-checker --onefile \
		--distpath ${DIR_BIN_BUILD} \
		--workpath ${DIR_TEMP} \
		--hidden-import gunicorn.glogging \
		--hidden-import gunicorn.workers.sync \
		datachecker/__main__.py

# clean environment
.PHONY: clean
clean:
	rm -Rf ${DIR_BUILD}
	rm -Rf ${DIR_DOCS_TARGET}/*
	rm -Rf ${DIR_WEB_TARGET}/*
	rm -f datagerry.spec

