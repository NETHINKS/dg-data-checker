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

import gunicorn.app.base

class WebApplication(gunicorn.app.base.BaseApplication):
    """Wrapper for gunicorn startup
    Args:
        - application: wsgi app
        - options: dict with gunicorn options
    """

    def __init__(self, application, options):
        """initialization method"""
        self.options = options or {}
        self.application = application
        super(WebApplication, self).__init__()

    def load_config(self):
        """loads the configuration"""
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        """loads the application"""
        return self.application
