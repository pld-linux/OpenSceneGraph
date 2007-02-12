%define		_snap	20050228
%define		_snap_time	2325
Summary:	Open Scene Graph - real-time visualization library
Summary(pl.UTF-8):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	0.9.8
Release:	0.%{_snap}.1
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
Source0:	http://openscenegraph.org/downloads/developer/%{name}-%{version}-%{_snap}%{_snap_time}.tar.gz
# Source0-md5:	13f0198d1a8a13707c25fd9ecdec9da2
Source1:	osg-doxygen-0.9.1.tar.gz
# Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
URL:		http://openscenegraph.org/
BuildRequires:	OpenThreads-devel
BuildRequires:	Producer-devel
BuildRequires:	freetype-devel
BuildRequires:	freetype1-devel
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

# no such package (yet?)
#%package plugin
#Summary:	Plugins for Open Scene Graph
#Summary(pl):	Wtyczki dla biblioteki Open Scene Graph
#Group:		Libraries
#Requires:	%{name} = %{version}-%{release}
#
#%description plugin
#Plugins for Open Scene Graph library.
#
#%description plugin -l pl
#Wtyczki dla biblioteki Open Scene Graph.

%prep
%setup -q -n %{name}-%{version}-%{_snap}%{_snap_time}

%build
%{__make} -f GNUmakefile \
	CC="%{__cc} %{rpmcflags}" \
	CXX="%{__cxx} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -f GNUmakefile install \
	INST_LOCATION=$RPM_BUILD_ROOT%{_prefix} \
	INST_SHARE_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INST_EXAMPLES=$RPM_BUILD_ROOT%{_bindir} \
	INST_EXAMPLE_SRC=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
install Make/openscenegraph.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
find $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} -name Linux??.Opt -type d |xargs rm -rf

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%dir %{_libdir}/osgPlugins
%attr(755,root,root) %{_libdir}/osgPlugins/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/osg*
%{_pkgconfigdir}/*.pc

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}-%{version}
