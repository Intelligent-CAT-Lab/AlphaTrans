import java

from Class c
where c.getLocation().toString().regexpMatch(".*/src/.*")
and not c.isAbstract()
select c.toString(), "false", c.getASupertype().toString(), c.getLocation().toString()
