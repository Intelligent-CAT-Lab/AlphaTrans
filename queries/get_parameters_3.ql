import java

from Interface c, Callable callable
where callable.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = c
    and callable.isAbstract()
select c, callable, callable.getAParameter(), callable.getLocation().toString(), callable.getLocation().toString()
