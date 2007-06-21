Summary:	Open Scene Graph - real-time visualization library
Summary(pl.UTF-8):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	2.0
Release:	0.1
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
Source0:	http://www.openscenegraph.com/downloads/snapshots/%{name}-%{version}.zip
# Source0-md5:	9e8d8311868f2acce377a6d7d69c26c2
#Source1:	osg-doxygen-0.9.1.tar.gz
## Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
URL:		http://openscenegraph.org/
BuildRequires:	cmake
BuildRequires:	freetype-devel
BuildRequires:	giflib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
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
%setup -q -n OpenSceneGraph

%build
mkdir build
cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
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
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%{_libdir}/*.so.11
%{_libdir}/*.so.7

%files plugins
%defattr(644,root,root,755)
%dir %{_libdir}/osgPlugins-2.0.0
%attr(755,root,root) %{_libdir}/osgPlugins-2.0.0/*.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/osg*
%{_includedir}/Open*

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
