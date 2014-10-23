set -e

virtualenv env
source env/bin/activate
pip install -r /vagrant/requirements.txt