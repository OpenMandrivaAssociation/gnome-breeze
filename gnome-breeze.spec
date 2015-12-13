%define date 20151214

Summary:	The Breeze theme for GTK+ windows
Name:		gnome-breeze
Version:	0.0.1
Release:	2.%{date}.1
License:	LGPLv2.1
Group:		Graphical desktop/GNOME
URL:		https://github.com/dirruk1/gnome-breeze
# rm -rf gnome-breeze && git clone https://github.com/dirruk1/gnome-breeze.git && cd gnome-breeze/
# git archive --prefix=gnome-breeze-$(date +%Y%m%d)/ --format=tar HEAD | xz > ../gnome-breeze-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{date}.tar.xz
BuildArch:	noarch
Obsoletes:	gnome-breeze0.0.1.git651e8f5-1

%description
This package contains a version of the KDE Breeze theme for GTK applications
and environments, such as GNOME.

%prep
%setup -qn %{name}-%{date}

%install
find Breeze* -type f -exec install -Dm644 '{}' "%{buildroot}%{_datadir}/themes/{}" \;

%files
%doc README.md LICENSE
%{_datadir}/themes/Breeze-gtk
%{_datadir}/themes/Breeze-dark-gtk
