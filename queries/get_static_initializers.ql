import java

from Class c, StaticInitializer i, BlockStmt s
where c.getLocation().toString().regexpMatch(".*/src/.*")
and c.getAMethod() = i and i.getBody().getAChild() = s
select c, s.getLocation()
