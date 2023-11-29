import java

//// get all fields of all classes
from Field field
where field.getLocation().toString().regexpMatch(".*/src/.*")
select field, field.getAModifier(), field.getType(), field.getDeclaration().getLocation().toString(), field.getDeclaringType().toString()
