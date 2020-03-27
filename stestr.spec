#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stestr
Version  : 3.0.0
Release  : 15
URL      : https://files.pythonhosted.org/packages/95/b9/79ad4add8860d2091942b6772d2584cf0e25578f98d7c84a4cfbd456da12/stestr-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/95/b9/79ad4add8860d2091942b6772d2584cf0e25578f98d7c84a4cfbd456da12/stestr-3.0.0.tar.gz
Summary  : A parallel Python test runner built around subunit
Group    : Development/Tools
License  : Apache-2.0
Requires: stestr-bin = %{version}-%{release}
Requires: stestr-license = %{version}-%{release}
Requires: stestr-python = %{version}-%{release}
Requires: stestr-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cliff
Requires: fixtures
Requires: pbr
Requires: python-future
Requires: python-subunit
Requires: subunit2sql
Requires: testtools
Requires: voluptuous
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cliff
BuildRequires : fixtures
BuildRequires : pbr
BuildRequires : python-future
BuildRequires : python-subunit
BuildRequires : subunit2sql
BuildRequires : testtools
BuildRequires : voluptuous

%description
stestr
======
.. image:: https://img.shields.io/travis/mtreinish/stestr/master.svg?style=flat-square
:target: https://travis-ci.org/mtreinish/stestr
:alt: Build status

%package bin
Summary: bin components for the stestr package.
Group: Binaries
Requires: stestr-license = %{version}-%{release}

%description bin
bin components for the stestr package.


%package license
Summary: license components for the stestr package.
Group: Default

%description license
license components for the stestr package.


%package python
Summary: python components for the stestr package.
Group: Default
Requires: stestr-python3 = %{version}-%{release}

%description python
python components for the stestr package.


%package python3
Summary: python3 components for the stestr package.
Group: Default
Requires: python3-core
Provides: pypi(stestr)
Requires: pypi(cliff)
Requires: pypi(fixtures)
Requires: pypi(future)
Requires: pypi(pbr)
Requires: pypi(python_subunit)
Requires: pypi(pyyaml)
Requires: pypi(testtools)
Requires: pypi(voluptuous)

%description python3
python3 components for the stestr package.


%prep
%setup -q -n stestr-3.0.0
cd %{_builddir}/stestr-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585269360
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/stestr
cp %{_builddir}/stestr-3.0.0/LICENSE %{buildroot}/usr/share/package-licenses/stestr/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/stestr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/stestr/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
