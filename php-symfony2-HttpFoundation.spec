%define		pearname	HttpFoundation
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 HttpFoundation Component
Name:		php-symfony2-HttpFoundation
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	e62a18fdf1e8d7dc919f6009eebbedad
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
%setup -q -n %{pearname}-%{version}

%build
# add --tolerant, see https://github.com/theseer/Autoload/issues/49
phpab -n -e '*/Tests/*' -o autoloader.php --tolerant .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

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
