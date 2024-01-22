import java

from ConstructorCall call
where call.getLocation().toString().regexpMatch(".*/src/.*")
and call.getCaller().getName() != call.getConstructor().getName()
and call.getNumArgument() = 0
select call, call.getConstructor().getStringSignature(), call.getLocation(), call.getNumArgument(), ""
