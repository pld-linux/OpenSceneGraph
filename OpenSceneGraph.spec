%define 	fversion	%(echo %{version} |tr r -)
Summary:	Open Scene Graph - real-time visualization library
Summary(pl):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	0.9.6r2
Release:	1
License:	OpenSceneGraph Public Licence (based on LGPL with exceptions)
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/openscenegraph/%{name}-%{fversion}.tar.gz
# Source0-md5:	7023c86478aa85ce2da3e16332f01f32
Source1:	http://openscenegraph.org/download/dox/osg-doxygen-0.9.1.tar.gz
# Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
URL:		http://openscenegraph.org/
BuildRequires:	OpenThreads-devel
BuildRequires:	Producer-devel
BuildRequires:	freetype-devel
BuildRequires:	freetype1-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Open Scene Graph is a cross-platform C++/OpenGL library for
the real-time visualization.

%description -l pl
Open Scene Graph to wieloplatformowa oparta o C++ i OpenGL biblioteka
do wizualizacji w czasie rzeczywistym.

%package devel
Summary:	Header files for Open Scene Graph
Summary(pl):	Pliki nagłówkowe dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers file for OSD library.

%description devel -l pl
Pliki nagłówkowe dla biblioteki Open Scene Graph.

%package examples
Summary:	Examples for Open Scene Graph
Summary(pl):	Przykłady dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description examples
Examples for Open Scene Graph Library.

%description examples -l pl
Przykłady dla biblioteki Open Scene Graph.

# no such package (yet?)
#%package plugin
#Summary:	Plugins for Open Scene Graph
#Summary(pl):	Wtyczki dla biblioteki Open Scene Graph
#Group:		Libraries
#Requires:	%{name} = %{version}
#
#%description plugin
#Plugins for Open Scene Graph library.
#
#%description plugin -l pl
#Wtyczki dla biblioteki Open Scene Graph.

%prep
%setup -q -n %{name}-%{fversion}

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
	INST_EXAMPLE_SRC=$RPM_BUILD_ROOT%{_examplesdir}/%{name}

find $RPM_BUILD_ROOT%{_examplesdir}/%{name} -name Linux??.Opt -type d |xargs rm -rf

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

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_examplesdir}/%{name}
