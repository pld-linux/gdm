# TODO:
# s=/dev/null=/home/services/xdm= in %%trigger for gracefull upgrade from xdm/kdm/gdm 2.2
# check /etc/pam.d/gdm-autologin
#

Summary:	GNOME Display Manager
Summary(es):	Administrador de Entrada del GNOME
Summary(ja):	GNOME ディスプレイマネージャ
Summary(pl):	gdm
Summary(pt_BR):	Gerenciador de Entrada do GNOME
Summary(ru):	簓嗤姪蔑拱 妖療綴賭 GNOME
Summary(uk):	簓嗤姪蔑品 妖療綴賭 GNOME
Name:		gdm
Version:	2.4.0.11
Release:	3
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/2.0.1/sources/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-conf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	intltool >= 0.22
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.0.3
BuildRequires:	libgnome-devel >= 2.0.3
BuildRequires:	libgnomeui-devel >= 2.0.4
BuildRequires:	librsvg-devel >= 2.0.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	pam-devel
BuildRequires:	perl-modules
BuildRequires:	scrollkeeper >= 0.3.11
Requires:	which
Requires:	/usr/X11R6/bin/sessreg
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,postun):scrollkeeper
Requires(post,preun):/sbin/chkconfig
Conflicts:	gdkxft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xdm kdm wdm

%define		_prefix		/usr/X11R6
%define		_bindir		%{_prefix}/bin
%define		_datadir	%{_prefix}/share
%define		_sbindir	%{_prefix}/sbin
%define		_mandir		%{_prefix}/man
%define		_localstatedir	/var/lib
%define		_sysconfdir	/etc/X11

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es
Administrador de Entrada del GNOME.

%description -l ja
Gdm (the GNOME Display Manager) は、高度に設定可能な xdm X Display
Manager の再実装版です。 Gdm を使うと、 X Window System
が動いているあなたの
システムにいろいろなセッションを選択してログインすることができます。

このバージョンの Gdm では、各種言語や、XIM を選択することも可能です。

%description -l pl
Gdm jest wysokokonfigurowaln� reimplementacj� xdma. Gdm pozwala
logowa� si� do systemu z poziomu X11 i wspiera jednoczesn� prac� kilku
r鷽nych Xsesji na lokalnej maszynie.

%description -l pt_BR
Gerenciador de Entrada do GNOME.

%description -l ru
GDM (GNOME Display Manager) - 榑� 凖浜侈斗杜堊檀� xdm (X Display
Manager). GDM 佻旌鰐囘� 彖� 徃歪不� � 喇嘖斗�, 料 墨塹厦� 攸侖歸力 X
Window � 佻陳賭嵒彖都 卅堆壞 療嗚鰐慱蛭 卅變挌 X 單僧嗜� 歪力徠斗杜力.

%description -l uk
GDM (GNOME Display Manager) - 壇 凖ν侈斗杜堊脱� xdm (X Display
Manager). GDM 掴旌鰐僂 彖� 徃歪不� � 喇嘖斗�, 料 冕κ 攸侖歸力 X
Window 堊 丶辻夘葉� 厦堆壞 胞蒙墨� 勁變蛭 X 單僧哘� 歪力涸嗄�.

%package Xnest
Summary:	Xnest (ie embedded X) server for GDM
Summary(pl):	Serwer Xnest dla GDM
Group:		X11/Applications
Requires:	%{name} = %{version}
Requires:	XFree86-Xnest

%description Xnest
This package add support for Xnest server in gdm.

%description Xnest -l pl
Ten pakiet dodaje do gdm wsparcie dla Xnest.

%package init
Summary:	Init script for GDM
Summary(pl):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires:	%{name} = %{version}

%description init
Init script for GDM.

%description init -l pl
Skrypt init dla GDM-a.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-xinerama=yes \
	--with-xdmcp=yes \
	--with-pam-prefix=/etc \
	--with-tcp-wrappers=yes \
	--enable-authentication-scheme=pam \
	--disable-console-helper

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,pam.d,security} \
	$RPM_BUILD_ROOT/home/services/xdm

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PAM_PREFIX=/etc \
	Settingsdir=%{_applnkdir}/Settings/GNOME \
	Systemdir=%{_applnkdir}/System

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

mv $RPM_BUILD_ROOT%{_applnkdir}/System/gdmsetup.desktop \
	$RPM_BUILD_ROOT%{_applnkdir}/Settings/GNOME/

%find_lang %{name} --all-name --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 55 -r -f xdm

if [ -z "`id -u xdm 2>/dev/null`" ]; then
	/usr/sbin/useradd -u 55 -r -d /home/services/xdm -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%post
/usr/bin/scrollkeeper-update

%postun
if [ "$1" = "0" ]; then
	if [ -n "`id -u xdm 2>/dev/null`" ]; then
		/usr/sbin/userdel xdm
	fi
	/usr/sbin/groupdel xdm
fi
/usr/bin/scrollkeeper-update

%post init
/sbin/chkconfig --add gdm
if [ -f /var/lock/subsys/gdm ]; then
	echo "Run \"/etc/rc.d/init.d/gdm restart\" to restart gdm." >&2
else
	echo "Run \"/etc/rc.d/init.d/gdm start\" to start gdm." >&2
fi

%preun init
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/gdm ]; then
		/etc/rc.d/init.d/gdm stop >&2
	fi
	/sbin/chkconfig --del gdm
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gdm
%attr(755,root,root) %{_bindir}/gdm-binary
%attr(755,root,root) %{_bindir}/gdmchooser
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_bindir}/gdmgreeter
%attr(755,root,root) %{_bindir}/gdmlogin
%attr(755,root,root) %{_bindir}/gdmmktemp
%attr(755,root,root) %{_bindir}/gdmphotosetup
%attr(755,root,root) %{_bindir}/gdmsetup
%attr(755,root,root) %{_bindir}/gdmthemetester
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/gdm
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/Sessions
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/gnomerc
%attr(755,root,root) %config %{_sysconfdir}/gdm/XKeepsCrashing
%config %{_sysconfdir}/gdm/factory-gdm.conf
%config(noreplace)  %verify(not size mtime md5) %{_sysconfdir}/gdm/gdm.conf
%config %{_sysconfdir}/gdm/locale.alias
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.gdm
%attr(750,xdm,xdm) /var/lib/gdm
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/*
%{_applnkdir}/Settings/GNOME/*
%{_applnkdir}/System/gdmflexiserver.desktop
%{_datadir}/gdm

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdmXnestchooser
%{_applnkdir}/System/gdmflexiserver-xnest.desktop

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
