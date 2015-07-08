#!/bin/bash
DIR='/opt/ddis/logs/'
for host in `cat /opt/ddis/scripts/Ka_hostnames_for_flag`
do
  if [ -d ${DIR}/${host} ]
  then
      touch ${DIR}/${host}/collect-log
      echo flag added to $host 
  else
      echo "host not matching"
  fi
done
echo "flag creation complited!"
