#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
Summary:	E-mail to Newsgroup Bridge
Name:		mail2nntp
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Communications
BuildRequires:	rpm-perlprov >= 4.1-13
Source0:	http://dl.sourceforge.net/mail2nntp/%{name}-%{version}.tar.bz2
# Source0-md5:	74a855669c9ec11a9c531c8a3860f624
URL:		http://freshmeat.net/projects/mail2nntp/
%if %{with autodeps}
BuildRequires:	perl-News-NNTPClient
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mail2nntp is a bridge from email realm to the newsgroup one. It can be
used to replicate a mailing-list on a newsgroup server. It is a
generic toot, using NNTP network commands.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install mail2nntp.pl $RPM_BUILD_ROOT%{_bindir}/mail2nntp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README.txt
%attr(755,root,root) %{_bindir}/mail2nntp
