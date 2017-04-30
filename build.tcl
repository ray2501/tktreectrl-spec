#!/usr/bin/tclsh

set arch "x86_64"
set base "tktreectrl-2.4.1"

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tktreectrl.spec]
exec >@stdout 2>@stderr {*}$buildit

