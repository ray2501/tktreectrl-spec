%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tktreectrl
Summary:       A flexible listbox widget for Tk
Version:       2.4.1
Release:       1
License:       TCL
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           http://tktreectrl.sourceforge.net/
BuildRequires: autoconf
BuildRequires: tcl-devel >= 8.5
BuildRequires: tk-devel >= 8.5
Requires:      tcl >= 8.5
Requires:      tk >= 8.5
BuildRoot:     %{buildroot}

%description
TkTreeCtrl is a multi-column hierarchical listbox widget for the Tk GUI toolkit.

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib} \
	--with-tk=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
/usr/share/man/mann/
