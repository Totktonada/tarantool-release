#!/bin/sh

set -exu

. ./env

distros="
    el:6
    el:7
    el:8
    fedora:25
    fedora:26
    fedora:27
    fedora:28
    fedora:29
    fedora:30
    fedora:31
"

if ! type packpack; then
    echo "Unable to find packpack"
    exit 1
fi

if [ -f build ]; then
    echo "Please, clean up build/ directory"
    exit 1
fi

# Bump it at rebuild.
#
# FIXME: We can use commits number as 'Release' tag value.
export RELEASE=1

function deploy() {
    aws s3 cp                                \
        --endpoint-url "${S3_ENDPOINT_URL}"  \
        --acl public-read                    \
        "${1}" "s3://${S3_TARGET_DIR}/$(basename "${1}")"
}

for distro in $distros; do
    export OS="${distro%%:*}"
    export DIST="${distro#*:}"
    export VERSION="${DIST}"

    packpack

    if [ "${OS}" = "el" ]; then
        RELEASE_SUFFIX=".el${DIST}"
    elif [ "${OS}" = "fedora" ]; then
        RELEASE_SUFFIX=".fc${DIST}"
    else
        false
    fi

    PKG=build/tarantool-release-${VERSION}-${RELEASE}${RELEASE_SUFFIX}.noarch.rpm
    PKG_LATEST=build/tarantool-release-${VERSION}-latest${RELEASE_SUFFIX}.noarch.rpm
    cp -i ${PKG} ${PKG_LATEST}

    deploy "${PKG}"
    deploy "${PKG_LATEST}"

    rm -r build
done
