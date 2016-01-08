#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsamplerate
Version  : 0.1.8
Release  : 1
URL      : http://www.mega-nerd.com/SRC/libsamplerate-0.1.8.tar.gz
Source0  : http://www.mega-nerd.com/SRC/libsamplerate-0.1.8.tar.gz
Summary  : An audio Sample Rate Conversion library
Group    : Development/Tools
License  : GPL-2.0
Requires: libsamplerate-bin
Requires: libsamplerate-lib
Requires: libsamplerate-data
BuildRequires : pkgconfig(fftw3)
BuildRequires : pkgconfig(sndfile)
BuildRequires : sed

%description
This is libsamplerate, 0.1.8
libsamplerate (also known as Secret Rabbit Code) is a library for
perfroming sample rate conversion of audio data.

%package bin
Summary: bin components for the libsamplerate package.
Group: Binaries
Requires: libsamplerate-data

%description bin
bin components for the libsamplerate package.


%package data
Summary: data components for the libsamplerate package.
Group: Data

%description data
data components for the libsamplerate package.


%package dev
Summary: dev components for the libsamplerate package.
Group: Development
Requires: libsamplerate-lib
Requires: libsamplerate-bin
Requires: libsamplerate-data
Provides: libsamplerate-devel

%description dev
dev components for the libsamplerate package.


%package lib
Summary: lib components for the libsamplerate package.
Group: Libraries
Requires: libsamplerate-data

%description lib
lib components for the libsamplerate package.


%prep
%setup -q -n libsamplerate-0.1.8

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sndfile-resample

%files data
%defattr(-,root,root,-)
/usr/share/doc/libsamplerate0-dev/html/SRC.css
/usr/share/doc/libsamplerate0-dev/html/SRC.png
/usr/share/doc/libsamplerate0-dev/html/api.html
/usr/share/doc/libsamplerate0-dev/html/api_callback.html
/usr/share/doc/libsamplerate0-dev/html/api_full.html
/usr/share/doc/libsamplerate0-dev/html/api_misc.html
/usr/share/doc/libsamplerate0-dev/html/api_simple.html
/usr/share/doc/libsamplerate0-dev/html/download.html
/usr/share/doc/libsamplerate0-dev/html/faq.html
/usr/share/doc/libsamplerate0-dev/html/history.html
/usr/share/doc/libsamplerate0-dev/html/index.html
/usr/share/doc/libsamplerate0-dev/html/license.html
/usr/share/doc/libsamplerate0-dev/html/lists.html
/usr/share/doc/libsamplerate0-dev/html/quality.html
/usr/share/doc/libsamplerate0-dev/html/win32.html

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
