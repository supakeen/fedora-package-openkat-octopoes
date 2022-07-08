Name:           openkat-octopoes
Version:        main
Release:        1%{?dist}
Summary:        The OpenKAT system knowledge-graph

License:        EUPL 1.2
URL:            https://openkat.nl
Source0:        https://github.com/minvws/nl-kat-octopoes/archive/refs/heads/main.zip

BuildArch:      noarch
BuildRequires:  python3-devel

Requires:       rabbitmq

%global _description %{expand:
openkat-octopoes is responsible for storing OpenKAT knowledge
}

%description %_description

%prep
%autosetup -p1 -n nl-kat-octopoes-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files scheduler

%check
%pyproject_check_import
# no pytest yet, it fails

%files -n openkat-octopoes -f %{pyproject_files}
/usr/bin/openkat-octopoes

%doc README.md
%license LICENSE

%changelog
* Wed Jul 6 2022 supakeen <cmdr@supakeen.com>
- Initial version of the package.
