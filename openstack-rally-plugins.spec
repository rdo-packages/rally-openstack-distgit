# Macros for py2/py3 compatibility
%if 0%{?fedora} || 0%{?rhel} > 7
%global pyver %{python3_pkgversion}
%else
%global pyver 2
%endif

%global pyver_bin python%{pyver}
%global pyver_sitelib %python%{pyver}_sitelib
%global pyver_install %py%{pyver}_install
%global pyver_build %py%{pyver}_build
# End of macros for py2/py3 compatibility

%global pname rally_openstack
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
rally-openstack is a collection of plugins for Rally framework \
designed for the OpenStack platform.

Name:             openstack-rally-plugins
Version:          XXX
Release:          XXX
Summary:          A collection of plugins for OpenStack Rally
License:          ASL 2.0
URL:              https://rally.readthedocs.io
Source0:          https://tarballs.openstack.org/rally-openstack/rally-openstack-%{upstream_version}.tar.gz
BuildArch:        noarch

BuildRequires:    git
BuildRequires:    python%{pyver}-devel
BuildRequires:    python%{pyver}-pbr
BuildRequires:    python%{pyver}-setuptools
BuildRequires:    openstack-macros

# test dependencies
BuildRequires:  python%{pyver}-pytest
BuildRequires:  python%{pyver}-ddt
BuildRequires:  python%{pyver}-mock
BuildRequires:  python%{pyver}-dateutil
BuildRequires:  python%{pyver}-testtools
BuildRequires:  python%{pyver}-kubernetes

Requires:       python%{pyver}-rally
Requires:       python%{pyver}-boto
Requires:       python%{pyver}-gnocchiclient
Requires:       python%{pyver}-keystoneauth1
Requires:       python%{pyver}-os-faults
Requires:       python%{pyver}-osprofiler
Requires:       python%{pyver}-barbicanclient
Requires:       python%{pyver}-ceilometerclient
Requires:       python%{pyver}-cinderclient
Requires:       python%{pyver}-designateclient
Requires:       python%{pyver}-heatclient
Requires:       python%{pyver}-glanceclient
Requires:       python%{pyver}-ironicclient
Requires:       python%{pyver}-keystoneclient
Requires:       python%{pyver}-magnumclient
Requires:       python%{pyver}-manilaclient
Requires:       python%{pyver}-mistralclient
Requires:       python%{pyver}-muranoclient
Requires:       python%{pyver}-monascaclient
Requires:       python%{pyver}-neutronclient
Requires:       python%{pyver}-novaclient
Requires:       python%{pyver}-octaviaclient
Requires:       python%{pyver}-saharaclient
Requires:       python%{pyver}-senlinclient
Requires:       python%{pyver}-swiftclient
Requires:       python%{pyver}-troveclient
Requires:       python%{pyver}-watcherclient
Requires:       python%{pyver}-zaqarclient
Requires:       python%{pyver}-requests
Requires:       python%{pyver}-kubernetes

%description
%{common_desc}

%prep
%autosetup -S git -n rally-openstack-%{upstream_version}

%py_req_cleanup

%build
%{pyver_build}

%install
%{pyver_install}

%check
# FIXME(chkumar246): watcherclient is not packaged in RDO
# So currently skipping the tests
%if %{pyver} > 2
  export PYTHON=/usr/bin/python3
%endif
%{pyver_bin} -m pytest tests/unit || true

%files
%license LICENSE
%{pyver_sitelib}/%{pname}
%{pyver_sitelib}/%{pname}*.egg-info

%changelog
