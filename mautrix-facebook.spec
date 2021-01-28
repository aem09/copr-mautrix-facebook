%global srcname mautrix-facebook

%global srcversion master

%{?python_enable_dependency_generator}

Name:       %{srcname}
Version:    0.2.0
Release:    1%{?dist}
Summary:    Matrix to facebook messenger bridge written in python.
License:    ASL 2.0
URL:        https://github.com/tulir/%{srcname}
Source0:    %{url}/archive/%{srcversion}/%{srcname}-%{srcversion}.tar.gz
Source1:    mautrix-facebook.service
BuildArch:  noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd-rpm-macros

Requires:       systemd

#Manually include the end-to-end dependencies.
Requires:       libolm-python3
Requires:       python3-unpaddedbase64
%py_provides    mautrix-facebook+e2be
%{?systemd_requires}

Requires: python3-crypto
%global __requires_exclude ^.*pycryptodome.*$

%description
Facebook to Matrix Bridge

%{?python_extras_subpkg:%python_extras_subpkg -n %{name} -i %{python3_sitelib}/*.egg-info metrics}

%prep
%autosetup -p1 -n %{srcname}-%{srcversion}

%build
%py3_build

%install
%py3_install

rm -r %{buildroot}%{_prefix}/alembic*

install -p -D -T -m 0644 %{buildroot}%{python3_sitelib}/mautrix_facebook/example-config.yaml %{buildroot}%{_sysconfdir}/mautrix/facebook/config.yaml
rm -r %{buildroot}%{_prefix}/example-config.yaml

install -p -D -T -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/mautrix-facebook.service

%post
%systemd_post mautrix-facebook.service

%preun
%systemd_preun mautrix-facebook.service

%postun
%systemd_postun_with_restart mautrix-facebook.service


%files
%license LICENSE
%doc *.md
%{python3_sitelib}/mautrix_facebook/
%{python3_sitelib}/mautrix_facebook*.egg-info/

%{python3_sitelib}/maufbapi/

%{_unitdir}/mautrix-facebook.service
%attr(755,root,root) %dir %{_sysconfdir}/mautrix/facebook
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/mautrix/facebook/*
