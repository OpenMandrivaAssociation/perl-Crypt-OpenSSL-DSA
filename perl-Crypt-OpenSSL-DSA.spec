%define upstream_name    Crypt-OpenSSL-DSA
%define upstream_version 0.14

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	2

Summary:	Digital Signature Algorithm using OpenSSL
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/authors/id/T/TJ/TJMATHER/Crypt-OpenSSL-DSA-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Crypt::OpenSSL::DSA implements the DSA 
(Digital Signature Algorithm) signature verification system.

It is a thin XS wrapper to the DSA functions contained in the 
OpenSSL crypto library, located at http://www.openssl.org

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# perl path hack
find . -type f | xargs %{__perl} -p -i -e "s|^#\!/usr/local/bin/perl|#\!/usr/bin/perl|g"

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/auto/Crypt
%{perl_vendorarch}/Crypt
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.130.0-5
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.130.0-4
+ Revision: 680864
- mass rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-3mdv2011.0
+ Revision: 555717
- rebuild

* Tue Apr 13 2010 Funda Wang <fwang@mandriva.org> 0.130.0-2mdv2010.1
+ Revision: 534174
- rebuild

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.0
+ Revision: 410155
- fixing error due to -Werror=format-security
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.13-6mdv2009.0
+ Revision: 256273
- rebuild

* Thu Jan 24 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.13-4mdv2008.1
+ Revision: 157725
- Rebuild for new perl

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.13-2mdv2008.1
+ Revision: 131425
- kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-2mdv2007.0
- Rebuild

* Mon Nov 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdk
- New release 0.13
- fix sources URL
- spec cleanup

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-2mdk
- Fix Url according to Perl policy( thanks guillomovitch )

* Tue Jun 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.12-1mdk
- 0.12
- Fix Description
- Fix Source url
- Fix Url
- %%mkrel

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.11-6mdk
- Rebuild for new perl

* Thu Apr 01 2004 Michael Scherer <misc@mandrake.org> 0.11-5mdk
- do not own standard dir
- [DIRM]


