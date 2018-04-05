#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-selectr
Version  : 0.4.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/selectr_0.4-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/selectr_0.4-0.tar.gz
Summary  : Translate CSS Selectors to XPath Expressions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-XML
Requires: R-stringi
Requires: R-xml2
BuildRequires : R-XML
BuildRequires : R-stringi
BuildRequires : R-xml2
BuildRequires : clr-R-helpers

%description
expression. This allows us to use CSS selectors when working with
  the XML package as it can only evaluate XPath expressions. Also
  provided are convenience functions useful for using CSS selectors on
  XML nodes. This package is a port of the Python package 'cssselect'

%prep
%setup -q -c -n selectr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1522244541

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1522244541
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library selectr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library selectr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library selectr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library selectr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/selectr/CITATION
/usr/lib64/R/library/selectr/DESCRIPTION
/usr/lib64/R/library/selectr/INDEX
/usr/lib64/R/library/selectr/LICENCE
/usr/lib64/R/library/selectr/Meta/Rd.rds
/usr/lib64/R/library/selectr/Meta/features.rds
/usr/lib64/R/library/selectr/Meta/hsearch.rds
/usr/lib64/R/library/selectr/Meta/links.rds
/usr/lib64/R/library/selectr/Meta/nsInfo.rds
/usr/lib64/R/library/selectr/Meta/package.rds
/usr/lib64/R/library/selectr/NAMESPACE
/usr/lib64/R/library/selectr/NEWS.Rd
/usr/lib64/R/library/selectr/R/selectr
/usr/lib64/R/library/selectr/R/selectr.rdb
/usr/lib64/R/library/selectr/R/selectr.rdx
/usr/lib64/R/library/selectr/demos/svg-mathml.svg
/usr/lib64/R/library/selectr/help/AnIndex
/usr/lib64/R/library/selectr/help/aliases.rds
/usr/lib64/R/library/selectr/help/paths.rds
/usr/lib64/R/library/selectr/help/selectr.rdb
/usr/lib64/R/library/selectr/help/selectr.rdx
/usr/lib64/R/library/selectr/html/00Index.html
/usr/lib64/R/library/selectr/html/R.css
