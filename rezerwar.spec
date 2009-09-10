Summary:	puzzle game
Summary(pl.UTF-8):	gra logiczna
Name:		rezerwar
Version:	0.4
Release:	1
License:	Distibutable
Group:		X11/Applications/Games
Source0:	http://tamentis.com/projects/rezerwar/files/%{name}-%{version}.tar.gz
# Source0-md5:	1acb71401b7499c2eaa8d0b10acc04f3
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-configure.patch
URL:		http://tamentis.com/projects/rezerwar/
BuildRequires:	SDL_mixer-devel
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
%patch1 -p1

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
