package org.apache.commons.codec.digest;

import java.util.zip.Checksum;
import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public class XXHash32 implements Checksum {
  private final byte[] buffer = new byte[BUF_SIZE];
  private final int[] state = new int[4];
  private final byte[] oneByte = new byte[1];
  private static final int PRIME5 = 374761393;
  private static final int PRIME4 = 668265263;
  private static final int PRIME3 = (int) 3266489917L;
  private static final int PRIME2 = (int) 2246822519L;
  private static final int PRIME1 = (int) 2654435761L;
  private static final int ROTATE_BITS = 13;
  private static final int BUF_SIZE = 16;
  private static Value clz = ContextInitializer.getPythonClass("/digest/XXHash32.py", "XXHash32");
  private Value obj;

  public XXHash32(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public long getValue() {
    //
    // int hash;
    // if (stateUpdated) {
    // hash =
    // rotateLeft(state[0], 1)
    // + rotateLeft(state[1], 7)
    // + rotateLeft(state[2], 12)
    // + rotateLeft(state[3], 18);
    // } else {
    // hash = state[2] + PRIME5;
    // }
    // hash += totalLen;
    //
    // int idx = 0;
    // final int limit = pos - 4;
    // for (; idx <= limit; idx += 4) {
    // hash = rotateLeft(hash + getInt(buffer, idx) * PRIME3, 17) * PRIME4;
    // }
    // while (idx < pos) {
    // hash = rotateLeft(hash + (buffer[idx++] & 0xff) * PRIME5, 11) * PRIME1;
    // }
    //
    // hash ^= hash >>> 15;
    // hash *= PRIME2;
    // hash ^= hash >>> 13;
    // hash *= PRIME3;
    // hash ^= hash >>> 16;
    // return hash & 0xffffffffL;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("getValue").as(long.class);
  }

  public void update(final byte[] b, final int off, final int len) {
    //

    obj.invokeMember("update", b, off, len);
  }

  public void update(final int b) {
    //

    obj.invokeMember("update", b);
  }

  public void reset() {
    //
    // initializeState();
    // totalLen = 0;
    // pos = 0;
    // stateUpdated = false;
    //

    obj.invokeMember("reset");
  }

  public void update1(final byte[] b, int off, final int len) {
    //
    // if (len <= 0) {
    // return;
    // }
    // totalLen += len;
    //
    // final int end = off + len;
    //
    // if (pos + len - BUF_SIZE < 0) {
    // System.arraycopy(b, off, buffer, pos, len);
    // pos += len;
    // return;
    // }
    //
    // if (pos > 0) {
    // final int size = BUF_SIZE - pos;
    // System.arraycopy(b, off, buffer, pos, size);
    // process(buffer, 0);
    // off += size;
    // }
    //
    // final int limit = end - BUF_SIZE;
    // while (off <= limit) {
    // process(b, off);
    // off += BUF_SIZE;
    // }
    //
    // if (off < end) {
    // pos = end - off;
    // System.arraycopy(b, off, buffer, 0, pos);
    // } else {
    // pos = 0;
    // }
    //

    obj.invokeMember("update1", b, off, len);
  }

  public void update0(final int b) {
    //
    // oneByte[0] = (byte) (b & 0xff);
    // update1(oneByte, 0, 1);
    //

    obj.invokeMember("update0", b);
  }

  public static XXHash32 XXHash321() {
    //
    // return new XXHash32(0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("XXHash321").as(XXHash32.class);
  }

  public XXHash32(final int seed) {
    //
    // this.seed = seed;
    // initializeState();
    //

    this.obj = clz.invokeMember("__init__", seed);
  }

  private void process(final byte[] b, final int offset) {
    //
    // int s0 = state[0];
    // int s1 = state[1];
    // int s2 = state[2];
    // int s3 = state[3];
    //
    // s0 = rotateLeft(s0 + getInt(b, offset) * PRIME2, ROTATE_BITS) * PRIME1;
    // s1 = rotateLeft(s1 + getInt(b, offset + 4) * PRIME2, ROTATE_BITS) * PRIME1;
    // s2 = rotateLeft(s2 + getInt(b, offset + 8) * PRIME2, ROTATE_BITS) * PRIME1;
    // s3 = rotateLeft(s3 + getInt(b, offset + 12) * PRIME2, ROTATE_BITS) * PRIME1;
    //
    // state[0] = s0;
    // state[1] = s1;
    // state[2] = s2;
    // state[3] = s3;
    //
    // stateUpdated = true;
    //

    obj.invokeMember("process", b, offset);
  }

  private void initializeState() {
    //
    // state[0] = seed + PRIME1 + PRIME2;
    // state[1] = seed + PRIME2;
    // state[2] = seed;
    // state[3] = seed - PRIME1;
    //

    obj.invokeMember("initializeState");
  }

  private static int getInt(final byte[] buffer, final int idx) {
    //
    // return ((buffer[idx] & 0xff))
    // | ((buffer[idx + 1] & 0xff) << 8)
    // | ((buffer[idx + 2] & 0xff) << 16)
    // | ((buffer[idx + 3] & 0xff) << 24);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getInt", buffer, idx).as(int.class);
  }
}
