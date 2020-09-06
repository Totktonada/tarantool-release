# tarantool-release

Tiny build infrastructure for tarantool-release RPM packages.

Uses [packpack](https://github.com/packpack/packpack).

## How to build and deploy packages

Fill `env` file (see `env.example`).

Run `./build.sh`.

TBD: Setup CI.

## How to use packages

It assumes that `${S3_TARGET_DIR}` is publicly available as
`https://download-test.tarantool.org`.

CentOS 7:

```shell
# Install repositories.
yum install https://download-test.tarantool.org/tarantool-release-7-latest.el7.noarch.rpm

# Install yum-config-manager.
yum install yum-utils

# Enable tarantool-2.4 repository.
yum-config-manager --enable tarantool-2.4

# Install tarantool.
yum install tarantool
```

Fedora 30:

```shell
# Install repositories.
dnf install https://download-test.tarantool.org/tarantool-release-30-latest.fc30.noarch.rpm

# Install yum-config-manager.
dnf install 'dnf-command(config-manager)'

# Enable tarantool-2.4 repository.
dnf config-manager --enable tarantool-2.4

# Install tarantool.
dnf install tarantool
```

TBD: Redeploy to production storage, replace `download-test.tarantool.org` with
`download.tarantool.org`.

## TODO

Deploy those packages (but not 'latest' ones) into tarantool repositories as
well to provide automatic updates of repositories list when any of them is
enabled.
