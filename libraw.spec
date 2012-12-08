%define oname	LibRaw

%define major	2
%define libname	%mklibname raw %{major}
%define devname %mklibname raw -d

Summary:	Library for reading and processing of RAW digicam images
Name:		libraw
Version:	0.13.5
Release:	%mkrel 3
License:	GPLv3
Group:		Development/C
URL:		http://www.libraw.org
Source0:	http://www.libraw.org/data/%{oname}-%{version}.tar.gz
Source1:        http://www.libraw.org/data/%{oname}-demosaic-pack-GPL2-%{version}.tar.gz
Source2:        http://www.libraw.org/data/%{oname}-demosaic-pack-GPL3-%{version}.tar.gz
BuildRequires:	libgomp-devel
Buildrequires:	lcms-devel

%description
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc, virtually all RAW formats are
supported).

It pays special attention to correct retrieval of data required for subsequent
RAW conversion.

The library is intended for embedding in RAW converters, data analyzers, and
other programs using RAW files as the initial data.

Since LibRaw is linked against LibRaw-demosaic-pack-GPL2 and
LibRaw-demosaic-pack-GPL3 the global licence is GPLv3.

%package -n %{libname}
Summary:	Library for reading and processing of RAW digicam images
Group:		System/Libraries

%description -n %{libname}
LibRaw is a library for reading RAW files from digital photo cameras
(CRW/CR2, NEF, RAF, DNG, MOS, KDC, DCR, etc, virtually all RAW formats are
supported).

It pays special attention to correct retrieval of data required for subsequent
RAW conversion.

The library is intended for embedding in RAW converters, data analyzers, and
other programs using RAW files as the initial data.

Since LibRaw is linked against LibRaw-demosaic-pack-GPL2 and
LibRaw-demosaic-pack-GPL3 the global licence is GPLv3.

%package -n %{devname}
Summary:	LibRaw development files and headers
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{name}-devel < 0.13.4

%description -n %{devname}
This package contains the development files and headers for %{oname}.

%package tools
Summary:	Command line tools from %{oname}
Group:		Graphics

%description tools
This packages provides tools to manipulate raw files.

%prep
%setup -qn %{oname}-%{version} -b1 -b2

%build
%configure2_5x --disable-openmp
#parallel build tends to broke build
make -j2

%install
rm -rf %{buildroot}
%makeinstall_std

# The source tree has these with execute permissions for some reason
chmod 644 LICENSE.CDDL LICENSE.LGPL LICENSE.LibRaw.pdf

# let files section handle docs
rm -rf %{buildroot}%{_datadir}/doc/*

# move docs to a better location
mv doc html

%clean
rm -rf %{buildroot}

%files tools
%defattr(-,root,root)
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%doc LICENSE* README README.demosaic-packs
%{_libdir}/libraw.so.%{major}*
%{_libdir}/libraw_r.so.%{major}*

%files -n %{devname}
%defattr(-,root,root)
%doc LICENSE* Changelog.* README README.demosaic-packs html/
%{_includedir}/libraw
%{_libdir}/libraw.*a
%{_libdir}/libraw_r.*a
%{_libdir}/libraw.so
%{_libdir}/libraw_r.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.13.5-1mdv2011.0
+ Revision: 681337
- update to new version 0.13.5

* Sat May 07 2011 Jani Välimaa <wally@mandriva.org> 0.13.4-1
+ Revision: 672257
- new version 0.13.4
- create a subpackage for tools
- build with demosaic packs (GPL2 and GPL3)
- change license to GPLv3
- enable debug package
- libify package
- fix summaries and descriptions

* Fri Jan 07 2011 Funda Wang <fwang@mandriva.org> 0.12.2-1mdv2011.0
+ Revision: 629452
- new version 0.12.2

* Thu Nov 25 2010 Funda Wang <fwang@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 600929
- update to new version 0.10.0

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.9.1-1mdv2011.0
+ Revision: 565591
- update tag
- import libraw


