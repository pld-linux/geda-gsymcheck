Summary:	Utilites for gEDA project - symbol checker
Summary(pl.UTF-8):	Narzędzia dla projektu gEDA - weryfikator symboli
Name:		geda-gsymcheck
Version:	20061020
Release:	0.1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/devel/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	729c8c32598a20ff8c551a96eef1a496
URL:		http://www.geda.seul.org/
BuildRequires:	libgeda-devel >= %{version}
BuildRequires:	pkgconfig
Requires:	libgeda >= %{version}
Obsoletes:	gsymcheck
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gEDA symbol checker.

%description -l pl.UTF-8
Weryfikator symboli dla projektu gEDA.

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gEDA/system-*
%{_mandir}/man*/*
