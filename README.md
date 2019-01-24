# mcd - memorizable 'change directory'

Copyright 2019 SiLeader.

## features
+ save the path
+ bash completion
+ move to the path by the alias name

## usage
### save
```bash
mcd --save ALIAS_NAME  # 1
mcd --save --directory /path/to/directory ALIAS_NAME  # 2
```

1. save current directory as ALIAS_NAME
1. save `/path/to/directory` as ALIAS_NAME

### move
```bash
mcd ALIAS_NAME
```

## install
1. clone this repository
1. write `source /path/to/repository/move.sh` to your .bashrc or .bash_profile

## license
GPL v3.0

See LICENSE.
