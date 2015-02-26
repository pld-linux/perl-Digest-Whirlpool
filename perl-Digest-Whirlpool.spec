#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Digest
%define	pnam	Whirlpool
Summary:	Digest::Whirlpool - A 512-bit, collision-resistant, one-way hash function
#Summary(pl.UTF-8):	
Name:		perl-Digest-Whirlpool
Version:	1.09
Release:	5
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	852a7672ef11d46b229c0be77330e991
URL:		http://search.cpan.org/dist/Digest-Whirlpool/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an interface to the WHIRLPOOL hash algorithm. This module
subclasses Digest::base and can be used either directly or through
the Digest meta-module. Using the latter is recommended.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Digest/*.pm
%dir %{perl_vendorarch}/auto/Digest/Whirlpool
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/Whirlpool/*.so
%{_mandir}/man?/*
