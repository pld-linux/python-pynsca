%define 	module	pynsca
Summary:	Python interface to Nagios Service Check Architecture (NSCA)
Name:		python-%{module}
Version:	1.5
Release:	1
License:	MPL v1.1
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/p/pynsca/pynsca-%{version}.tar.gz
# Source0-md5:	c4c6ede5e92ea3343adb978a9b6b31f4
URL:		https://github.com/djmitche/pynsca
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A very simple module to allow nagios service check results to be
submitted via NSCA.

- Python 2.4 or higher
- python-mcrypt, if using AES encryption
- pycrypto, if using 3DES encryption
- No other libraries

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{py_sitescriptdir}/pynsca.py[co]
%{py_sitescriptdir}/pynsca-%{version}-py*.egg-info
