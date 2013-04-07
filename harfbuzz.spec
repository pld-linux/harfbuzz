#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	HarfBuzz - internationalized text shaping library
Summary(pl.UTF-8):	HarfBuzz - biblioteka rysująca tekst z obsługą wielu języków
Name:		harfbuzz
Version:	0.9.15
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/harfbuzz/release/%{name}-%{version}.tar.bz2
# Source0-md5:	f6075024947eb445dd3bec587b1753d1
URL:		http://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	cairo-devel >= 1.8.0
BuildRequires:	freetype-devel >= 2.3.8
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	graphite2-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.20
Requires:	cairo >= 1.8.0
Requires:	glib2 >= 1:2.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Internationalized OpenType text layout and rendering library.

%description -l pl.UTF-8
Biblioteka rozmieszczająca i rysująca tekst z fontów OpenType,
obsługująca wiele języków.

%package devel
Summary:	Header files for HarfBuzz library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki HarfBuzz
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype-devel >= 2.3.8
Requires:	glib2-devel >= 1:2.16
Requires:	graphite2-devel
Requires:	libicu-devel
Requires:	libstdc++-devel

%description devel
Header files for HarfBuzz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HarfBuzz.

%package static
Summary:	Static HarfBuzz library
Summary(pl.UTF-8):	Statyczna biblioteka HarfBuzz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static HarfBuzz library.

%description static -l pl.UTF-8
Statyczna biblioteka HarfBuzz.

%package apidocs
Summary:	HarfBuzz API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki HarfBuzz
Group:		Documentation

%description apidocs
API and internal documentation for HarfBuzz library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki HarfBuzz.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static}
%{__make}

# missing
cat >> harfbuzz.pc <<EOF
Requires.private: glib-2.0 gobject-2.0 icu-le icu-uc freetype2 graphite2
EOF

%install
rm -rf $RPM_BUILD_ROOT

# parallel install broken (hb-version.h both in pkginclude_HEADERS and
# nodist_pkginclude_HEADERS)
%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_bindir}/hb-ot-shape-closure
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-view
%attr(755,root,root) %{_libdir}/libharfbuzz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz.so
%{_includedir}/harfbuzz
%{_pkgconfigdir}/harfbuzz.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz.a
%endif
