%define module  Crypt-OpenSSL-DSA
%define name	perl-%{module}
%define version	0.13
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Digital Signature Algorithm using OpenSSL
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRequires:	perl-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Crypt::OpenSSL::DSA implements the DSA 
(Digital Signature Algorithm) signature verification system.

It is a thin XS wrapper to the DSA functions contained in the 
OpenSSL crypto library, located at http://www.openssl.org

%prep
%setup -q -n %{module}-%{version} 
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

