Name: facile
Summary: Constraint programming library
Version: 1.1
Release: %mkrel 9
License: GPL
Group: System/Libraries
URL: http://www.recherche.enac.fr/log/facile/
Source0: http://www.recherche.enac.fr/log/facile/distrib/%name-%version.tar.gz
Patch0: facile-1.1-install.patch
Patch1: 10-srcMakefile
Patch2: 20-Makefile
Patch3:	30-non-opt-check
Buildroot:	%_tmppath/%name-%version-%release-root
BuildRequires: ocaml
Requires: ocaml

%description
FaCiLe is a constraint programming library on integer and integer set finite
domains written in OCaml.

%files
%defattr(-,root,root)
%_libdir/ocaml/facile

%prep
%setup -q 
%patch0 -p1
%patch1 -p1 -b .10
%patch2 -p1 -b .20
%patch3 -p1 -b .30

%build
./configure

%ifarch %arm %mips
make OCAMLC="ocamlc -g" OCAMLMLI=ocamlc
%else
make
%endif

%install
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

