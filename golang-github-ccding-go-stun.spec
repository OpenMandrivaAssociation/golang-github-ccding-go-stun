# https://github.com/ccding/go-stun
%global goipath github.com/ccding/go-stun
%global commit  be486d185f3dfcb2dbf8429332da50a0da7f95a6

%gometa

Name:           golang-github-ccding-go-stun
Version:        0.1.0
Release:        11%{?dist}
Summary:        STUN client (RFC 3489 and RFC 5389) implementation in Go
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-11
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0.1.0-10
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Aug 31 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-9.20180726gitbe486d1
- Bump to commit be486d1.
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8.20171206.gitd9bbe8f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7.20171206.gitd9bbe8f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-6.20171206.gitd9bbe8f
- Clean up .spec file.

* Sat Dec 09 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-5.git20171206.gitd9bbe8f
- Bump to commit d9bbe8f.

* Fri Nov 10 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-4.git20171107.git82abcd5
- Bump to commit 82abcd5.

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Fabio Valentini <decathorpe@gmail.com> - 0.1.0-1
- Bump version to latest release (no code changes).

* Tue Mar 21 2017 Fabio Valentini <decathorpe@gmail.com> - 0-0.1.20170323.git04a4eed
- First package for Fedora

