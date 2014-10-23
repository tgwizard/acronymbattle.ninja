VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 9123, host: 9123
  config.vm.synced_folder ".", "/vagrant"

  config.vm.provision :shell, path: "bootstrap.sh"
  config.vm.provision :shell, path: "bootstrap-user.sh", privileged: false
end
