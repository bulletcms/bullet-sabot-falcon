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

```zsh
$ ./run.sh
```


## Test

```zsh
$ curl localhost:5000
# response: Hello World!
```
