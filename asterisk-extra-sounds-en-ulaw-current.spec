# $Id: freepbx-src.spec,v 1.2 2013/05/22 02:40:06 unnilennium Exp $
# Authority: vip-ire
# Name: Daniel Berteaud

%define version 20150623
%define release 1
%define name asterisk-extra-sounds-en-ulaw-current


Summary:        asterisk-extra-sounds-en-ulaw-current
Name:           %{name}
Version:        %{version}
Release:        %{release}%{?dist}
License:        GPL
Group:          System/Servers
Requires:       asterisk
Source0:	asterisk-extra-sounds-en-ulaw-current-%{version}.tar.gz

BuildRoot:      /var/tmp/%{name}-%{version}-%{release}-buildroot
URL:            http://downloads.asterisk.org/pub/telephony/sounds/asterisk-extra-sounds-en-ulaw-current.tar.gz

BuildArch:	noarch

BuildRequires:	e-smith-devtools

AutoReqProv:    no

%description
Get the additional sound files

%changelog
* Sun Jun 23 2015 stephane de Labrusse <stephdl@de-labrusse.fr> 2150623-1
- Initial release to sme9

%prep

%setup

%build
# Extract freePBX archive
%{__mkdir_p} root/usr/share/asterisk/sounds
tar xzf %{SOURCE0} -C root/usr/share/asterisk/sounds
ln -sfn /var/lib/asterisk/sounds/en root/usr/share/asterisk/sounds/

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
	> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)


