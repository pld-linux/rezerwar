Summary:	puzzle game
Summary(pl.UTF-8):	gra logiczna
Name:		rezerwar
Version:	0.3
Release:	1
License:	Distibutable
Group:		X11/Applications/Games
Source0:	http://tamentis.com/projects/rezerwar/files/%{name}-%{version}.tar.gz
# Source0-md5:	b410f43b7e3c05995efdcd51e9f24c34
Patch0:		%{name}-makefile.patch
URL:		http://tamentis.com/projects/rezerwar/
BuildRequires:	SDL_mixer-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of this game is basically to create networks of water to make
them disappear, a couple tricks and techniques will help you achieve
this goal faster.

%description -l pl.UTF-8
Celem gry jest tworzenie sieci wodenej tak, aby znikęła ona z
planszy. Kilka trików i technik umożliwi szybsze osiągnięcie celu.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@games/@@' mkfiles/config_h_unix

%build
./configure
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} `sdl-config --cflags`" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/rezerwar
%{_datadir}/rezerwar
