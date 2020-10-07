#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libmodulemd
Version  : 2.9.4
Release  : 23
URL      : https://github.com/fedora-modularity/libmodulemd/archive/libmodulemd-2.9.4.tar.gz
Source0  : https://github.com/fedora-modularity/libmodulemd/archive/libmodulemd-2.9.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: libmodulemd-bin = %{version}-%{release}
Requires: libmodulemd-data = %{version}-%{release}
Requires: libmodulemd-lib = %{version}-%{release}
Requires: libmodulemd-man = %{version}-%{release}
Requires: libmodulemd-python = %{version}-%{release}
Requires: libmodulemd-python3 = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : file-dev
BuildRequires : glib-dev
BuildRequires : glib-staticdev
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : help2man
BuildRequires : libassuan-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt
BuildRequires : libxslt-dev
BuildRequires : libxslt-staticdev
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(rpm)
BuildRequires : pkgconfig(yaml-0.1)
BuildRequires : pygobject
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : rpm-dev
BuildRequires : rpm-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev

%description
[![Travis](https://img.shields.io/travis/fedora-modularity/libmodulemd.svg?style=plastic)](https://travis-ci.org/fedora-modularity/libmodulemd)
[![Travis](https://img.shields.io/coverity/scan/13739.svg?style=plastic)](https://scan.coverity.com/projects/sgallagher-libmodulemd)

%package bin
Summary: bin components for the libmodulemd package.
Group: Binaries
Requires: libmodulemd-data = %{version}-%{release}

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
Requires: libmodulemd-lib = %{version}-%{release}
Requires: libmodulemd-bin = %{version}-%{release}
Requires: libmodulemd-data = %{version}-%{release}
Provides: libmodulemd-devel = %{version}-%{release}
Requires: libmodulemd = %{version}-%{release}

%description dev
dev components for the libmodulemd package.


%package lib
Summary: lib components for the libmodulemd package.
Group: Libraries
Requires: libmodulemd-data = %{version}-%{release}

%description lib
lib components for the libmodulemd package.


%package man
Summary: man components for the libmodulemd package.
Group: Default

%description man
man components for the libmodulemd package.


%package python
Summary: python components for the libmodulemd package.
Group: Default
Requires: libmodulemd-python3 = %{version}-%{release}

%description python
python components for the libmodulemd package.


%package python3
Summary: python3 components for the libmodulemd package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libmodulemd package.


%prep
%setup -q -n libmodulemd-libmodulemd-2.9.4
cd %{_builddir}/libmodulemd-libmodulemd-2.9.4

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602108301
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC"
#
export FCFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export FFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
export CFFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export LDFLAGS="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC"
#
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags1 end
##
%define _lto_cflags 1
##
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Ddeveloper_build=false \
-Dskip_formatters=true \
-Dwith_docs=false \
-Dwith_manpages=enabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
meson test -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/modulemd-validator

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Modulemd-2.0.typelib
/usr/share/gir-1.0/*.gir

%files dev
%defattr(-,root,root,-)
/usr/include/modulemd-2.0/modulemd-buildopts.h
/usr/include/modulemd-2.0/modulemd-component-module.h
/usr/include/modulemd-2.0/modulemd-component-rpm.h
/usr/include/modulemd-2.0/modulemd-component.h
/usr/include/modulemd-2.0/modulemd-compression.h
/usr/include/modulemd-2.0/modulemd-defaults-v1.h
/usr/include/modulemd-2.0/modulemd-defaults.h
/usr/include/modulemd-2.0/modulemd-dependencies.h
/usr/include/modulemd-2.0/modulemd-deprecated.h
/usr/include/modulemd-2.0/modulemd-errors.h
/usr/include/modulemd-2.0/modulemd-module-index-merger.h
/usr/include/modulemd-2.0/modulemd-module-index.h
/usr/include/modulemd-2.0/modulemd-module-stream-v1.h
/usr/include/modulemd-2.0/modulemd-module-stream-v2.h
/usr/include/modulemd-2.0/modulemd-module-stream.h
/usr/include/modulemd-2.0/modulemd-module.h
/usr/include/modulemd-2.0/modulemd-profile.h
/usr/include/modulemd-2.0/modulemd-rpm-map-entry.h
/usr/include/modulemd-2.0/modulemd-service-level.h
/usr/include/modulemd-2.0/modulemd-subdocument-info.h
/usr/include/modulemd-2.0/modulemd-translation-entry.h
/usr/include/modulemd-2.0/modulemd-translation.h
/usr/include/modulemd-2.0/modulemd.h
/usr/lib64/libmodulemd.so
/usr/lib64/pkgconfig/modulemd-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmodulemd.so.2
/usr/lib64/libmodulemd.so.2.9.4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/modulemd-validator.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
