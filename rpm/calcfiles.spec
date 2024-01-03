Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/tortikplus/Repository1
Source0:       https://github.com/tortikplus/Repository1/archive/main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
%setup -q -n Repository1-main

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Wed Jan 03 2024 tortikplus <usenock2018@gmail.com> - 1.0-1
- Initial build
