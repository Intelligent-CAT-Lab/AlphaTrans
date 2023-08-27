import java

//// get all interfaces
from Interface c, Callable callable
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
    and callable.getDeclaringType() = c
select c, c.getLocation().toString(), callable, callable.getLocation().toString()
