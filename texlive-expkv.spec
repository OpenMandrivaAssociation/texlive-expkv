Name:		texlive-expkv
Version:	60573
Release:	2
Summary:	An expandable key=val implementation
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expkv
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
expkv is a minimalistic but fast and expandable <key>=<val>
implementation. It provides two parsing macros:
\ekvset{<set>}{<key=val list>} which is comparable to keyval's
\setkeys. \ekvparse<cs1><cs2>{<key=val list>} which can be used
inside \expanded and expands to <cs1>{key} and <cs2>{key}{val}
for the entries in the <key=val list>. expkv has predictable
brace-stripping behaviour and handles commas and equal signs
with category codes 12 and 13 correctly. A key-defining
interface that is not as rudimentary as the macros provided in
this package is contained in expkv-def.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/expkv
%{_texmfdistdir}/tex/latex/expkv
%{_texmfdistdir}/tex/generic/expkv
%{_texmfdistdir}/tex/context/third/expkv
%doc %{_texmfdistdir}/doc/latex/expkv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
