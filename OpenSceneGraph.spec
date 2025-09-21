# TODO: nvtt
#
# Conditional build:
%bcond_with	fbx		# Autodesk FBX SDK support (proprietary)
%bcond_with	ffmpeg		# FFmpeg support, needs ffmpeg < 5

Summary:	Open Scene Graph - real-time visualization library
Summary(pl.UTF-8):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	3.6.5
Release:	7
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
#Source0Download: https://github.com/openscenegraph/OpenSceneGraph/releases
Source0:	https://github.com/openscenegraph/OpenSceneGraph/archive/%{name}-%{version}.tar.gz
# Source0-md5:	51b1c6ee5627246e78b23adbf0aa48f8
# https://src.fedoraproject.org/rpms/OpenSceneGraph/blob/rawhide/f/OpenSceneGraph_asio.patch
Patch0:		%{name}-asio.patch
Patch1:		%{name}-OpenCASCADE.patch
Patch2:		%{name}-gta.patch
# https://src.fedoraproject.org/rpms/OpenSceneGraph/blob/rawhide/f/OpenSceneGraph-openexr3.patch
Patch3:		%{name}-openexr3.patch
Patch4:		boost-detect.patch
URL:		https://www.openscenegraph.org/index.php/33-openscenegraph/4-front-page
BuildRequires:	Coin-devel
BuildRequires:	EGL-devel
BuildRequires:	EGL-devel
BuildRequires:	OpenCASCADE-devel >= 7.8.0
BuildRequires:	OpenEXR-devel
BuildRequires:	OpenGL-devel >= 2
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5OpenGL-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	SDL2-devel >= 2
BuildRequires:	SoXt-devel
BuildRequires:	asio-devel >= 1.11
BuildRequires:	boost-devel >= 1.37
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	collada-dom-devel
BuildRequires:	curl-devel
BuildRequires:	dcmtk-devel
%{?with_fbx:BuildRequires:	fbxsdk-devel}
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel >= 2
BuildRequires:	gdal-devel
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	gtk+2-devel
# only for osgviewerGTK, which is not built
#BuildRequires:	gtkglext-devel
BuildRequires:	jasper-devel
BuildRequires:	libgta-devel
BuildRequires:	libjpeg-devel
BuildRequires:	liblas-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.35
BuildRequires:	libtiff-devel
BuildRequires:	libvncserver-devel
BuildRequires:	lua52-devel >= 5.2
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel
BuildRequires:	qt5-build >= 5
BuildRequires:	qt5-qmake >= 5
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#define		specflags	-std=c++11

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for the
real-time visualization.

%description -l pl.UTF-8
Open Scene Graph to wieloplatformowa oparta o C++ i OpenGL biblioteka
do wizualizacji w czasie rzeczywistym.

%package plugins
Summary:	Plugins for Open Scene Graph
Summary(pl.UTF-8):	Wtyczki dla biblioteki Open Scene Graph
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	librsvg-devel >= 1:2.35

%description plugins
Plugins for Open Scene Graph library.

%description plugins -l pl.UTF-8
Wtyczki dla biblioteki Open Scene Graph.

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

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1

%build
install -d build
cd build
%cmake .. \
	-DDESIRED_QT_VERSION=5 \
%if "%{_lib}" == "lib64"
	-DLIB_POSTFIX=64 \
%endif
%if "%{_lib}" == "libx32"
	-DLIB_POSTFIX=x32 \
%endif
	%{!?with_ffmpeg:-DCMAKE_DISABLE_FIND_PACKAGE_FFmpeg=1} \
	-DOSG_USE_LOCAL_LUA_SOURCE=OFF

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
%doc AUTHORS.txt ChangeLog LICENSE.txt NEWS.txt README.md
%attr(755,root,root) %{_libdir}/libOpenThreads.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOpenThreads.so.21
%attr(755,root,root) %{_libdir}/libosg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosg.so.161
%attr(755,root,root) %{_libdir}/libosgAnimation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgAnimation.so.161
%attr(755,root,root) %{_libdir}/libosgDB.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgDB.so.161
%attr(755,root,root) %{_libdir}/libosgFX.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgFX.so.161
%attr(755,root,root) %{_libdir}/libosgGA.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgGA.so.161
%attr(755,root,root) %{_libdir}/libosgManipulator.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgManipulator.so.161
%attr(755,root,root) %{_libdir}/libosgParticle.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgParticle.so.161
%attr(755,root,root) %{_libdir}/libosgPresentation.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgPresentation.so.161
#%attr(755,root,root) %{_libdir}/libosgQt.so.*.*.*
#%attr(755,root,root) %ghost %{_libdir}/libosgQt.so.141
%attr(755,root,root) %{_libdir}/libosgShadow.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgShadow.so.161
%attr(755,root,root) %{_libdir}/libosgSim.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgSim.so.161
%attr(755,root,root) %{_libdir}/libosgTerrain.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgTerrain.so.161
%attr(755,root,root) %{_libdir}/libosgText.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgText.so.161
%attr(755,root,root) %{_libdir}/libosgUI.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgUI.so.161
%attr(755,root,root) %{_libdir}/libosgUtil.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgUtil.so.161
%attr(755,root,root) %{_libdir}/libosgViewer.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgViewer.so.161
%attr(755,root,root) %{_libdir}/libosgVolume.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgVolume.so.161
%attr(755,root,root) %{_libdir}/libosgWidget.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libosgWidget.so.161

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
#%attr(755,root,root) %{_libdir}/libosgQt.so
%attr(755,root,root) %{_libdir}/libosgShadow.so
%attr(755,root,root) %{_libdir}/libosgSim.so
%attr(755,root,root) %{_libdir}/libosgTerrain.so
%attr(755,root,root) %{_libdir}/libosgText.so
%attr(755,root,root) %{_libdir}/libosgUI.so
%attr(755,root,root) %{_libdir}/libosgUtil.so
%attr(755,root,root) %{_libdir}/libosgViewer.so
%attr(755,root,root) %{_libdir}/libosgVolume.so
%attr(755,root,root) %{_libdir}/libosgWidget.so
%{_includedir}/OpenThreads
%{_includedir}/osg*
%{_pkgconfigdir}/openscenegraph.pc
%{_pkgconfigdir}/openthreads.pc
%{_pkgconfigdir}/openscenegraph-osg.pc
%{_pkgconfigdir}/openscenegraph-osgAnimation.pc
%{_pkgconfigdir}/openscenegraph-osgDB.pc
%{_pkgconfigdir}/openscenegraph-osgFX.pc
%{_pkgconfigdir}/openscenegraph-osgGA.pc
%{_pkgconfigdir}/openscenegraph-osgManipulator.pc
%{_pkgconfigdir}/openscenegraph-osgParticle.pc
#%{_pkgconfigdir}/openscenegraph-osgQt.pc
%{_pkgconfigdir}/openscenegraph-osgShadow.pc
%{_pkgconfigdir}/openscenegraph-osgSim.pc
%{_pkgconfigdir}/openscenegraph-osgTerrain.pc
%{_pkgconfigdir}/openscenegraph-osgText.pc
%{_pkgconfigdir}/openscenegraph-osgUtil.pc
%{_pkgconfigdir}/openscenegraph-osgViewer.pc
%{_pkgconfigdir}/openscenegraph-osgVolume.pc
%{_pkgconfigdir}/openscenegraph-osgWidget.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/osgarchive
%attr(755,root,root) %{_bindir}/osgconv
%attr(755,root,root) %{_bindir}/osgfilecache
%attr(755,root,root) %{_bindir}/osgversion
%attr(755,root,root) %{_bindir}/osgviewer
%attr(755,root,root) %{_bindir}/present3D
%{_examplesdir}/%{name}-%{version}
