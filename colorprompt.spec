%define profilefile 92user-color.sh

Summary:	Make the user prompt in bash different colors depending on your user
Name:		colorprompt
Version:	0.1
Release:	8
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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2011.0
+ Revision: 617407
- the mass rebuild of 2010.0 packages

* Mon Jun 01 2009 Gustavo De Nardin <gustavodn@mandriva.com> 0.1-2mdv2010.0
+ Revision: 381775
- don't spawn a subshell for the test
- quote $colorregex, so it is not subject to be expanded to nothing by bash,
  when shopt nullglob is on
- make grep quiet and redirect stderr to null

* Wed May 27 2009 Colin Guthrie <cguthrie@mandriva.org> 0.1-1mdv2010.0
+ Revision: 380164
- import colorprompt


