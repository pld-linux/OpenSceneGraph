Summary:	Open Scene Graph - real-time visualization library
Summary(pl):	Open Scene Graph - biblioteka do wizualizacji
Name:		OpenSceneGraph
Version:	0.9.3
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://openscenegraph.org/download/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	a6e2193e7c5b9b650a71f25cea326994
Source1:	http://openscenegraph.org/download/dox/osg-doxygen-0.9.1.tar.gz
# Source1-md5:	7e6d785d1b763aaeae03c2dc4c148805
URL:		http://openscenegraph.org/
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
Summary(pl):	Pliki nag³ówkowe dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers file for OSD library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki Open Scene Graph.

%package examples
Summary:	Examples for Open Scene Graph
Summary(pl):	Przyk³ady dla Open Scene Graph
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description examples
Examples for Open Scene Graph Library.

%description examples -l pl
Przyk³ady dla biblioteki Open Scene Graph.

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
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	INC="-I/usr/X11R6/include -I/usr/include/freetype2"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
	INST_SYS_PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	INST_SHARE_PREFIX=$RPM_BUILD_ROOT%{_datadir} \
	INST_SRC=$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	INST_DEMOS=$RPM_BUILD_ROOT%{_examplesdir}/%{name} \
	install

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
%attr(644,root,root) %{_includedir}/osg*

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/%{name}
%{_examplesdir}/%{name}/Make
%{_examplesdir}/%{name}/demos
%attr(755,root,root) %{_examplesdir}/%{name}/osg*
