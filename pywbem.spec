%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
Name:           pywbem 
Version:        0.7.0
Release:        4%{dist} 
Summary:        Python WBEM Client and Provider Interface
Group:          Development/Libraries
License:        LGPLv2
URL:            http://pywbem.sourceforge.net
Source0:        http://downloads.sourceforge.net/pywbem/pywbem-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python-setuptools-devel 
BuildArch:      noarch
Requires:       python-twisted
%description
A Python library for making CIM (Common Information Model) operations over HTTP 
using the WBEM CIM-XML protocol. It is based on the idea that a good WBEM 
client should be easy to use and not necessarily require a large amount of 
programming knowledge. It is suitable for a large range of tasks from simply 
poking around to writing web and GUI applications. 

WBEM, or Web Based Enterprise Management is a manageability protocol, like 
SNMP, standardised by the Distributed Management Task Force (DMTF) available 
at http://www.dmtf.org/standards/wbem.

It also provides a Python provider interface, and is the fastest and 
easiest way to write providers on the planet.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
mkdir -p -m755 %{buildroot}%{_bindir}
mv %{buildroot}/%{python_sitelib}/%{name}/wbemcli.py %{buildroot}/%{_bindir}/pywbemcli
mv %{buildroot}/%{python_sitelib}/%{name}/mof_compiler.py %{buildroot}/%{_bindir}/mofcomp

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{python_sitelib}/*
%attr(755,root,root) %{_bindir}/mofcomp
%attr(755,root,root) %{_bindir}/pywbemcli
%doc README

%changelog
* Thu May 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.7.0-4
- rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 David Nalley <david@gnsa.us> 0.7.0-2
- Added some verbiage regarding what WBEM is and expanding WBEM and CIM acronyms
- Added python-twisted as a dependency
* Mon Jun 25 2009 David Nalley <david@gnsa.us> 0.7.0-1
- Initial packaging

