import java

from Import i
where i.getLocation().toString().regexpMatch(".*/src/.*")
select i.toString(), i.getLocation().toString()
