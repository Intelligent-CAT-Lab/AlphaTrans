import java

from Class c
where c.getLocation().toString().regexpMatch(".*/src/.*")
and c.isAbstract()
select c.toString(), "true", c.getASupertype().toString(), c.getLocation().toString()
