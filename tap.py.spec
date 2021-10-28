#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tap.py
Version  : 3.0
Release  : 13
URL      : https://files.pythonhosted.org/packages/3e/56/a3d6bd61d8238e78f8b48295a1bc69c30a5c21a8bb5b1ebd685ce3cffef0/tap.py-3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/56/a3d6bd61d8238e78f8b48295a1bc69c30a5c21a8bb5b1ebd685ce3cffef0/tap.py-3.0.tar.gz
Summary  : Test Anything Protocol (TAP) tools
Group    : Development/Tools
License  : BSD-2-Clause
Requires: tap.py-bin = %{version}-%{release}
Requires: tap.py-license = %{version}-%{release}
Requires: tap.py-python = %{version}-%{release}
Requires: tap.py-python3 = %{version}-%{release}
Requires: PyYAML
Requires: more-itertools
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : more-itertools

%description
tappy is a set of tools for working with the `Test Anything Protocol (TAP)

%package bin
Summary: bin components for the tap.py package.
Group: Binaries
Requires: tap.py-license = %{version}-%{release}

%description bin
bin components for the tap.py package.


%package license
Summary: license components for the tap.py package.
Group: Default

%description license
license components for the tap.py package.


%package python
Summary: python components for the tap.py package.
Group: Default
Requires: tap.py-python3 = %{version}-%{release}

%description python
python components for the tap.py package.


%package python3
Summary: python3 components for the tap.py package.
Group: Default
Requires: python3-core
Provides: pypi(tap.py)

%description python3
python3 components for the tap.py package.


%prep
%setup -q -n tap.py-3.0
cd %{_builddir}/tap.py-3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603405462
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tap.py
cp %{_builddir}/tap.py-3.0/LICENSE %{buildroot}/usr/share/package-licenses/tap.py/d0693ae3fe545a42770e2e03087f9ebdde726bb4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tap
/usr/bin/tappy

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tap.py/d0693ae3fe545a42770e2e03087f9ebdde726bb4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
