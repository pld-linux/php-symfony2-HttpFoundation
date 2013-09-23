%define		pearname	HttpFoundation
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 HttpFoundation Component
Name:		php-symfony2-HttpFoundation
Version:	2.3.4
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.symfony.com/get/%{pearname}-%{version}.tgz
# Source0-md5:	10045fb5fc110f3ccc6ede4d99c6fe74
URL:		http://symfony.com/doc/current/components/http_foundation/index.html
BuildRequires:	php-channel(pear.symfony.com)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-channel(pear.symfony.com)
Requires:	php-pear >= 4:1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HttpFoundation Component defines an object-oriented layer for the
HTTP specification.

%prep
%pear_package_setup

# no packaging of tests
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/Tests .
mv .%{php_pear_dir}/Symfony/Component/%{pearname}/phpunit.xml.dist .

# fixups
mv docs/%{pearname}/Symfony/Component/%{pearname}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/Symfony/Component/HttpFoundation
%{php_pear_dir}/Symfony/Component/HttpFoundation/*.php
%{php_pear_dir}/Symfony/Component/HttpFoundation/File
%{php_pear_dir}/Symfony/Component/HttpFoundation/Resources
%{php_pear_dir}/Symfony/Component/HttpFoundation/Session
