#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libmodulemd
Version  : 1.5.2
Release  : 3
URL      : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-1.5.2/modulemd-1.5.2.tar.xz
Source0  : https://github.com/fedora-modularity/libmodulemd/releases/download/libmodulemd-1.5.2/modulemd-1.5.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libmodulemd-bin
Requires: libmodulemd-data
Requires: libmodulemd-lib
Requires: libmodulemd-license
BuildRequires : docbook-xml
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : libxslt
BuildRequires : meson
BuildRequires : ninja
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk-doc)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : python3
BuildRequires : valgrind

%description
[![Travis](https://img.shields.io/travis/fedora-modularity/libmodulemd.svg?style=plastic)](https://travis-ci.org/fedora-modularity/libmodulemd)
[![Travis](https://img.shields.io/coverity/scan/13739.svg?style=plastic)](https://scan.coverity.com/projects/sgallagher-libmodulemd)

%package bin
Summary: bin components for the libmodulemd package.
Group: Binaries
Requires: libmodulemd-data
Requires: libmodulemd-license

%description bin
bin components for the libmodulemd package.


%package data
Summary: data components for the libmodulemd package.
Group: Data

%description data
data components for the libmodulemd package.


%package dev
Summary: dev components for the libmodulemd package.
Group: Development
Requires: libmodulemd-lib
Requires: libmodulemd-bin
Requires: libmodulemd-data
Provides: libmodulemd-devel

%description dev
dev components for the libmodulemd package.


%package doc
Summary: doc components for the libmodulemd package.
Group: Documentation

%description doc
doc components for the libmodulemd package.


%package lib
Summary: lib components for the libmodulemd package.
Group: Libraries
Requires: libmodulemd-data
Requires: libmodulemd-license

%description lib
lib components for the libmodulemd package.


%package license
Summary: license components for the libmodulemd package.
Group: Default

%description license
license components for the libmodulemd package.


%prep
%setup -q -n modulemd-1.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531430044
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Ddeveloper_build=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/libmodulemd
cp COPYING %{buildroot}/usr/share/doc/libmodulemd/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulemd-validator

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Modulemd-1.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/modulemd/modulemd-buildopts.h
/usr/include/modulemd/modulemd-component-module.h
/usr/include/modulemd/modulemd-component-rpm.h
/usr/include/modulemd/modulemd-component.h
/usr/include/modulemd/modulemd-defaults.h
/usr/include/modulemd/modulemd-dependencies.h
/usr/include/modulemd/modulemd-intent.h
/usr/include/modulemd/modulemd-module.h
/usr/include/modulemd/modulemd-prioritizer.h
/usr/include/modulemd/modulemd-profile.h
/usr/include/modulemd/modulemd-servicelevel.h
/usr/include/modulemd/modulemd-simpleset.h
/usr/include/modulemd/modulemd-subdocument.h
/usr/include/modulemd/modulemd.h
/usr/lib64/libmodulemd.so
/usr/lib64/pkgconfig/modulemd.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/modulemd/home.png
/usr/share/gtk-doc/html/modulemd/index.html
/usr/share/gtk-doc/html/modulemd/left-insensitive.png
/usr/share/gtk-doc/html/modulemd/left.png
/usr/share/gtk-doc/html/modulemd/modulemd-ModulemdComponent.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-component-module.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-component-rpm.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-defaults.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-dependencies.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-module.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-prioritizer.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-profile.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-servicelevel.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-simpleset.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd-subdocument.html
/usr/share/gtk-doc/html/modulemd/modulemd-modulemd.html
/usr/share/gtk-doc/html/modulemd/modulemd.devhelp2
/usr/share/gtk-doc/html/modulemd/modulemd.html
/usr/share/gtk-doc/html/modulemd/right-insensitive.png
/usr/share/gtk-doc/html/modulemd/right.png
/usr/share/gtk-doc/html/modulemd/style.css
/usr/share/gtk-doc/html/modulemd/up-insensitive.png
/usr/share/gtk-doc/html/modulemd/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmodulemd.so.1
/usr/lib64/libmodulemd.so.1.5.2

%files license
%defattr(-,root,root,-)
/usr/share/doc/libmodulemd/COPYING
