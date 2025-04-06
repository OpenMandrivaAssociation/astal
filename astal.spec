%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

Summary:    Metapackage for Astal
Name:       astal
Version:    1~%{bumpver}.git%{astal_shortcommit}
Release:    1
Group:      Window Manager/Utilities
License:    GPL-2.1
BuildArch:	noarch

Requires:   astal-io
Requires:   astal-lib
Requires:   astal-lua
Requires:   astal3
Requires:   astal4
Requires:   astal-gjs
Requires:   typelib(AppmenuGLibTranslator)

%description
This package is a meta-package, meaning that its purpose is to contain all dependencies for running astal/ags2

%files

#---------------------------------------------------------------------------
