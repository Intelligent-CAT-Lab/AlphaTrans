import java

//// get all interfaces
from Interface c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
    and callable.getDeclaringType() = c
select c, c.getLocation().toString(), callable, callable.getAModifier(), callable.getReturnType(), callable.getStringSignature(), callable.getLocation().toString()
