package org.apache.commons.pool;

import java.util.concurrent.atomic.AtomicInteger;
import org.graalvm.polyglot.Value;

public class Waiter {
  private final int id = instanceCount.getAndIncrement();
  private static final AtomicInteger instanceCount = new AtomicInteger();
  private static Value clz = ContextInitializer.getPythonClass("/Waiter.py", "Waiter");
  private Value obj;

  public Waiter(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public String toString() {
    //
    // final StringBuilder buff = new StringBuilder();
    // buff.append("ID = " + id + '\n');
    // buff.append("valid = " + valid + '\n');
    // buff.append("active = " + active + '\n');
    // buff.append("lastPassivated = " + lastPassivatedMillis + '\n');
    // buff.append("lastIdleTimeMs = " + lastIdleTimeMillis + '\n');
    // buff.append("latency = " + latency + '\n');
    // return buff.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public int hashCode() {
    //
    // return id;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("hashCode").as(int.class);
  }

  public boolean equals(final Object obj) {
    //
    // if (!(obj instanceof Waiter)) {
    // return false;
    // }
    // return obj.hashCode() == id;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("equals", obj).as(boolean.class);
  }

  public static void sleepQuietly(final long millis) {
    //
    // try {
    // Thread.sleep(millis);
    // } catch (final InterruptedException e) {
    // }
    //

    clz.invokeMember("sleepQuietly", millis);
  }

  public void setValid(final boolean valid) {
    //
    // this.valid = valid;
    //

    obj.invokeMember("setValid", valid);
  }

  public void setLatency(final long latency) {
    //
    // this.latency = latency;
    //

    obj.invokeMember("setLatency", latency);
  }

  public void setActive(final boolean active) {
    //
    // final boolean activeState = this.active;
    // if (activeState == active) {
    // return;
    // }
    // this.active = active;
    // final long currentTimeMillis = System.currentTimeMillis();
    // if (active) { // activating
    // lastIdleTimeMillis = currentTimeMillis - lastPassivatedMillis;
    // } else { // passivating
    // lastPassivatedMillis = currentTimeMillis;
    // passivationCount++;
    // }
    //

    obj.invokeMember("setActive", active);
  }

  public boolean isValid() {
    //
    // validationCount++;
    // return valid;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isValid").as(boolean.class);
  }

  public boolean isActive() {
    //
    // return active;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("isActive").as(boolean.class);
  }

  public long getValidationCount() {
    //
    // return validationCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValidationCount").as(long.class);
  }

  public long getPassivationCount() {
    //
    // return passivationCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getPassivationCount").as(long.class);
  }

  public long getLatency() {
    //
    // return latency;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLatency").as(long.class);
  }

  public long getLastPassivatedMillis() {
    //
    // return lastPassivatedMillis;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastPassivatedMillis").as(long.class);
  }

  public long getLastIdleTimeMillis() {
    //
    // return lastIdleTimeMillis;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastIdleTimeMillis").as(long.class);
  }

  public void doWait() {
    //
    // sleepQuietly(latency);
    //

    obj.invokeMember("doWait");
  }

  public Waiter(final boolean active, final boolean valid, final long latency) {
    //
    // this.active = active;
    // this.valid = valid;
    // this.latency = latency;
    // this.lastPassivatedMillis = System.currentTimeMillis();
    //

    this.obj = clz.invokeMember("__init__", active, valid, latency);
  }
}
