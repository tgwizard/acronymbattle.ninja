set -e

virtualenv env
source env/bin/activate
pip install -r /vagrant/requirements.txt

grep "cd /vagrant" .bashrc > /dev/null || echo "cd /vagrant" >> .bashrc
grep ". /home/vagrant/env/bin/activate" .bashrc > /dev/null || echo ". /home/vagrant/env/bin/activate" >> .bashrc