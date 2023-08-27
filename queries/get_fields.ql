import java

//// get all fields of all classes
from Field field
where field.getLocation().toString().regexpMatch(".*/src/main/.*")
select field.toString(), field.getLocation().toString(), field.getDeclaringType().toString()
