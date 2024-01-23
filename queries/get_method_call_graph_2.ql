import java

from MethodAccess call
where call.getLocation().toString().regexpMatch(".*/src/.*")
and call.getMethod().getNumberOfParameters() = 0
select call.getLocation(), call.getMethod().getName(), call.getMethod().getNumberOfParameters(), "", call.getMethod().getStringSignature(), call.getCaller(), call.getCaller().getLocation(), call.getCaller().getDeclaringType(), call.getCallee(), call.getCallee().getLocation(), call.getCallee().getDeclaringType()
