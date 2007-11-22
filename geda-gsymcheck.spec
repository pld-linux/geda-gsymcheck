Summary:	Utilites for gEDA project - symbol checker
Summary(pl.UTF-8):	Narzędzia dla projektu gEDA - weryfikator symboli
Name:		geda-gsymcheck
Version:	1.2.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.geda.seul.org/pub/geda/release/v1.2/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	bf23cf68e82f14f1e44b83fa9b951b90
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
%{_docdir}/geda-doc/man/*
