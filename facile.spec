%define	debug_package %{nil}

Summary:	Constraint programming library
Name:		facile
Version:	1.1
Release:	13
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.recherche.enac.fr/log/facile/
Source0:	http://www.recherche.enac.fr/log/facile/distrib/%name-%version.tar.gz
Patch0:		facile-1.1-install.patch
Patch1:		10-srcMakefile
Patch2:		20-Makefile
Patch3:		30-non-opt-check
BuildRequires:	ocaml
Requires:	ocaml

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml.

%prep
%setup -q 
%apply_patches

%build
./configure

%ifarch %arm %mips
%make OCAMLC="ocamlc -g" OCAMLMLI=ocamlc
%else
%make
%endif

%install
%makeinstall_std

%files
%{_libdir}/ocaml/facile

