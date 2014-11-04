%define _topdir /home/jonathan/rpmbuild
%define lilyrelease 2.4
%define lilybuild 2014110400
%define _sourcedir      %{_topdir}/SOURCES
%define _tmppath        /var/tmp
%define _rpmfilename  lily-%{lilyrelease}-%{lilybuild}.x86_64.rpm
%define __os_install_post    \
    /usr/lib/rpm/redhat/brp-compress \
    %{!?__debug_package:/usr/lib/rpm/redhat/brp-strip %{__strip}} \
    /usr/lib/rpm/redhat/brp-strip-static-archive %{__strip} \
    /usr/lib/rpm/redhat/brp-strip-comment-note %{__strip} %{__objdump} \
%{nil}
%define __jar_repack %{nil}
Summary: ThoughtWave Lily %{lilyrelease} Distribution
Vendor: ThoughtWave
Name: lily
Version: %{lilyrelease} 
Release: %{lilybuild}
Group: ThoughtWave/lily
AutoReqProv: no
Packager: Jonathan Kalbfeld <jonathan.kalbfeld@thoughtwave.com>
Provides: thoughtwave(lily) = %{lilyrelease}
License: Unknown
BuildArch: x86_64
BuildRoot: %{_topdir}/BUILD

%description
Vendor: ThoughtWave Technologies LLC

%install
install -d $RPM_BUILD_ROOT/
cd $RPM_BUILD_ROOT/
mkdir -p opt
mkdir -p etc/rc.d/init.d
mkdir -p etc/sysconfig
cp %{_sourcedir}/lily etc/rc.d/init.d
cd opt
curl http://lilyproject.org/release/%{lilyrelease}/lily-%{lilyrelease}.tar.gz | tar -zxpf -

%files
/opt
/etc

%post
touch /etc/sysconfig/lily
chkconfig --add lily
chkconfig lily on
echo "Starting lily"
service lily start
