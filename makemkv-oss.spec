Name:           makemkv-oss
Version:        1.18.4
Release:        %autorelease
Summary:        The open-source components of MakeMKV

License:        GPL-2.0-or-later
URL:            https://www.makemkv.com/
Source0:        https://www.makemkv.com/download/makemkv-oss-%{version}.tar.gz
Source1:        makemkv.metainfo.xml

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(zlib)

Provides:       bundled(libdvdnav) = 6.1.1
Provides:       bundled(libdvdread) = 6.1.2
Provides:       bundled(libebml) = 1.3.10
Provides:       bundled(libmatroska) = 1.5.2

%description
This package contains the open-source supporting components of MakeMKV.

%package -n makemkv
Summary:        A decryption and transcoding tool for DVD and Blu-ray discs
Requires:       makemkv-bin%{?_isa} >= %{version}-1

%description -n makemkv
MakeMKV is a toolkit for decrypting and transcoding DVD, HD DVD, and Blu-ray
discs to MKV files. It can integrate with libbluray to allow video players
(VLC, MPV) to play discs with bus encryption (e.g., Ultra HD Blu-ray).

This package contains the main GUI for MakeMKV.

%package -n libmakemkv
Summary:        A MKV multiplexer library used by MakeMKV

%description -n libmakemkv
A MKV multiplexer library used by MakeMKV.

%package -n libmakemkv-devel
Summary:        Development files for libmakemkv
Requires:       libmakemkv%{?_isa} = %{version}-%{release}

%description -n libmakemkv-devel
Library and header files for applications using libmakemkv.

%package -n libdriveio
Summary:        A drive interrogation library used by MakeMKV

%description -n libdriveio
A drive interrogation library used by MakeMKV.

%package -n libdriveio-devel
Summary:        Development files for libdriveio
Requires:       libdriveio%{?_isa} = %{version}-%{release}

%description -n libdriveio-devel
Library and header files for applications using libdriveio.

%package -n libmmbd
Summary:        A library for decrypting Blu-ray files using MakeMKV
Requires:       makemkv-bin%{?_isa} >= %{version}-1

%description -n libmmbd
A library for decrypting Blu-ray files using MakeMKV. It can be used by
libbluray to allow for on-the-fly decryption in video players such as MPV.

%package -n libmmbd-devel
Summary:        Development files for libmmbd
Requires:       libmmbd%{?_isa} = %{version}-%{release}

%description -n libmmbd-devel
Library and header files for applications using libmmbd.

%prep
%autosetup

%build
%configure
%make_build ENABLE_DEBUG=yes

%install
%make_install
# Install AppData
mkdir -p %{buildroot}%{_metainfodir}
install %{SOURCE1} %{buildroot}%{_metainfodir}/makemkv.metainfo.xml
# Correct library permissions for Fedora / Red Hat systems
chmod 755 %{buildroot}%{_libdir}/libdriveio.so*
chmod 755 %{buildroot}%{_libdir}/libmakemkv.so*
chmod 755 %{buildroot}%{_libdir}/libmmbd.so*
# Install headers
mkdir -p %{buildroot}%{_includedir}/driveio
install -m0644 libdriveio/inc/driveio/*.h %{buildroot}%{_includedir}/driveio
mkdir -p %{buildroot}%{_includedir}/libmkv
install -m0644 libmakemkv/inc/libmkv/*.h %{buildroot}%{_includedir}/libmkv
mkdir -p %{buildroot}%{_includedir}/libmmbd
install -m0644 libmmbd/inc/libmmbd/*.h %{buildroot}%{_includedir}/libmmbd

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/makemkv.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license License.txt
%{_bindir}/mmccextr
%{_bindir}/mmgplsrv

%files -n makemkv
%license License.txt
%{_bindir}/makemkv
%{_datadir}/applications/makemkv.desktop
%{_metainfodir}/makemkv.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/makemkv.png

%files -n libdriveio
%license License.txt
%{_libdir}/libdriveio.so*

%files -n libdriveio-devel
%license License.txt
%{_includedir}/driveio

%files -n libmakemkv
%license License.txt
%{_libdir}/libmakemkv.so*

%files -n libmakemkv-devel
%license License.txt
%{_includedir}/libmkv

%files -n libmmbd
%license License.txt
%{_libdir}/libmmbd.so*

%files -n libmmbd-devel
%license License.txt
%{_includedir}/libmmbd

%changelog
%autochangelog
