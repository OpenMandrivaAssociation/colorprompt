%define		profilefile 92user-color.sh
%define		profilefile2 92user-color-clock.sh

Summary:	Make the user prompt in bash different colors depending on your user
Name:		colorprompt
Version:	1.0
Release:	2
Source0:	https://github.com/solbu/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License:	GPLv3+
Group:		Shells
Url:		https://github.com/solbu/colorprompt
BuildArch:	noarch

%description
A little bash profile extension to color your user prompt appropriately.
It will make regular logins green and root logins red.

%package	clock
Summary:	Make the user prompt in bash different colors depending on your user
Group:		Shells

%description	clock
A little bash profile extension to color your user prompt appropriately.
It will make regular logins green and root logins red.
This version also add a timestamp at the front of the prompt,
showing a timestamp of when the previous command completed.

%prep
%setup -q

%build

%install
install -D -m 0644 %{profilefile} %{buildroot}%{_sysconfdir}/profile.d/%{profilefile}
install -D -m 0644 %{profilefile2} %{buildroot}%{_sysconfdir}/profile.d/%{profilefile2}

%files
%doc AUTHORS README
%{_sysconfdir}/profile.d/%{profilefile}
%license COPYING

%files clock
%doc AUTHORS README
%{_sysconfdir}/profile.d/%{profilefile2}
%license COPYING
