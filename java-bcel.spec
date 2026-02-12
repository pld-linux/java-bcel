#
# Conditional build:
%bcond_without	javadoc		# don't build javadoc

%define		srcname		bcel
Summary:	Byte Code Engineering Library
Summary(pl.UTF-8):	Biblioteka do obróbki bajtkodu Javy
Name:		java-bcel
Version:	5.2
Release:	4
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/jakarta/bcel/source/%{srcname}-%{version}-src.tar.gz
# Source0-md5:	905b7e718e30e7ca726530ecf106e532
Patch0:		jakarta-%{srcname}-manifest.patch
Patch1:		%{name}-noproxy.patch
URL:		http://jakarta.apache.org/bcel/
BuildRequires:	ant
BuildRequires:	java-regexp >= 1.2
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
Requires:	java-regexp >= 1.2
Obsoletes:	jakarta-bcel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create,
and manipulate (binary) Java class files (those ending with .class).
Classes are represented by objects which contain all the symbolic
information of the given class: methods, fields and byte code
instructions, in particular. Such objects can be read from an existing
file, be transformed by a program (e.g. a class loader at run-time)
and dumped to a file again. An even more interesting application is
the creation of classes from scratch at run-time. The Byte Code
Engineering Library (BCEL) may be also useful if you want to learn
about the Java Virtual Machine (JVM) and the format of Java .class
files. BCEL is already being used successfully in several projects
such as compilers, optimizers, obsfuscators and analysis tools, the
most popular probably being the Xalan XSLT processor at Apache.

%description -l pl.UTF-8
BCEL (Byte Code Engineering Library, poprzednio znana jako JavaClass)
ma umożliwić wygodne analizowanie, tworzenie i obróbkę (binarnych)
plików klas Javy (tych z nazwą kończącą się na .class). Klasy są
reprezentowane przez obiekty zawierające wszystkie symboliczne
informacje o danej klasie, w szczególności metody, pola i instrukcje
bajtkodu. Obiekty te mogą być odczytywane z istniejącego pliku,
przekształcane przez program (np. wczytujący klasy w czasie działania)
i zrzucane z powrotem do pliku. Jeszcze ciekawszym zastosowaniem jest
tworzenie klas od zera w czasie działania programu. Biblioteka BCEL
może być także użyteczna, jeśli chcemy nauczyć się czegoś o maszynie
wirtualnej Javy (JVM) oraz formacie plików .class. BCEL jest używana z
sukcesem w różnych projektach, takich jak kompilatory, optymalizatory,
narzędzia utrudniające analizę oraz narzędzia do analizy, z których
najpopularniejszym jest procesor XSLT Xalan.

%package javadoc
Summary:	Byte Code Engineering Library documentation
Summary(pl.UTF-8):	Dokumentacja do biblioteki do obróbki bajtkodu Javy
Group:		Documentation
Requires:	jpackage-utils
Obsoletes:	jakarta-bcel-doc
Obsoletes:	jakarta-bcel-javadoc

%description javadoc
Byte Code Engineering Library documentation.

%description javadoc -l pl.UTF-8
Dokumentacja do biblioteki do obróbki bajtkodu Javy.

%prep
%setup -q -n bcel-%{version}
%patch -P0 -p1
%patch -P1 -p1
find -name '*.jar' | xargs rm -f

%build
CLASSPATH="$(build-classpath regexp)"
export JAVA_HOME="%{java_home}"
export LC_ALL=en_US

%ant jar %{?with_javadoc:javadoc} \
	-Dnoget=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

cp -p target/%{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -sf %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

%if %{with javadoc}
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
cp -R dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{srcname}-%{version}
ln -s %{srcname}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{srcname} # ghost symlink
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{srcname}-%{version} %{_javadocdir}/%{srcname}

%files
%defattr(644,root,root,755)
%doc LICENSE.txt
%{_javadir}/bcel-%{version}.jar
%{_javadir}/bcel.jar

%if %{with javadoc}
%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{srcname}-%{version}
%ghost %{_javadocdir}/%{srcname}
%endif
