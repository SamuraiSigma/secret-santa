#!/bin/bash
# Creates a Python virtualenv in the current dierctory.

set -e

# Project's directory
DIR=`cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd`

# File containing requirements
REQ="$DIR/doc/requirements.txt"

# Files/directories installed by this script
VENV_FILES="bin include lib lib64 man share pip-selfcheck.json pyvenv.cfg"

PYTHON_VER="python3"  # Python version to use
PIP_VER="pip3"        # Pip version to use

# ---------------------------------------------------------------------
# Shows how to use the script.

function usage {
    echo -e "\e[1mUSAGE\e[0m"
    echo -e "\t./`basename $0` [\e[1m-h\e[0m] [\e[1m-r\e[0m]\n"

    echo -e "\e[1mDESCRIPTION\e[0m"
    echo -e "\tCreates a Python virtualenv in the current directory."
    echo -e "\tAlso installs any requirements in '$REQ'.\n"

    echo -e "\e[1mOPTIONS\e[0m"
    echo -e "\tSeparate each option with a blank space.\n"
    echo -e "\t\e[1m-h\e[0m\tShows how to use this script, leaving it afterwards.\n"
    echo -e "\t\e[1m-r\e[0m\tRemoves all files installed by this script," \
            "leaving it afterwards."
}

# =====================================================================

# Command line arguments
for arg in "$@"; do
    case $arg in
    -h|--help)
        usage
        exit 0;;
    -r)
        rm -rf $VENV_FILES
        echo "Successfully removed all virtualenv-related files!"
        exit 0;;
    *)
        >&2 echo "Unrecognized option '$arg'"
        exit 1;;
    esac
done

echo -e "\e[36m>> Creating virtualenv\e[0m"
$PYTHON_VER -m venv $DIR
if [ -f "$REQ" ]; then
    source $DIR/bin/activate
    echo -e "\e[36m>> Installing requirements contained in $REQ\e[0m"
    $PIP_VER install --upgrade pip
    $PIP_VER install wheel
    $PIP_VER install -r $REQ
fi

echo -e "\e[36m>> Done!\e[0m"
