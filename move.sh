#!/usr/bin/env bash

# Copyright 2019 SiLeader.
# Licensed under the GNU General Public License 3.0

array_check () {
    check=$1
    if [ -z "$check" ];then
        return 1
    fi
    if [ -z "$2" ];then
        return 1
    fi

    for i in ${check[@]};do
        if [ $2 = $i ];then
            return 0
        fi
    done
    return 1
}

function mcd() {
    if array_check "$*" '--aliases' || array_check "$*" '--list' || array_check "$*" '--help' || array_check "$*" '-h' ; then
        $(cd $(dirname ${BASH_SOURCE:-$0}); pwd)/__mcd.py $*
    else
        path=`$(cd $(dirname ${BASH_SOURCE:-$0}); pwd)/__mcd.py $*`
        if [[ $? = 1 ]]; then
            cd ${path}
        fi
    fi
}

__mcd_comp() {
    COMPREPLY=( $(compgen -W "$(mcd --aliases)" ${COMP_WORDS[COMP_CWORD]}  ) )
}

complete -o default -F __mcd_comp mcd

export PATH="$(cd $(dirname ${BASH_SOURCE:-$0}); pwd):$PATH"
