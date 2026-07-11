%global tl_name jpneduenumerate
%global tl_revision 72898

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Enumerative expressions in Japanese education
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jpneduenumerate
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jpneduenumerate.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jpneduenumerate.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Mathematical equation representation in Japanese education differs
somewhat from the standard LaTeX writing style. This package introduces
enumerative expressions in Japanese education.

