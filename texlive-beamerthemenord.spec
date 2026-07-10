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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a simple beamer theme using the Nord color theme.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerthemenord
%dir %{_datadir}/texmf-dist/tex/latex/beamerthemenord
%dir %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/beamerthemeNord.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/beamerthemeNord.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-blocks.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-colors.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-fonts.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-titlepage.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-toc.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/dark-usage.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-blocks.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-colors.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-fonts.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-titlepage.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-toc.png
%doc %{_datadir}/texmf-dist/doc/latex/beamerthemenord/screenshots/light-usage.png
%{_datadir}/texmf-dist/tex/latex/beamerthemenord/beamercolorthemeNord.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemenord/beamerfontthemeNord.sty
%{_datadir}/texmf-dist/tex/latex/beamerthemenord/beamerthemeNord.sty
