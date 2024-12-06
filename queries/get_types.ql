import java

from TypeAccess t
where t.getLocation().toString().regexpMatch(".*/src/.*")
select t, t.getType().getTypeDescriptor()
