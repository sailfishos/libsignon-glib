Name: libsignon-glib
Version: 1.7
Release: 1
Summary: Single signon authentication library for GLib applications
License: LGPLv2+
URL: https://gitlab.com/groups/accounts-sso
Source0: %{name}-%{version}.tar.gz
Patch0: 0001-Patch-out-docs-build.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: signon-qt5-devel
BuildRequires: pkgconfig(check)
BuildRequires: python
BuildRequires: libtool
# For signond
Requires: signon-qt5

%description
%{summary}.

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libsignon-glib.so.*
%{_datadir}/vala/vapi/signon.vapi
%exclude /usr/doc/reference/*

%package devel
Summary: Development files for libsignon-glib
Requires: %{name} = %{version}-%{release}
# signond.pc, required by libsignon-glib.pc
Requires: signon-qt5-devel

%description devel
%{summary}

%files devel
%defattr(-,root,root,-)
%{_libdir}/libsignon-glib.so
%{_includedir}/libsignon-glib/*.h
%{_libdir}/pkgconfig/libsignon-glib.pc

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%reconfigure
# %{?jobs:-j%jobs} disabled to fix errors with xgen-getc
make

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig
