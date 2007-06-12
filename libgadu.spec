%define major 3
%define libname %mklibname gadu %{major}

Summary:	A Gadu-gadu protocol compatibile library
Name:		libgadu
Version:	1.7.1
Release:	%mkrel 1
License:	LGPL
Group:		Networking/Instant messaging
Url:		http://toxygen.net/libgadu
Source0:	http://toxygen.net/libgadu/files/%{name}-%{version}.tar.bz2
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description 
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{libname}
Summary:	A Gadu-gadu protocol compatibile library
Group:		Networking/Instant messaging

%description -n %{libname}
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{libname}-devel
Summary:	Development files for libgadu library
Group:		Development/C
Provides:	libgadu-devel = %{version}-%{release}
Provides:	gadu-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{realease}

%description -n %{libname}-devel
Development files for libgadu library.

%package -n %{libname}-static-devel
Summary:	Static development files for libgadu library
Group:		Development/C

%description -n %{libname}-static-devel
Static development files for libgadu library.


%prep
%setup -q

%build
%configure2_5x \
	--with-pthread \
	--without-bind

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std


%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc COPYING
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_libdir}/pkgconfig/%{name}.pc

%files -n %{libname}-static-devel
%defattr(-,root,root)
%{_libdir}/%{name}.a
