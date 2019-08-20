#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jacoco
Version  : 0.7.5
Release  : 1
URL      : https://github.com/jacoco/jacoco/archive/v0.7.5.tar.gz
Source0  : https://github.com/jacoco/jacoco/archive/v0.7.5.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.jar
Source2  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.pom
Source3  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.jar
Source4  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.pom
Source5  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.build/0.7.5.201505241946/org.jacoco.build-0.7.5.201505241946.pom
Source6  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.jar
Source7  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.pom
Source8  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.jar
Source9  : https://repo.maven.apache.org/maven2/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 EPL-1.0
Requires: mvn-jacoco-data = %{version}-%{release}
Requires: mvn-jacoco-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : buildreq-mvn

%description
JaCoCo Java Code Coverage Library
=================================
[![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.jacoco/org.jacoco.core/badge.svg?style=flat)](http://search.maven.org/#search|ga|1|g%3Aorg.jacoco)

%package data
Summary: data components for the mvn-jacoco package.
Group: Data

%description data
data components for the mvn-jacoco package.


%package license
Summary: license components for the mvn-jacoco package.
Group: Default

%description license
license components for the mvn-jacoco package.


%prep
%setup -q -n jacoco-0.7.5

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jacoco
cp LICENSE.md %{buildroot}/usr/share/package-licenses/mvn-jacoco/LICENSE.md
cp org.jacoco.doc/docroot/doc/license.html %{buildroot}/usr/share/package-licenses/mvn-jacoco/org.jacoco.doc_docroot_doc_license.html
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.build/0.7.5.201505241946
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.build/0.7.5.201505241946/org.jacoco.build-0.7.5.201505241946.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946
cp %{SOURCE9} %{buildroot}/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.jar
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.agent/0.7.5.201505241946/org.jacoco.agent-0.7.5.201505241946.pom
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.jar
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.ant/0.7.5.201505241946/org.jacoco.ant-0.7.5.201505241946.pom
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.build/0.7.5.201505241946/org.jacoco.build-0.7.5.201505241946.pom
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.jar
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.core/0.7.5.201505241946/org.jacoco.core-0.7.5.201505241946.pom
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.jar
/usr/share/java/.m2/repository/org/jacoco/org.jacoco.report/0.7.5.201505241946/org.jacoco.report-0.7.5.201505241946.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jacoco/LICENSE.md
/usr/share/package-licenses/mvn-jacoco/org.jacoco.doc_docroot_doc_license.html
