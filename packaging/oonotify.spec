Name:           oonotify
Version:        0.1.0
Release:        1%{?dist}
Summary:        Sends Freedesktop desktop notifications over D-Bus with custom icons and urgency.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oonotify
Source0:        oonotify-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oonotify is a sovereign, capability-bounded DESKTOP NOTIFIER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oonotify
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oonotify-uninstall

%files
/usr/bin/oonotify
/usr/bin/oonotify-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
