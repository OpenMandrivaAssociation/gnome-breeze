Summary:    The Breeze theme for GTK+ windows
Name:       gnome-breeze
Version:    0.0.1.git651e8f5
Release:    1
License:    LGPLv2.1
Group:      Graphical desktop/GNOME
URL:        https://github.com/dirruk1/gnome-breeze
Source0:    %{name}-%{version}.tar.xz

BuildArch:  noarch

%description
This package contains a version of the KDE Breeze theme for GTK applications
and environments, such as GNOME.

%prep
%setup -qn %{name}

%install
find Breeze* -type f -exec install -Dm644 '{}' "%{buildroot}%{_datadir}/themes/{}" \;

%files
%doc README.md LICENSE
%{_datadir}/themes/Breeze-gtk
%{_datadir}/themes/Breeze-dark-gtk
