import java

from Interface c
where c.getLocation().toString().regexpMatch(".*/src/.*")
select c.toString(), c.getLocation().toString(), c.getEnclosingType()
