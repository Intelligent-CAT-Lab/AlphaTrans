import java

from ConstructorCall call
where call.getLocation().toString().regexpMatch(".*/src/.*")
and call.getCaller().getName() != call.getConstructor().getName()
select call, call.getConstructor().getStringSignature(), call.getLocation(), call.getNumArgument(), call.getAnArgument().getLocation()
