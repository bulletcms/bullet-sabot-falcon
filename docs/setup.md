# Setup

## Installation

- Install docker
  - example on archlinux: `$ sudo pacman -S docker`
- To start docker service
```zsh
$ sudo systemctl start docker
```
- To start docker service on boot
```zsh
$ sudo systemctl enable docker
```
- To give user privliges to build and run docker
```zsh
$ usermod -a -G docker USER
```

## Build

```zsh
$ ./build.sh
```


## Run

- Start 1 container
```zsh
$ ./start.sh
```
- Start 3 containers
```zsh
$ ./start3.sh
```
- Stop 1 container
```zsh
$ ./stop.sh
```
- Stop 3 containers
```zsh
$ ./stop3.sh
```


## Test
- Build the virtual env
```zsh
$ ./venv_setup.sh
```
- Run using the virtual env
```zsh
$ ./test-run.sh
```
- Make an http request
```zsh
$ curl localhost:5000/api/pages
```
