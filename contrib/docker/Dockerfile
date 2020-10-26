FROM centos:8
LABEL maintainer="monitoring@nethinks.com"

# set locale
ARG build_locale=en_US

# install dg-data-checker
COPY files/dg-data-checker /opt
RUN yum -y install glibc-locale-source glibc-langpack-en \
    && localedef -c -i ${build_locale} -f UTF-8 ${build_locale}.utf-8

# set locale
ENV LANG ${build_locale}.utf8

# start DATAGERRY
CMD ["/opt/dg-data-checker"]
