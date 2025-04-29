#
# TODO:
# - s=/dev/null=/home/services/xdm= in %%trigger for graceful upgrade from xdm/kdm/gdm 2.2
# - check all /etc/pam.d/gdm-* to be pldized:
#   gdm-autologin[4] gdm-fingerprint[10] gdm-password[1] gdm-smartcard gdm-launch-environment[11]
#
# Conditional build:
%bcond_without	static_libs	# static library

%define		glib2_ver	1:2.68.0
Summary:	GNOME Display Manager
Summary(es.UTF-8):	Administrador de Entrada del GNOME
Summary(ja.UTF-8):	GNOME ディスプレイマネージャ
Summary(pl.UTF-8):	gdm - zarządca ekranów GNOME
Summary(pt_BR.UTF-8):	Gerenciador de Entrada do GNOME
Summary(ru.UTF-8):	Дисплейный менеджер GNOME
Summary(uk.UTF-8):	Дисплейний менеджер GNOME
Name:		gdm
Version:	48.0
Release:	1
Epoch:		2
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/gdm/48/%{name}-%{version}.tar.xz
# Source0-md5:	a17868752c9a90ed560891886f2882f2
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
Source4:	%{name}-autologin.pamd
Source5:	%{name}-custom.desktop
Source6:	%{name}-default.desktop
Source9:	%{name}.tmpfiles
Source10:	%{name}-fingerprint.pamd
Source11:	%{name}-launch-environment.pamd
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-xsession.patch
Patch2:		%{name}-defaults.patch
Patch3:		%{name}-both-libraries.patch
URL:		https://wiki.gnome.org/Projects/GDM
BuildRequires:	accountsservice-devel >= 0.6.35
BuildRequires:	audit-libs-devel
BuildRequires:	check-devel >= 0.9.4
BuildRequires:	dconf-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= %{glib2_ver}
BuildRequires:	gobject-introspection-devel >= 0.9.12
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	iso-codes
BuildRequires:	json-glib-devel >= 1.2.0
BuildRequires:	keyutils-devel >= 1.6
BuildRequires:	libcanberra-gtk3-devel >= 0.4
BuildRequires:	libgudev-devel >= 232
BuildRequires:	libselinux-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libwrap-devel
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.57
BuildRequires:	ninja >= 1.5
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
BuildRequires:	plymouth-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
# for "XServer disables tcp access by default" detection
BuildRequires:	xorg-xserver-server-devel >= 1.17
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= %{glib2_ver}
Requires(post,postun):	gtk-update-icon-cache
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(posttrans):	dconf
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	/usr/bin/X
Requires:	accountsservice >= 0.6.35
Requires:	dbus-x11
Requires:	gdm-wm >= 3.2.1
Requires:	glib2 >= %{glib2_ver}
Requires:	gnome-session >= 3.26.0
Requires:	gnome-settings-daemon >= 3.26.0
Requires:	hicolor-icon-theme
Requires:	iso-codes
Requires:	json-glib >= 1.2.0
Requires:	libcanberra-gtk3 >= 0.4
Requires:	libgudev >= 232
Requires:	pam >= 0.99.7.1
Requires:	polkit-gnome >= 0.93
Requires:	which
Requires:	xinitrc-ng >= 1.0
Requires:	xorg-app-sessreg
Requires:	xorg-app-xmodmap
Suggests:	ConsoleKit-x11 >= 0.4.1
Suggests:	pam-pam_gnome_keyring
Suggests:	xorg-xserver-Xephyr >= 1.17
Suggests:	zenity
Provides:	XDM
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	gdm-Xnest < 2:2.28
Obsoletes:	gdm-systemd < 2:3.2.1.1-10
Obsoletes:	gdm-upstart < 2:3.20
Obsoletes:	gdm-user-switch-applet < 2:3.0.0-2
Obsoletes:	gnome-applet-fast-user-switch < 2.21
Conflicts:	gdkxft
Conflicts:	systemd < 186
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es.UTF-8
Administrador de Entrada del GNOME.

%description -l ja.UTF-8
Gdm (the GNOME Display Manager) は、高度に設定可能な xdm X Display Manager
の再実装版です。 Gdm を使うと、 X Window System が動いているあなたの
システムにいろいろなセッションを選択してログインすることができます。

このバージョンの Gdm では、各種言語や、XIM を選択することも可能です。

%description -l pl.UTF-8
Gdm jest wysokokonfigurowalną reimplementacją xdma. Gdm pozwala
logować się do systemu z poziomu X11 i wspiera jednoczesną pracę kilku
różnych sesji X na lokalnej maszynie.

%description -l pt_BR.UTF-8
Gerenciador de Entrada do GNOME.

%description -l ru.UTF-8
GDM (GNOME Display Manager) - это реимплементация xdm (X Display
Manager). GDM позволяет вам входить в систему, на которой запущено X
Window и поддерживает работу нескольуих разных X сеансов одновременно.

%description -l uk.UTF-8
GDM (GNOME Display Manager) - це реімплементація xdm (X Display
Manager). GDM дозволяє вам входити в систему, на якій запущено X
Window та підтримує роботу кількох різних X сеансів одночасно.

%package init
Summary:	Init script for GDM
Summary(pl.UTF-8):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires(post,preun):	/sbin/chkconfig
Requires(post,preun,postun):	systemd-units >= 38
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	open
Requires:	rc-scripts >= 0.4.3.0
Requires:	systemd-units >= 38

%description init
Init script for GDM.

%description init -l pl.UTF-8
Skrypt init dla GDM-a.

%package libs
Summary:	GDM libraries
Summary(pl.UTF-8):	Biblioteki GDM
Group:		Libraries
Requires:	glib2 >= %{glib2_ver}

%description libs
GDM libraries.

%description libs -l pl.UTF-8
Biblioteki GDM.

%package devel
Summary:	Header files for GDM
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= %{glib2_ver}
Requires:	libselinux-devel
Requires:	systemd-devel >= 1:209

%description devel
This package contains the files necessary to develop applications
using GDM's libraries.

%description devel -l pl.UTF-8
Pakiet zawiera pliki potrzebne do rozwoju aplikacji używających
bibliotek programu GDM.

%package static
Summary:	Static libraries for GDM
Summary(pl.UTF-8):	Biblioteki statyczne dla GDM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
This package contains static libraries for GDM.

%description static -l pl.UTF-8
Pakiet zawiera statyczne biblioteki GDM.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%meson \
	%{!?with_static_libs:--default-library=shared} \
	-Dgdm-xsession=true \
	-Dgroup=xdm \
	-Dinitial-vt=9 \
	-Dipv6=true \
	-Dlibaudit=enabled \
	-Dpam-mod-dir=/%{_lib}/security \
	-Dpam-prefix=/etc \
	-Dplymouth=enabled \
	-Dselinux=enabled \
	-Dtcp-wrappers=true \
	-Dudev-dir=/lib/udev/rules.d \
	-Duser=xdm \
	-Dxdmcp=enabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/lib/gdm/.local,/var/log/gdm,/var/run/gdm/greeter} \
	$RPM_BUILD_ROOT{%{_pixmapsdir},%{_datadir}/xsessions,%{systemdunitdir}} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%meson_install

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm-password
cp -p %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/gdm-fingerprint
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/pam.d/gdm-launch-environment
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
cp -p %{SOURCE9} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

# replace file with mask (to allow choosing via prefdm.service)
ln -sf /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/gdm.service

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --with-gnome

# allow executing ~/.Xclients and ~/.xsession
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/custom.desktop
cp -p %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/default.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
umask 022
/usr/bin/dconf update

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%triggerpostun -- %{name} < 2:3.2.1.1-10
if [ -f /etc/X11/gdm/gdm.conf-custom.rpmsave ]; then
	mv -f /etc/X11/gdm/gdm.conf-custom.rpmsave /etc/gdm/custom.conf
fi

%post init
/sbin/chkconfig --add gdm
# -n skips restarting as it would otherise terminate all sessions opened from gdm!
%service -n gdm restart
%systemd_reload

%postun init
%systemd_reload

%preun init
if [ "$1" = "0" ]; then
	%service gdm stop
	/sbin/chkconfig --del gdm
fi

%post libs
/sbin/ldconfig
%glib_compile_schemas

%postun libs
/sbin/ldconfig
if [ "$1" = "0" ]; then
	%glib_compile_schemas
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_sbindir}/gdm
%attr(755,root,root) %{_bindir}/gdm-config
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-runtime-config
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-wayland-session
%attr(755,root,root) %{_libexecdir}/gdm-x-session
%attr(755,root,root) /%{_lib}/security/pam_gdm.so
/lib/udev/rules.d/61-gdm.rules
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%dir %{_sysconfdir}/gdm/PostLogin
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(640,root,xdm) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/gdm.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm-*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%{_datadir}/dconf/profile/gdm
%{_datadir}/polkit-1/rules.d/20-gdm.rules
%dir %{systemduserunitdir}/gnome-session@gnome-login.target.d
%{systemduserunitdir}/gnome-session@gnome-login.target.d/session.conf
%attr(1770,root,xdm) %dir /var/lib/gdm
%attr(755,xdm,xdm) /var/lib/gdm/.local
%attr(750,xdm,xdm) %dir /var/log/gdm
%attr(711,root,xdm) %dir /var/run/gdm
%attr(755,xdm,xdm) %dir /var/run/gdm/greeter
%attr(750,xdm,xdm) /home/services/xdm
%{systemdtmpfilesdir}/%{name}.conf
%{_pixmapsdir}/gdm-pld-logo.png
%{_datadir}/gdm
%{_datadir}/gnome-session/sessions/gnome-login.session
%{_datadir}/xsessions/custom.desktop
%{_datadir}/xsessions/default.desktop

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
%{systemdunitdir}/gdm.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdm.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libgdm.so.1
%{_libdir}/girepository-1.0/Gdm-1.0.typelib
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdm.so
%{_includedir}/gdm
%{_pkgconfigdir}/gdm.pc
%{_pkgconfigdir}/gdm-pam-extensions.pc
%{_datadir}/gir-1.0/Gdm-1.0.gir

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgdm.a
%endif
