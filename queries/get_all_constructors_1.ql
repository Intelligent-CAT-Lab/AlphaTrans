import java

from Constructor c, Call call
where c.getLocation().getStartLine() != 0
and c.getLocation().getStartColumn() != 0
and call.getCaller() = c
select c, c.getLocation(), c.getBody().getLocation(), c.getStringSignature(), c.getNumberOfParameters(), c.getAParameter().getLocation(), call.toString(), call.getLocation()
