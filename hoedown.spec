Summary:	Standards compliant, fast, secure markdown processing library in C
Summary(pl.UTF-8):	Zgodna ze standardami, szybka, bezpieczna biblioteka do preztwarzania formatu markdown z poziomu C
Name:		hoedown
Version:	3.0.7
Release:	1
License:	ISC
Group:		Applications/Text
#Source0Download: https://github.com/hoedown/hoedown/tags
Source0:	https://github.com/hoedown/hoedown/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	dc0a6b4a3553db6cd9aa1ad53b880f81
URL:		https://github.com/hoedown/hoedown
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hoedown is a revived fork of Sundown
(<https://github.com/vmg/sundown>), the Markdown parser based on the
original code of the Upskirt library
(<http://fossil.instinctive.eu/libupskirt/index>) by Natacha Porte.

%description -l pl.UTF-8
Hoedown to odrodzone odgałęzienie Sundown
(<https://github.com/vmg/sundown>) - parsera Markdown opartego na
oryginalnym kodzie biblioteki Upskirt
(<http://fossil.instinctive.eu/libupskirt/index>) autorstwa Natachy
Porté.

%package devel
Summary:	Header file for hoedown library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki hoedown
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header file for hoedown library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki hoedown.

%package static
Summary:	Static hoedown library
Summary(pl.UTF-8):	Statyczna biblioteka hoedown
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static hoedown library.

%description static -l pl.UTF-8
Statyczna biblioteka hoedown.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -ansi -pedantic -Wall -Wextra -Wno-unused-parameter" \
	LDFLAGS="%{rpmldflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_bindir}/hoedown
%attr(755,root,root) %{_bindir}/smartypants
%attr(755,root,root) %{_libdir}/libhoedown.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhoedown.so
%{_includedir}/hoedown

%files static
%defattr(644,root,root,755)
%{_libdir}/libhoedown.a
