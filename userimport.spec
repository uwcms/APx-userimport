%define name userimport

Name:           %{name}
Version:        %{version_rpm_spec_version}
Release:        %{version_rpm_spec_release}%{?dist}
Summary:        A tool for adding users to APx-style boards.

License:        Reserved
URL:            https://github.com/uwcms/APx-%{name}
Source0:        %{name}-%{version_rpm_spec_version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3 python-rpm-macros python3-rpm-macros python3-setuptools
Requires:       python3

%global debug_package %{nil}

%description
A tool for adding users to APx-style boards.


%prep
%autosetup -n %{name}-%{version}


%build
export %{version_shellvars}
%py3_build


%install
export %{version_shellvars}
%py3_install


%files
%{python3_sitelib}/*
%{_bindir}/userimport


%changelog
* Tue Oct 27 2020 Jesra Tikalsky <jtikalsky@hep.wisc.edu>
- Initial spec file
