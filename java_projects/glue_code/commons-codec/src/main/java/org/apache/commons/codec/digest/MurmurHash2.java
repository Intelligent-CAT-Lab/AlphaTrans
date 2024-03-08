package org.apache.commons.codec.digest;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class MurmurHash2 {
  private static final int R64 = 47;
  private static final long M64 = 0xc6a4a7935bd1e995L;
  private static final int R32 = 24;
  private static final int M32 = 0x5bd1e995;
  private static Value clz =
      ContextInitializer.getPythonClass("/digest/MurmurHash2.py", "MurmurHash2");
  private Value obj;

  public MurmurHash2(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static long hash643(final String text, final int from, final int length) {
    //
    // return hash642(text.substring(from, from + length));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash643", text, from, length).as(long.class);
  }

  public static long hash642(final String text) {
    //
    // final byte[] bytes = StringUtils.getBytesUtf8(text);
    // return hash641(bytes, bytes.length);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash642", text).as(long.class);
  }

  public static long hash641(final byte[] data, final int length) {
    //
    // return hash640(data, length, 0xe17a1465);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash641", data, length).as(long.class);
  }

  public static long hash640(final byte[] data, final int length, final int seed) {
    //
    // long h = (seed & 0xffffffffL) ^ (length * M64);
    //
    // final int nblocks = length >> 3;
    //
    // for (int i = 0; i < nblocks; i++) {
    // final int index = (i << 3);
    // long k = getLittleEndianLong(data, index);
    //
    // k *= M64;
    // k ^= k >>> R64;
    // k *= M64;
    //
    // h ^= k;
    // h *= M64;
    // }
    //
    // final int index = (nblocks << 3);
    // switch (length - index) {
    // case 7:
    // h ^= ((long) data[index + 6] & 0xff) << 48;
    // case 6:
    // h ^= ((long) data[index + 5] & 0xff) << 40;
    // case 5:
    // h ^= ((long) data[index + 4] & 0xff) << 32;
    // case 4:
    // h ^= ((long) data[index + 3] & 0xff) << 24;
    // case 3:
    // h ^= ((long) data[index + 2] & 0xff) << 16;
    // case 2:
    // h ^= ((long) data[index + 1] & 0xff) << 8;
    // case 1:
    // h ^= ((long) data[index] & 0xff);
    // h *= M64;
    // }
    //
    // h ^= h >>> R64;
    // h *= M64;
    // h ^= h >>> R64;
    //
    // return h;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash640", data, length, seed).as(long.class);
  }

  public static int hash323(final String text, final int from, final int length) {
    //
    // return hash322(text.substring(from, from + length));
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash323", text, from, length).as(int.class);
  }

  public static int hash322(final String text) {
    //
    // final byte[] bytes = StringUtils.getBytesUtf8(text);
    // return hash321(bytes, bytes.length);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash322", text).as(int.class);
  }

  public static int hash321(final byte[] data, final int length) {
    //
    // return hash320(data, length, 0x9747b28c);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash321", data, length).as(int.class);
  }

  public static int hash320(final byte[] data, final int length, final int seed) {
    //
    // int h = seed ^ length;
    //
    // final int nblocks = length >> 2;
    //
    // for (int i = 0; i < nblocks; i++) {
    // final int index = (i << 2);
    // int k = getLittleEndianInt(data, index);
    // k *= M32;
    // k ^= k >>> R32;
    // k *= M32;
    // h *= M32;
    // h ^= k;
    // }
    //
    // final int index = (nblocks << 2);
    // switch (length - index) {
    // case 3:
    // h ^= (data[index + 2] & 0xff) << 16;
    // case 2:
    // h ^= (data[index + 1] & 0xff) << 8;
    // case 1:
    // h ^= (data[index] & 0xff);
    // h *= M32;
    // }
    //
    // h ^= h >>> 13;
    // h *= M32;
    // h ^= h >>> 15;
    //
    // return h;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash320", data, length, seed).as(int.class);
  }

  private static long getLittleEndianLong(final byte[] data, final int index) {
    //
    // return (((long) data[index] & 0xff))
    // | (((long) data[index + 1] & 0xff) << 8)
    // | (((long) data[index + 2] & 0xff) << 16)
    // | (((long) data[index + 3] & 0xff) << 24)
    // | (((long) data[index + 4] & 0xff) << 32)
    // | (((long) data[index + 5] & 0xff) << 40)
    // | (((long) data[index + 6] & 0xff) << 48)
    // | (((long) data[index + 7] & 0xff) << 56);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getLittleEndianLong", data, index).as(long.class);
  }

  private static int getLittleEndianInt(final byte[] data, final int index) {
    //
    // return ((data[index] & 0xff))
    // | ((data[index + 1] & 0xff) << 8)
    // | ((data[index + 2] & 0xff) << 16)
    // | ((data[index + 3] & 0xff) << 24);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("getLittleEndianInt", data, index).as(int.class);
  }

  private MurmurHash2() {
    //

    this.obj = clz.invokeMember("__init__");
  }
}
