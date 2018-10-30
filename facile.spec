%define	debug_package %{nil}

# The ocaml(*) dependency generator seems to be broken
%global __requires_exclude ^ocaml.*$

Summary:	Constraint programming library
Name:		facile
Version:	1.1.3
Release:	4
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.recherche.enac.fr/log/facile/
# Git repository at
#Source0:	https://github.com/Emmanuel-PLF/facile/archive/%{version}.tar.gz
Source0:	http://opti.recherche.enac.fr/facile/distrib/%{name}-%{version}.tar.gz
Source1:	facile.rpmlintrc
Patch0:		facile-1.1-install.patch
Patch1:		10-srcMakefile
Patch2:		20-Makefile
Patch3:		30-non-opt-check
BuildRequires:	ocaml
Requires:	ocaml ocaml-compiler-libs

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml.

%prep
%autosetup -p1

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

