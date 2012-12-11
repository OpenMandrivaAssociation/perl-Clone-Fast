%define upstream_name    Clone-Fast
%define upstream_version 0.93

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.930.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.930.0-4
+ Revision: 680833
- mass rebuild

* Wed Jul 21 2010 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-3mdv2011.0
+ Revision: 556552
- removing faulty test failing with perl >= 5.11
- rebuild
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.930.0-1mdv2010.0
+ Revision: 401702
- rebuild using %%perl_convert_version
- fixed license field

* Fri Feb 20 2009 Jérôme Quelin <jquelin@mandriva.org> 0.93-1mdv2009.1
+ Revision: 343338
- import perl-Clone-Fast


* Fri Feb 20 2009 cpan2dist 0.93-1mdv
- initial mdv release, generated with cpan2dist

