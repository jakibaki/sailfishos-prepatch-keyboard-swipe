Name:       prepatch-keyboard-swipe

BuildArch: noarch

Summary:    A prepatch-patch which allows you to move the cursor by swiping on the keyboard
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    Other
Source0:    %{name}-%{version}.tar.bz2
Requires:   patch

%description
A prepatch-patch which allows you to move the cursor by swiping on the keyboard

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/prepatch
cp -r 050-prepatch-keyboard-swipe %{buildroot}/usr/share/prepatch

%pre

%preun

%files
%defattr(-,root,root,-)
%{_datadir}/prepatch/050-prepatch-keyboard-swipe
