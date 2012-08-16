%define major 3
%define libname %mklibname gadu %{major}
%define develname %mklibname gadu -d

Summary:	A Gadu-gadu protocol compatibile library
Name:		libgadu
Version:	1.11.2
Release:	1
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
