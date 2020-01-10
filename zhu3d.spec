Summary:	OpenGL-based equation viewer and solver
Name:		zhu3d
Version:	4.2.4
Release:	3
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://kde-apps.org/content/show.php?content=43071
Source0:	http://switch.dl.sourceforge.net/project/zhu3d/zhu3d/zhu3d-%version.tar.gz
Source1:	%{name}.desktop
Patch0:		zhu3d-4.2.4-paths.patch
Patch1:		zhu3d-4.2.4-mdv-linkage.patch
Patch2:		zhu3d-4.2.4-compile.patch
BuildRequires:	qt4-devel
BuildRequires:	mesaglu-devel
BuildRequires:	dos2unix

%description
With Zhu3D you interactively can view and animate functions,
isosurfaces and a further independent parametric system. 
Numerical solutions of equation systems can be found with 
a precise and reliable adaptive random search. The 
OpenGL-viewer supports zooming, scaling, rotating and
translating as well as filed lightning or surface properties. 
Special effects are transparency, textures, fog and motion blur.

%prep
%setup -q
%autopatch -p1
dos2unix readme.txt

%build
# setup compile flags is needed so that -fPIC and -DPIC will be overwritten
%setup_compile_flags
%qmake_qt4
%make

%install
mkdir -p %{buildroot}%{_datadir}/%{name}/{work/textures,system/languages}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install work/*.zhu %{buildroot}%{_datadir}/%{name}/work
install work/textures/* %{buildroot}%{_datadir}/%{name}/work/textures
install system/*.zhu %{buildroot}%{_datadir}/%{name}/system
install system/languages/*.qm %{buildroot}%{_datadir}/%{name}/system/languages
install system/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

#useless file
#rm -f %{buildroot}%{_datadir}/apps/%{name}/work/.directory

%find_lang %{name} --with-qt

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc doc/ readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/work
%dir %{_datadir}/%{name}/work/textures
%dir %{_datadir}/%{name}/system
%dir %{_datadir}/%{name}/system/languages
%{_datadir}/%{name}/work/*.zhu
%{_datadir}/%{name}/work/textures/*.jpg
%{_datadir}/%{name}/work/textures/*.txt
%{_datadir}/%{name}/system/*.zhu
%{_iconsdir}/hicolor/64x64/apps/*.png
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Dec  4 2012 Bernhard Rosenkraenzer <bero@bero.eu> 4.2.4-2
- Fix build in current environment

* Thu Mar 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 4.2.4-1mdv2012.0
+ Revision: 781620
- new version 4.2.4

* Wed Jun 03 2009 Funda Wang <fwang@mandriva.org> 4.2.2-1mdv2010.0
+ Revision: 382342
- New version 4.2.2
- use setup_compile_flags to export FLAGS, in order that Qt4 implies -fPIC -DPIC

* Tue Jan 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 4.1.8-1mdv2009.1
+ Revision: 325176
- remove DPIC and fPIC from compile flags

  + Funda Wang <fwang@mandriva.org>
    - New version 4.1.8
    - rediff path patch
    - New version 4.1.2
    - no needed to use flags as it is exported by qmake macro

* Sun Jul 27 2008 Funda Wang <fwang@mandriva.org> 4.1.0-1mdv2009.0
+ Revision: 250483
- New version 4.1.0

* Mon Jul 21 2008 Funda Wang <fwang@mandriva.org> 4.0.8-1mdv2009.0
+ Revision: 239506
- New version 4.0.8
- drop unneeded gcc 4.3 patch

* Sat Jun 28 2008 Funda Wang <fwang@mandriva.org> 4.0.6-1mdv2009.0
+ Revision: 229756
- add gcc43 patch from arklinux
- use correct optflags
- New version 4.0.6

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Apr 12 2008 Funda Wang <fwang@mandriva.org> 4.0.4-1mdv2009.0
+ Revision: 192602
- New version 4.0.4

* Tue Mar 11 2008 Funda Wang <fwang@mandriva.org> 4.0.0-1mdv2008.1
+ Revision: 185931
- Updated to new version 4.0.0

* Sun Mar 09 2008 Funda Wang <fwang@mandriva.org> 3.4.8-1mdv2008.1
+ Revision: 182805
- New version 3.4.8

* Sat Mar 08 2008 Funda Wang <fwang@mandriva.org> 3.4.6-1mdv2008.1
+ Revision: 182052
- update to new version 3.4.6

* Sun Feb 24 2008 Funda Wang <fwang@mandriva.org> 3.4.4-1mdv2008.1
+ Revision: 174227
- New version 3.4.4

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 3.4.2-1mdv2008.1
+ Revision: 158672
- New version 3.4.2

* Tue Jan 08 2008 Funda Wang <fwang@mandriva.org> 3.4.0-1mdv2008.1
+ Revision: 146569
- update to new version 3.4.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.3.6-1mdv2008.1
+ Revision: 133092
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Funda Wang <fwang@mandriva.org> 3.3.4-1mdv2008.1
+ Revision: 119081
- New version 3.3.4

* Fri Dec 07 2007 Funda Wang <fwang@mandriva.org> 3.3.2-1mdv2008.1
+ Revision: 116309
- update to new version 3.3.2

* Mon Dec 03 2007 Funda Wang <fwang@mandriva.org> 3.3.0-1mdv2008.1
+ Revision: 114556
- New version 3.3.0
- rediff patch0

* Sat Dec 01 2007 Funda Wang <fwang@mandriva.org> 3.2.9-3mdv2008.1
+ Revision: 114248
- remove quotes in desktop file

* Fri Nov 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.9-2mdv2008.1
+ Revision: 114035
- fix patch 0 :|

* Fri Nov 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.2.9-1mdv2008.1
+ Revision: 113997
- rewrite patch 0
- new version

* Mon Nov 26 2007 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2008.1
+ Revision: 112079
- New version 3.2.0

* Fri Nov 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.8-1mdv2008.1
+ Revision: 111372
- new version

* Mon Nov 19 2007 Funda Wang <fwang@mandriva.org> 3.1.6-1mdv2008.1
+ Revision: 110399
- drop kdelibs BR
- New version 3.1.6

* Thu Nov 15 2007 Funda Wang <fwang@mandriva.org> 3.1.4-1mdv2008.1
+ Revision: 108889
- New version 3.1.4

* Mon Nov 05 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.2-2mdv2008.1
+ Revision: 106221
- fix typo in desktop file

* Sun Nov 04 2007 Funda Wang <fwang@mandriva.org> 3.1.2-1mdv2008.1
+ Revision: 105741
- New version 3.1.2

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.0-2mdv2008.1
+ Revision: 102410
- better desktop file
- new license policy

* Fri Oct 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.1.0-1mdv2008.1
+ Revision: 102326
- new version

* Tue Oct 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.9-1mdv2008.1
+ Revision: 101371
- new version

* Tue Oct 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.6-1mdv2008.1
+ Revision: 98767
- new version

* Sun Sep 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.4-1mdv2008.0
+ Revision: 93933
- new version
- new version

* Fri Aug 10 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 3.0.0-1mdv2008.0
+ Revision: 61051
- new version

* Thu Jul 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.8-1mdv2008.0
+ Revision: 53663
- new version
- drop X-MandrivaLinux from desktop file

* Mon May 28 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.6-2mdv2008.0
+ Revision: 32015
- rebuild


* Tue Feb 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.6-1mdv2007.0
+ Revision: 123170
- new version
- some cleans in spec file

* Tue Jan 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.9.4-1mdv2007.1
+ Revision: 112454
- provide desktop file
- add patch 0
- complete spec file
- Import zhu3d

