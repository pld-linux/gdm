#
# TODO:
# - s=/dev/null=/home/services/xdm= in %%trigger for graceful upgrade from xdm/kdm/gdm 2.2
# - check /etc/pam.d/gdm-autologin
# - upstart package
#
# Conditiional build:
%bcond_without	selinux	# without selinux

Summary:	GNOME Display Manager
Summary(es.UTF-8):	Administrador de Entrada del GNOME
Summary(ja.UTF-8):	GNOME ディスプレイマネージャ
Summary(pl.UTF-8):	gdm - zarządca ekranów GNOME
Summary(pt_BR.UTF-8):	Gerenciador de Entrada do GNOME
Summary(ru.UTF-8):	Дисплейный менеджер GNOME
Summary(uk.UTF-8):	Дисплейний менеджер GNOME
Name:		gdm
Version:	3.0.3
Release:	1
Epoch:		2
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gdm/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	50a9ed65cab062e27ac87b7870b6ad89
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
Source4:	%{name}-autologin.pamd
Source5:	%{name}-custom.desktop
Source6:	%{name}-default.desktop
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-polkit.patch
Patch2:		%{name}-xsession.patch
Patch3:		%{name}-defaults.patch
URL:		http://www.gnome.org/projects/gdm/
BuildRequires:	GConf2-devel >= 2.32.0
BuildRequires:	accountsservice-devel >= 0.6.12
BuildRequires:	attr-devel
BuildRequires:	audit-libs-devel
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.11
BuildRequires:	check >= 0.9.4
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd412-xml
BuildRequires:	fontconfig-devel >= 2.5.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-panel-devel >= 2.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	iso-codes
BuildRequires:	libcanberra-gtk3-devel >= 0.4
%{?with_selinux:BuildRequires:	libselinux-devel}
BuildRequires:	libtool
BuildRequires:	libwrap-devel
BuildRequires:	libxklavier-devel >= 4.0-2
BuildRequires:	pam-devel
BuildRequires:	pango-devel >= 1.3.0
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper >= 0.1.4
BuildRequires:	upower-devel >= 0.9.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXdmcp-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires(post,postun):	/usr/bin/scrollkeeper-update
Requires(post,postun):	gtk-update-icon-cache
Requires(post,preun):	GConf2
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	/usr/bin/X
Requires:	ConsoleKit >= 0.4.1
Requires:	accountsservice >= 0.6.12
Requires:	gnome-session >= 2.91.91.1
Requires:	gnome-settings-daemon >= 2.91.91
Requires:	hicolor-icon-theme
Requires:	pam >= 0.99.7.1
Requires:	polkit-gnome >= 0.93
Requires:	which
Requires:	xorg-app-sessreg
Requires:	xorg-app-xmodmap
Suggests:	zenity
Provides:	XDM
Provides:	group(xdm)
Provides:	user(xdm)
Obsoletes:	gdm-Xnest
Obsoletes:	gdm-user-switch-applet
Obsoletes:	gnome-applet-fast-user-switch
Conflicts:	gdkxft
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	open
Requires:	rc-scripts >= 0.4.3.0

%description init
Init script for GDM.

%description init -l pl.UTF-8
Skrypt init dla GDM-a.

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
	--disable-console-helper \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--with-console-kit \
	--enable-authentication-scheme=pam \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers=yes \
	--with%{!?with_selinux:out}-selinux \
	--with-xdmcp=yes \
	--with-xinerama=yes \
	--with-user=xdm \
	--with-group=xdm

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT{/home/services/xdm,/var/log/gdm} \
	$RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/gdm-autologin
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}
touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --with-gnome --with-omf --all-name

# allow executing ~/.Xclients and ~/.xsession
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/xsessions/custom.desktop
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/xsessions/default.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 55 -r -f xdm
%useradd -u 55 -r -d /home/services/xdm -s /bin/false -c "X Display Manager" -g xdm xdm

%post
%gconf_schema_install gdm-simple-greeter.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gdm-simple-greeter.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

if [ "$1" = "0" ]; then
	%userremove xdm
	%groupremove xdm
fi

%triggerpostun -- %{name} < 1:2.13.0.8-1
if [ -f /etc/X11/gdm/gdm.conf-custom.rpmsave ]; then
    mv /etc/X11/gdm/gdm.conf-custom.rpmsave /etc/gdm/custom.conf
fi

%post init
/sbin/chkconfig --add gdm
if [ -f /var/lock/subsys/gdm ]; then
	echo "Run \"/sbin/service gdm restart\" to restart gdm." >&2
	echo "WARNING: it will terminate all sessions opened from gdm!" >&2
else
	echo "Run \"/sbin/service gdm start\" to start gdm." >&2
fi

%preun init
if [ "$1" = "0" ]; then
	%service gdm stop
	/sbin/chkconfig --del gdm
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/gdm
%attr(755,root,root) %{_sbindir}/gdm-binary
%attr(755,root,root) %{_bindir}/gdm-screenshot
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_libexecdir}/gdm-crash-logger
%attr(755,root,root) %{_libexecdir}/gdm-factory-slave
%attr(755,root,root) %{_libexecdir}/gdm-host-chooser
%attr(755,root,root) %{_libexecdir}/gdm-product-slave
%attr(755,root,root) %{_libexecdir}/gdm-session-worker
%attr(755,root,root) %{_libexecdir}/gdm-simple-chooser
%attr(755,root,root) %{_libexecdir}/gdm-simple-greeter
%attr(755,root,root) %{_libexecdir}/gdm-simple-slave
%attr(755,root,root) %{_libexecdir}/gdm-xdmcp-chooser-slave
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init/Default
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%dir %{_sysconfdir}/gdm/PostLogin
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gdm/custom.conf
%{_sysconfdir}/gconf/schemas/gdm-simple-greeter.schemas
%config(noreplace) %verify(not md5 mtime size) /etc/dbus-1/system.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/security/blacklist.gdm
%{_sysconfdir}/dconf/db/gdm
%{_sysconfdir}/dconf/profile/gdm
%attr(1755,root,xdm) %dir /var/cache/gdm
%attr(1770,root,xdm) %dir /var/gdm
%attr(1770,root,xdm) %dir /var/lib/gdm
%dir /var/lib/gdm/.config
%attr(755,xdm,xdm) %dir /var/lib/gdm/.config/dconf
%attr(1750,root,xdm) %dir /var/lib/gdm/.gconf.mandatory
%attr(1640,root,xdm) /var/lib/gdm/.gconf.mandatory/*.xml
%attr(644,root,xdm) /var/lib/gdm/.gconf.path
%attr(755,xdm,xdm) /var/lib/gdm/.local
%attr(750,xdm,xdm) %dir /var/log/gdm
%attr(711,root,xdm) %dir /var/run/gdm
%attr(755,xdm,xdm) %dir /var/run/gdm/greeter
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/*
%{_datadir}/gdm
%{_datadir}/polkit-1/actions/gdm.policy
%{_datadir}/gnome-session/sessions/gdm.session
%{_datadir}/xsessions/custom.desktop
%{_datadir}/xsessions/default.desktop
%{_iconsdir}/hicolor/*/apps/*.png

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
