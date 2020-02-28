#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : stestr
Version  : 2.6.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/b4/8c/67aec3a38f4653344a49240cd085136a88e095dbad67ebafb540d820700a/stestr-2.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/b4/8c/67aec3a38f4653344a49240cd085136a88e095dbad67ebafb540d820700a/stestr-2.6.0.tar.gz
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
Requires: six
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
BuildRequires : six
BuildRequires : subunit2sql
BuildRequires : testtools
BuildRequires : voluptuous

%description
stestr
======

.. image:: https://img.shields.io/travis/mtreinish/stestr/master.svg?style=flat-square
    :target: https://travis-ci.org/mtreinish/stestr
    :alt: Build status

.. image:: https://dev.azure.com/stestr/stestr/_apis/build/status/mtreinish.stestr?branchName=master
    :target: https://dev.azure.com/stestr/stestr/_build/latest?definitionId=1&branchName=master
    :alt: Azure DevOps build status

.. image:: https://img.shields.io/coveralls/github/mtreinish/stestr/master.svg?style=flat-square
    :target: https://coveralls.io/github/mtreinish/stestr?branch=master
    :alt: Code coverage

.. image:: https://img.shields.io/pypi/v/stestr.svg?style=flat-square
    :target: https://pypi.python.org/pypi/stestr
    :alt: Latest Version

* Read this in other languages: `English`_, `日本語`_
* You can see the full rendered docs at: http://stestr.readthedocs.io/en/latest/
* The code of the project is on Github: https://github.com/mtreinish/stestr

.. _English: https://github.com/mtreinish/stestr/blob/master/README.rst
.. _日本語: https://github.com/mtreinish/stestr/blob/master/README_ja.rst

.. note:: stestr v2.x.x release series will be the last series that supports
    Python 2. Support for Python 2.7 will be dropped in stestr release 3.0.0
    which is being planned for early 2020.

Overview
--------

stestr is parallel Python test runner designed to execute `unittest`_ test
suites using multiple processes to split up execution of a test suite. It also
will store a history of all test runs to help in debugging failures and
optimizing the scheduler to improve speed. To accomplish this goal it uses the
`subunit`_ protocol to facilitate streaming and storing results from multiple
workers.

.. _unittest: https://docs.python.org/3/library/unittest.html
.. _subunit: https://github.com/testing-cabal/subunit

stestr originally started as a fork of the `testrepository`_ project. But,
instead of being an interface for any test runner that used subunit, like
testrepository, stestr concentrated on being a dedicated test runner for python
projects. While stestr was originally forked from testrepository it is not
backwards compatible with testrepository. At a high level the basic concepts of
operation are shared between the two projects but the actual usage is not
exactly the same.

.. _testrepository: https://testrepository.readthedocs.org/en/latest


Installing stestr
-----------------

stestr is available via pypi, so all you need to do is run::

  pip install -U stestr

to get stestr on your system. If you need to use a development version of
stestr you can clone the repo and install it locally with::

  git clone https://github.com/mtreinish/stestr.git && pip install -e stestr

which will install stestr in your python environment in editable mode for local
development

Using stestr
------------

After you install stestr to use it to run tests is pretty straightforward. The
first thing you'll want to do is create a ``.stestr.conf`` file for your
project. This file is used to tell stestr where to find tests and basic
information about how tests are run. A basic minimal example of the
contents of this is::

  [DEFAULT]
  test_path=./project_source_dir/tests

which just tells stestr the relative path for the directory to use for
test discovery. This is the same as ``--start-directory`` in the standard
`unittest discovery`_.

.. _unittest discovery: https://docs.python.org/3/library/unittest.html#test-discovery

After this file is created you should be all set to start using stestr to run
tests. To run tests just use::

    stestr run

it will first create a results repository at ``.stestr/`` in the current
working directory and then execute all the tests found by test discovery. If
you're just running a single test (or module) and want to avoid the overhead of
doing test discovery you can use the ``--no-discover``/``-n`` option to specify
that test.

For all the details on these commands and more thorough explanation of options
see the stestr manual: https://stestr.readthedocs.io/en/latest/MANUAL.html

Migrating from testrepository
-----------------------------

If you have a project that is already using testrepository stestr's source repo
contains a helper script for migrating your repo to use stestr. This script
just creates a ``.stestr.conf`` file from a ``.testr.conf`` file.
(assuming it uses a standard subunit.run test command format) To run
this from your project repo just call::

    $STESTR_SOURCE_DIR/tools/testr_to_stestr.py

and you'll have a ``.stestr.conf`` created.

Building a manpage
------------------

The stestr manual has been formatted so that it renders well as html and as a
manpage. The html output and is autogenerated and published to:
https://stestr.readthedocs.io/en/latest/MANUAL.html but the manpage has to be
generated by hand. To do this you have to manually run sphinx-build with the
manpage builder. This has been automated in a small script that should be run
from the root of the stestr repository::

  tools/build_manpage.sh

which will generate the troff file in doc/build/man/stestr.1 which is ready to
be packaged and or put in your system's man pages.

Contributing
------------

To browse the latest code, see: https://github.com/mtreinish/stestr
To clone the latest code, use: ``git clone https://github.com/mtreinish/stestr.git``

Guidelines for contribution are documented at: http://stestr.readthedocs.io/en/latest/developer_guidelines.html

Use `github pull requests`_ to submit patches. Before you submit a pull request
ensure that all the automated testing will pass by running ``tox`` locally.
This will run the test suite and also the automated style rule checks just as
they will in CI. If CI fails on your change it will not be able to merge.

.. _github pull requests: https://help.github.com/articles/about-pull-requests/

Community
---------

Besides Github interactions there is also a stestr IRC channel:

#stestr on Freenode

feel free to join to ask questions, or just discuss stestr.

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

%description python3
python3 components for the stestr package.


%prep
%setup -q -n stestr-2.6.0
cd %{_builddir}/stestr-2.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582915335
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
cp %{_builddir}/stestr-2.6.0/LICENSE %{buildroot}/usr/share/package-licenses/stestr/294b43b2cec9919063be1a3b49e8722648424779
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
