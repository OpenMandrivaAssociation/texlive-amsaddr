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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is to be used with the amsart documentclass. It lets you
move the authors' affiliations either just below the authors' names on
the front page or as footnotes on the first page. The email addresses
are always listed as a footnote on the front page.

