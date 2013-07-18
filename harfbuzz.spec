#
# Conditional build:
%bcond_without	static_libs	# static libraries build
%bcond_without	graphite2	# Graphite2 library usage
%bcond_without	icu		# ICU integration
#
Summary:	HarfBuzz - internationalized text shaping library
Summary(pl.UTF-8):	HarfBuzz - biblioteka rysująca tekst z obsługą wielu języków
Name:		harfbuzz
Version:	0.9.19
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://www.freedesktop.org/software/harfbuzz/release/%{name}-%{version}.tar.bz2
# Source0-md5:	9782581ee6ef972554772e84ca448131
URL:		http://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	cairo-devel >= 1.8.0
BuildRequires:	freetype-devel >= 2.3.8
BuildRequires:	glib2-devel >= 1:2.16
%{?with_graphite2:BuildRequires:	graphite2-devel}
%{?with_icu:BuildRequires:	libicu-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig >= 1:0.20
Requires:	cairo >= 1.8.0
Requires:	freetype >= 2.3.8
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
%{?with_graphite2:Requires:	graphite2-devel}
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

%package icu
Summary:	HarfBuzz text shaping library - ICU integration
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - integracja z ICU
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description icu
HarfBuzz text shaping library - ICU integration.

%description icu -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - integracja z ICU.

%package icu-devel
Summary:	Header file for HarfBuzz ICU library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki HarfBuzz ICU
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-icu = %{version}-%{release}
Requires:	libicu-devel

%description icu-devel
Header file for HarfBuzz ICU library.

%description icu-devel -l pl.UTF-8
Plik nagłówkowy biblioteki HarfBuzz ICU.

%package icu-static
Summary:	Static HarfBuzz ICU library
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz ICU
Group:		Development/Libraries
Requires:	%{name}-icu-devel = %{version}-%{release}

%description icu-static
Static HarfBuzz ICU library.

%description icu-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz ICU.

%prep
%setup -q

# missing dependencies
cat >> src/harfbuzz.pc.in <<EOF
Requires.private: glib-2.0 gobject-2.0 freetype2%{?with_graphite2: graphite2}
EOF

%build
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-cairo \
	--with-freetype \
	--with-glib \
	%{?with_graphite2:--with-graphite2} \
	--with-icu%{!?with_icu:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	icu -p /sbin/ldconfig
%postun	icu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/hb-ot-shape-closure
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-view
%attr(755,root,root) %{_libdir}/libharfbuzz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz.so
%dir %{_includedir}/harfbuzz
%{_includedir}/harfbuzz/hb.h
%{_includedir}/harfbuzz/hb-blob.h
%{_includedir}/harfbuzz/hb-buffer.h
%{_includedir}/harfbuzz/hb-common.h
%{_includedir}/harfbuzz/hb-font.h
%{_includedir}/harfbuzz/hb-ft.h
%{_includedir}/harfbuzz/hb-glib.h
%{_includedir}/harfbuzz/hb-gobject.h
%{?with_graphite2:%{_includedir}/harfbuzz/hb-graphite2.h}
%{_includedir}/harfbuzz/hb-ot-layout.h
%{_includedir}/harfbuzz/hb-ot-tag.h
%{_includedir}/harfbuzz/hb-ot.h
%{_includedir}/harfbuzz/hb-set.h
%{_includedir}/harfbuzz/hb-shape-plan.h
%{_includedir}/harfbuzz/hb-shape.h
%{_includedir}/harfbuzz/hb-unicode.h
%{_includedir}/harfbuzz/hb-version.h
%{_pkgconfigdir}/harfbuzz.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz.a
%endif

%if %{with icu}
%files icu
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-icu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz-icu.so.0

%files icu-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-icu.so
%{_includedir}/harfbuzz/hb-icu.h
%{_pkgconfigdir}/harfbuzz-icu.pc

%if %{with static_libs}
%files icu-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-icu.a
%endif
%endif
