%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name capture-stack-trace
#%global commit0 eb46ce326fa9074b6ce17a94d4b76500321a331f
#%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        10%{?dist}
Summary:        Error.captureStackTrace ponyfill

License:        MIT
URL:            https://github.com/floatdrop/capture-stack-trace
Source0:        https://github.com/floatdrop/%{module_name}/archive/v%{version}.tar.gz#/%{module_name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -p package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-10
- Use proper macro in -runtime dependency
- use git tags

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-6
- Rebuilt with updated metapackage

* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-5
- Enable scl macros

* Thu Aug 06 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-2
- fix summary macro

* Fri Jul 31 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
