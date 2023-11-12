import java

from MethodAccess call
where call.getLocation().toString().regexpMatch(".*/src/.*")
// and call.getMethod().getNumberOfParameters() = 0
// select call.getLocation(), call.getMethod().getName(), call.getMethod().getNumberOfParameters(), "", call.getMethod().getStringSignature(), call.getCaller(), call.getCaller().getLocation(), call.getCallee(), call.getCallee().getLocation()
select call.getLocation(), call.getMethod().getName(), call.getMethod().getNumberOfParameters(), call.getAnArgument().getLocation(), call.getMethod().getStringSignature(), call.getCaller(), call.getCaller().getLocation(), call.getCallee(), call.getCallee().getLocation()
