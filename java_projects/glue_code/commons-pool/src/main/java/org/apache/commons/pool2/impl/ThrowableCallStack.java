package org.apache.commons.pool;

import java.io.PrintWriter;
import org.graalvm.polyglot.Value;

public class ThrowableCallStack implements CallStack {
  private static Value clz =
      ContextInitializer.getPythonClass("/ThrowableCallStack.py", "ThrowableCallStack");
  private Value obj;

  public ThrowableCallStack(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public synchronized boolean printStackTrace(final PrintWriter writer) {
    //
    // final Snapshot snapshotRef = this.snapshot;
    // if (snapshotRef == null) {
    // return false;
    // }
    // final String message;
    // if (dateFormat == null) {
    // message = messageFormat;
    // } else {
    // synchronized (dateFormat) {
    // message = dateFormat.format(Long.valueOf(snapshotRef.timestampMillis));
    // }
    // }
    // writer.println(message);
    // snapshotRef.printStackTrace(writer);
    // return true;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("printStackTrace", writer).as(boolean.class);
  }

  public void fillInStackTrace() {
    //
    // snapshot = new Snapshot();
    //

    obj.invokeMember("fillInStackTrace");
  }

  public void clear() {
    //
    // snapshot = null;
    //

    obj.invokeMember("clear");
  }

  public ThrowableCallStack(final String messageFormat, final boolean useTimestamp) {
    //
    // this.messageFormat = messageFormat;
    // this.dateFormat = useTimestamp ? new SimpleDateFormat(messageFormat) : null;
    //

    this.obj = clz.invokeMember("__init__", messageFormat, useTimestamp);
  }

  private static class Snapshot extends Throwable {
    private final long timestampMillis = System.currentTimeMillis();
    private static final long serialVersionUID = 1L;
    private static Value clz =
        ContextInitializer.getPythonClass("/ThrowableCallStack.py", "Snapshot");
    private Value obj;

    public Snapshot(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }
  }
}
