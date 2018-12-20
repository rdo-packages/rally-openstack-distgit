%global pname rally_openstack
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global common_desc \
rally-openstack is a collection of plugins for Rally framework \
designed for the OpenStack platform.

Name:             openstack-rally-plugins
Version:          1.3.0
Release:          1%{?dist}
Summary:          A collection of plugins for OpenStack Rally
License:          ASL 2.0
URL:              https://rally.readthedocs.io
Source0:          https://tarballs.openstack.org/rally-openstack/rally-openstack-%{upstream_version}.tar.gz
BuildArch:        noarch

BuildRequires:    git
BuildRequires:    python2-devel
BuildRequires:    python2-pbr
BuildRequires:    python2-setuptools
BuildRequires:    openstack-macros

# test dependencies
BuildRequires:  python2-pytest
BuildRequires:  python2-ddt
BuildRequires:  python2-mock
BuildRequires:  python2-dateutil
BuildRequires:  python2-testtools
BuildRequires:  python2-kubernetes

Requires:       python2-rally
Requires:       python2-boto
Requires:       python2-gnocchiclient
Requires:       python2-keystoneauth1
Requires:       python2-os-faults
Requires:       python2-osprofiler
Requires:       python2-ceilometerclient
Requires:       python2-cinderclient
Requires:       python2-designateclient
Requires:       python2-heatclient
Requires:       python2-glanceclient
Requires:       python2-ironicclient
Requires:       python2-keystoneclient
Requires:       python2-magnumclient
Requires:       python2-manilaclient
Requires:       python2-mistralclient
Requires:       python2-muranoclient
Requires:       python2-monascaclient
Requires:       python2-neutronclient
Requires:       python2-novaclient
Requires:       python2-octaviaclient
Requires:       python2-saharaclient
Requires:       python2-senlinclient
Requires:       python2-swiftclient
Requires:       python2-troveclient
Requires:       python2-zaqarclient
Requires:       python2-requests
Requires:       python2-kubernetes

%description
%{common_desc}

%prep
%autosetup -S git -n rally-openstack-%{upstream_version}

%py_req_cleanup

%build
%py2_build

%install
%py2_install

%check
# FIXME(chkumar246): watcherclient is not packaged in RDO
# So currently skipping the tests
%{__python2} -m pytest tests/unit ||

%files
%license LICENSE
%{python2_sitelib}/%{pname}
%{python2_sitelib}/%{pname}*.egg-info

%changelog
* Thu Dec 20 2018 RDO <dev@lists.rdoproject.org> 1.3.0-1
- Update to 1.3.0
