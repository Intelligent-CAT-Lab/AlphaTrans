import java

from MethodAccess call
where call.getLocation().toString().regexpMatch(".*/src/.*")
select call.getLocation(), call.getMethod().getName(), call.getMethod().getNumberOfParameters(), call.getAnArgument().getLocation(), call.getMethod().getStringSignature(), call.getCaller(), call.getCaller().getLocation(), call.getCaller().getDeclaringType(), call.getCallee(), call.getCallee().getLocation(), call.getCallee().getDeclaringType()
