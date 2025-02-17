%define major 3
%define libname %mklibname gadu %{major}
%define devname %mklibname gadu -d

Summary:	A Gadu-gadu protocol compatibile library
Name:		libgadu
Version:	1.12.2
Release:	5
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		https://toxygen.net/libgadu
Source0:	http://toxygen.net/libgadu/files/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:	pkgconfig(gnutls)

%description
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{libname}
Summary:	A Gadu-gadu protocol compatibile library
Group:		Networking/Instant messaging

%description -n %{libname}
The libgadu is intended to make it easy to add Gadu-Gadu communication
support to your software.

%package -n %{devname}
Summary:	Development files for libgadu library
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for libgadu library.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-pthread \
	--without-bind \
	--without-openssl \
	--with-gnutls \
	--with-c99-vsnprintf

%make_build

%install
%make_install

%files -n %{libname}
%{_libdir}/%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

