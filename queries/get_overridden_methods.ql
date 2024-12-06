import java

from Method m
where m.getLocation().toString().regexpMatch(".*/src/.*")
select m, m.getLocation(), m.getAnOverride(), m.getAnOverride().getLocation(), m.getAnOverride().getDeclaringType()
