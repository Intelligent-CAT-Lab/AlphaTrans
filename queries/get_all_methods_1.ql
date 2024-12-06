import java

from Interface i, Callable callable
where i.getLocation().toString().regexpMatch(".*/src/.*")
    and callable.getDeclaringType() = i
select i, i.getLocation().toString(), callable, callable.getStringSignature(), callable.getLocation().toString(), callable.getLocation().toString()
