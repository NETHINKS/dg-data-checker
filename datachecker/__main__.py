#!/usr/bin/env python
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

import datachecker.gunicornsupport
import datachecker.dispatcher

def main():
    webapp_conf = {
        "bind": "0.0.0.0:5000",
        "workers": "2"
    }
    webapp = datachecker.gunicornsupport.WebApplication(datachecker.dispatcher.app, webapp_conf)
    webapp.run()


if __name__ == "__main__":
    main()
