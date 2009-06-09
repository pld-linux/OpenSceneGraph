Summary:	Open Scene Graph - real-time visualization library
Summary(pl.UTF-8):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	2.8.1
Release:	0.1
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
Source0:	http://www.openscenegraph.org/downloads/stable_releases/OpenSceneGraph-%{version}/source/%{name}-%{version}.zip
# Source0-md5:	18a8d3f01a72b6027147b3918c18c662
#Source1:	osg-doxygen-0.9.1.tar.gz
## Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
URL:		http://www.openscenegraph.org/projects/osg/
BuildRequires:	cmake
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for
the real-time visualization.

%description -l pl.UTF-8
Open Scene Graph to wieloplatformowa oparta o C++ i OpenGL biblioteka
do wizualizacji w czasie rzeczywistym.

%package devel
Summary:	Header files for Open Scene Graph
Summary(pl.UTF-8):	Pliki nagłówkowe dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers file for OSD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki Open Scene Graph.

%package examples
Summary:	Examples for Open Scene Graph
Summary(pl.UTF-8):	Przykłady dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
Examples for Open Scene Graph Library.

%description examples -l pl.UTF-8
Przykłady dla biblioteki Open Scene Graph.

%package plugins
Summary:	Plugins for Open Scene Graph
Summary(pl):	Wtyczki dla biblioteki Open Scene Graph
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description plugins
Plugins for Open Scene Graph library.

%description plugins -l pl
Wtyczki dla biblioteki Open Scene Graph.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=None \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_VERBOSE_MAKEFILE=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -r examples/osg* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenThreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenThreads.so.11
%attr(755,root,root) %{_libdir}/libosg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosg.so.55
%attr(755,root,root) %{_libdir}/libosgAnimation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgAnimation.so.55
%attr(755,root,root) %{_libdir}/libosgDB.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgDB.so.55
%attr(755,root,root) %{_libdir}/libosgFX.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgFX.so.55
%attr(755,root,root) %{_libdir}/libosgGA.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgGA.so.55
%attr(755,root,root) %{_libdir}/libosgManipulator.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgManipulator.so.55
%attr(755,root,root) %{_libdir}/libosgParticle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgParticle.so.55
%attr(755,root,root) %{_libdir}/libosgShadow.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgShadow.so.55
%attr(755,root,root) %{_libdir}/libosgSim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgSim.so.55
%attr(755,root,root) %{_libdir}/libosgTerrain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgTerrain.so.55
%attr(755,root,root) %{_libdir}/libosgText.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgText.so.55
%attr(755,root,root) %{_libdir}/libosgUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgUtil.so.55
%attr(755,root,root) %{_libdir}/libosgViewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgViewer.so.55
%attr(755,root,root) %{_libdir}/libosgVolume.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgVolume.so.55
%attr(755,root,root) %{_libdir}/libosgWidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgWidget.so.55

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/osgPlugins-%{version}
%attr(755,root,root) %{_libdir}/osgPlugins-%{version}/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenThreads.so
%attr(755,root,root) %{_libdir}/libosg.so
%attr(755,root,root) %{_libdir}/libosgAnimation.so
%attr(755,root,root) %{_libdir}/libosgDB.so
%attr(755,root,root) %{_libdir}/libosgFX.so
%attr(755,root,root) %{_libdir}/libosgGA.so
%attr(755,root,root) %{_libdir}/libosgManipulator.so
%attr(755,root,root) %{_libdir}/libosgParticle.so
%attr(755,root,root) %{_libdir}/libosgShadow.so
%attr(755,root,root) %{_libdir}/libosgSim.so
%attr(755,root,root) %{_libdir}/libosgTerrain.so
%attr(755,root,root) %{_libdir}/libosgText.so
%attr(755,root,root) %{_libdir}/libosgUtil.so
%attr(755,root,root) %{_libdir}/libosgViewer.so
%attr(755,root,root) %{_libdir}/libosgVolume.so
%attr(755,root,root) %{_libdir}/libosgWidget.so
%{_includedir}/OpenThreads
%{_includedir}/osg*
%{_pkgconfigdir}/openscenegraph.pc
%{_pkgconfigdir}/openthreads.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
