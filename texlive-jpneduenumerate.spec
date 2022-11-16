Name:		texlive-jpneduenumerate
Version:	63893
Release:	1
Summary:	Enumerative expressions in Japanese education
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jpneduenumerate
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpneduenumerate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jpneduenumerate.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Mathematical equation representation in Japanese education
differs somewhat from the standard LaTeX writing style. This
package introduces enumerative expressions in Japanese
education.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jpneduenumerate
%doc %{_texmfdistdir}/doc/latex/jpneduenumerate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
