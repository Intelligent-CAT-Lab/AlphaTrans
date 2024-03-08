package org.apache.commons.pool;

import java.util.HashMap;
import java.util.Map;
import org.graalvm.polyglot.PolyglotException;
import org.graalvm.polyglot.Value;

public class WaiterFactory<K> {
  private final Map<K, Integer> activeCounts = new HashMap<>();
  private static Value clz =
      ContextInitializer.getPythonClass("/WaiterFactory.py", "WaiterFactory");
  private Value obj;

  public WaiterFactory(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public boolean validateObject1(final PooledObject<Waiter> obj) {
    //
    // doWait(validateLatency);
    // return obj.getObject().isValid();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject1", obj).as(boolean.class);
  }

  public boolean validateObject0(final K key, final PooledObject<Waiter> obj) {
    //
    // return validateObject1(obj);
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("validateObject0", key, obj).as(boolean.class);
  }

  public synchronized void reset() {
    //
    // activeCount = 0;
    // if (activeCounts.isEmpty()) {
    // return;
    // }
    // final Iterator<K> it = activeCounts.keySet().iterator();
    // while (it.hasNext()) {
    // final K key = it.next();
    // activeCounts.put(key, Integer.valueOf(0));
    // }
    //

    obj.invokeMember("reset");
  }

  public void passivateObject1(final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // obj.getObject().setActive(false);
      // doWait(passivateLatency);
      // if (Math.random() < passivateInvalidationProbability) {
      // obj.getObject().setValid(false);
      // }
      //

      obj.invokeMember("passivateObject1", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.passivateObject1");
    }
  }

  public void passivateObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // passivateObject1(obj);
      //

      obj.invokeMember("passivateObject0", key, obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.passivateObject0");
    }
  }

  public synchronized long getMaxActive() {
    //
    // return maxActive;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getMaxActive").as(long.class);
  }

  protected void doWait(final long latency) {
    //
    // if (latency == 0) {
    // return;
    // }
    // Waiter.sleepQuietly(latency);
    //

    obj.invokeMember("doWait", latency);
  }

  public void destroyObject1(final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // doWait(destroyLatency);
      // obj.getObject().setValid(false);
      // obj.getObject().setActive(false);
      // synchronized (this) {
      // activeCount--;
      // }
      //

      obj.invokeMember("destroyObject1", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.destroyObject1");
    }
  }

  public void destroyObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // destroyObject1(obj);
      // synchronized (this) {
      // final Integer count = activeCounts.get(key);
      // activeCounts.put(key, Integer.valueOf(count.intValue() - 1));
      // }
      //

      obj.invokeMember("destroyObject0", key, obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.destroyObject0");
    }
  }

  public void activateObject1(final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // doWait(activateLatency);
      // obj.getObject().setActive(true);
      //

      obj.invokeMember("activateObject1", obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.activateObject1");
    }
  }

  public void activateObject0(final K key, final PooledObject<Waiter> obj) throws Exception {
    try {
      //
      // activateObject1(obj);
      //

      obj.invokeMember("activateObject0", key, obj);
    } catch (PolyglotException e) {
      // TODO: Handle Exception
      throw (Exception) ExceptionHandler.handle(e, "WaiterFactory.activateObject0");
    }
  }

  public static WaiterFactory WaiterFactory2(
      final long activateLatency,
      final long destroyLatency,
      final long makeLatency,
      final long passivateLatency,
      final long validateLatency,
      final long waiterLatency) {
    //
    // return new WaiterFactory(
    // activateLatency,
    // destroyLatency,
    // makeLatency,
    // passivateLatency,
    // validateLatency,
    // waiterLatency,
    // Long.MAX_VALUE,
    // Long.MAX_VALUE,
    // 0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "WaiterFactory2",
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency)
        .as(WaiterFactory.class);
  }

  public static WaiterFactory WaiterFactory1(
      final long activateLatency,
      final long destroyLatency,
      final long makeLatency,
      final long passivateLatency,
      final long validateLatency,
      final long waiterLatency,
      final long maxActive) {
    //
    // return new WaiterFactory(
    // activateLatency,
    // destroyLatency,
    // makeLatency,
    // passivateLatency,
    // validateLatency,
    // waiterLatency,
    // maxActive,
    // Long.MAX_VALUE,
    // 0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember(
            "WaiterFactory1",
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            maxActive)
        .as(WaiterFactory.class);
  }

  public WaiterFactory(
      final long activateLatency,
      final long destroyLatency,
      final long makeLatency,
      final long passivateLatency,
      final long validateLatency,
      final long waiterLatency,
      final long maxActive,
      final long maxActivePerKey,
      final double passivateInvalidationProbability) {
    //
    // this.activateLatency = activateLatency;
    // this.destroyLatency = destroyLatency;
    // this.makeLatency = makeLatency;
    // this.passivateLatency = passivateLatency;
    // this.validateLatency = validateLatency;
    // this.waiterLatency = waiterLatency;
    // this.maxActive = maxActive;
    // this.maxActivePerKey = maxActivePerKey;
    // this.passivateInvalidationProbability = passivateInvalidationProbability;
    //

    this.obj =
        clz.invokeMember(
            "__init__",
            activateLatency,
            destroyLatency,
            makeLatency,
            passivateLatency,
            validateLatency,
            waiterLatency,
            maxActive,
            maxActivePerKey,
            passivateInvalidationProbability);
  }
}
