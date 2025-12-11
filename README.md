# Boson-S3 Buildroot

#### Checking out and building the project:

run the following commands to create a project directory and checkout the project.

```shell
mkdir -p ~/boson/downloads
cd ~/boson
sudo apt-get update
sudo apt-get -y install build-essential bc gcc g++ patch binutils unzip rsync wget bzip2 gzip perl gcc-multilib g++-multilib libssl-dev
wget -O ~/boson/downloads/buildroot-2024.02.tar.gz https://buildroot.org/downloads/buildroot-2024.02.tar.gz
tar -xaf ~/boson/downloads/buildroot-2024.02.tar.gz
git clone https://github.com/groupgets/boson-s3-dev-sw.git
```

Run the following commands to start the build.

```shell
cd buildroot-2024.02
make BR2_EXTERNAL=../boson-s3-dev-sw/buildroot/ boson_s3_dev_defconfig
export BR2_DL_DIR=~/boson/downloads/
make
```

Once the build completes the finished image can be found in
- ~/boson/buildroot-2024.02/output/images/sdcard.img



#### Flashing the Build to uSD card:

The simplest way to flash the image to an SD card is by using the flashing utility BalenaEtcher.

BalenaEtcher can be downloaded and installed by using the following link.
- https://etcher.balena.io/

Once BalenaEtcher is installed run the utility.  Select Flash From File and browse to the image location.  Click on the Select Target button and select the uSD card as the target.
Then click the Flash Button.




#### Powering up and booting the board:

Insert the uSD card into the Boson camera board.  Plug in an Ethernet cable to the camera board and
connect to a PoE switch or PoE injector.  Either can be used to power the camera board.  The board will power on and boot.
Give the camera board about 30 seconds to boot and obtain an IP address.  By default the IP is set to DHCP.  This can be changed later if a static IP address is desired.

mDNS is enabled on the board so you do not need to know the ip address that the board is assigned.  Open a web browser and enter "http://boson-s3" into the address bar.
This will allow you to log into the embedded web page to control and view the camera.  The embedded web page is password protected.  The default username and password are;

- username:  admin
- password:  password

The username and password can be changed through the Web UI.

The user can ssh into the operating system simply by using the name "boson-s3" instead of the assigned IP address.  The username and password for Linux is as follows;

- username: root
- password: dev

IP configuration is found in the filesystem at `/etc/systemd/network/eth0.network`


#### Streaming Video

The video can be viewed either through the embedded web interface or by using any media player that is capable of playing an rtsp stream.  The rtsp stream can be accessed
by using the address rtsp://boson-s3:8554/stream.
