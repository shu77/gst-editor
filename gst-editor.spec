Summary: 	GStreamer streaming media editor and GUI tools
Name: 		gst-editor
Version: 	0.10.3.2
Release: 	@GST_EDITOR_VERSION_RELEASE@

License: 	LGPL
Group: 		Applications/Multimedia
Source: 	%{name}-%{version}.tar.gz
BuildRoot: 	%{_tmppath}/%{name}-%{version}-root

Requires: 	libxml2 >= 2.0.0
Requires:    	libgnomeui >= 1.109.0
Requires:	gstreamer >= 0.10.6
Requires:	libglade2 >= 2
Requires:	scrollkeeper >= 0.3.8
BuildRequires: 	libxml2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 1.109.0
BuildRequires:	gtk2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 0.10.6
BuildRequires:	libglade2-devel >= 2
BuildRequires:	scrollkeeper

%description
This package contains gst-editor and a few graphical tools.
gst-editor is a development tool for graphically creating
applications based on GStreamer.
gst-launch-gui is an extension of gst-launch allowing you to dynamically
turn on logging domains.
gst-inspect-gui is a graphical element browser.

%package devel
Summary: 	Development headers for the Editor
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
This package provides the necessary development libraries and include
files to allow you to embed the editor in other applications or call upon its
functionality.

%prep
%setup

%build
##%{?__libtoolize:[ -f configure.in ] && %{__libtoolize} --copy --force} ; \
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ; \
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS ; \
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS ; \
./configure \
  --prefix=%{_prefix} \
  --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} \
  --sbindir=%{_sbindir} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir}
if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0) 
else
  make
fi

make  

%makeinstall
# Clean out files that should not be part of the rpm.
# This is the recommended way of dealing with it for RH8
rm -rf $RPM_BUILD_ROOT/var/*
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
[ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != / ] && rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update -q
# %{_prefix}/bin/gst-register --gst-mask=0

%postun
/sbin/ldconfig
scrollkeeper-update -q

%files
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog INSTALL COPYING
%{_bindir}/gst-editor
%{_bindir}/gst-launch-gui
%{_bindir}/gst-inspect-gui
%{_libdir}/libgstdebugui.so.*
%{_libdir}/libgsteditor.so.*
%{_libdir}/libgstelementbrowser.so.*
%{_libdir}/libgstelementui.so.*
%{_datadir}/gst-editor/*.glade2
%{_datadir}/applications/gst-editor.desktop
%{_datadir}/applications/gst-inspect.desktop
%{_datadir}/applications/gst-launch.desktop
%{_datadir}/pixmaps/gst-editor.png
%{_datadir}/pixmaps/gst-inspect.png
%{_datadir}/pixmaps/gst-launch.png
%{_datadir}//gst-editor/gst-editor.png
%{_datadir}/omf/gst-editor/gst-editor-manual-C.omf
%{_datadir}/gst-editor/gnome/help/gst-editor/C/*
%{_mandir}/man1/gst-editor.*
%{_mandir}/man1/gst-launch-gui.*
%{_mandir}/man1/gst-inspect-gui.1


%files devel
%defattr(-, root, root)
%{_includedir}/gst-editor-%{version}/gst/debug-ui/debug-ui.h
%{_includedir}/gst-editor-%{version}/gst/editor/*
%{_includedir}/gst-editor-%{version}/gst/element-browser/*
%{_includedir}/gst-editor-%{version}/gst/element-ui/*
%{_libdir}/libgstdebugui.so
%{_libdir}/libgsteditor.so
%{_libdir}/libgstelementbrowser.so
%{_libdir}/libgstelementui.so
%{_libdir}/libgstdebugui.a
%{_libdir}/libgsteditor.a
%{_libdir}/libgstelementbrowser.a
%{_libdir}/libgstelementui.a

%changelog
* Sun Sep 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- updated requires and buildrequires

* Sat Sep 21 2002 Christian Fredrik Kalager Schaller <Uraeus@linuxrising.org>
- Added desktop file and icon for gst-editor

* Mon May 11 2002 Christian Fredrik Kalager Schaller <Uraeus@linuxrising.org>
- Cleaned up SPEC file some more
- Added devel package

* Mon Apr 22 2002 Thomas Vander Stichele <thomas@apestaart.org>
- Cleaned up description
- Added gst-inspect-gui

* Sat Dec 29 2001 Rodney Dawes <dobey@free.fr>
- Cleaned up the spec file for the gstreamer core/plug-ins split
- Improve spec file
