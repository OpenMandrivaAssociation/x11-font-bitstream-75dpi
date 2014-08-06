Name: x11-font-bitstream-75dpi
Version: 1.0.3
Release: 12
Summary: Xorg X11 font bitstream-75dpi
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-bitstream-75dpi-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-75dpi-fonts <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bitstream-75dpi

%prep
%setup -q -n font-bitstream-75dpi-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/75dpi
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.scale

%post
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%postun
mkfontscale %{_datadir}/fonts/75dpi
mkfontdir %{_datadir}/fonts/75dpi

%files
%doc COPYING
%{_datadir}/fonts/75dpi/char*.pcf.gz
%{_datadir}/fonts/75dpi/tech*.pcf.gz
%{_datadir}/fonts/75dpi/term*.pcf.gz
