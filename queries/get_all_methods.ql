import java

from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
select c, c.getLocation().toString(), callable, callable.getStringSignature(), callable.getLocation().toString(), callable.getBody().getLocation().toString()

from Interface i, Callable callable
where i.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = i
select i, i.getLocation().toString(), callable, callable.getStringSignature(), callable.getLocation().toString(), callable.getLocation().toString()
