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

import datachecker.output

class DataCheckOrganizer:

    def __init__(self, input_data):
        self.__input_data = input_data

    def check_data(self):
        # get checknames from the first dataset
        checks = []
        if len(self.__input_data) > 0:
            for checkname in self.__input_data[0]["variables"]:
                checks.append(checkname)

        # organize data checks and create output report
        report = "DATAGERRY data check\n"
        report+= "====================\n"
        report+= "\n"
        for checkname in checks:
            report+= checkname + "\n"
            report+= "---------------------------\n"
            if checkname.startswith("check_duplicate"):
                checker = DuplicateDataCheck(self.__input_data, checkname)
                report+= checker.check()

        # output report
        output = datachecker.output.TextfileOutput()
        output.write_output(report)


class DataCheck:

    def __init__(self, input_data, checkname):
        self._input_data = input_data
        self._checkname = checkname

    def check(self):
        pass


class DuplicateDataCheck(DataCheck):

    def check(self):
        # duplicate check:
        results = {}
        for dataset in self._input_data:
            object_id = dataset["object_id"]
            value = dataset["variables"][self._checkname]
            if value not in results:
                results[value] = []
            results[value].append(object_id)

        # create output report
        output = ""
        for element in results:
            if len(results[element]) > 1:
                output+= element + ": \n"
                for element_id in results[element]:
                    output+= "- Object ID: " + element_id + "\n"
                output += "\n"
        return output
