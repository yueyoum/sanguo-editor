#!/bin/bash

dump() {
    declare -a arr
    arr=(`echo "$1" | tr ':', ' '`)
    echo ${arr[@]}
    python manage.py dumpdata ${arr[0]} --indent=4 > fixtures/${arr[1]}
}


while read LINE
do
    dump "$LINE"
done < datatable

python dump_package.py

exit $?

