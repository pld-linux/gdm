# TODO:
# /etc/X11/dm dir should belong to XFree? I is common for KDE and GNOME
# s=/dev/null=/home/services/xdm= in %%trigger for gracefull upgrade from xdm/kdm/gdm 2.2
# check /etc/pam.d/gdm-autologin
#

Summary:	GNOME Display Manager
Summary(es):	Administrador de Entrada del GNOME
Summary(ja):	GNOME �ǥ����ץ쥤�ޥ͡�����
Summary(pl):	gdm - zarz�dca ekran�w GNOME
Summary(pt_BR):	Gerenciador de Entrada do GNOME
Summary(ru):	���������� �������� GNOME
Summary(uk):	���������� �������� GNOME
Name:		gdm
Version:	2.4.2.97
Release:	0.9
Epoch:		1
License:	GPL/LGPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	300033d842870987ed8509b5bc13a722
Source1:	%{name}.pamd
Source2:	%{name}.init
Source3:	%{name}-pld-logo.png
Patch0:		%{name}-xdmcp.patch
Patch1:		%{name}-conf.patch
URL:		http://www.jirka.org/gdm.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	intltool >= 0.22
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomecanvas-devel >= 2.0.3
BuildRequires:	libgnome-devel >= 2.0.6
BuildRequires:	libgnomeui-devel >= 2.0.4
BuildRequires:	librsvg-devel >= 2.0.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	pam-devel
BuildRequires:	perl-modules
Requires:	libgnome >= 2.1.0-3
Requires:	which
Requires:	sessreg
Requires(pre):	/bin/id
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(postun):	/usr/sbin/groupdel
Requires(post,preun):	/sbin/chkconfig
Obsoletes:	xdm kdm wdm
Conflicts:	gdkxft
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11
%define		_localstatedir	/var/lib

%description
Gdm (the GNOME Display Manager) is a highly configurable
reimplementation of xdm, the X Display Manager. Gdm allows you to log
into your system with the X Window System running and supports running
several different X sessions on your local machine at the same time.

%description -l es
Administrador de Entrada del GNOME.

%description -l ja
Gdm (the GNOME Display Manager) �ϡ����٤������ǽ�� xdm X Display
Manager �κƼ����ǤǤ��� Gdm ��Ȥ��ȡ� X Window System
��ư���Ƥ��뤢�ʤ���
�����ƥ�ˤ�����ʥ��å��������򤷤ƥ����󤹤뤳�Ȥ��Ǥ��ޤ���

���ΥС������� Gdm �Ǥϡ��Ƽ����䡢XIM �����򤹤뤳�Ȥ��ǽ�Ǥ���

%description -l pl
Gdm jest wysokokonfigurowaln� reimplementacj� xdma. Gdm pozwala
logowa� si� do systemu z poziomu X11 i wspiera jednoczesn� prac� kilku
r�nych sesji X na lokalnej maszynie.

%description -l pt_BR
Gerenciador de Entrada do GNOME.

%description -l ru
GDM (GNOME Display Manager) - ��� ��������������� xdm (X Display
Manager). GDM ��������� ��� ������� � �������, �� ������� �������� X
Window � ������������ ������ ���������� ������ X ������� ������������.

%description -l uk
GDM (GNOME Display Manager) - �� �Ŧ���������æ� xdm (X Display
Manager). GDM ������Ѥ ��� ������� � �������, �� �˦� �������� X
Window �� Ц�����դ ������ ˦����� Ҧ���� X ����Ӧ� ���������.

%package Xnest
Summary:	Xnest (ie embedded X) server for GDM
Summary(pl):	Serwer Xnest dla GDM
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	XFree86-Xnest

%description Xnest
This package add support for Xnest server in gdm.

%description Xnest -l pl
Ten pakiet dodaje do gdm wsparcie dla Xnest.

%package init
Summary:	Init script for GDM
Summary(pl):	Skrypt init dla GDM-a
Group:		X11/Applications
Requires:	%{name} = %{epoch}:%{version}
Requires:	open

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
	PAM_PREFIX=/etc

install %{SOURCE1} $RPM_BUILD_ROOT/etc/pam.d/gdm
install %{SOURCE2} $RPM_BUILD_ROOT/etc/rc.d/init.d/gdm

install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

touch $RPM_BUILD_ROOT/etc/security/blacklist.gdm

%find_lang %{name} --all-name --with-gnome

# Remove useless files
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/modules/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -g 55 -r -f xdm

if [ -z "`id -u xdm 2>/dev/null`" ]; then
       /usr/sbin/useradd -u 55 -r -d /home/services/xdm -s /bin/false -c 'X Display Manager' -g xdm xdm 1>&2
fi

%postun
if [ "$1" = "0" ]; then
       if [ -n "`id -u xdm 2>/dev/null`" ]; then
               /usr/sbin/userdel xdm
       fi
       /usr/sbin/groupdel xdm
fi

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
%doc AUTHORS ChangeLog NEWS README TODO docs/GdmGreeterThemeManual.txt
%attr(755,root,root) %{_bindir}/gdm
%attr(755,root,root) %{_bindir}/gdm-binary
%attr(755,root,root) %{_bindir}/gdmchooser
%attr(755,root,root) %{_bindir}/gdmflexiserver
%attr(755,root,root) %{_bindir}/gdmgreeter
%attr(755,root,root) %{_bindir}/gdmlogin
%attr(755,root,root) %{_bindir}/gdmphotosetup
%attr(755,root,root) %{_bindir}/gdmsetup
%attr(755,root,root) %{_bindir}/gdmthemetester
%attr(755,root,root) %{_libdir}/gdmaskpass
%attr(755,root,root) %{_libdir}/gdmopen
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/gdm
%dir %{_sysconfdir}/gdm/modules
%attr(755,root,root) %config %{_sysconfdir}/gdm/Init
%attr(755,root,root) %config %{_sysconfdir}/gdm/PreSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/PostSession
%attr(755,root,root) %config %{_sysconfdir}/gdm/XKeepsCrashing
%attr(755,root,root) %config %{_sysconfdir}/gdm/Xsession
%config %{_sysconfdir}/gdm/factory-gdm.conf
%config %{_sysconfdir}/gdm/PostLogin/Default.sample
%config %{_sysconfdir}/gdm/modules/*
%{_sysconfdir}/dm/Sessions/*.desktop

%config(noreplace)  %verify(not size mtime md5) %{_sysconfdir}/gdm/gdm.conf
%config %{_sysconfdir}/gdm/locale.alias
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/gdm*
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/security/blacklist.gdm
%attr(750,xdm,xdm) /var/lib/gdm
%attr(750,xdm,xdm) /home/services/xdm
%{_pixmapsdir}/*
%{_desktopdir}/gdmsetup.desktop
%{_desktopdir}/gdmflexiserver.desktop
%{_datadir}/gnome/capplets/*
%{_datadir}/gdm
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/lib*.so

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gdmXnestchooser
%{_desktopdir}/gdmflexiserver-xnest.desktop

%files init
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/gdm
