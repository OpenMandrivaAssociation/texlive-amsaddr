%global tl_name amsaddr
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Alter the position of affiliations in amsart
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/amsaddr
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is to be used with the amsart documentclass. It lets you
move the authors' affiliations either just below the authors' names on
the front page or as footnotes on the first page. The email addresses
are always listed as a footnote on the front page.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/amsaddr
%dir %{_datadir}/texmf-dist/source/latex/amsaddr
%dir %{_datadir}/texmf-dist/tex/latex/amsaddr
%doc %{_datadir}/texmf-dist/doc/latex/amsaddr/README.md
%doc %{_datadir}/texmf-dist/doc/latex/amsaddr/amsaddr.pdf
%doc %{_datadir}/texmf-dist/source/latex/amsaddr/amsaddr.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsaddr/amsaddr.ins
%{_datadir}/texmf-dist/tex/latex/amsaddr/amsaddr.sty
