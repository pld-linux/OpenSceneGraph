Summary:	Open Scene Graph - real-time visualization library
Summary(pl):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	0.9.3
Release:	1
Copyright:	LGPL
Group:		X11/Graphics
Source0:	http://openscenegraph.org/download/snapshots/%{name}-%{version}.tar.gz
Source1:	http://openscenegraph.org/download/dox/osg-doxygen-0.9.1.tar.gz
URL:		http://openscenegraph.org/
BuildRequires:	libtiff-devel
BuildRequires:	freetype-devel
BuildRequires:	freetype1-devel
BuildRequires:	libpng-devel
BuildRequires:	libungif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
#BuildRequires:	libtiff-devel
#BuildRequires:	libtiff-devel
#BuildRequires:	libtiff-devel
#Requires:	
#Patch0:		osg-Makefile.patch
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
The Open Scene Graph is a cross-plathorm C++/OpenGL library for 
the real-time visualization.

%description -l pl

%package devel
Summary:	Header files of Open Scene Graph 
Summary(pl):	Pliki nag³ówkowe dla Open Scene Graph
Group:		Development/Library
Requires:	%{name} = %{version}
%description devel 
Headers file for OSD library.
%description devel -l pl
Pliki nag³ówkowe dla biblioteki Open Scene Graph

%package examples
Summary:	Examples for Open Scene Graph 
Summary(pl):	Przyk³ady dla Open Scene Graph
Group:		Development/Library
Requires:	%{name} = %{version}
%description examples
Examples for Open Scene Graph Library
%description examples -l pl
Przyk³ady dla biblioteki Open Scene Graph

%package plugin
Summary:	Plug-Ins for Open Scene Graph 
Summary(pl):	Pluginy dla Open Scene Graph
Group:		Development/Library
Requires:	%{name} = %{version}
%description plugin
Plugins for OSD library.
%description plugin -l pl
Pluginy dla biblioteki Open Scene Graph

%prep
%setup -q

#%patch0 -p1

%build
%{__make} CC=gcc CXX=g++ INC="-I/usr/X11R6/include -I/usr/include -I/usr/include/freetype2"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	INST_SYS_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INST_SHARE_PREFIX=$RPM_BUILD_ROOT%{_datadir} \
	INST_SRC=$RPM_BUILD_ROOT/usr/src/examples/%{name} \
	INST_DEMOS=$RPM_BUILD_ROOT/usr/src/examples/%{name} \
	install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc
%attr(755, root, root) %{_libdir}/*.so
%attr(755, root, root) %{_libdir}/osgPlugins/*

%files devel
%defattr(644, root, root, 755)
%attr(644, root, root) %{_includedir}/osg*/*

%files examples
%defattr(644, root, root, 755)
%attr(644, root, root) /usr/src/examples/%{name}/Make/*
%attr(644, root, root) /usr/src/examples/%{name}/demos/*/*
%attr(755, root, root) /usr/src/examples/%{name}/osg*

%files plugin
