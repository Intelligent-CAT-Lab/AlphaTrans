import java

//// get all nested classes
from Class c
where c.getLocation().toString().regexpMatch(".*/src/main/.*")
select c.toString(), c.getLocation().toString(), c.getEnclosingType()
