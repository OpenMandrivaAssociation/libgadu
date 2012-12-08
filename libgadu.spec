%define major 3
%define libname %mklibname gadu %{major}
%define develname %mklibname gadu -d

Summary:	A Gadu-gadu protocol compatibile library
Name:		libgadu
Version:	1.11.1
Release:	2
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		http://toxygen.net/libgadu
Source0:	http://toxygen.net/libgadu/files/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	gnutls-devel >= 3.0

%description
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{libname}
Summary:	A Gadu-gadu protocol compatibile library
Group:		Networking/Instant messaging

%description -n %{libname}
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{develname}
Summary:	Development files for libgadu library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gadu-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname gadu 3 -d} < %{version}-%{release}
Obsoletes:	%{mklibname gadu -s -d} < %{version}-%{release}

%description -n %{develname}
Development files for libgadu library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-pthread \
	--without-bind \
	--without-openssl \
	--with-gnutls \
	--with-c99-vsnprintf

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Mar 23 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.11.1-2
+ Revision: 786407
- Rebuild for gnutls 3.x

* Sun Jan 29 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.11.1-1
+ Revision: 769553
- broken tar archive fix
- version update 1.11.1

* Tue Jun 14 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.11.0-1
+ Revision: 685172
- update to new version 1.11.0

* Sat Apr 16 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.1-1
+ Revision: 653295
- update to new version 1.10.1

* Wed Mar 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.10.0-1
+ Revision: 641367
- update to new version 1.10.0
- drop patch 0
- add buildrequires on doxygen and gnutls-devel

* Sun Nov 28 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.1-1mdv2011.0
+ Revision: 602353
- update to new version 1.9.1

* Thu Jul 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-1mdv2011.0
+ Revision: 553709
- update to new version 1.9.0
- Patch0: fix memory leak

* Tue Mar 16 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-0.rc3.1mdv2010.1
+ Revision: 522306
- update to new version 1.9.0-rc3

* Thu Nov 19 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-0.rc2.1mdv2010.1
+ Revision: 467528
- update to new version 1.9.0-rc2

* Fri Oct 09 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-0.rc1.2mdv2010.0
+ Revision: 456420
- this is just a noop if it won't work i'll revert asap

* Sun Sep 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.9.0-0.rc1.1mdv2010.0
+ Revision: 445064
- update to new version 1.9.0-rc1

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Tue Nov 04 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.2-1mdv2009.1
+ Revision: 299840
- update to new version 1.8.2 (security fixes)

* Mon Jul 07 2008 Adam Williamson <awilliamson@mandriva.org> 1.8.1-2mdv2009.0
+ Revision: 232634
- replace arbitrary obsolete version with < %%version-%%release
- really obsolete static devel library (changelog indicated this had been done
  but it had not)

* Sun Jun 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.1-1mdv2009.0
+ Revision: 227838
- update to new version 1.8.1

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-2mdv2009.0
+ Revision: 212061
- properlly obsolete static library

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.8.0-1mdv2008.1
+ Revision: 175174
- new version

* Thu Jan 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.90-0.svn513.2mdv2008.1
+ Revision: 153938
- rebuild due to wrong tag

* Tue Jan 15 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.90-0.svn513.1mdv2008.1
+ Revision: 152005
- update to the latest upstream svn revision, upcoming kadu 0.6.0 need this

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-7mdv2008.1
+ Revision: 113534
- disable support for SSL, as it is incompataibile with GPL license and Gadu-Gadu network still do not use it, and probably will never do

* Sun Nov 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-6mdv2008.1
+ Revision: 105862
- disable compiling of static library, as it is really useless
- do not ship COPYING files, thus no docs at all ;)
- new license policy

* Wed Jun 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-5mdv2008.0
+ Revision: 41835
- obsolete static-devel library

* Wed Jun 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-4mdv2008.0
+ Revision: 41820
- new devel library policy

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-3mdv2008.0
+ Revision: 38638
- disable debug
- static pkg requires devel

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-2mdv2008.0
+ Revision: 38419
- fix typo

* Tue Jun 12 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-1mdv2008.0
+ Revision: 38311
- libgadu has beed exhaled from ekg
- new version
- Import libgadu

