package org.apache.commons.codec.digest;

import org.apache.commons.codec.ContextInitializer;
import org.graalvm.polyglot.Value;

public final class Blake3 {
  private static final byte[][] MSG_SCHEDULE = {
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15},
    {2, 6, 3, 10, 7, 0, 4, 13, 1, 11, 12, 5, 9, 14, 15, 8},
    {3, 4, 10, 12, 13, 2, 7, 14, 6, 5, 9, 0, 11, 15, 8, 1},
    {10, 7, 12, 9, 14, 3, 13, 15, 4, 0, 11, 2, 5, 8, 1, 6},
    {12, 13, 9, 11, 15, 10, 14, 8, 7, 2, 5, 3, 0, 1, 6, 4},
    {9, 14, 11, 5, 8, 12, 15, 1, 13, 3, 0, 10, 2, 6, 4, 7},
    {11, 15, 5, 0, 1, 9, 8, 6, 14, 10, 2, 12, 3, 4, 7, 13}
  };
  private static final int DERIVE_KEY_MATERIAL = 1 << 6;
  private static final int DERIVE_KEY_CONTEXT = 1 << 5;
  private static final int KEYED_HASH = 1 << 4;
  private static final int ROOT = 1 << 3;
  private static final int PARENT = 1 << 2;
  private static final int CHUNK_END = 1 << 1;
  private static final int CHUNK_START = 1;
  private static final int[] IV = {
    0x6A09E667, 0xBB67AE85, 0x3C6EF372, 0xA54FF53A, 0x510E527F, 0x9B05688C, 0x1F83D9AB, 0x5BE0CD19
  };
  private static final int CHAINING_VALUE_INTS = 8;
  private static final int CHUNK_LEN = 1024;
  private static final int OUT_LEN = 32;
  private static final int KEY_INTS = KEY_LEN / INT_BYTES;
  private static final int KEY_LEN = 32;
  private static final int BLOCK_INTS = BLOCK_LEN / INT_BYTES;
  private static final int BLOCK_LEN = 64;
  private static final int INT_BYTES = Integer.SIZE / Byte.SIZE;
  private static Value clz = ContextInitializer.getPythonClass("/digest/Blake3.py", "Blake3");
  private Value obj;

  public Blake3(Value obj) {
    this.obj = obj;
  }

  public Value getPythonObject() {
    return obj;
  }

  public static byte[] keyedHash(final byte[] key, final byte[] data) {
    //
    // final Blake3 blake3 = Blake3.initKeyedHash(key);
    // blake3.update0(data);
    // return blake3.doFinalize2(OUT_LEN);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("keyedHash", key, data).as(byte[].class);
  }

  public static byte[] hash(final byte[] data) {
    //
    // final Blake3 blake3 = Blake3.initHash();
    // blake3.update0(data);
    // return blake3.doFinalize2(OUT_LEN);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("hash", data).as(byte[].class);
  }

  public static Blake3 initKeyDerivationFunction(final byte[] kdfContext) {
    //
    // Objects.requireNonNull(kdfContext);
    // final EngineState kdf = new EngineState(IV, DERIVE_KEY_CONTEXT);
    // kdf.inputData(kdfContext, 0, kdfContext.length);
    // final byte[] key = new byte[KEY_LEN];
    // kdf.outputHash(key, 0, key.length);
    // return new Blake3(unpackInts(key, KEY_INTS), DERIVE_KEY_MATERIAL);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("initKeyDerivationFunction", kdfContext).as(Blake3.class);
  }

  public static Blake3 initKeyedHash(final byte[] key) {
    //
    // Objects.requireNonNull(key);
    // if (key.length != KEY_LEN) {
    // throw new IllegalArgumentException("Blake3 keys must be 32 bytes");
    // }
    // return new Blake3(unpackInts(key, KEY_INTS), KEYED_HASH);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("initKeyedHash", key).as(Blake3.class);
  }

  public static Blake3 initHash() {
    //
    // return new Blake3(IV, 0);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("initHash").as(Blake3.class);
  }

  public byte[] doFinalize2(final int nrBytes) {
    //
    // if (nrBytes < 0) {
    // throw new IllegalArgumentException("Requested bytes must be non-negative");
    // }
    // final byte[] hash = new byte[nrBytes];
    // doFinalize0(hash);
    // return hash;
    //

    // TODO: Check the type mapping below!
    return obj.invokeMember("doFinalize2", nrBytes).as(byte[].class);
  }

  public void doFinalize1(final byte[] out, final int offset, final int length) {
    //
    // checkBufferArgs(out, offset, length);
    // engineState.outputHash(out, offset, length);
    //

    obj.invokeMember("doFinalize1", out, offset, length);
  }

  public void doFinalize0(final byte[] out) {
    //
    // Objects.requireNonNull(out);
    // doFinalize1(out, 0, out.length);
    //

    obj.invokeMember("doFinalize0", out);
  }

  public void update1(final byte[] in, final int offset, final int length) {
    //
    // checkBufferArgs(in, offset, length);
    // engineState.inputData(in, offset, length);
    //

    obj.invokeMember("update1", in, offset, length);
  }

  public void update0(final byte[] in) {
    //
    // Objects.requireNonNull(in);
    // update1(in, 0, in.length);
    //

    obj.invokeMember("update0", in);
  }

  public void reset() {
    //
    // engineState.reset();
    //

    obj.invokeMember("reset");
  }

  private static int[] parentChainingValue(
      final int[] leftChildCV, final int[] rightChildCV, final int[] key, final int flags) {
    //
    // return parentOutput(leftChildCV, rightChildCV, key, flags).chainingValue();
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("parentChainingValue", leftChildCV, rightChildCV, key, flags)
        .as(int[].class);
  }

  private static Output parentOutput(
      final int[] leftChildCV, final int[] rightChildCV, final int[] key, final int flags) {
    //
    // final int[] blockWords = Arrays.copyOf(leftChildCV, BLOCK_INTS);
    // System.arraycopy(rightChildCV, 0, blockWords, 8, CHAINING_VALUE_INTS);
    // return new Output(key.clone(), blockWords, 0, BLOCK_LEN, flags | PARENT);
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("parentOutput", leftChildCV, rightChildCV, key, flags).as(Output.class);
  }

  private static int[] compress(
      final int[] chainingValue,
      final int[] blockWords,
      final int blockLength,
      final long counter,
      final int flags) {
    //
    // final int[] state = Arrays.copyOf(chainingValue, BLOCK_INTS);
    // System.arraycopy(IV, 0, state, 8, 4);
    // state[12] = (int) counter;
    // state[13] = (int) (counter >> Integer.SIZE);
    // state[14] = blockLength;
    // state[15] = flags;
    // for (int i = 0; i < 7; i++) {
    // final byte[] schedule = MSG_SCHEDULE[i];
    // round(state, blockWords, schedule);
    // }
    // for (int i = 0; i < state.length / 2; i++) {
    // state[i] ^= state[i + 8];
    // state[i + 8] ^= chainingValue[i];
    // }
    // return state;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("compress", chainingValue, blockWords, blockLength, counter, flags)
        .as(int[].class);
  }

  private static void round(final int[] state, final int[] msg, final byte[] schedule) {
    //
    // g(state, 0, 4, 8, 12, msg[schedule[0]], msg[schedule[1]]);
    // g(state, 1, 5, 9, 13, msg[schedule[2]], msg[schedule[3]]);
    // g(state, 2, 6, 10, 14, msg[schedule[4]], msg[schedule[5]]);
    // g(state, 3, 7, 11, 15, msg[schedule[6]], msg[schedule[7]]);
    //
    // g(state, 0, 5, 10, 15, msg[schedule[8]], msg[schedule[9]]);
    // g(state, 1, 6, 11, 12, msg[schedule[10]], msg[schedule[11]]);
    // g(state, 2, 7, 8, 13, msg[schedule[12]], msg[schedule[13]]);
    // g(state, 3, 4, 9, 14, msg[schedule[14]], msg[schedule[15]]);
    //

    clz.invokeMember("round", state, msg, schedule);
  }

  private static void g(
      final int[] state,
      final int a,
      final int b,
      final int c,
      final int d,
      final int mx,
      final int my) {
    //
    // state[a] += state[b] + mx;
    // state[d] = Integer.rotateRight(state[d] ^ state[a], 16);
    // state[c] += state[d];
    // state[b] = Integer.rotateRight(state[b] ^ state[c], 12);
    // state[a] += state[b] + my;
    // state[d] = Integer.rotateRight(state[d] ^ state[a], 8);
    // state[c] += state[d];
    // state[b] = Integer.rotateRight(state[b] ^ state[c], 7);
    //

    clz.invokeMember("g", state, a, b, c, d, mx, my);
  }

  private static int[] unpackInts(final byte[] buf, final int nrInts) {
    //
    // final int[] values = new int[nrInts];
    // for (int i = 0, off = 0; i < nrInts; i++, off += INT_BYTES) {
    // values[i] = unpackInt(buf, off);
    // }
    // return values;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("unpackInts", buf, nrInts).as(int[].class);
  }

  private static int unpackInt(final byte[] buf, final int off) {
    //
    // return buf[off] & 0xFF
    // | (buf[off + 1] & 0xFF) << 8
    // | (buf[off + 2] & 0xFF) << 16
    // | (buf[off + 3] & 0xFF) << 24;
    //

    // TODO: Check the type mapping below!
    return clz.invokeMember("unpackInt", buf, off).as(int.class);
  }

  private static void packInt(final int value, final byte[] dst, final int off, final int len) {
    //
    // for (int i = 0; i < len; i++) {
    // dst[off + i] = (byte) (value >>> i * Byte.SIZE);
    // }
    //

    clz.invokeMember("packInt", value, dst, off, len);
  }

  private static void checkBufferArgs(final byte[] buffer, final int offset, final int length) {
    //
    // Objects.requireNonNull(buffer);
    // if (offset < 0) {
    // throw new IndexOutOfBoundsException("Offset must be non-negative");
    // }
    // if (length < 0) {
    // throw new IndexOutOfBoundsException("Length must be non-negative");
    // }
    // final int bufferLength = buffer.length;
    // if (offset > bufferLength - length) {
    // throw new IndexOutOfBoundsException(
    // "Offset "
    // + offset
    // + " and length "
    // + length
    // + " out of bounds with buffer length "
    // + bufferLength);
    // }
    //

    clz.invokeMember("checkBufferArgs", buffer, offset, length);
  }

  private Blake3(final int[] key, final int flags) {
    //
    // engineState = new EngineState(key, flags);
    //

    this.obj = clz.invokeMember("__init__", key, flags);
  }

  private static class EngineState {
    private final int[][] cvStack = new int[54][];
    private static Value clz =
        ContextInitializer.getPythonClass("/digest/Blake3.py", "EngineState");
    private Value obj;

    public EngineState(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    private int[] popCV() {
      //
      // return cvStack[--stackLen];
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("popCV").as(int[].class);
    }

    private void pushCV(final int[] cv) {
      //
      // cvStack[stackLen++] = cv;
      //

      obj.invokeMember("pushCV", cv);
    }

    private void addChunkCV(final int[] firstCV, final long totalChunks) {
      //
      // int[] newCV = firstCV;
      // long chunkCounter = totalChunks;
      // while ((chunkCounter & 1) == 0) {
      // newCV = parentChainingValue(popCV(), newCV, key, flags);
      // chunkCounter >>= 1;
      // }
      // pushCV(newCV);
      //

      obj.invokeMember("addChunkCV", firstCV, totalChunks);
    }

    void reset() {
      //
      // stackLen = 0;
      // Arrays.fill(cvStack, null);
      // state = new ChunkState(key, 0, flags);
      //

      obj.invokeMember("reset");
    }

    void outputHash(final byte[] out, final int offset, final int length) {
      //
      // Output output = state.output();
      // int parentNodesRemaining = stackLen;
      // while (parentNodesRemaining-- > 0) {
      // final int[] parentCV = cvStack[parentNodesRemaining];
      // output = parentOutput(parentCV, output.chainingValue(), key, flags);
      // }
      // output.rootOutputBytes(out, offset, length);
      //

      obj.invokeMember("outputHash", out, offset, length);
    }

    void inputData(final byte[] in, int offset, int length) {
      //
      // while (length > 0) {
      // if (state.length() == CHUNK_LEN) {
      // final int[] chunkCV = state.output().chainingValue();
      // final long totalChunks = state.chunkCounter + 1;
      // addChunkCV(chunkCV, totalChunks);
      // state = new ChunkState(key, totalChunks, flags);
      // }
      //
      // final int want = CHUNK_LEN - state.length();
      // final int take = Math.min(want, length);
      // state.update(in, offset, take);
      // offset += take;
      // length -= take;
      // }
      //

      obj.invokeMember("inputData", in, offset, length);
    }

    EngineState(final int[] key, final int flags) {
      //
      // this.key = key;
      // this.flags = flags;
      // state = new ChunkState(key, 0, flags);
      //

      this.obj = clz.invokeMember("__init__", key, flags);
    }
  }

  private static class ChunkState {
    private final byte[] block = new byte[BLOCK_LEN];
    private static Value clz = ContextInitializer.getPythonClass("/digest/Blake3.py", "ChunkState");
    private Value obj;

    public ChunkState(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    Output output() {
      //
      // final int[] blockWords = unpackInts(block, BLOCK_INTS);
      // final int outputFlags = flags | startFlag() | CHUNK_END;
      // return new Output(chainingValue, blockWords, chunkCounter, blockLength, outputFlags);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("output").as(Output.class);
    }

    void update(final byte[] input, int offset, int length) {
      //
      // while (length > 0) {
      // if (blockLength == BLOCK_LEN) {
      // final int[] blockWords = unpackInts(block, BLOCK_INTS);
      // chainingValue =
      // Arrays.copyOf(
      // compress(
      // chainingValue,
      // blockWords,
      // BLOCK_LEN,
      // chunkCounter,
      // flags | startFlag()),
      // CHAINING_VALUE_INTS);
      // blocksCompressed++;
      // blockLength = 0;
      // Arrays.fill(block, (byte) 0);
      // }
      //
      // final int want = BLOCK_LEN - blockLength;
      // final int take = Math.min(want, length);
      // System.arraycopy(input, offset, block, blockLength, take);
      // blockLength += take;
      // offset += take;
      // length -= take;
      // }
      //

      obj.invokeMember("update", input, offset, length);
    }

    int startFlag() {
      //
      // return blocksCompressed == 0 ? CHUNK_START : 0;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("startFlag").as(int.class);
    }

    int length() {
      //
      // return BLOCK_LEN * blocksCompressed + blockLength;
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("length").as(int.class);
    }

    ChunkState(final int[] key, final long chunkCounter, final int flags) {
      //
      // chainingValue = key;
      // this.chunkCounter = chunkCounter;
      // this.flags = flags;
      //

      this.obj = clz.invokeMember("__init__", key, chunkCounter, flags);
    }
  }

  private static class Output {
    private static Value clz = ContextInitializer.getPythonClass("/digest/Blake3.py", "Output");
    private Value obj;

    public Output(Value obj) {
      this.obj = obj;
    }

    public Value getPythonObject() {
      return obj;
    }

    void rootOutputBytes(final byte[] out, int offset, int length) {
      //
      // int outputBlockCounter = 0;
      // while (length > 0) {
      // int chunkLength = Math.min(OUT_LEN * 2, length);
      // length -= chunkLength;
      // final int[] words =
      // compress(
      // inputChainingValue,
      // blockWords,
      // blockLength,
      // outputBlockCounter++,
      // flags | ROOT);
      // int wordCounter = 0;
      // while (chunkLength > 0) {
      // final int wordLength = Math.min(INT_BYTES, chunkLength);
      // packInt(words[wordCounter++], out, offset, wordLength);
      // offset += wordLength;
      // chunkLength -= wordLength;
      // }
      // }
      //

      obj.invokeMember("rootOutputBytes", out, offset, length);
    }

    int[] chainingValue() {
      //
      // return Arrays.copyOf(
      // compress(inputChainingValue, blockWords, blockLength, counter, flags),
      // CHAINING_VALUE_INTS);
      //

      // TODO: Check the type mapping below!
      return obj.invokeMember("chainingValue").as(int[].class);
    }

    Output(
        final int[] inputChainingValue,
        final int[] blockWords,
        final long counter,
        final int blockLength,
        final int flags) {
      //
      // this.inputChainingValue = inputChainingValue;
      // this.blockWords = blockWords;
      // this.counter = counter;
      // this.blockLength = blockLength;
      // this.flags = flags;
      //

      this.obj =
          clz.invokeMember("__init__", inputChainingValue, blockWords, counter, blockLength, flags);
    }
  }
}
