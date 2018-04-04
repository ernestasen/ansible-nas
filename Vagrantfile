# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "vagrant" do |nas|
    nas.vm.box = "debian/stretch64"
    nas.vm.network "public_network", bridge: "en0: Wi-Fi (AirPort)"
    nas.vm.provider :virtualbox do |v|
      v.customize ["modifyvm", :id, "--name", "nas", "--memory", "4096"]
      v.customize ["createhd", "--filename", "/tmp/wd1.vdi", "--size", 10 * 1024]
      v.customize ["storageattach", :id, "--storagectl", "SATA Controller", "--port", 1, "--device", 0, "--type", "hdd", "--medium", "/tmp/wd1.vdi"]
      v.customize ["createhd", "--filename", "/tmp/wd2.vdi", "--size", 10 * 1024]
      v.customize ["storageattach", :id, "--storagectl", "SATA Controller", "--port", 2, "--device", 0, "--type", "hdd", "--medium", "/tmp/wd2.vdi"]
      v.customize ["createhd", "--filename", "/tmp/sm1.vdi", "--size", 1 * 1024]
      v.customize ["storageattach", :id, "--storagectl", "SATA Controller", "--port", 3, "--device", 0, "--type", "hdd", "--medium", "/tmp/sm1.vdi"]
    end
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "nas.yml"
    ansible.extra_vars = {
      nginx_server: "{{ ansible_eth1.ipv4.address }}",
    }
  end
end
