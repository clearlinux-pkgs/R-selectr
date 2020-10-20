#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-selectr
Version  : 0.4.2
Release  : 30
URL      : https://cran.r-project.org/src/contrib/selectr_0.4-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/selectr_0.4-2.tar.gz
Summary  : Translate CSS Selectors to XPath Expressions
Group    : Development/Tools
License  : BSD-3-Clause
Requires: R-R6
Requires: R-stringr
BuildRequires : R-R6
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
expression. This allows us to use CSS selectors when working with
  the XML package as it can only evaluate XPath expressions. Also
  provided are convenience functions useful for using CSS selectors on
  XML nodes. This package is a port of the Python package 'cssselect'

%prep
%setup -q -c -n selectr
cd %{_builddir}/selectr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589585189

%install
export SOURCE_DATE_EPOCH=1589585189
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc selectr || :


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
/usr/lib64/R/library/selectr/tests/test-all.R
/usr/lib64/R/library/selectr/tests/testthat/test-main.R
/usr/lib64/R/library/selectr/tests/testthat/test-method-registration.R
/usr/lib64/R/library/selectr/tests/testthat/test-parse-errors.R
/usr/lib64/R/library/selectr/tests/testthat/test-parser.R
/usr/lib64/R/library/selectr/tests/testthat/test-pseudo.R
/usr/lib64/R/library/selectr/tests/testthat/test-querySelector-XML.R
/usr/lib64/R/library/selectr/tests/testthat/test-querySelector-default.R
/usr/lib64/R/library/selectr/tests/testthat/test-querySelector-xml2.R
/usr/lib64/R/library/selectr/tests/testthat/test-quoting.R
/usr/lib64/R/library/selectr/tests/testthat/test-select-XML.R
/usr/lib64/R/library/selectr/tests/testthat/test-select-xml2.R
/usr/lib64/R/library/selectr/tests/testthat/test-series.R
/usr/lib64/R/library/selectr/tests/testthat/test-shakespeare-XML.R
/usr/lib64/R/library/selectr/tests/testthat/test-shakespeare-xml2.R
/usr/lib64/R/library/selectr/tests/testthat/test-specificity.R
/usr/lib64/R/library/selectr/tests/testthat/test-tokenizer.R
/usr/lib64/R/library/selectr/tests/testthat/test-translation.R
/usr/lib64/R/library/selectr/tests/testthat/test-xmllang-XML.R
/usr/lib64/R/library/selectr/tests/testthat/test-xmllang-xml2.R
/usr/lib64/R/library/selectr/tests/testthat/test-xpath.R
