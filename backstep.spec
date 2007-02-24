Summary:	Program that draws icons for minimized windows on desktop
Summary(pl.UTF-8):	Program który rysuje ikony zminimalizowanych aplikacji na pulpicie
Name:		backstep
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/backstep/%{name}-%{version}.tar.bz2
# Source0-md5:	fb8980b7f59b66f87b0bfdb32c3a9032
Patch0:		%{name}-xcomposite.patch
URL:		http://backstep.sourceforge.net/
BuildRequires:	gtk+2-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Backstep is a program that draws icons for minimized windows on your
desktop. It doesn't depend on the window manager or on a
desktop-drawing program (for example, I use it with Nautilus). It is
meant to work with window managers that are EWHM compliant. However, I
only know for sure that it works with Metacity and Xfwm4. And I know
that it doesn't work with Fluxbox and that it only partially works
with Kwin (hopefully this will be corrected soon). I haven't yet
tested it with other window managers.

%description -l pl.UTF-8
Backstep to program, który rysuje ikony zminimalizowanych okienek na
twoim pulpicie. Nie zależy od zarządcy pulpitu czy od programu
rysującego na pulpicie (dla przykładu, autor korzysta z Nautilusa).
Jego celem jest działanie z zarządcami okien zgodnymi z EWHM. Jednakże
autor wie na pewno, że jego program działa z Metacity i Xfwm4. Wie
również, że nie działa z Fluxboxem i tylko częściowo z Kwin (i ma
nadzieję, że zostanie to poprawione wkrótce). Backstep nie był
przetestowany jeszcze dla innych zarządcy okien.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-x

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
