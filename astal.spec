%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

Summary:    Metapackage for Astal
Name:       astal
Version:    1~%{bumpver}.git%{astal_shortcommit}
Group:      Window Manager/Utilities
BuildArch:	noarch

Requires:   lib64astal-io
Requires:   lib64astal-lib
Requires:   lib64astal-lua
Requires:   lib64astal-gtk3
Requires:   lib64astal-gtk4
Requires:   lib64astal-gjs
Requires:   lib64appmenu-glib-translator

%descrption
This package is a meta-package, meaning that its purpose is to contain all dependencies for running astal/ags2

%files

#---------------------------------------------------------------------------
