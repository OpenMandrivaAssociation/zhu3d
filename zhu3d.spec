Summary:	OpenGL-based equation viewer and solver
Name:		zhu3d
Version:	4.2.4
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://kde-apps.org/content/show.php?content=43071
Source0:	http://downloads.sourceforge.net/project/zhu3d/zhu3d/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		zhu3d-4.2.4-paths.patch
Patch1:		zhu3d-4.2.4-mdv-linkage.patch
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
%patch0 -p1
%patch1 -p1
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
rm -f %{buildroot}%{_datadir}/apps/%{name}/work/.directory

%if %{mdvversion} >= 201200
%find_lang %{name} --with-qt
%else
echo > %{name}.lang
%endif

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
%if %{mdvversion} <= 201100
%lang(cs) %{_datadir}/zhu3d/system/languages/zhu3d_cs.qm
%lang(de) %{_datadir}/zhu3d/system/languages/zhu3d_de.qm
%lang(es) %{_datadir}/zhu3d/system/languages/zhu3d_es.qm
%lang(fr) %{_datadir}/zhu3d/system/languages/zhu3d_fr.qm
%lang(zh) %{_datadir}/zhu3d/system/languages/zhu3d_zh.qm
%endif
