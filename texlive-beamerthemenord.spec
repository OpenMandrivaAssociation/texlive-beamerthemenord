Name:		texlive-beamerthemenord
Version:	56180
Release:	2
Summary:	A simple beamer theme using the "Nord" color theme
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamerthemenord
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenord.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerthemenord.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple beamer theme using the Nord
color theme.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamerthemenord
%doc %{_texmfdistdir}/doc/latex/beamerthemenord

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
