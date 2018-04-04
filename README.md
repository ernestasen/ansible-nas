# Ansible NAS
After trying FreeNAS and OpenMediaVault I decided to create my own NAS solution. Here's why:
- I didn't like the idea of managing my server with BSD (FreeNAS) because I am more familiar with Debian based systems.
- OpenMediaVault seemed like a good alternative to FreeNAS, but after trying it I couldn't successfully find/install some of the plugins. I started few Docker containers to get my desired functionality alongside OMV and it seemed a little messy to switch between Docker based and Web based plugin management. In the end I decided to run all the plugins myself via Docker and be in full control of the whole system without depending on OMV releases.
- I found `davestephens`\\[`ansible-nas`](https://github.com/davestephens/ansible-nas) repo which seemed like a perfect start for my NAS server.
- I like building things with Ansible!

## What This Provides
 * Creates RAIDs from two or more HDDs attached to your NAS
 * Creates partitions from single HDDs attached to your NAS (in my case for Time Machine)
 * Creates Samba shares for you to store your stuff
 * Creates\\Removes Docker containers:
    - [Plex Media Server](https://www.plex.tv/) for Media streaming and management
    - [Sonarr](https://sonarr.tv/) for downloading and managing TV shows
    - [Radarr](https://radarr.video/) for downloading and managing movies
    - [Jackett](https://github.com/Jackett/Jackett) for translating Sonarr and Radarr queries to tracker-site-specific HTTP queries
    - [Transmission](https://transmissionbt.com/) BitTorrent client (with OpenVPN if you have a supported VPN provider)
    - [Duplicati](https://www.duplicati.com/) for backing up stuff
    - [Time Machine](https://github.com/odarriba/docker-timemachine) for backing up macOS to NAS server
    - [Glances](https://nicolargo.github.io/glances/) for seeing the state of the system using a web browser
    - [Portainer](https://portainer.io/) for managing Docker and running custom images
    - [Nginx](https://www.nginx.com/) for proxy passing domain names to Docker containers on NAS server

## Creating RAIDs and partitions
I decided to include tasks for creating disk partitions mostly for testing purposes using Vagrant. However, since I applied this config for new system with new HDDs, I didn't really care about data integrity on my hard drives.

:heavy_exclamation_mark: I only recommend using `mdadm` and `parted` roles for Vagrant or entirely new systems, because getting partitioning wrong can be incredibly destructive.

## Hardware
Ansible NAS should work on any recent Debian box. Development was done on Debian Stretch.

## How To Use
1. `git clone https://www.github.com/ernestasen/ansible-nas && cd ansible-nas`
2. Copy `roles/nas/defaults/main.yml` to `group_vars/nas.yml`
3. Edit `group_vars/nas.yml` and update variables based on your needs
5. Edit `hosts` file and update it with your NAS box hostname, IP and remote user
6. Run the playbook: `ansible-playbook -i hosts playbook.yml`

## How To Test
1. Install Vagrant and VirtualBox
2. `git clone https://www.github.com/ernestasen/ansible-nas && cd ansible-nas`
3. Copy `roles/nas/defaults/main.yml` to `group_vars/vagrant.yml`
4. Edit `group_vars/vagrant.yml` and update variables based on your needs
5. `vagrant up`

## To Do
See Issues
