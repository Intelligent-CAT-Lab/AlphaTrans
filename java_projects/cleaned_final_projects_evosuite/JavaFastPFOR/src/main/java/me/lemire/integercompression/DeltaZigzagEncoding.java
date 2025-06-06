
/*
  Licensed to the Apache Software Foundation (ASF) under one or more
  contributor license agreements.  See the NOTICE file distributed with
  this work for additional information regarding copyright ownership.
  The ASF licenses this file to You under the Apache License, Version 2.0
  (the "License"); you may not use this file except in compliance with
  the License.  You may obtain a copy of the License at

      http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
 */

package me.lemire.integercompression;

/**
 * Delta+Zigzag Encoding.
 * 
 * @author MURAOKA Taro http://github.com/koron
 */
public final class DeltaZigzagEncoding {

        static class Context {
                int contextValue;

                Context(int contextValue) {
                        this.contextValue = contextValue;
                }

                void setContextValue(int contextValue) {
                        this.contextValue = contextValue;
                }

                int getContextValue() {
                        return this.contextValue;
                }
        }

        static class Encoder extends Context {
                Encoder(int contextValue) {
                        super(contextValue);
                }

                int encodeInt(int value) {
                        int n = value - this.contextValue;
                        this.contextValue = value;
                        return (n << 1) ^ (n >> 31);
                }

                int[] encodeArray0(int[] src, int srcoff, int length,
                                   int[] dst, int dstoff) {
                        for (int i = 0; i < length; ++i) {
                                dst[dstoff + i] = encodeInt(src[srcoff + i]);
                        }
                        return dst;
                }

                int[] encodeArray1(int[] src, int srcoff, int length,
                                   int[] dst) {
                        return encodeArray0(src, srcoff, length, dst, 0);
                }

                int[] encodeArray2(int[] src, int offset, int length) {
                        return encodeArray0(src, offset, length,
                                new int[length], 0);
                }

                int[] encodeArray3(int[] src) {
                        return encodeArray0(src, 0, src.length,
                                new int[src.length], 0);
                }
        }

        static class Decoder extends Context {
                Decoder(int contextValue) {
                        super(contextValue);
                }

                int decodeInt(int value) {
                        int n = (value >>> 1) ^ ((value << 31) >> 31);
                        n += this.contextValue;
                        this.contextValue = n;
                        return n;
                }

                int[] decodeArray0(int[] src, int srcoff, int length,
                                   int[] dst, int dstoff) {
                        for (int i = 0; i < length; ++i) {
                                dst[dstoff + i] = decodeInt(src[srcoff + i]);
                        }
                        return dst;
                }

                int[] decodeArray1(int[] src, int offset, int length) {
                        return decodeArray0(src, offset, length,
                                new int[length], 0);
                }

                int[] decodeArray2(int[] src) {
                        return decodeArray1(src, 0, src.length);
                }
        }
}
