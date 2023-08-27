import java

//// get all classes and superclasses
from Class c
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
// and c.isAbstract()
and not c.isAbstract()
// select c.toString(), "true", c.getASupertype().toString(), c.getLocation().toString()
select c.toString(), "false", c.getASupertype().toString(), c.getLocation().toString()
