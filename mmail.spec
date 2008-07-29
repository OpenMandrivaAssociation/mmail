%define name mmail
%define version 0.47
%define release %mkrel 3


Name:		%{name}
Summary:	MultiMail Offline Mailer Reader
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Mail
URL:		http://multimail.sourceforge.net/
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-0.47.patch
BuildRequires:  ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

Conflicts:       mirror

%description
MultiMail is an offline mail packet reader for Unix and other systems.
(This version also compiles under MSDOS, with DJGPP; OS/2, with EMX; and
Win32, with RSX/NT.) It currently supports the Blue Wave and QWK formats.
It has a full screen, color user interface, built with the curses library.


%prep
%setup -q
%patch -p1


%build
PREFIX=%{buildroot}%{_prefix}
export PREFIX
export RPM_OPT_FLAGS

make


%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1

PREFIX=%{buildroot}%{_prefix}
export PREFIX
HELPDIR=%{buildroot}%{_mandir}/man1
export HELPDIR

make install

# fix attributes of docs
chmod -R a+rX $RPM_BUILD_DIR/%{name}-%{version}/{COPYING,HISTORY,INSTALL,README,TODO,FAQ,colors}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
rm -rf $RPM_BUILD_DIR/%{name}-%{version}


%files
%defattr(-,root,root,0755)
%doc COPYING HISTORY INSTALL README TODO FAQ colors
%{_bindir}/mm
%{_mandir}/man1/mm.1*
%{_mandir}/man1/mmail.1*


