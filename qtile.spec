Name:               qtile
Version:            0.18.1
Release:            1%{?dist}
BuildArch:          noarch
Summary:            A pure-Python tiling window manager

# libqtile/widget/pacman.py:GPL (v3 or later)
License:            MIT
Url:                http://qtile.org
Source:             https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz

Patch0:             01-use-scm-version-to-false.patch
Patch1:             02-adding-version-manually.patch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-setuptools_scm
BuildRequires:      python3-cffi
BuildRequires:      python3-xcffib
BuildRequires:      python3-cairocffi
BuildRequires:      cairo
BuildRequires:      python3-six
BuildRequires:      python3-pip
BuildRequires:      python3-pycparser
 
Requires:           python3-cairocffi
Requires:           python3-cffi
Requires:           python3-xcffib
Requires:           cairo

%description
A full-featured, hackable tiling window manager written and configured in Python.

Features
========

    * Simple, small and extensible. It's easy to write your own layouts,
      widgets and commands.
    * Configured in Python.
    * Command shell that allows all aspects of
      Qtile to be managed and inspected.
    * Complete remote scriptability - write scripts to set up workspaces,
      manipulate windows, update status bar widgets and more.
    * Qtile's remote scriptability makes it one of the most thoroughly
      unit-tested window mangers around.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
 
%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES
mkdir -p %{buildroot}%{_datadir}/xsessions/
install -m 644 resources/qtile.desktop %{buildroot}%{_datadir}/xsessions/

%files
%license LICENSE
%doc README.rst
%{_bindir}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/libqtile
%{_datadir}/xsessions/%{name}.desktop
  
%changelog

* Sat Nov 27 2021 Jhordy Caceres <jhordycg@fedoraproject.org> - 0.18.1-1
- Update to latest release

* Mon Feb 03 2020 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.14.2-1
- Update to latest release
- Remove buildrequires python-nose-cov
 
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
 
* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)
 
* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.0-4
- Rebuilt for Python 3.8
 
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
 
* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
 
* Thu Jan 17 2019 Mairi Dulaney <jdulaney@fedoraproject.org> - 0.13.0-1
- !!! deprecation warning !!!
-   wmii layout is deprecated in terms of columns layout, which has the
-   same behavior with different defaults, see the wmii definition for
-   more details
- * features
-   add svg handling for images
-   allow addgroup command to set the layout
-   add command to get current log level
-   allow groupbox to hide unused groups
-   add caps lock indicator widget
-   add custom_command to check_update widget
- * bugfixes
-   better shutdown handling
-   fix clientlist current client tracking
-   fix typo in up command on ratiotile layout
-   various fixes to check_update widget
-   fix 0 case for resize screen
 
* Wed Jul 18 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.12.0-1
- !!! Config breakage !!!
-   Tile layout commands up/down/shuffle_up/shuffle_down changed to be
-   more consistent with other layouts
-   move qcmd to qtile-cmd because of conflict with renameutils, move
-   dqcmd to dqtile-cmd for symmetry
- add `add_after_last` option to Tile layout to add windows to the end of the list
- add new formatting options to TaskList
- allow Volume to open app on right click
- fix floating of file transfer windows and java drop-downs
- fix exception when calling `cmd_next` and `cmd_previous` on layout without windows
- fix caps lock affected behaviour of key bindings
- re-create cache dir if it is deleted while qtile is running
- fix CheckUpdates widget color when no updates
- handle cases where BAT_DIR does not exist
- fix the wallpaper widget when using `wallpaper_command`
- fix Tile layout order to not reverse on reset
- fix calling `focus_previous/next` with no windows* Wed Jul 18 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.12.0-1
- !!! Config breakage !!!
-   Tile layout commands up/down/shuffle_up/shuffle_down changed to be
-   more consistent with other layouts
-   move qcmd to qtile-cmd because of conflict with renameutils, move
-   dqcmd to dqtile-cmd for symmetry
- add `add_after_last` option to Tile layout to add windows to the end of the list
- add new formatting options to TaskList
- allow Volume to open app on right click
- fix floating of file transfer windows and java drop-downs
- fix exception when calling `cmd_next` and `cmd_previous` on layout without windows
- fix caps lock affected behaviour of key bindings
- re-create cache dir if it is deleted while qtile is running
- fix CheckUpdates widget color when no updates
- handle cases where BAT_DIR does not exist
- fix the wallpaper widget when using `wallpaper_command`
- fix Tile layout order to not reverse on reset
- fix calling `focus_previous/next` with no windows
 
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
 
* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.11.1-3
- Rebuilt for Python 3.7
- Don't require trollius (only needed on Python < 3.4)
 
* Wed Mar 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.11.1-2
- Add unpackaged files %#{_bindir}/dqcmd %#{_bindir}/qcmd
* Wed Feb 28 2018 John Dulaney <jdulaney@fedoraproject.org> - 0.11.1-1
- !!! Completely changed extension configuration, see the documentation !!!
- !!! `extention` subpackage renamed to `extension` !!!
- !!! `extentions` configuration variable changed to `extension_defaults` !!!
- qshell improvements
- new MonadWide layout
- new Bsp layout
- new pomodoro widget
- new stock ticker widget
- new `client_name_updated` hook
- new RunCommand and J4DmenuDesktop extension
- task list expands to fill space, configurable via `spacing` parameter
- add group.focus_by_name() and group.info_by_name()
- add disk usage ratio to df widget
- allow displayed group name to differ from group name
- enable custom TaskList icon size
- add qcmd and dqcmd to extend functionality around qtile.command functionality
- add ScratchPad group that has configurable drop downs
- fix race condition in Window.fullscreen
- fix for string formatting in qtile_top
- fix unicode literal in tasklist
- move mpris2 initialization out of constructor
- fix wlan widget variable naming and division
- normalize behavior of layouts on various commands
- add better fallback to default config
- update btc widget to use coinbase
- fix cursor warp when using default layout implementation
- don't crash when using widget with unmet dependencies
- fix floating window default location
 
* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
 
* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
 
* Tue Feb 14 2017 John Dulaney <jdulaney@fedoraproject.org> - 0.10.7-1
- new MPD widget, widget.MPD2, based on `mpd2` library
- add option to ignore duplicates in prompt widget
- add additional margin options to GroupBox widget
- add option to ignore mouse wheel to GroupBox widget
- add `watts` formatting string option to Battery widgets
- add volume commands to Volume widget
- add Window.focus command
 
 
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.6-3
- Rebuild for Python 3.6
 
* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages
 
* Wed May 25 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.6-1
- Add `startup_complete` hook
- Restore dynamic groups on restart
- Major bug fixes with floating window handling
 
* Fri Mar 04 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.5-1
- Python 3.2 support dropped !!!
- GoogleCalendar widget dropped for KhalCalendar widget !!!
- qtile-session script removed in favor of qtile script !!!
- new Columns layout, composed of dynamic and configurable columns of windows
- new iPython kernel for qsh, called iqsh, see docs for installing
- new qsh command `display_kb` to show current key binding
- add json interface to IPC server
- add commands for resizing MonadTall main panel
- wlan widget shows when you are disconnected and uses a configurable format
- fix path handling in PromptWidget
- fix KeyboardLayout widget cycling keyboard
- properly guard against setting screen to too large screen index
 
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
 
* Wed Jan 20 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.4-2
- Fix rpmlint issues
 
* Tue Jan 19 2016 John Dulaney <jdulaney@fedoraproject.org> - 0.10.4-1
- New release
 
* Fri Dec 25 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.3-1
- New upstream release
 
* Fri Nov 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-5
- Build against new python-xcffib
 
* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5
 
* Wed Oct 21 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-3
- Fix minor issue with spec file.
 
* Tue Oct 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-2
- /usr/bin/qtile-top to files list
 
* Tue Oct 20 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.2-1
- Update to latest upstream
 
* Mon Oct 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.1-1
- Fix soname issue
 
* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.10.1-0
- Update to latest upstream
 
* Mon Aug 03 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-4
- Use Python3
 
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
 
* Sun Feb 22 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-2
- Final update to licensing
 
* Sat Feb 14 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.1-1
- Update for new upstream release
- Fix license headers.
 
* Sun Feb 01 2015 John Dulaney <jdulaney@fedoraproject.org> - 0.9.0-2
- Update spec for qtile-0.9.0
- Include in Fedora.
 
* Wed Oct 08 2014 John Dulaney <jdulaney@fedoraproject.org> - 0.8.0-1
- Initial packaging
- Spec based on python-nose