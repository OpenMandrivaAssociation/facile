Name:		facile
Summary:	Constraint programming library
Version:	1.1
Release:	12
License:	GPL
Group:		System/Libraries
URL:		http://www.recherche.enac.fr/log/facile/
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

%files
%{_libdir}/ocaml/facile

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
%makeinstall_std

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-10mdv2011.0
+ Revision: 664243
- mass rebuild

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-9mdv2011.0
+ Revision: 496468
- Rebuild

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 1.1-8mdv2010.0
+ Revision: 448917
- fix build on platforms withoyt ocaml*opt*, by merging patches from
  debian to get it building on arm & mips
  (from Arnaud Patard)

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-7mdv2010.0
+ Revision: 389532
- Rebuild against new ocaml

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-6mdv2009.1
+ Revision: 313362
- Rebuild against new OCAML

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1-5mdv2009.0
+ Revision: 220741
- rebuild

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.1-4mdv2008.1
+ Revision: 182267
- Rebuild against new ocaml

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2008.1
+ Revision: 170826
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2008.1
+ Revision: 149712
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Helio Chissini de Castro <helio@mandriva.com> 1.1-1mdv2008.0
+ Revision: 48648
- First release

