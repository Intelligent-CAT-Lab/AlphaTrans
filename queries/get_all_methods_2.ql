import java

from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
select c, c.getLocation().toString(), callable, callable.getStringSignature(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
