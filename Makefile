# DATAGERRY Data Checker
# Copyright (C) 2020 NETHINKS GmbH
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# set environment variables
BIN_PYINSTALLER = pyinstaller
BIN_PIP = pip
BIN_RPMBUILD = rpmbuild
DIR_BUILD = $(CURDIR)/target
DIR_BIN_BUILD = ${DIR_BUILD}/bin
DIR_TEMP= ${DIR_BUILD}/temp
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

# create Docker image
.PHONY: docker
docker: bin
	mkdir -p ${DIR_DOCKER_BUILD}
	mkdir -p ${DIR_DOCKER_BUILD}/src
	mkdir -p ${DIR_DOCKER_BUILD}/src/files
	cp contrib/docker/Dockerfile ${DIR_DOCKER_BUILD}/src
	cp ${DIR_BIN_BUILD}/dg-data-checker ${DIR_DOCKER_BUILD}/src/files
	docker build -f ${DIR_DOCKER_BUILD}/src/Dockerfile -t nethinks/dg-data-checker ${DIR_DOCKER_BUILD}/src

# clean environment
.PHONY: clean
clean:
	rm -Rf ${DIR_BUILD}
	rm -f datagerry.spec

