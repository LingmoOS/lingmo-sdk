Name:           lingmo-sdk
Version:        5.0.9
Release:        1.lingmo5u1%{?dist}
Summary:        Lingmo desktop application SDK
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/lingmo-sdk
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.22
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  wayland-devel >= 1.23
BuildRequires:  wayland-protocols-devel >= 1.39
BuildRequires:  pkgconfig(egl) pkgconfig(glesv2) pkgconfig(fontconfig)
BuildRequires:  pkgconfig(xkbcommon) pkgconfig(libsystemd)
BuildRequires:  pkgconfig(icu-uc) pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libpng) pkgconfig(libwebp) pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(libtiff-4) pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl) pkgconfig(libjxl_threads)
BuildRequires:  pkgconfig(freetype2) pkgconfig(harfbuzz) pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib) pkgconfig(expat)

%description
Runtime libraries for Lingmo desktop applications.

%package devel
Summary:        Development files for the Lingmo SDK
Requires:       %{name} = %{version}-%{release}
Requires:       wayland-devel >= 1.23

%description devel
Headers, CMake package metadata and link libraries required to build Lingmo
applications.

%prep
%autosetup -p1

%build
%cmake -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/liblingmo-sdk.so.*
%{_libdir}/liblingmo-sdk-base.so.*

%files devel
%{_includedir}/lingmo-sdk/
%{_libdir}/liblingmo-sdk.so
%{_libdir}/liblingmo-sdk-base.so
%{_libdir}/cmake/LingmoSDK/

%changelog
* Mon Nov 16 2026 Lingmo OS Team <team@lingmo.org> - 5.0.9-1.lingmo5u1
- Generate Debian and RPM sources from the same Skia-complete tree.
