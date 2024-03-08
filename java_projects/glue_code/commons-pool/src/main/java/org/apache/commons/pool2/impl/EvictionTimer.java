package org.apache.commons.pool;

import java.lang.ref.WeakReference;
import java.time.Duration;
import java.util.HashMap;
import org.graalvm.polyglot.Value;

private static class Reaper implements Runnable {
  private static Value clz = ContextInitializer.getPythonClass("/EvictionTimer.py", "Reaper");
  private Value obj;

  public Reaper(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void run() {
    //
    // synchronized (EvictionTimer.class) {
    // for (final Entry<WeakReference<Runnable>, WeakRunner> entry : taskMap.entrySet()) {
    // if (entry.getKey().get() == null) {
    // executor.remove(entry.getValue());
    // taskMap.remove(entry.getKey());
    // }
    // }
    // if (taskMap.isEmpty() && executor != null) {
    // executor.shutdown();
    // executor.setCorePoolSize(0);
    // executor = null;
    // }
    // }
    //

    obj.invokeMember("run");
  }
}

class EvictionTimer {
  private static final HashMap<WeakReference<Runnable>, WeakRunner> taskMap =
      new HashMap<>(); // @GuardedBy("EvictionTimer.class")
  private static Value clz =
      ContextInitializer.getPythonClass("/EvictionTimer.py", "EvictionTimer");
  private Value obj;

  public EvictionTimer(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder builder = new StringBuilder();
    // builder.append("EvictionTimer []");
    // return builder.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  static synchronized int getNumTasks() {
    //
    // return taskMap.size();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getNumTasks").as(int.class);
  }

  static synchronized void cancel(
      final BaseGenericObjectPool<?>.Evictor evictor,
      final Duration timeout,
      final boolean restarting) {
    //
    // if (evictor != null) {
    // evictor.cancel();
    // remove(evictor);
    // }
    // if (!restarting && executor != null && taskMap.isEmpty()) {
    // executor.shutdown();
    // try {
    // executor.awaitTermination(timeout.toMillis(), TimeUnit.MILLISECONDS);
    // } catch (final InterruptedException e) {
    // }
    // executor.setCorePoolSize(0);
    // executor = null;
    // }
    //

    clz.invokeMember("cancel", evictor, timeout, restarting);
  }

  private EvictionTimer() {
    //

    this.obj = clz.invokeMember("__init__");
  }

  private static void remove(final BaseGenericObjectPool<?>.Evictor evictor) {
    //
    // for (final Entry<WeakReference<Runnable>, WeakRunner> entry : taskMap.entrySet()) {
    // if (entry.getKey().get() == evictor) {
    // executor.remove(entry.getValue());
    // taskMap.remove(entry.getKey());
    // break;
    // }
    // }
    //

    clz.invokeMember("remove", evictor);
  }

  private static class WeakRunner implements Runnable {
    private static Value clz = ContextInitializer.getPythonClass("/EvictionTimer.py", "WeakRunner");
    private Value obj;

    public WeakRunner(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    public void run() {
      //
      // final Runnable task = ref.get();
      // if (task != null) {
      // task.run();
      // } else {
      // executor.remove(this);
      // taskMap.remove(ref);
      // }
      //

      obj.invokeMember("run");
    }

    private WeakRunner(final WeakReference<Runnable> ref) {
      //
      // this.ref = ref;
      //

      this.obj = clz.invokeMember("__init__", ref);
    }
  }
}
