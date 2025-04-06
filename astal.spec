%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

Summary:	Metapackage for Astal
Name:		astal
Version:	1~%{bumpver}.git%{astal_shortcommit}
Release:	1
Group:		Window Manager/Utilities
License:	LGPL-2.1
BuildArch:	noarch

Requires:	%{mklibname astal-io}
Requires:	%{mklibname astal-lib}
Requires:	%{mklibname astal-lua}
Requires:	%{mklibname astal-gtk3}
Requires:	%{mklibname astal-gtk4}
Requires:	%{mklibname astal-gjs}
Requires:	%{mklibname appmenu-glib-translator}
Requires:	typelib(AppmenuGLibTranslator)

%description
This package is a meta-package, meaning that its purpose is to contain all dependencies for running astal/ags2

%files

#---------------------------------------------------------------------------
