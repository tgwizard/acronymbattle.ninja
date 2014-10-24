# Acronym Battle Ninja!

A soon-to-be awesome competition site, [acronymbattle.ninja](http://acronymbattle.ninja).

## Development

1. Install VirtualBox: https://www.virtualbox.org/wiki/Downloads
2. Install Vagrant: https://www.vagrantup.com/downloads.html

Then:

```bash
git clone git@github.com:tgwizard/acronymbattle.ninja.git
cd acronymbattle.ninja
vagrant up
vagrant ssh
python src/runserver.py
```

And browse to http://localhost:9123/

### Deployment

Push to master, CircleCI automatically deploys to Heroku.
