# revision 29630
# category Package
# catalog-ctan /macros/latex/contrib/amsaddr
# catalog-date 2013-04-03 11:32:41 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-amsaddr
Version:	1.1
Release:	1
Summary:	Alter the position of affiliations in amsart
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/amsaddr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is to be used with the amsart documentclass. It
lets you move the authors' affiliations either just below the
authors' names on the front page or as footnotes on the first
page. The email addresses are always listed as a footnote on
the front page.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/amsaddr/amsaddr.sty
%doc %{_texmfdistdir}/doc/latex/amsaddr/README
%doc %{_texmfdistdir}/doc/latex/amsaddr/amsaddr.pdf
#- source
%doc %{_texmfdistdir}/source/latex/amsaddr/amsaddr.dtx
%doc %{_texmfdistdir}/source/latex/amsaddr/amsaddr.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
