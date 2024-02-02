import java

from Class c, Callable callable
where callable.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
select c, callable, callable.getAParameter(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
