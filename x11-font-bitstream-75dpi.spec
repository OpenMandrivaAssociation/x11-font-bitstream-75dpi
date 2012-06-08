%define	oname	font-bitstream-75dpi

Name:		x11-%{oname}
Version:	1.0.3
Release:	5
Summary:	Xorg X11 font bitstream-75dpi
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/font/%{oname}-%{version}.tar.bz2
License:	MIT
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	x11-font-util >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
Conflicts:	xorg-x11-75dpi-fonts <= 6.9.0
Requires(post):	mkfontdir
Requires(postun):mkfontdir
Requires(post):	mkfontscale
Requires(postun):mkfontscale

%description
Xorg X11 font bitstream-75dpi

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x	--build=%{_arch}-%{_target_vendor}-%{_target_os}%{?_gnu} \
		--x-libraries=%{_libdir} \
		--with-fontdir=%{_datadir}/fonts/75dpi

%make

%install
%makeinstall_std
rm -f %{buildroot}%{_datadir}/fonts/75dpi/fonts.dir

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
