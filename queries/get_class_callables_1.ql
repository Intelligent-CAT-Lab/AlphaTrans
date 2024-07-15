import java

from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and callable.hasAnnotation()
select c, c.getLocation().toString(), callable, callable.getAModifier(), callable.getReturnType(), callable.getReturnType().getTypeDescriptor(), callable.getStringSignature(), callable.getAnAnnotation().getLocation().toString(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
