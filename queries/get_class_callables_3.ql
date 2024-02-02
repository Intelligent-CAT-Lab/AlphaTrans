import java

from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and not callable.hasModifier(".*")
select c, c.getLocation().toString(), callable, "null", callable.getReturnType(), callable.getReturnType().getTypeDescriptor(), callable.getStringSignature(), "null", callable.getLocation().toString(), callable.getBody().getLocation().toString()
