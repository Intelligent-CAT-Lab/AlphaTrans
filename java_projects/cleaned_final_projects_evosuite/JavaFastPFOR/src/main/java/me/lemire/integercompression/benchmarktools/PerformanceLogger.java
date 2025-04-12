
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

package me.lemire.integercompression.benchmarktools;

/**
 * PerformanceLogger for IntegerCODEC.
 * 
 * @author MURAOKA Taro http://github.com/koron
 */
public final class PerformanceLogger {
        static class Timer {
                private long startNano;
                private long duration = 0;

                public Timer() {
                }

                public void start() {
                        this.startNano = System.nanoTime();
                }

                public long end() {
                        return this.duration += System.nanoTime()
                                - this.startNano;
                }

                public long getDuration() {
                        return this.duration;
                }
        }

        final Timer compressionTimer = new Timer();

        final Timer decompressionTimer = new Timer();

        private long originalSize = 0;

        private long compressedSize = 0;

        long addOriginalSize(long value) {
                return this.originalSize += value;
        }

        long addCompressedSize(long value) {
                return this.compressedSize += value;
        }

        long getOriginalSize() {
                return this.originalSize;
        }

        long getCompressedSize() {
                return this.compressedSize;
        }

        double getBitPerInt() {
                return this.compressedSize * 32.0 / this.originalSize;
        }

        private static double getMiS(long size, long nanoTime) {
                return (size * 1e-6) / (nanoTime * 1.0e-9);
        }

        double getCompressSpeed() {
                return getMiS(this.originalSize,
                        this.compressionTimer.getDuration());
        }

        double getDecompressSpeed() {
                return getMiS(this.originalSize,
                        this.decompressionTimer.getDuration());
        }
}
