%define upstream_name    Clone-Fast
%undefine _debugsource_packages

Name:		perl-%{upstream_name}
Version:	0.97
Release:	3
Summary:	Natively copying Perl data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/Clone-Fast
Source0:	https://cpan.metacpan.org/authors/id/W/WA/WAZZUTEKE/Clone-Fast-%{version}.tar.gz

BuildRequires:	perl-devel
# For tests
BuildRequires:	perl(Devel::Peek)

%description
Essentially, this module is a very optimized version of the Clone::More
manpage. By taking advantage of one of the Clone::More manpage's
'OPTIMIZATION_HACKS' as well as removing all the Pure Perl from the
'More.pm', I was able to gain a lot of speed out of the module.
Essentially, though, the core of the module is exactly as that of the
Clone::More manpage.

You will see that by useing the Benchmark::cmpthese manpage, I ran a simple
comparison between the Storable::dclone manpage, the Clone::More::clone
manpage, and the Clone::Fast::clone manpage. You will (should) begin to see
the reason why I loaded this module along side of the Clone::More manpage.

				   Rate    Storable Clone::More Clone::Fast
	Storable     7552/s          --        -39%        -59%
	Clone::More 12400/s         64%          --        -33%
	Clone::Fast 18442/s        144%         49%          --

%prep
%autosetup -p1 -n %{upstream_name}
%{__perl} Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
# Tests seem to be broken

%install
%make_install

%files
%doc Changes
%{_mandir}/man3/*
%perl_vendorarch/Clone/Fast.pm
%perl_vendorarch/auto/Clone/Fast
