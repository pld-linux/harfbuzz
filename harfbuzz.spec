#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	graphite2	# Graphite2 complementary shaper
%bcond_without	icu		# ICU integration
%bcond_with	tests		# "make check" call (cmap14 test fails as of 2.6.2 +otsanitizer-8.0.0 +fonttools-3.44.0)

Summary:	HarfBuzz - internationalized text shaping library
Summary(pl.UTF-8):	HarfBuzz - biblioteka rysująca tekst z obsługą wielu języków
Name:		harfbuzz
Version:	11.2.1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	53d77e130fc16e95c4e8a09c0c6fbd85
URL:		https://harfbuzz.github.io/
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	chafa-devel >= 1.6.0
%{?with_tests:BuildRequires:	fonttools}
BuildRequires:	freetype-devel >= 1:2.11
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 1.34.0
%{?with_graphite2:BuildRequires:	graphite2-devel >= 1.2.0}
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	help2man
%{?with_icu:BuildRequires:	libicu-devel >= 49.0}
BuildRequires:	libstdc++-devel >= 6:4.9
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
%{?with_tests:BuildRequires:	otsanitizer >= 8}
BuildRequires:	pkgconfig >= 1:0.28
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	freetype%{?_isa} >= 1:2.11
Requires:	glib2%{?_isa} >= 1:2.38
%{?with_graphite2:Requires:	graphite2%{?_isa} >= 1.2.0}
Provides:	harfbuzz-gobject = %{version}-%{release}
Obsoletes:	harfbuzz-gobject < 2.7.1-2
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
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	freetype-devel%{?_isa} >= 1:2.11
Requires:	glib2-devel%{?_isa} >= 1:2.38
%{?with_graphite2:Requires:	graphite2-devel%{?_isa} >= 1.2.0}
Requires:	libstdc++-devel%{?_isa} >= 6:4.9
Provides:	harfbuzz-gobject-devel = %{version}-%{release}
Obsoletes:	harfbuzz-gobject-devel < 2.7.1-2

%description devel
Header files for HarfBuzz library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HarfBuzz.

%package static
Summary:	Static HarfBuzz library
Summary(pl.UTF-8):	Statyczna biblioteka HarfBuzz
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Provides:	harfbuzz-gobject-static = %{version}-%{release}
Obsoletes:	harfbuzz-gobject-static < 2.7.1-3

%description static
Static HarfBuzz library.

%description static -l pl.UTF-8
Statyczna biblioteka HarfBuzz.

%package cairo
Summary:	HarfBuzz text shaping library - cairo integration
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - integracja z cairo
Group:		Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description cairo
HarfBuzz text shaping library - cairo integration.

%description cairo -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - integracja z cairo.

%package cairo-devel
Summary:	Header files for HarfBuzz cairo library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki HarfBuzz cairo
Group:		Development/Libraries
Requires:	%{name}-cairo%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description cairo-devel
Header files for HarfBuzz cairo library.

%description cairo-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HarfBuzz cairo.

%package cairo-static
Summary:	Static HarfBuzz cairo library
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz cairo
Group:		Development/Libraries
Requires:	%{name}-cairo-devel%{?_isa} = %{version}-%{release}

%description cairo-static
Static HarfBuzz cairo library.

%description cairo-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz cairo.

%package icu
Summary:	HarfBuzz text shaping library - ICU integration
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - integracja z ICU
Group:		Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libicu%{?_isa} >= 49.0

%description icu
HarfBuzz text shaping library - ICU integration.

%description icu -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - integracja z ICU.

%package icu-devel
Summary:	Header file for HarfBuzz ICU library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki HarfBuzz ICU
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-icu%{?_isa} = %{version}-%{release}
Requires:	libicu-devel%{?_isa} >= 49.0

%description icu-devel
Header file for HarfBuzz ICU library.

%description icu-devel -l pl.UTF-8
Plik nagłówkowy biblioteki HarfBuzz ICU.

%package icu-static
Summary:	Static HarfBuzz ICU library
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz ICU
Group:		Development/Libraries
Requires:	%{name}-icu-devel%{?_isa} = %{version}-%{release}

%description icu-static
Static HarfBuzz ICU library.

%description icu-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz ICU.

%package subset
Summary:	HarfBuzz text shaping library - font subsetter
Summary(pl.UTF-8):	Biblioteka HarfBuzz do rysowania tekstu - font subsetter
Group:		Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description subset
HarfBuzz text shaping library - font subsetter.

%description subset -l pl.UTF-8
Biblioteka HarfBuzz do rysowania tekstu - font subsetter.

%package subset-devel
Summary:	Header files for HarfBuzz subset library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki HarfBuzz subset
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	%{name}-subset%{?_isa} = %{version}-%{release}

%description subset-devel
Header files for HarfBuzz subset library.

%description subset-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki HarfBuzz subset.

%package subset-static
Summary:	Static HarfBuzz subset library
Summary(pl.UTF-8):	Biblioteka statyczna HarfBuzz subset
Group:		Development/Libraries
Requires:	%{name}-subset-devel%{?_isa} = %{version}-%{release}

%description subset-static
Static HarfBuzz subset library.

%description subset-static -l pl.UTF-8
Biblioteka statyczna HarfBuzz subset.

%package progs
Summary:	HarfBuzz command-line utilities
Summary(pl.UTF-8):	Narzędzia HarfBuzz uruchamiane z linii poleceń
Group:		Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	cairo%{?_isa} >= 1.10.0
Requires:	chafa-libs%{?_isa} >= 1.6.0

%description progs
HarfBuzz command-line utilities.

%description progs -l pl.UTF-8
Narzędzia HarfBuzz uruchamiane z linii poleceń.

%package apidocs
Summary:	HarfBuzz API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek HarfBuzz
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for HarfBuzz libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek HarfBuzz.

%prep
%setup -q

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Dcairo=enabled \
	-Dchafa=enabled \
	-Ddocs=enabled \
	-Dfreetype=enabled \
	-Dglib=enabled \
	-Dgobject=enabled \
	-Dgraphite2=%{__enabled_disabled graphite2} \
	-Dicu=%{__enabled_disabled icu} \
	-Dintrospection=enabled \
	-Dtests=%{__enabled_disabled tests}

%meson_build

%{?with_tests:%meson_test}

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	cairo -p /sbin/ldconfig
%postun	cairo -p /sbin/ldconfig

%post	icu -p /sbin/ldconfig
%postun	icu -p /sbin/ldconfig

%post	subset -p /sbin/ldconfig
%postun	subset -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README.md THANKS
%attr(755,root,root) %{_libdir}/libharfbuzz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz.so.0
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz-gobject.so.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz.so
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so
%dir %{_includedir}/harfbuzz
%{_includedir}/harfbuzz/hb.h
%{_includedir}/harfbuzz/hb-aat.h
%{_includedir}/harfbuzz/hb-aat-layout.h
%{_includedir}/harfbuzz/hb-blob.h
%{_includedir}/harfbuzz/hb-buffer.h
%{_includedir}/harfbuzz/hb-common.h
%{_includedir}/harfbuzz/hb-cplusplus.hh
%{_includedir}/harfbuzz/hb-deprecated.h
%{_includedir}/harfbuzz/hb-draw.h
%{_includedir}/harfbuzz/hb-face.h
%{_includedir}/harfbuzz/hb-features.h
%{_includedir}/harfbuzz/hb-font.h
%{_includedir}/harfbuzz/hb-ft.h
%{_includedir}/harfbuzz/hb-glib.h
%{_includedir}/harfbuzz/hb-gobject.h
%{_includedir}/harfbuzz/hb-gobject-enums.h
%{_includedir}/harfbuzz/hb-gobject-structs.h
%{?with_graphite2:%{_includedir}/harfbuzz/hb-graphite2.h}
%{_includedir}/harfbuzz/hb-map.h
%{_includedir}/harfbuzz/hb-ot-color.h
%{_includedir}/harfbuzz/hb-ot-deprecated.h
%{_includedir}/harfbuzz/hb-ot-font.h
%{_includedir}/harfbuzz/hb-ot-layout.h
%{_includedir}/harfbuzz/hb-ot-math.h
%{_includedir}/harfbuzz/hb-ot-meta.h
%{_includedir}/harfbuzz/hb-ot-metrics.h
%{_includedir}/harfbuzz/hb-ot-name.h
%{_includedir}/harfbuzz/hb-ot-shape.h
%{_includedir}/harfbuzz/hb-ot-var.h
%{_includedir}/harfbuzz/hb-ot.h
%{_includedir}/harfbuzz/hb-paint.h
%{_includedir}/harfbuzz/hb-script-list.h
%{_includedir}/harfbuzz/hb-set.h
%{_includedir}/harfbuzz/hb-shape-plan.h
%{_includedir}/harfbuzz/hb-shape.h
%{_includedir}/harfbuzz/hb-style.h
%{_includedir}/harfbuzz/hb-unicode.h
%{_includedir}/harfbuzz/hb-version.h
%{_pkgconfigdir}/harfbuzz.pc
%{_pkgconfigdir}/harfbuzz-gobject.pc
%dir %{_libdir}/cmake/harfbuzz
%{_libdir}/cmake/harfbuzz/harfbuzz-config.cmake
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz.a
%{_libdir}/libharfbuzz-gobject.a
%endif

%files cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-cairo.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz-cairo.so.0

%files cairo-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-cairo.so
%{_includedir}/harfbuzz/hb-cairo.h
%{_pkgconfigdir}/harfbuzz-cairo.pc

%if %{with static_libs}
%files cairo-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-cairo.a
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

%files subset
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-subset.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz-subset.so.0

%files subset-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-subset.so
%{_includedir}/harfbuzz/hb-subset.h
%{_includedir}/harfbuzz/hb-subset-serialize.h
%{_pkgconfigdir}/harfbuzz-subset.pc

%if %{with static_libs}
%files subset-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-subset.a
%endif

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hb-info
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-subset
%attr(755,root,root) %{_bindir}/hb-view
%{_mandir}/man1/hb-info.1*
%{_mandir}/man1/hb-shape.1*
%{_mandir}/man1/hb-subset.1*
%{_mandir}/man1/hb-view.1*

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/harfbuzz
