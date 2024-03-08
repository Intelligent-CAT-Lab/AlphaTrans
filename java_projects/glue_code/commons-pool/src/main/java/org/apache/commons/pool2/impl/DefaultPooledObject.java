package org.apache.commons.pool;

import java.io.PrintWriter;
import java.time.Clock;
import java.time.Duration;
import java.time.Instant;
import org.apache.commons.pool2.PooledObject;
import org.apache.commons.pool2.PooledObjectState;
import org.graalvm.polyglot.Value;

public class DefaultPooledObject<T> {
  private volatile CallStack usedBy = NoOpCallStack.INSTANCE;
  private volatile CallStack borrowedBy = NoOpCallStack.INSTANCE;
  private volatile Instant lastReturnInstant = createInstant;
  private volatile Instant lastUseInstant = createInstant;
  private volatile Instant lastBorrowInstant = createInstant;
  private final Instant createInstant = now();
  private final Clock systemClock = Clock.systemUTC();
  private PooledObjectState state =
      PooledObjectState.IDLE; // @GuardedBy("this") to ensure transitions are valid
  private static Value clz =
      ContextInitializer.getPythonClass("/DefaultPooledObject.py", "DefaultPooledObject");
  private Value obj;

  public DefaultPooledObject(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public void use() {
    //
    // lastUseInstant = now();
    // usedBy.fillInStackTrace();
    //

    obj.invokeMember("use");
  }

  public String toString() {
    //
    // final StringBuilder result = new StringBuilder();
    // result.append("Object: ");
    // result.append(object.toString());
    // result.append(", State: ");
    // synchronized (this) {
    // result.append(state.toString());
    // }
    // return result.toString();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("toString").as(String.class);
  }

  public synchronized boolean startEvictionTest() {
    //
    // if (state == PooledObjectState.IDLE) {
    // state = PooledObjectState.EVICTION;
    // return true;
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("startEvictionTest").as(boolean.class);
  }

  public void setLogAbandoned(final boolean logAbandoned) {
    //
    // this.logAbandoned = logAbandoned;
    //

    obj.invokeMember("setLogAbandoned", logAbandoned);
  }

  public void printStackTrace(final PrintWriter writer) {
    //
    // boolean written = borrowedBy.printStackTrace(writer);
    // written |= usedBy.printStackTrace(writer);
    // if (written) {
    // writer.flush();
    // }
    //

    obj.invokeMember("printStackTrace", writer);
  }

  public synchronized void markReturning() {
    //
    // state = PooledObjectState.RETURNING;
    //

    obj.invokeMember("markReturning");
  }

  public synchronized void markAbandoned() {
    //
    // state = PooledObjectState.ABANDONED;
    //

    obj.invokeMember("markAbandoned");
  }

  public synchronized void invalidate() {
    //
    // state = PooledObjectState.INVALID;
    //

    obj.invokeMember("invalidate");
  }

  public synchronized PooledObjectState getState() {
    //
    // return state;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getState").as(PooledObjectState.class);
  }

  public T getObject() {
    //
    // return object;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getObject").as(T.class);
  }

  public long getLastUsedTime() {
    //
    // return getLastUsedInstant().toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastUsedTime").as(long.class);
  }

  public Instant getLastUsedInstant() {
    //
    // if (object instanceof TrackedUse) {
    // return PoolImplUtils.max(((TrackedUse) object).getLastUsedInstant(), lastUseInstant);
    // }
    // return lastUseInstant;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastUsedInstant").as(Instant.class);
  }

  public long getLastReturnTime() {
    //
    // return lastReturnInstant.toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastReturnTime").as(long.class);
  }

  public Instant getLastReturnInstant() {
    //
    // return lastReturnInstant;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastReturnInstant").as(Instant.class);
  }

  public long getLastBorrowTime() {
    //
    // return lastBorrowInstant.toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowTime").as(long.class);
  }

  public Instant getLastBorrowInstant() {
    //
    // return lastBorrowInstant;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getLastBorrowInstant").as(Instant.class);
  }

  public long getIdleTimeMillis() {
    //
    // return getIdleDuration().toMillis();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleTimeMillis").as(long.class);
  }

  public Duration getIdleTime() {
    //
    // return getIdleDuration();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleTime").as(Duration.class);
  }

  public Duration getIdleDuration() {
    //
    // final Duration elapsed = Duration.between(lastReturnInstant, now());
    // return elapsed.isNegative() ? Duration.ZERO : elapsed;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getIdleDuration").as(Duration.class);
  }

  public long getCreateTime() {
    //
    // return createInstant.toEpochMilli();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreateTime").as(long.class);
  }

  public Instant getCreateInstant() {
    //
    // return createInstant;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getCreateInstant").as(Instant.class);
  }

  public long getBorrowedCount() {
    //
    // return borrowedCount;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getBorrowedCount").as(long.class);
  }

  public synchronized boolean deallocate() {
    //
    // if (state == PooledObjectState.ALLOCATED || state == PooledObjectState.RETURNING) {
    // state = PooledObjectState.IDLE;
    // lastReturnInstant = now();
    // borrowedBy.clear();
    // return true;
    // }
    //
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("deallocate").as(boolean.class);
  }

  public int compareTo(final PooledObject<T> other) {
    //
    // final int compareTo = getLastReturnInstant().compareTo(other.getLastReturnInstant());
    // if (compareTo == 0) {
    // return System.identityHashCode(this) - System.identityHashCode(other);
    // }
    // return compareTo;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("compareTo", other).as(int.class);
  }

  public synchronized boolean allocate() {
    //
    // if (state == PooledObjectState.IDLE) {
    // state = PooledObjectState.ALLOCATED;
    // lastBorrowInstant = now();
    // lastUseInstant = lastBorrowInstant;
    // borrowedCount++;
    // if (logAbandoned) {
    // borrowedBy.fillInStackTrace();
    // }
    // return true;
    // }
    // if (state == PooledObjectState.EVICTION) {
    // state = PooledObjectState.EVICTION_RETURN_TO_HEAD;
    // }
    // return false;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("allocate").as(boolean.class);
  }

  public DefaultPooledObject(final T object) {
    //
    // this.object = object;
    //

    this.obj = clz.invokeMember("__init__", object);
  }

  private Instant now() {
    //
    // return systemClock.instant();
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("now").as(Instant.class);
  }
}
