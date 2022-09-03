#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbapply
Version  : 1.5.0
Release  : 47
URL      : https://cran.r-project.org/src/contrib/pbapply_1.5-0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbapply_1.5-0.tar.gz
Summary  : Adding Progress Bar to '*apply' Functions
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
progress bar to vectorized R functions
  ('*apply'). The implementation can easily be added
  to functions where showing the progress is
  useful (e.g. bootstrap). The type and style of the
  progress bar (with percentages or remaining time)
  can be set through options.
  Supports several parallel processing backends.

%prep
%setup -q -c -n pbapply
cd %{_builddir}/pbapply

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641071127

%install
export SOURCE_DATE_EPOCH=1641071127
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbapply
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbapply
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbapply
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pbapply || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbapply/DESCRIPTION
/usr/lib64/R/library/pbapply/INDEX
/usr/lib64/R/library/pbapply/Meta/Rd.rds
/usr/lib64/R/library/pbapply/Meta/features.rds
/usr/lib64/R/library/pbapply/Meta/hsearch.rds
/usr/lib64/R/library/pbapply/Meta/links.rds
/usr/lib64/R/library/pbapply/Meta/nsInfo.rds
/usr/lib64/R/library/pbapply/Meta/package.rds
/usr/lib64/R/library/pbapply/NAMESPACE
/usr/lib64/R/library/pbapply/R/pbapply
/usr/lib64/R/library/pbapply/R/pbapply.rdb
/usr/lib64/R/library/pbapply/R/pbapply.rdx
/usr/lib64/R/library/pbapply/help/AnIndex
/usr/lib64/R/library/pbapply/help/aliases.rds
/usr/lib64/R/library/pbapply/help/paths.rds
/usr/lib64/R/library/pbapply/help/pbapply.rdb
/usr/lib64/R/library/pbapply/help/pbapply.rdx
/usr/lib64/R/library/pbapply/html/00Index.html
/usr/lib64/R/library/pbapply/html/R.css
/usr/lib64/R/library/pbapply/tests/tests.R
