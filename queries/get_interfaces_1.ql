import java

from Interface c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and callable.isAbstract()
select c, c.getLocation().toString(), callable, callable.getAModifier(), callable.getReturnType(), callable.getReturnType().getTypeDescriptor(), callable.getStringSignature(), callable.getLocation().toString(), callable.getLocation().toString()
