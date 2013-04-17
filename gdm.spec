#
# TODO:
# - s=/dev/null=/home/services/xdm= in %%trigger for graceful upgrade from xdm/kdm/gdm 2.2
# - check all /etc/pam.d/gdm-* to be pldized:
#   gdm-autologin[4] gdm-fingerprint[10] gdm-password[1] gdm-smartcard gdm-launch-environment[11]
#
# Conditional build:
%bcond_without  systemd # by default use systemd for session tracking instead of ConsoleKit (fallback to ConsoleKit on runtime)

%define		glib2_version 1:2.35.0
Summary:	GNOME Display Manager
Summary(es.UTF-8):	Administrador de Entrada del GNOME
Summary(ja.UTF-8):	GNOME ディスプレイマネージャ
Summary(pl.UTF-8):	gdm - zarządca ekranów GNOME
Summary(pt_BR.UTF-8):	Gerenciador de Entrada do GNOME
Summary(ru.UTF-8):	Дисплейный менеджер GNOME
Summary(uk.UTF-8):	Дисплейний менеджер GNOME
Name:		gdm
Version:	3.8.1
Release:	1
Epoch:		2
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	fbfe02e3eb744e3f898b11ad7a7d37d2
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
Source4:	%{name}-autologin.pamd
Source5:	%{name}-custom.desktop
Source6:	%{name}-default.desktop
Source7:	%{name}.upstart
Source9:	%{name}.tmpfiles
Source10:	%{name}-fingerprint.pamd
Source11:	%{name}-launch-environment.pamd
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-xsession.patch
Patch2:		%{name}-defaults.patch
Patch3:		shell-check.patch
URL:		http://www.gnome.org/projects/gdm/
BuildRequires:	accountsservice-devel >= 0.6.12
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	check-devel >= 0.9.4
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	fontconfig-devel >= 2.5.0
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	gobject-introspection-devel >= 0.9.12
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel >= 0.4
BuildRequires:	libselinux-devel
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	nss-devel >= 3.11.1
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1.3.0
BuildRequires:	pkgconfig
BuildRequires:	plymouth-devel
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.627
%{?with_systemd:BuildRequires:	systemd-devel >= 186}
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.9.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-xserver-Xephyr
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= %{glib2_version}
Requires(post,postun):	gtk-update-icon-cache
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(posttrans):	dconf
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	/usr/bin/X
Requires:	accountsservice >= 0.6.12
Requires:	dbus-x11
Requires:	gdm-wm >= 3.2.1
Requires:	glib2 >= %{glib2_version}
Requires:	gnome-session >= 3.0.0
Requires:	gnome-settings-daemon >= 3.0.0
Requires:	hicolor-icon-theme
Requires:	pam >= 0.99.7.1
Requires:	polkit-gnome >= 0.93
Requires:	which
Requires:	xinitrc-ng >= 1.0
Requires:	xorg-app-sessreg
Requires:	xorg-app-xmodmap
Suggests:	ConsoleKit-x11 >= 0.4.1
Suggests:	pam-pam_gnome_keyring
Suggests:	xorg-xserver-Xephyr
Suggests:	zenity
Provides:	XDM
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	gdm-Xnest
Obsoletes:	gdm-systemd
Obsoletes:	gdm-user-switch-applet
Obsoletes:	gnome-applet-fast-user-switch
Conflicts:	gdkxft
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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

%package libs
Summary:	GDM libraries
Summary(pl.UTF-8):	Biblioteki GDM
Group:		Libraries

%description libs
GDM libraries.

%description libs -l pl.UTF-8
Biblioteki GDM.

%package devel
Summary:	Header files for GDM
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

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

%package upstart
Summary:	Upstart job description for GDM
Summary(pl.UTF-8):	Opis zadania Upstart dla GDM
Group:		Daemons
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	upstart >= 0.6

%description upstart
Upstart job description for GDM.

%description upstart -l pl.UTF-8
Opis zadania Upstart dla GDM.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
touch data/gdm.schemas.in.in
%{__libtoolize}
%{__glib_gettextize}
%{__intltoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	SYSTEMD_X_SERVER=/lib/systemd/systemd-multi-seat-x \
	%{?debug:--enable-debug} \
	--disable-console-helper \
	--disable-silent-rules \
	%{__with_without systemd systemd} \
	--with-console-kit \
	--enable-authentication-scheme=pam \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers=yes \
	--with-xdmcp=yes \
	--with-xinerama=yes \
	--with-user=xdm \
	--with-group=xdm \
	--enable-ipv6

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security,init} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \
	$RPM_BUILD_ROOT{%{_datadir}/xsessions,%{systemdunitdir}} \
	$RPM_BUILD_ROOT%{systemdtmpfilesdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=%{_sysconfdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm-password
cp -p %{SOURCE10} $RPM_BUILD_ROOT/etc/pam.d/gdm-fingerprint
cp -p %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
cp -p %{SOURCE11} $RPM_BUILD_ROOT/etc/pam.d/gdm-launch-environment
install -p %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm
cp -p %{SOURCE7} $RPM_BUILD_ROOT/etc/init/%{name}.conf
cp -p %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
ln -s /dev/null $RPM_BUILD_ROOT%{systemdunitdir}/gdm.service
install %{SOURCE9} $RPM_BUILD_ROOT%{systemdtmpfilesdir}/%{name}.conf

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --with-gnome --with-omf --all-name

# allow executing ~/.Xclients and ~/.xsession
cp -p %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/custom.desktop
cp -p %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/default.desktop

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gdm/simple-greeter/extensions/*.{a,la} \
    $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%posttrans
umask 022
/usr/bin/dconf update

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor
if [ "$1" = "0" ]; then
	%glib_compile_schemas
	%userremove xdm
	%groupremove xdm
fi

%triggerpostun -- %{name} < 2:3.2.1.1-10
if [ -f /etc/X11/gdm/gdm.conf-custom.rpmsave ]; then
	mv /etc/X11/gdm/gdm.conf-custom.rpmsave /etc/gdm/custom.conf
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

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/gdm
%attr(755,root,root) %{_bindir}/gdm-screenshot
%attr(755,root,root) %{_bindir}/gdmflexiserver
%dir %{_libdir}/gdm
%dir %{_libdir}/gdm/simple-greeter
%dir %{_libdir}/gdm/simple-greeter/extensions
%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libfingerprint.so
%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libpassword.so
%attr(755,root,root) %{_libdir}/gdm/simple-greeter/extensions/libsmartcard.so
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-simple-greeter
%attr(755,root,root) %{_libexecdir}/gdm-simple-slave
%attr(755,root,root) %{_libexecdir}/gdm-xdmcp-chooser-slave
%attr(755,root,root) %{_libexecdir}/gdm-smartcard-worker
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%dir %{_sysconfdir}/gdm/PostLogin
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%{_sysconfdir}/dconf/db/gdm.d
%{_sysconfdir}/dconf/profile/gdm
%attr(1755,root,xdm) %dir /var/cache/gdm
%attr(1770,root,xdm) %dir /var/gdm
%attr(1770,root,xdm) %dir /var/lib/gdm
%dir /var/lib/gdm/.config
%attr(755,xdm,xdm) %dir /var/lib/gdm/.config/dconf
%attr(755,xdm,xdm) /var/lib/gdm/.local
%attr(750,xdm,xdm) %dir /var/log/gdm
%attr(711,root,xdm) %dir /var/run/gdm
%attr(755,xdm,xdm) %dir /var/run/gdm/greeter
%attr(750,xdm,xdm) /home/services/xdm
%{systemdtmpfilesdir}/%{name}.conf
%{_pixmapsdir}/*
%{_datadir}/gdm
%{_datadir}/gnome-session/sessions/gdm-fallback.session
%{_datadir}/gnome-session/sessions/gdm-shell.session
%{_datadir}/xsessions/custom.desktop
%{_datadir}/xsessions/default.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/glib-2.0/schemas/org.gnome.login-screen.gschema.xml

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgdm.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libgdm.so.1
%attr(755,root,root) %{_libdir}/libgdmsimplegreeter.so.1.0.0
%attr(755,root,root) %ghost %{_libdir}/libgdmsimplegreeter.so.1
%{_libdir}/girepository-1.0/Gdm-1.0.typelib

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/gdm
%{_includedir}/gdm/gdm-client-glue.h
%{_includedir}/gdm/gdm-client.h
%{_includedir}/gdm/gdm-sessions.h
%{_includedir}/gdm/gdm-user-switching.h
%dir %{_includedir}/gdm/simple-greeter
%{_includedir}/gdm/simple-greeter/gdm-login-extension.h
%{_pkgconfigdir}/gdm.pc
%{_pkgconfigdir}/gdmsimplegreeter.pc
%{_libdir}/libgdm.so
%{_libdir}/libgdmsimplegreeter.so
%{_datadir}/gir-1.0/Gdm-1.0.gir

%files static
%defattr(644,root,root,755)
%{_libdir}/libgdm.a
%{_libdir}/libgdmsimplegreeter.a

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
%{systemdunitdir}/gdm.service

%files upstart
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) /etc/init/%{name}.conf
