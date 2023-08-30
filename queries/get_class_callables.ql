import java

//// get all methods and constructors of all classes
from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
    and callable.getDeclaringType() = c
    // and callable.hasAnnotation()
    and not callable.hasAnnotation()
// select c, c.getLocation().toString(), callable, callable.getAModifier(), callable.getReturnType(), callable.getStringSignature(), callable.getAnAnnotation(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
select c, c.getLocation().toString(), callable, callable.getAModifier(), callable.getReturnType(), callable.getStringSignature(), "null", callable.getLocation().toString(), callable.getBody().getLocation().toString()
