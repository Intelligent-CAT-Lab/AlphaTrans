package org.apache.commons.graph.visit;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.graph.ContextInitializer;
import org.apache.commons.graph.ExceptionHandler;
import org.apache.commons.graph.IntegrationUtils;
import org.apache.commons.graph.Graph;
import static org.apache.commons.graph.visit.VisitState.CONTINUE;
public class BaseGraphVisitHandler<V, E, G extends Graph<V, E>, O>
    private static Value clz = ContextInitializer.getPythonClass("/visit/BaseGraphVisitHandler.py", "BaseGraphVisitHandler");
    private Value obj;
    public BaseGraphVisitHandler(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public O onCompleted() {
// 
// return null;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("onCompleted").as(O.class);
}
    public VisitState finishVertex(V vertex) {
// 
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("finishVertex", vertex).as(VisitState.class);
}
    public void finishGraph(G graph) {
// 

obj.invokeMember("finishGraph", graph);
}
    public VisitState finishEdge(V head, E edge, V tail) {
// 
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("finishEdge", head, edge, tail).as(VisitState.class);
}
    public VisitState discoverVertex(V vertex) {
// 
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverVertex", vertex).as(VisitState.class);
}
    public void discoverGraph(G graph) {
// 

obj.invokeMember("discoverGraph", graph);
}
    public VisitState discoverEdge(V head, E edge, V tail) {
// 
// return CONTINUE;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("discoverEdge", head, edge, tail).as(VisitState.class);
}
}
