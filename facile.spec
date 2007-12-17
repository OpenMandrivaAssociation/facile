Name: facile
Summary: FaCiLe is a constraint programming library
Version: 1.1
Release: %mkrel 1
License: GPL
Group: System/Libraries
URL: http://www.recherche.enac.fr/log/facile/
Source0: http://www.recherche.enac.fr/log/facile/distrib/%name-%version.tar.gz
Patch0: facile-1.1-install.patch
BuildRequires: ocaml
Requires: ocaml

%description
FaCiLe is a constraint programming library on integer and integer set finite domains written in OCaml.

%files
%defattr(-,root,root)
%_libdir/ocaml/facile

%prep
%setup -q 
%patch0 -p1

%build
./configure

make

%install
make DESTDIR=%buildroot install

%clean
rm -rf %buildroot

