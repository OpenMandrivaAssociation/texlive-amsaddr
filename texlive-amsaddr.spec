Name:		texlive-amsaddr
Version:	64357
Release:	2
Summary:	Alter the position of affiliations in amsart
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/amsaddr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsaddr.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/amsaddr
%doc %{_texmfdistdir}/doc/latex/amsaddr
#- source
%doc %{_texmfdistdir}/source/latex/amsaddr

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
