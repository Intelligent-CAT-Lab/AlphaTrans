
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
 * Helper class to compose schemes.
 * 
 * @author Daniel Lemire
 */
public class SkippableComposition implements SkippableIntegerCODEC {
    SkippableIntegerCODEC F1, F2;

    /**
     * Compose a scheme from a first one (f1) and a second one (f2). The first
     * one is called first and then the second one tries to compress whatever
     * remains from the first run.
     * 
     * By convention, the first scheme should be such that if, during decoding,
     * a 32-bit zero is first encountered, then there is no output.
     * 
     * @param f1
     *            first codec
     * @param f2
     *            second codec
     */
    public SkippableComposition(SkippableIntegerCODEC f1,
            SkippableIntegerCODEC f2) {
        F1 = f1;
        F2 = f2;
    }

    @Override
    public void headlessCompress(int[] in, IntWrapper inpos, int inlength, int[] out,
            IntWrapper outpos) {
        int init = inpos.get();
        int outposInit = outpos.get();
        F1.headlessCompress(in, inpos, inlength, out, outpos);
        if (outpos.get() == outposInit) {
            out[outposInit] = 0;
            outpos.increment();
        }
        inlength -= inpos.get() - init;
        F2.headlessCompress(in, inpos, inlength, out, outpos);
    }

    @Override
    public void headlessUncompress(int[] in, IntWrapper inpos, int inlength, int[] out,
            IntWrapper outpos, int num) {
        int init = inpos.get();
        F1.headlessUncompress(in, inpos, inlength, out, outpos, num);
        if (inpos.get() == init) {
        	  inpos.increment();
        }
        inlength -= inpos.get() - init;
        num -= outpos.get();
        F2.headlessUncompress(in, inpos, inlength, out, outpos, num);
    }

    @Override
    public String toString() {
        return F1.toString() + "+" + F2.toString();
    }

}
