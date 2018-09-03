%global pname rally_openstack
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%global with_doc %{!?_without_doc:1}%{?_without_doc:0}

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
BuildRequires:    python2-devel
BuildRequires:    python2-pbr
BuildRequires:    python2-setuptools
BuildRequires:    openstack-macros

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
Requires:       python2-watcherclient
Requires:       python2-zaqarclient
Requires:       python2-requests
Requires:       python2-kubernetes

%description
%{common_desc}

%if 0%{?with_doc}
%package doc
Summary:    Documentation for rally-openstack

BuildRequires:  python2-sphinx
BuildRequires:  python2-oslo-sphinx
BuildRequires:  python2-oslotest
BuildRequires:  python2-rally

%description doc
%{common_desc}

This package contains documentation files for rally-openstack.
%endif

%prep
%autosetup -S git -n %{pname}-%{upstream_version}

%py_req_cleanup

%build
%py2_build

# for Documentation
%if 0%{?with_doc}
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%py2_install

%files
%license LICENSE
%{python2_sitelib}/%{pname}
%{python2_sitelib}/%{pname}*.egg-info

%if 0%{?with_doc}
%files doc
%license LICENSE
%doc doc/build/html
%endif

%changelog
