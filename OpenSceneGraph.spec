Summary:	Open Scene Graph - real-time visualization library
Summary(pl.UTF-8):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	2.9.11
Release:	0.beta.1
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
Source0:	http://www.openscenegraph.org/downloads/developer_releases/%{name}-%{version}.zip
# Source0-md5:	98cd9b63b4c2648caaa2e03321288b07
#Source1:	osg-doxygen-0.9.1.tar.gz
## Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
Patch0:		%{name}-link.patch
URL:		http://www.openscenegraph.org/projects/osg/
BuildRequires:	cairo-devel
BuildRequires:	cmake
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	rpmbuild(macros) >= 1.577
BuildRequires:	unzip
#BuildRequires:	xulrunner-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for the
real-time visualization.

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
%patch0 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -a examples/osg* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libOpenThreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenThreads.so.12
%attr(755,root,root) %{_libdir}/libosg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosg.so.71
%attr(755,root,root) %{_libdir}/libosgAnimation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgAnimation.so.71
%attr(755,root,root) %{_libdir}/libosgDB.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgDB.so.71
%attr(755,root,root) %{_libdir}/libosgFX.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgFX.so.71
%attr(755,root,root) %{_libdir}/libosgGA.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgGA.so.71
%attr(755,root,root) %{_libdir}/libosgManipulator.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgManipulator.so.71
%attr(755,root,root) %{_libdir}/libosgParticle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgParticle.so.71
%attr(755,root,root) %{_libdir}/libosgPresentation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgPresentation.so.71
%attr(755,root,root) %{_libdir}/libosgShadow.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgQt.so.71
%attr(755,root,root) %{_libdir}/libosgQt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgShadow.so.71
%attr(755,root,root) %{_libdir}/libosgSim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgSim.so.71
%attr(755,root,root) %{_libdir}/libosgTerrain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgTerrain.so.71
%attr(755,root,root) %{_libdir}/libosgText.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgText.so.71
%attr(755,root,root) %{_libdir}/libosgUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgUtil.so.71
%attr(755,root,root) %{_libdir}/libosgViewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgViewer.so.71
%attr(755,root,root) %{_libdir}/libosgVolume.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgVolume.so.71
%attr(755,root,root) %{_libdir}/libosgWidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgWidget.so.71

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
%attr(755,root,root) %{_libdir}/libosgPresentation.so
%attr(755,root,root) %{_libdir}/libosgQt.so
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
%{_pkgconfigdir}/openscenegraph-osg.pc
%{_pkgconfigdir}/openscenegraph-osgAnimation.pc
%{_pkgconfigdir}/openscenegraph-osgDB.pc
%{_pkgconfigdir}/openscenegraph-osgFX.pc
%{_pkgconfigdir}/openscenegraph-osgGA.pc
%{_pkgconfigdir}/openscenegraph-osgManipulator.pc
%{_pkgconfigdir}/openscenegraph-osgParticle.pc
%{_pkgconfigdir}/openscenegraph-osgQt.pc
%{_pkgconfigdir}/openscenegraph-osgShadow.pc
%{_pkgconfigdir}/openscenegraph-osgSim.pc
%{_pkgconfigdir}/openscenegraph-osgTerrain.pc
%{_pkgconfigdir}/openscenegraph-osgText.pc
%{_pkgconfigdir}/openscenegraph-osgUtil.pc
%{_pkgconfigdir}/openscenegraph-osgViewer.pc
%{_pkgconfigdir}/openscenegraph-osgVolume.pc
%{_pkgconfigdir}/openscenegraph-osgWidget.pc
%{_pkgconfigdir}/openthreads.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
