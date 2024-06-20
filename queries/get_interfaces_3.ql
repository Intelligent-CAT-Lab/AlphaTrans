import java

from Interface c
where c.getLocation().toString().regexpMatch(".*/src/.*")
select c, c.getLocation().toString(), "null", "null", "null", "null", "null", "null", "null"
