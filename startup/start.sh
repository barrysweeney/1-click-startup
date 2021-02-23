sudo mkdir /var/lib/ipa-data
echo "172.17.0.1  host.docker.internal" | sudo tee -a /etc/hosts
echo "127.0.0.1  ipa.d.test" | sudo tee -a /etc/hosts
sudo docker run --name my-selenium-container -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-firefox:4.0.0-beta-1-prerelease-20210210
sudo docker run --name my-nextcloud-container -d -p 9000:80 -e NEXTCLOUD_ADMIN_USER=admin -e NEXTCLOUD_ADMIN_PASSWORD=password nextcloud
sudo docker run -h ipa.d.test --name my-freeipa-container -d -p 80:80 -p 443:443 -p 389:389 -v /sys/fs/cgroup:/sys/fs/cgroup:ro -v /var/lib/ipa-data:/data:Z -e PASSWORD=Secret123 --sysctl net.ipv6.conf.all.disable_ipv6=0 freeipa/freeipa-server:centos-8-4.8.7 ipa-server-install -U -r D.TEST --no-ntp
#sudo docker run --name my-autoadmin-container barrysweeney/auto-admin



