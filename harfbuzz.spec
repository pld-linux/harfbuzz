#
# Conditional build:
%bcond_without	static_libs	# static libraries build
%bcond_without	graphite2	# Graphite2 library usage
%bcond_without	icu		# ICU integration
%bcond_without	tests		# "make check" call

Summary:	HarfBuzz - internationalized text shaping library
Summary(pl.UTF-8):	HarfBuzz - biblioteka rysująca tekst z obsługą wielu języków
Name:		harfbuzz
Version:	1.4.5
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://www.freedesktop.org/software/harfbuzz/release/%{name}-%{version}.tar.bz2
# Source0-md5:	635126eeab703d1729df9391ffb7983c
Patch0:		pc_deps.patch
URL:		https://www.freedesktop.org/wiki/HarfBuzz
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11.1
BuildRequires:	cairo-devel >= 1.8.0
# hb-fc-list is disabled in util/Makefile.am
#BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 1:2.4.2
BuildRequires:	glib2-devel >= 1:2.38
BuildRequires:	gobject-introspection-devel >= 1.34.0
%{?with_graphite2:BuildRequires:	graphite2-devel}
BuildRequires:	gtk-doc >= 1.15
%{?with_icu:BuildRequires:	libicu-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig >= 1:0.27
BuildRequires:	sed >= 4.0
Requires:	freetype >= 1:2.4.2
Requires:	glib2 >= 1:2.38
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
Requires:	freetype-devel >= 1:2.4.2
Requires:	glib2-devel >= 1:2.38
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

%package gobject
Summary:	Harfbuzz GObject interface
Summary(pl.UTF-8):	Interfejs GObject do biblioteki Harfbuzz
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gobject
Harfbuzz GObject interface.

%description gobject -l pl.UTF-8
Interfejs GObject do biblioteki Harfbuzz.

%package gobject-devel
Summary:	Header files for Harfbuzz GObject interface
Summary(pl.UTF-8):	Pliki nagłówkowe interfejsu GObject do biblioteki Harfbuzz
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gobject = %{version}-%{release}

%description gobject-devel
This is the package containing the header files for Harfbuzz GObject
interface.

%description gobject-devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe interfejsu GObject do biblioteki
Harfbuzz.

%package gobject-static
Summary:	Static Harfbuzz GObject library
Summary(pl.UTF-8):	Statyczna biblioteka Harfbuzz GObject
Group:		Development/Libraries
Requires:	%{name}-gobject-devel = %{version}-%{release}

%description gobject-static
Static Harfbuzz GObject library.

%description gobject-static -l pl.UTF-8
Statyczna biblioteka Harfbuzz GObject.

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

%package progs
Summary:	HarfBuzz command-line utilities
Summary(pl.UTF-8):	Narzędzia HarfBuzz uruchamiane z linii poleceń
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cairo >= 1.8.0

%description progs
HarfBuzz command-line utilities.

%description progs -l pl.UTF-8
Narzędzia HarfBuzz uruchamiane z linii poleceń.

%package apidocs
Summary:	HarfBuzz API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek HarfBuzz
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for HarfBuzz libraries.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek HarfBuzz.

%prep
%setup -q

%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-cairo \
	--with-freetype \
	--with-glib \
	--with-gobject \
	%{?with_graphite2:--with-graphite2} \
	--with-html-dir=%{_gtkdocdir} \
	--with-icu%{!?with_icu:=no}
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	gobject -p /sbin/ldconfig
%postun	gobject -p /sbin/ldconfig

%post	icu -p /sbin/ldconfig
%postun	icu -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS TODO
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
%{_includedir}/harfbuzz/hb-deprecated.h
%{_includedir}/harfbuzz/hb-face.h
%{_includedir}/harfbuzz/hb-font.h
%{_includedir}/harfbuzz/hb-ft.h
%{_includedir}/harfbuzz/hb-glib.h
%{?with_graphite2:%{_includedir}/harfbuzz/hb-graphite2.h}
%{_includedir}/harfbuzz/hb-ot-font.h
%{_includedir}/harfbuzz/hb-ot-layout.h
%{_includedir}/harfbuzz/hb-ot-math.h
%{_includedir}/harfbuzz/hb-ot-shape.h
%{_includedir}/harfbuzz/hb-ot-tag.h
%{_includedir}/harfbuzz/hb-ot-var.h
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

%files gobject
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libharfbuzz-gobject.so.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files gobject-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libharfbuzz-gobject.so
%{_includedir}/harfbuzz/hb-gobject.h
%{_includedir}/harfbuzz/hb-gobject-enums.h
%{_includedir}/harfbuzz/hb-gobject-structs.h
%{_pkgconfigdir}/harfbuzz-gobject.pc
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%if %{with static_libs}
%files gobject-static
%defattr(644,root,root,755)
%{_libdir}/libharfbuzz-gobject.a
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

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/hb-ot-shape-closure
%attr(755,root,root) %{_bindir}/hb-shape
%attr(755,root,root) %{_bindir}/hb-view

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/harfbuzz
