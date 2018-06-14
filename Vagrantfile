Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |v|
    v.name = "pOrtals::reconLIVE:AV"
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.box = "debian/stretch64"
  config.vm.network "private_network", ip: "192.168.50.42"
  #config.vm.network "public_network", use_dhcp_assigned_default_route: true
  config.vm.synced_folder ".", "/workspace", type: "rsync", rsync__exclude: ".git/"
  config.vm.provision "shell", path: "config/vm_setup.sh"
end
