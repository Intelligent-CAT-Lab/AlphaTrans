import java

from Field field
where field.getLocation().toString().regexpMatch(".*/src/.*")
select field, field.getAModifier(), field.getType(), field.getType().getTypeDescriptor(), field.getDeclaration().getLocation().toString(), field.getDeclaringType().toString()
