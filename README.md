# dg-data-checker
A small plugin for DATAGERRY to find duplicate entries

## functionality
This is a small plugin for DATAGERRY to perform some data check on existing objects. Currently, duplicate field entries
can be found. A report with the name dg-data-checker\_report.txt will be generated.

## usage
This tool is designed to be used as Docker image and a plugin for DATAGERRY exportd.

* create a new exportd job
* choose ExternalSystemGenericRestCall as destination
* for every check add an export variable. The variable name of duplicate checks needs to be `check_duplicate_xyz`

Have a look into the contrib/docker/docker-compose.yml file to get a starting point


