%define name colorprompt
%define version 0.1
%define release %mkrel 1
%define profilefile 92user-color.sh

Summary: Make the user prompt in bash different colors depending on your user
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{profilefile}
License: BSD
Group: Shells
Url: http://colin.guthr.ie/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch

%description
A little bash profile extension to color your user prompt appropriately.
It will make regular logins green and root logins red.

%prep

%build

%install
rm -rf %{buildroot}
install -D -m 0644 %SOURCE0 %{buildroot}%{_sysconfdir}/profile.d/%{profilefile}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_sysconfdir}/profile.d/%{profilefile}
