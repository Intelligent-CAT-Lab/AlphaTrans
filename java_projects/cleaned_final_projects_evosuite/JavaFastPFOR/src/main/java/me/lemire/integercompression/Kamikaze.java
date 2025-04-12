package me.lemire.integercompression;

import com.kamikaze.pfordelta.PForDelta;


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

public class Kamikaze implements SkippableIntegerCODEC, IntegerCODEC {

    private int BLOCK_SIZE = 128;

    @Override
    public void headlessCompress(int[] in, IntWrapper inpos, int inlength, int[] out,
            IntWrapper outpos) {
        inlength = Util.greatestMultiple(inlength, BLOCK_SIZE);
        if (inlength > 0) {
            int[] out2 = PForDelta.compressOneBlockOpt(in, inlength);
            inpos.add(inlength);
            System.arraycopy(out2, 0, out, outpos.get(), out2.length);
            outpos.add(out2.length);
        }
    }

    @Override
    public void headlessUncompress(int[] in, IntWrapper inpos, int inlength, int[] out,
            IntWrapper outpos, int num) {
        num = Util.greatestMultiple(num, BLOCK_SIZE);
        if (num > 0) {
            int d = PForDelta.decompressOneBlock(out, in, num);
            inpos.add(d / 32);
            outpos.add(num);
        }
    }

    @Override
    public String toString() {
        return "Kamikaze's PForDelta";
    }

    @Override
    public void compress0(int[] in, IntWrapper inpos, int inlength, int[] out,
                          IntWrapper outpos) {
        inlength = Util.greatestMultiple(inlength, BLOCK_SIZE);
        if (inlength == 0)
                return;
        out[outpos.get()] = inlength;
        outpos.increment();
        headlessCompress(in, inpos, inlength, out, outpos);        
    }

    @Override
    public void uncompress0(int[] in, IntWrapper inpos, int inlength, int[] out,
                            IntWrapper outpos) {
        if (inlength == 0)
            return;
        final int outlength = in[inpos.get()];
        inpos.increment();
        headlessUncompress(in, inpos, inlength, out, outpos, outlength);

    }
}