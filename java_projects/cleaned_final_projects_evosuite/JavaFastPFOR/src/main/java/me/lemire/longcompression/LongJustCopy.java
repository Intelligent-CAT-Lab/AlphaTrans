
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


package me.lemire.longcompression;

import me.lemire.integercompression.IntWrapper;

/**
 * @author Benoit lacelle
 * 
 */
public final class LongJustCopy implements LongCODEC, SkippableLongCODEC {

        @Override
        public void headlessCompress(long[] in, IntWrapper inpos, int inlength,
        		long[] out, IntWrapper outpos) {
                System.arraycopy(in, inpos.get(), out, outpos.get(), inlength);
                inpos.add(inlength);
                outpos.add(inlength);
        }

        @Override
        public void uncompress1(long[] in, IntWrapper inpos, int inlength,
                                long[] out, IntWrapper outpos) {
            headlessUncompress(in,inpos,inlength,out,outpos,inlength);
        }

        @Override
        public String toString() {
                return this.getClass().getSimpleName();
        }

        @Override
        public void headlessUncompress(long[] in, IntWrapper inpos, int inlength,
        		long[] out, IntWrapper outpos, int num) {
            System.arraycopy(in, inpos.get(), out, outpos.get(), num);
            inpos.add(num);
            outpos.add(num);
            
        }

        @Override
        public void compress0(long[] in, IntWrapper inpos, int inlength,
                              long[] out, IntWrapper outpos) {
            headlessCompress(in,inpos,inlength,out,outpos);
        }

}
