%global tl_name beamerthemenord
%global tl_revision 56180

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.0
Release:	%{tl_revision}.1
Summary:	A simple beamer theme using the Nord color theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamerthemenord
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenord.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenord.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple beamer theme using the Nord color theme.

