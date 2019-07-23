%define profilefile 92user-color.sh

Summary:	Make the user prompt in bash different colors depending on your user
Name:		colorprompt
Version:	1.0
Release:	1
Source0:	%{profilefile}
License:	BSD
Group:		Shells
Url:		http://colin.guthr.ie/
BuildArch:	noarch

%description
A little bash profile extension to color your user prompt appropriately.
It will make regular logins green and root logins red.

%prep

%build

%install
install -D -m 0644 %SOURCE0 %{buildroot}%{_sysconfdir}/profile.d/%{profilefile}

%files
%{_sysconfdir}/profile.d/%{profilefile}
