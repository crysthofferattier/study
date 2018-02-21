# Docker install

## Installation

* Ubuntu 16.04 LTS x64

## Get Docker CE for Ubuntu 

### Docker wiki installation [here](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)

### Uninstall old versions

```
$ sudo apt-get remove docker docker-engine docker.io
```

### Install using the repository

#### SET UP THE REPOSITORY

* Update the apt package index:

```
$ sudo apt-get update
```

* Install packages to allow apt to use a repository over HTTPS:

```
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
```

* Add Docker’s official GPG key:

```
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

* Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

```
$ sudo apt-key fingerprint 0EBFCD88

pub   4096R/0EBFCD88 2017-02-22
      Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
uid                  Docker Release (CE deb) <docker@docker.com>
sub   4096R/F273FCD8 2017-02-22
```

* Use the following command to set up the stable repository. You always need the stable repository, even if you want to install builds from the edge or test repositories as well. To add the edge or test repository, add the word edge or test (or both) after the word stable in the commands below.
x86_64 / amd64

```
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

### INSTALL DOCKER CE
* Update the apt package index.

```
$ sudo apt-get update
```

* Install the latest version of Docker CE, or go to the next step to install a specific version. Any existing installation of Docker is replaced.

```
$ sudo apt-get install docker-ce
```

## Install from a package

If you cannot use Docker’s repository to install Docker CE, you can download the .deb file for your release and install it manually. You need to download a new file each time you want to upgrade Docker CE.

 * Go to https://download.docker.com/linux/ubuntu/dists/, choose your Ubuntu version, browse to pool/stable/ and choose amd64, armhf, ppc64el, or s390x. Download the .deb file for the Docker version you want to install.

Note: To install an edge package, change the word stable in the URL to edge. Learn about stable and edge channels.

* Install Docker CE, changing the path below to the path where you downloaded the Docker package.

```
$ sudo dpkg -i /path/to/package.deb
```

The Docker daemon starts automatically.

* Verify that Docker CE is installed correctly by running the hello-world image.

```
$ sudo docker run hello-world
```