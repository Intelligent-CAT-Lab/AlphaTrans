import java

from Call call
where call.getLocation().toString().regexpMatch(".*/src/.*")
select call.getLocation(), call.getCaller().getName(), call.getCaller().getLocation(), call.getCallee().getName(), call.getCallee().getLocation()
