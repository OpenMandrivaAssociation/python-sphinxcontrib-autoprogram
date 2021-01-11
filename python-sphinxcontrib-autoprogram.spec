# Created by pyp2rpm-3.3.5
%global pypi_name sphinxcontrib-autoprogram
%define git_version 20201122

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        1
Summary:        Documenting CLI programs
Group:          Development/Python
License:        BSD
URL:            https://github.com/sphinx-contrib/autoprogram
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx) >= 1.2

%description
sphinxcontrib.autoprogram This contrib extension, sphinxcontrib.autoprogram,
provides an automated way to document CLI programs. It scans
arparser.ArgumentParser object,

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# Tests are broken 
%check
%{__python3} setup.py test

%files -n python-%{pypi_name}
%doc README.rst
%{python3_sitelib}/sphinxcontrib
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/sphinxcontrib_autoprogram-%{version}-py3.9-nspkg.pth