Name:		python-sphinxcontrib-autoprogram
Version:	0.1.9
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib_autoprogram/sphinxcontrib-autoprogram-%{version}.tar.gz
Summary:	Documenting CLI programs
URL:		https://pypi.org/project/sphinxcontrib-autoprogram/
License:	2-Clause BSD
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(six)
BuildRequires:	python%{pyver}dist(sphinx) >= 1.2
BuildSystem:	python
BuildArch:	noarch

%description
Documenting CLI programs

%prep
%autosetup -p1 -n sphinxcontrib-autoprogram-%{version}

%files
%{py_sitedir}/sphinxcontrib
%{py_sitedir}/*.pth
%{py_sitedir}/sphinxcontrib_autoprogram-%{version}*-info
