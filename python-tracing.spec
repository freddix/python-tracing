Summary:	Python framework for Unix-like command line programs
Name:		python-tracing
Version:	0.8
Release:	1
License:	GPL v3
Group:		Libraries/Python
Source0:	http://code.liw.fi/debian/pool/main/p/python-tracing/%{name}_%{version}.orig.tar.gz
# Source0-md5:	9f449746b2ae19ca62bca5363ae0b432
URL:		http://liw.fi/cliapp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Python library tracing helps with logging debug messages.
It provides a couple of functions for logging debug messages,
and allows the user to enable or disable logging for particular
code modules.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/tracing.py[co]

