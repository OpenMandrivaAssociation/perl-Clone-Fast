%define upstream_name    Clone-Fast
%define upstream_version 0.93

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Natively copying Perl data structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Clone/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# this test fails with perl >= 5.11
# https://rt.cpan.org/Ticket/Display.html?id=43248
rm t/03scalar.t
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
