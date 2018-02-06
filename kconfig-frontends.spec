#
# spec file for package kconfig-frontends
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kconfig-frontends
%define lname	libkconfig-parser
Version:        4.11.0.1
Release:        1
Summary:        The kconfig build config option selector, its frontends and tools
License:        GPL-2.0
Group:          Development/Tools/Building
Url:            http://ymorin.is-a-geek.org/projects/kconfig-frontends

#Hg-Clone:	http://ymorin.is-a-geek.org/hg/kconfig-frontends
Source:         http://ymorin.is-a-geek.org/download/kconfig-frontends/%name-%version.tar.xz
Patch0:         gperf-3.1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  qt5-devel

%description
Kconfig is the configuration language used by the Linux kernel. This
package is a copy of the frontends and the parser found in the Linux
kernel source tree, adapted to being built outside of the kernel build
infrastructure.

%package -n %lname
Summary:        The kconfig description language parser
Group:          System/Libraries

%description -n %lname
Kconfig is the configuration language used by the Linux kernel. This
library provides a copy of the parser found therein, with minor
changes to adapt them to be built and used outside of the kernel
build infrastructure.

%package devel
Summary:        Development files for the kconfig language parser
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
Kconfig is the configuration language used by the Linux kernel. This
library provides a copy of the parser found therein, with minor
changes to adapt them to be built and used outside of the kernel
build infrastructure.

This subpackage contains libraries and header files for developing
applications that want to make use of libkconfig-parser.

%package curses
Summary:        Curses frontends for kconfig, a build config option selector
Group:          Development/Tools/Building

%description curses
A curses frontend for selecting options for a Kconfig-style configuration.

%package gtk
Summary:        GTK frontends for kconfig, a build config option selector
Group:          Development/Tools/Building

%description gtk
A GTK frontend for selecting options for a Kconfig-style configuration.

%package qt
Summary:        Qt frontends for kconfig, a build config option selector
Group:          Development/Tools/Building

%description qt
A Qt frontend for selecting options for a Kconfig-style configuration.

%prep
%setup -q
%patch0 -p1

%build
%configure
make %{?_smp_mflags} V=1

%install
b="%buildroot"
%make_install docdir="%_docdir/%name"
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_docdir/%name"
cp -a COPYING "$b/%_docdir/%name/"

%check
make check

%files
%defattr(-,root,root)
%_bindir/kconfig
%_bindir/kconfig-conf
%_bindir/kconfig-diff
%_bindir/kconfig-gettext
%_bindir/kconfig-merge
%_bindir/kconfig-tweak
%dir %_docdir/%name
%_docdir/%name/COPYING
%_docdir/%name/kconfig.txt
%_docdir/%name/kconfig-language.txt

%files -n %lname
%defattr(-,root,root)
%_libdir/libkconfig-parser-*.so

%files devel
%defattr(-,root,root)
%_includedir/kconfig
%_libdir/libkconfig-parser.so
%_libdir/pkgconfig/kconfig-parser.pc

%files curses
%_bindir/kconfig-mconf
%_bindir/kconfig-nconf

%files gtk
%defattr(-,root,root)
%_bindir/kconfig-gconf
%dir %_datadir/%name
%_datadir/%name/gconf.glade

%files qt
%defattr(-,root,root)
%_bindir/kconfig-qconf

%changelog
* Tue Feb  6 2018 mironov.ivan@gmail.com
- Update to new upstream release 4.11.0.1
- Modify original SPEC from SUSE to work on Fedora.
* Fri Apr  3 2015 jengelh@inai.de
- Update to new upstream release 3.12.0.0
  * Synchronize codebase with Linux 3.12
* Wed Aug  7 2013 jengelh@inai.de
- Update to new upstream release 3.10.0.0
  * Synchronize codebase with Linux 3.10
* Tue Feb 19 2013 jengelh@inai.de
- Initial package (version 3.8.0.0) for build.opensuse.org
