package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
class InterruptibleReentrantLock extends ReentrantLock {
    private static final long serialVersionUID = 1L;
    private static Value clz = ContextInitializer.getPythonClass("/InterruptibleReentrantLock.py", "InterruptibleReentrantLock");
    private Value obj;
    public InterruptibleReentrantLock(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public void interruptWaiters(final Condition condition) {
// 
// getWaitingThreads(condition).forEach(Thread::interrupt);
// 

obj.invokeMember("interruptWaiters", condition);
}
    public InterruptibleReentrantLock(final boolean fairness) {
// 
// super(fairness);
// 

this.obj = clz.invokeMember("__init__", fairness);
}
        getWaitingThreads(condition).forEach(Thread::interrupt);
    private static Value clz = ContextInitializer.getPythonClass("/InterruptibleReentrantLock.py", "new Consumer<Thread>(...) { ... }");
    private Value obj;
    public new Consumer<Thread>(...) { ... }(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        getWaitingThreads(condition).forEach(Thread::interrupt);
}
}
