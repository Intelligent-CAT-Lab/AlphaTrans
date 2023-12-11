import java

//// get all callables' parameters
from Class c, Callable callable
// from Interface c, Callable callable
where callable.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and callable.isAbstract()
// select c, callable, callable.getAParameter(), callable.getLocation().toString(), callable.getBody().getLocation().toString()
select c, callable, callable.getAParameter(), callable.getLocation().toString(), callable.getLocation().toString()
