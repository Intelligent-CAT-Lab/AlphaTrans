import java

//// get all imports in files
from Import i
where i.getLocation().toString().regexpMatch(".*/src/main/.*")
select i.toString(), i.getLocation().toString()
