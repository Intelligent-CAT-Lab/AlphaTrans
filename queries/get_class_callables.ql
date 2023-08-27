import java

//// get all methods and constructors of all classes
from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
    and callable.getDeclaringType() = c
    // and callable.hasAnnotation()
    and not callable.hasAnnotation()
// select c, c.getLocation().toString(), callable, callable.getAnAnnotation(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
select c, c.getLocation().toString(), callable, "null", callable.getLocation().toString(), callable.getBody().getLocation().toString()
