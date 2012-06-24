Summary:	Utilites for gEDA project
Summary(pl):	Narz�dzia dla projektu gEDA
Name:		geda-gsymcheck
Version:	20030901
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	e841d4ba32d57593fc1f9ea09ff49dbd
URL:		http://www.geda.seul.org/
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	libgeda >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gEDA symbol checker.

%description -l pl
Weryfikator symboli dla projektu gEDA.

%prep
%setup  -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-*
%{_mandir}/man*/*
