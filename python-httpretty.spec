Name:		python-httpretty
Version:	1.1.4
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/h/httpretty/httpretty-%{version}.tar.gz
Summary:	HTTP client mock for Python
URL:		https://pypi.org/project/httpretty/
License:	MIT
Group:		Development/Python
BuildRequires:	python-setuptools
BuildArch:	noarch

%description
HTTP client mock for Python.

It provides a full fake TCP socket module.

%prep
%autosetup -p1 -n httpretty-%{version}

%build
python setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

%files
%{py_puresitedir}/httpretty*.egg-info
%{py_puresitedir}/httpretty
