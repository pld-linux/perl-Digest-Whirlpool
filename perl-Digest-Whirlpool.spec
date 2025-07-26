#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Digest
%define	pnam	Whirlpool
Summary:	Digest::Whirlpool - A 512-bit, collision-resistant, one-way hash function
Summary(pl.UTF-8):	Digest::Whirlpool - 512-bitowa, odporna na kolizje, jednokierunkowa funkcja skrótu
Name:		perl-Digest-Whirlpool
Version:	2.04
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Digest/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b3f1c042e2ab3226a71cc51a07b3f66a
URL:		http://search.cpan.org/dist/Digest-Whirlpool/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Module-Install
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an interface to the WHIRLPOOL hash algorithm. This module
subclasses Digest::base and can be used either directly or through
the Digest meta-module. Using the latter is recommended.

%description -l pl.UTF-8
Moduł ten udostępnia interfejs do algorytmu mieszania WHIRLPOOL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%{__sed} -i -e '1s|#!/usr/bin/env perl$|#!%{__perl}|' script/whirlpoolsum

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
