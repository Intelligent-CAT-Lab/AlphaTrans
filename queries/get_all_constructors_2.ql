import java

from Constructor c, Call call
where c.getLocation().getStartLine() != 0
and c.getLocation().getStartColumn() != 0
and call.getCaller() = c
and c.getNumberOfParameters() = 0
select c, c.getLocation(), c.getBody().getLocation(), c.getStringSignature(), c.getNumberOfParameters(), "", call.toString(), call.getLocation()
