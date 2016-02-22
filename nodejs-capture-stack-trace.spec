%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name capture-stack-trace
%global commit0 eb46ce326fa9074b6ce17a94d4b76500321a331f
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        5%{?dist}
Summary:        Error.captureStackTrace ponyfill

License:        MIT
URL:            https://github.com/floatdrop/capture-stack-trace
Source0:        https://github.com/floatdrop/%{module_name}/archive/%{commit0}.tar.gz#/%{module_name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs010-runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{commit0}
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
* Fri Jan 15 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-5
- Enable scl macros

* Thu Aug 06 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-2
- fix summary macro

* Fri Jul 31 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging
