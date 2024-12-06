import java

from Class c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and callable.isAbstract()
select c, c.getLocation().toString(), callable, callable.getStringSignature(), callable.getLocation().toString(), callable.getLocation().toString()
