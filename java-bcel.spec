Summary:        Byte Code Engineering Library
Summary(pl):	Biblioteka do obróbki bytecodu Javy
Name:           jakarta-bcel
Version:        5.1
Release:        0.1
License:        Apache Software License
Group:		Development/Languages/Java
Source0:        http://jakarta.apache.org/builds/jakarta-bcel/release/v%{version}/bcel-%{version}-src.tar.gz
# Source0-md5:	c9ebfa7373eb4416e590205fd0005039
Patch0:		%{name}-build.patch
Patch1:		%{name}-manifest.patch
URL:            http://jakarta.apache.org/bcel/
BuildRequires:  jakarta-ant
BuildRequires:	jakarta-regexp
Requires:       jakarta-regexp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javalibdir	%{_datadir}/java

%description
The Byte Code Engineering Library (formerly known as JavaClass) is
intended to give users a convenient possibility to analyze, create,
and manipulate (binary) Java class files (those ending with
.class). Classes are represented by objects which contain all the
symbolic information of the given class: methods, fields and byte code
instructions, in particular.  Such objects can be read from an
existing file, be transformed by a program (e.g. a class loader at
run-time) and dumped to a file again. An even more interesting
application is the creation of classes from scratch at run-time. The
Byte Code Engineering Library (BCEL) may be also useful if you want to
learn about the Java Virtual Machine (JVM) and the format of Java
.class files.  BCEL is already being used successfully in several
projects such as compilers, optimizers, obsfuscators and analysis
tools, the most popular probably being the Xalan XSLT processor at
Apache.

%description -l pl
BCEL (Byte Code Engineering Library, poprzednio znana jako JavaClass)
ma umo¿liwiæ wygodne analizowanie, tworzenie i obróbkê (binarnych)
plików klas Javy (tych z nazw± koñcz±c± siê na .class). Klasy s±
reprezentowane przez obiekty zawieraj±ce wszystkie symboliczne
informacje o danej klasie, w szczególno¶ci metody, pola i instrukcje
bytecodu. Obiekty te mog± byæ odczytywane z istniej±cego pliku,
przekszta³cane przez program (np. wczytuj±cy klasy w czasie dzia³ania)
i zrzucane z powrotem do pliku. Jeszcze ciekawszym zastosowaniem jest
tworzenie klas od zera w czasie dzia³ania programu. Biblioteka BCEL
mo¿e byæ tak¿e u¿yteczna, je¶li chcemy nauczyæ siê czego¶ o maszynie
wirtualnej Javy (JVM) oraz formacie plików .class. BCEL jest u¿ywana z
sukcesem w ró¿nych projektach, takich jak kompilatory, optymalizatory,
narzêdzia utrudniaj±ce analizê oraz narzêdzia do analizy, z których
najpopularniejszym jest procesor XSLT Xalan.

%prep
%setup -q -n bcel-%{version}
%patch0 -p1
%patch1 -p1
find . -name "*.jar" -exec rm -f {} \;

%build
CLASSPATH=%{_javalibdir}/regexp.jar
export CLASSPATH
ant jar apidocs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javalibdir}
cp -p bin/bcel.jar $RPM_BUILD_ROOT%{_javalibdir}
ln -sf bcel.jar $RPM_BUILD_ROOT%{_javalibdir}/bcel-%{version}.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt docs/*
%{_javalibdir}/*.jar
