import java

from Field field
where field.getLocation().toString().regexpMatch(".*/src/.*")
select field, "null", field.getType(), field.getType().getTypeDescriptor(), field.getDeclaration().getLocation().toString(), field.getDeclaringType().toString()
