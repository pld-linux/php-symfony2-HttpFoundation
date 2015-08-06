%define		package	HttpFoundation
%define		php_min_version 5.3.9
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 HttpFoundation Component
Name:		php-symfony2-HttpFoundation
Version:	2.7.3
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{package}/archive/v%{version}/%{package}-%{version}.tar.gz
# Source0-md5:	03c0e75712f0535f46a8230cfc606715
URL:		http://symfony.com/doc/current/components/http_foundation/index.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php-pear >= 4:1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HttpFoundation Component defines an object-oriented layer for the
HTTP specification.

%prep
%setup -q -n %{package}-%{version}

%build
# add --tolerant, see https://github.com/theseer/Autoload/issues/49
phpab -n -e '*/Tests/*' -o autoloader.php --tolerant .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{package}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/HttpFoundation
%{php_pear_dir}/Symfony/Component/HttpFoundation/*.php
%{php_pear_dir}/Symfony/Component/HttpFoundation/File
%{php_pear_dir}/Symfony/Component/HttpFoundation/Resources
%{php_pear_dir}/Symfony/Component/HttpFoundation/Session
