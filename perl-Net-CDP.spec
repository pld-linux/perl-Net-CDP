#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	CDP
Summary:	Net::CDP - Cisco Discovery Protocol (CDP) advertiser/listener
Summary(pl.UTF-8):	Net::CDP - rozgłaszający/nasłuchujący dla protokołu Cisco Discovery Protocol
Name:		perl-Net-CDP
Version:	0.09
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4cd5e76cae8fbd47591579db749ca2aa
URL:		http://search.cpan.org/dist/Net-CDP/
BuildRequires:	libnet-devel >= 1:1.1.0
BuildRequires:	libpcap-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Clan
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Net::CDP module implements an advertiser/listener for the Cisco
Discovery Protocol.

CDP is a proprietary Cisco protocol for discovering devices on a
network. A typical CDP implementation sends periodic CDP packets on
every network port. It might also listen for packets for
advertisements sent by neighboring devices.

A Net::CDP object represents an advertiser/listener for a single
network port. It can send and receive individual CDP packets, each
represented by a Net::CDP::Packet object.

To manage multiple ports simultaneously, you might like to take a look
at Net::CDP::Manager.

%description -l pl.UTF-8
Moduł Net::CDP jest implementacją rozgłaszającego/nasłuchującego dla
protokołu Cisco Discovery Protocol.

CDP to własnościowy protokół Cisco do wykrywania urządzeń w sieci.
Typowa implementacja CDP wysyła okresowe pakiety CDP na każdym porcie
sieciowym. Może także nasłuchiwać zbierając pakiety rozgłaszane przez
sąsiednie urządzenia.

Obiekt Net::CDP reprezentuje rozgłaszającego/nasłuchującego dla
pojedynczego portu sieciowego. Może wysyłać i odbierać poszczególne
pakiety CDP, z których każdy jest reprezentowany przez obiekt
Net::CDP::Packet.

Do zarządzania jednocześnie wieloma portami można użyć modułu
Net::CDP::Manager.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__install} -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{perl_vendorarch}/Net/example.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Net/*.pm
%dir %{perl_vendorarch}/Net/CDP
%{perl_vendorarch}/Net/CDP/*.pm
%dir %{perl_vendorarch}/auto/Net/CDP
%{perl_vendorarch}/auto/Net/CDP/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Net/CDP/*.so
%{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
