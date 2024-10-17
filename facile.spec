%define	debug_package %{nil}

# The ocaml(*) dependency generator seems to be broken
%global __requires_exclude ^ocaml.*$

Summary:	Constraint programming library
Name:		facile
Version:	1.1.4
Release:	5
License:	GPLv2+
Group:		System/Libraries
Url:		https://facile.recherche.enac.fr/
# Git repository at
#Source0:	https://github.com/Emmanuel-PLF/facile/archive/%{version}.tar.gz
Source0:	https://github.com/Emmanuel-PLF/facile/releases/download/%{version}/facile-%{version}.tbz
Source1:	facile.rpmlintrc
Patch1:		10-srcMakefile
BuildRequires:	ocaml
Requires:	ocaml ocaml-compiler-libs

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml.

%prep
%autosetup -p1
# "Pervasives" has been dropped in ocaml 5.0
sed -i -e 's,Pervasives,Stdlib,g' lib/*.ml

%build
cd lib

%ifarch %arm %mips
%make_build OCAMLC="ocamlc -g" OCAMLMLI=ocamlc
%else
%make_build
%endif

%install
mkdir -p %{buildroot}%{_libdir}/ocaml/facile
cp -a lib/facile.{a,cma,cmi,cmxa} lib/*.mli %{buildroot}%{_libdir}/ocaml/facile/

%files
%{_libdir}/ocaml/facile
