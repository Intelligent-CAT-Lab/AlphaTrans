package org.apache.commons.graph.connectivity;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import java.util.List;
import java.util.LinkedList;
import org.apache.commons.graph.Graph;
import org.apache.commons.graph.visit.BaseGraphVisitHandler;
import org.apache.commons.graph.visit.VisitState;
import static org.apache.commons.graph.visit.VisitState.CONTINUE;
final class ConnectedComponentHandler<V, E>
    private final List<V> touchedVertices = new LinkedList<V>();
    private static Value clz = ContextInitializer.getPythonClass("/connectivity/ConnectedComponentHandler.py", "ConnectedComponentHandler");
    private Value obj;
    public ConnectedComponentHandler(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public List<V> onCompleted() {
// 
// return touchedVertices;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("onCompleted").as(List.class);
}
    public VisitState finishVertex(V vertex) {
// 
// untouchedVertices.remove(vertex);
// touchedVertices.add(vertex);
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("finishVertex", vertex).as(VisitState.class);
}
    public ConnectedComponentHandler(List<V> untouchedVertices) {
// 
// this.untouchedVertices = untouchedVertices;
// 

this.obj = clz.invokeMember("__init__", untouchedVertices);
}
}
