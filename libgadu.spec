%define major 3
%define libname %mklibname gadu %{major}
%define develname %mklibname gadu -d

Summary:	A Gadu-gadu protocol compatibile library
Name:		libgadu
Version:	1.7.1
Release:	%mkrel 6
License:	LGPLv2+
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

%package -n %{develname}
Summary:	Development files for libgadu library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	gadu-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{libname}-static-devel

%description -n %{develname}
Development files for libgadu library.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-pthread \
	--without-bind \
	--disable-debug

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

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/%{name}.la
%{_libdir}/pkgconfig/%{name}.pc
