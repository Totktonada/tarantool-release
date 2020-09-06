%if 0%{?rhel} > 0
%global pkgman yum
%global repoman yum-config-manager
%global repoman_install yum install yum-utils
%endif
%if 0%{?fedora} > 0
%global pkgman dnf
%global repoman dnf config-manager
%global repoman_install dnf install 'dnf-command(config-manager)'
%endif

%global suggested_repository tarantool-2.4

# /etc/pki/rpm-gpg
%global build_gpg_dir %{buildroot}%{_sysconfdir}/pki/rpm-gpg
%global gpg_dir %{_sysconfdir}/pki/rpm-gpg

# /etc/yum.repos.d
%global build_repos_dir %{buildroot}%{_sysconfdir}/yum.repos.d
%global repos_dir %{_sysconfdir}/yum.repos.d

Name: tarantool-release
%if 0%{?rhel} > 0
Version: %{rhel}
%endif
%if 0%{?fedora} > 0
Version: %{fedora}
%endif
Release: 1%{?dist}
BuildArch: noarch
URL: https://tarantool.org
Group: Applications/Databases
%if 0%{?rhel} > 0
Summary: YUM configuration for tarantool repository
%endif
%if 0%{?fedora} > 0
Summary: DNF configuration for tarantool repository
%endif
License: BSD
Source0: tarantool-release-${version}.tar.xz

Requires: /etc/yum.repos.d

# It is not clear whether we actually want to depend on packages
# from EPEL repository, but it worth to be on the safe side and
# enable it now.
#
# See https://github.com/tarantool/tarantool/issues/4611
%if 0%{?rhel} > 0
Requires: epel-release = %{rhel}
%endif

%description
This package contains %{pkgman} configuration for the tarantool
RPM repositories, as well as the public GPG keys used to sign them.

The repositories are not enabled after installation, so you must use
the --enablerepo=%{suggested_repository} option for %{pkgman}.

Alternatively you can install %{repoman} to enable or disable
certain repositories.

%{repoman_install}
%{repoman} --enable %{suggested_repository}

%prep
%setup -q -n %{name}-%{version}

%if 0%{?rhel} > 0
sed -i -e 's/@OS@/el/g' tarantool*.repo
sed -i -e 's/@DIST@/%{rhel}/g' tarantool*.repo
%endif
%if 0%{?fedora} > 0
sed -i -e 's/@OS@/fedora/g' tarantool*.repo
sed -i -e 's/@DIST@/%{fedora}/g' tarantool*.repo
%endif

sed -e 's/@RELEASE_SERIES@/1.10/g' tarantool.repo > tarantool-1.10.repo
sed -e 's/@RELEASE_SERIES@/2.1/g'  tarantool.repo > tarantool-2.1.repo
sed -e 's/@RELEASE_SERIES@/2.2/g'  tarantool.repo > tarantool-2.2.repo
sed -e 's/@RELEASE_SERIES@/2.3/g'  tarantool.repo > tarantool-2.3.repo
sed -e 's/@RELEASE_SERIES@/2.4/g'  tarantool.repo > tarantool-2.4.repo
sed -e 's/@RELEASE_SERIES@/2.5/g'  tarantool.repo > tarantool-2.5.repo
sed -e 's/@RELEASE_SERIES@/2.6/g'  tarantool.repo > tarantool-2.6.repo

sed -e 's/@RELEASE_SERIES@/1.10/g' tarantool-live.repo > tarantool-1.10-live.repo
sed -e 's/@RELEASE_SERIES@/2.1/g'  tarantool-live.repo > tarantool-2.1-live.repo
sed -e 's/@RELEASE_SERIES@/2.2/g'  tarantool-live.repo > tarantool-2.2-live.repo
sed -e 's/@RELEASE_SERIES@/2.3/g'  tarantool-live.repo > tarantool-2.3-live.repo
sed -e 's/@RELEASE_SERIES@/2.4/g'  tarantool-live.repo > tarantool-2.4-live.repo
sed -e 's/@RELEASE_SERIES@/2.5/g'  tarantool-live.repo > tarantool-2.5-live.repo
sed -e 's/@RELEASE_SERIES@/2.6/g'  tarantool-live.repo > tarantool-2.6-live.repo

sed -e 's/@RELEASE_SERIES@/1.10/g' tarantool-source.repo > tarantool-1.10-source.repo
sed -e 's/@RELEASE_SERIES@/2.1/g'  tarantool-source.repo > tarantool-2.1-source.repo
sed -e 's/@RELEASE_SERIES@/2.2/g'  tarantool-source.repo > tarantool-2.2-source.repo
sed -e 's/@RELEASE_SERIES@/2.3/g'  tarantool-source.repo > tarantool-2.3-source.repo
sed -e 's/@RELEASE_SERIES@/2.4/g'  tarantool-source.repo > tarantool-2.4-source.repo
sed -e 's/@RELEASE_SERIES@/2.5/g'  tarantool-source.repo > tarantool-2.5-source.repo
sed -e 's/@RELEASE_SERIES@/2.6/g'  tarantool-source.repo > tarantool-2.6-source.repo

sed -e 's/@RELEASE_SERIES@/1.10/g' tarantool-live-source.repo > tarantool-1.10-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.1/g'  tarantool-live-source.repo > tarantool-2.1-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.2/g'  tarantool-live-source.repo > tarantool-2.2-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.3/g'  tarantool-live-source.repo > tarantool-2.3-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.4/g'  tarantool-live-source.repo > tarantool-2.4-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.5/g'  tarantool-live-source.repo > tarantool-2.5-live-source.repo
sed -e 's/@RELEASE_SERIES@/2.6/g'  tarantool-live-source.repo > tarantool-2.6-live-source.repo

%build
echo "Nothing to build"

%install
install -Dp -m 644 RPM-GPG-KEY-tarantool %{build_gpg_dir}/RPM-GPG-KEY-tarantool

install -Dp -m 644 tarantool-1.10.repo %{build_repos_dir}/tarantool-1.10.repo
install -Dp -m 644 tarantool-2.1.repo  %{build_repos_dir}/tarantool-2.1.repo
install -Dp -m 644 tarantool-2.2.repo  %{build_repos_dir}/tarantool-2.2.repo
install -Dp -m 644 tarantool-2.3.repo  %{build_repos_dir}/tarantool-2.3.repo
install -Dp -m 644 tarantool-2.4.repo  %{build_repos_dir}/tarantool-2.4.repo
install -Dp -m 644 tarantool-2.5.repo  %{build_repos_dir}/tarantool-2.5.repo
install -Dp -m 644 tarantool-2.6.repo  %{build_repos_dir}/tarantool-2.6.repo

install -Dp -m 644 tarantool-1.10-live.repo %{build_repos_dir}/tarantool-1.10-live.repo
install -Dp -m 644 tarantool-2.1-live.repo  %{build_repos_dir}/tarantool-2.1-live.repo
install -Dp -m 644 tarantool-2.2-live.repo  %{build_repos_dir}/tarantool-2.2-live.repo
install -Dp -m 644 tarantool-2.3-live.repo  %{build_repos_dir}/tarantool-2.3-live.repo
install -Dp -m 644 tarantool-2.4-live.repo  %{build_repos_dir}/tarantool-2.4-live.repo
install -Dp -m 644 tarantool-2.5-live.repo  %{build_repos_dir}/tarantool-2.5-live.repo
install -Dp -m 644 tarantool-2.6-live.repo  %{build_repos_dir}/tarantool-2.6-live.repo

install -Dp -m 644 tarantool-1.10-source.repo %{build_repos_dir}/tarantool-1.10-source.repo
install -Dp -m 644 tarantool-2.1-source.repo  %{build_repos_dir}/tarantool-2.1-source.repo
install -Dp -m 644 tarantool-2.2-source.repo  %{build_repos_dir}/tarantool-2.2-source.repo
install -Dp -m 644 tarantool-2.3-source.repo  %{build_repos_dir}/tarantool-2.3-source.repo
install -Dp -m 644 tarantool-2.4-source.repo  %{build_repos_dir}/tarantool-2.4-source.repo
install -Dp -m 644 tarantool-2.5-source.repo  %{build_repos_dir}/tarantool-2.5-source.repo
install -Dp -m 644 tarantool-2.6-source.repo  %{build_repos_dir}/tarantool-2.6-source.repo

install -Dp -m 644 tarantool-1.10-live-source.repo %{build_repos_dir}/tarantool-1.10-live-source.repo
install -Dp -m 644 tarantool-2.1-live-source.repo  %{build_repos_dir}/tarantool-2.1-live-source.repo
install -Dp -m 644 tarantool-2.2-live-source.repo  %{build_repos_dir}/tarantool-2.2-live-source.repo
install -Dp -m 644 tarantool-2.3-live-source.repo  %{build_repos_dir}/tarantool-2.3-live-source.repo
install -Dp -m 644 tarantool-2.4-live-source.repo  %{build_repos_dir}/tarantool-2.4-live-source.repo
install -Dp -m 644 tarantool-2.5-live-source.repo  %{build_repos_dir}/tarantool-2.5-live-source.repo
install -Dp -m 644 tarantool-2.6-live-source.repo  %{build_repos_dir}/tarantool-2.6-live-source.repo

%files
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-tarantool
%config(noreplace) %{_sysconfdir}/yum.repos.d/tarantool*.repo

%changelog
* Sun Sep 06 2020 Alexander Turenko <alexander.turenko@tarantool.org>
- Initial version based on Remi's Collet repository:
  https://git.remirepo.net/cgit/rpms/remi-release.git/
