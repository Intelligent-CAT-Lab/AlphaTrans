# find dependency
function build_deps() {
    mvn dependency:build-classpath -Dmdep.outputFile=cp
}

# mvn compile
function compile() {
    mkdir -p target/classes; javac -cp $(cat cp) -d target/classes $(find src/main/ -name '*java' -type f)
}

# mvn test-compile
function test_compile() {
    mkdir -p target/test-classes; javac -cp target/classes:$(cat cp) -d target/test-classes $(find src/test/ -name '*java' -type f)
}

# mvn surefire:test
wget https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/1.9.3/junit-platform-console-standalone-1.9.3.jar
java -cp target/test-classes:target/classes:$(cat cp):/home/mrigankpawagi/.m2/repository/junit/junit/4.13.2/junit-4.13.2.jar org.junit.runner.JUnitCore $(find target/test-classes/ -name '*class' | cut -f3- -d/ | sed -e sX/X.Xg -e s/.class$// | egrep '^Test|Test$|TestCase$' | xargs -n 1 echo -c)