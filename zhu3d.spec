Summary:	OpenGL-based equation viewer and solver
Name:		zhu3d
Version:	4.0.8
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://kde-apps.org/content/show.php?content=43071
Source0:	http://ovh.dl.sourceforge.net/sourceforge/zhu3d/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-3.3.0-path.patch
BuildRequires:	qt4-devel	>= 4.0
BuildRequires:	libmesaglu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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

%build
%qmake_qt4
%make CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" LFLAGS="%{ldflags}"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/apps/%{name}/{work/textures,system/languages}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install work/*.zhu %{buildroot}%{_datadir}/apps/%{name}/work
install work/textures/* %{buildroot}%{_datadir}/apps/%{name}/work/textures
install system/*.zhu %{buildroot}%{_datadir}/apps/%{name}/system
install system/languages/*.qm %{buildroot}%{_datadir}/apps/%{name}/system/languages
install system/icons/%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png

#useless file
rm -f %{buildroot}%{_datadir}/apps/%{name}/work/.directory

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc doc/ readme.txt
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/apps/%{name}
%dir %{_datadir}/apps/%{name}/work
%dir %{_datadir}/apps/%{name}/work/textures
%dir %{_datadir}/apps/%{name}/system
%dir %{_datadir}/apps/%{name}/system/languages
%{_datadir}/apps/%{name}/work/*.zhu
%{_datadir}/apps/%{name}/work/textures/*.jpg
%{_datadir}/apps/%{name}/work/textures/*.txt
%{_datadir}/apps/%{name}/system/*.zhu
%{_iconsdir}/hicolor/64x64/apps/*.png
%{_datadir}/applications/%{name}.desktop
%lang(de) %{_datadir}/apps/%{name}/system/languages/%{name}_de.qm
%lang(es) %{_datadir}/apps/%{name}/system/languages/%{name}_es.qm
%lang(fr) %{_datadir}/apps/%{name}/system/languages/%{name}_fr.qm
%lang(zh) %{_datadir}/apps/%{name}/system/languages/%{name}_zh.qm
