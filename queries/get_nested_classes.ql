import java

from Class c
where c.getLocation().toString().regexpMatch(".*/src/.*")
select c.toString(), c.getLocation().toString(), c.getEnclosingType()
