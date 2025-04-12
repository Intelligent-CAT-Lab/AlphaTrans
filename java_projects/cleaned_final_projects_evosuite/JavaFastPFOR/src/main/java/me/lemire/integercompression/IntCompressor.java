package me.lemire.integercompression;

import java.util.Arrays;


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

public class IntCompressor {


    SkippableIntegerCODEC codec;
    /**
     * Constructor wrapping a codec.
     * 
     * @param c the underlying codec
     */
//     public IntCompressor(SkippableIntegerCODEC c) {
//       codec = c;
//     }
    
    /**
     * Constructor with default codec.
     */
public IntCompressor(int constructorId, SkippableIntegerCODEC c) {
    if (constructorId == 0) {

      codec = c;
        }
    else {

        codec = new SkippableComposition(new BinaryPacking(),
                new VariableByte());
        }
}
//     public IntCompressor() {
//         codec = new SkippableComposition(new BinaryPacking(),
//                 new VariableByte());
//     }

    /**
     * Compress an array and returns the compressed result as a new array.
     * 
     * @param input array to be compressed
     * @return compressed array
     * @throws UncompressibleInputException if the data is too poorly compressible
     */
    public  int[] compress(int[] input) {
        int [] compressed = new int[input.length + input.length / 100 + 1024];
        compressed[0] = input.length;
        IntWrapper outpos = new IntWrapper(1);
        try {
            codec.headlessCompress(input, new IntWrapper(0),
                    input.length, compressed, outpos);
        } catch (IndexOutOfBoundsException ioebe) {
            throw new
            UncompressibleInputException("Your input is too poorly compressible "
                    + "with the current codec : "+codec);
        }
        compressed = Arrays.copyOf(compressed,outpos.intValue());
        return compressed;
    }

    /**
     * Uncompress an array and returns the uncompressed result as a new array.
     * 
     * @param compressed compressed array
     * @return uncompressed array
     */
    public int[] uncompress(int[] compressed) {
        int[] decompressed = new int[compressed[0]];
        IntWrapper inpos = new IntWrapper(1);
        codec.headlessUncompress(compressed, inpos, 
                compressed.length - inpos.intValue(), 
                decompressed, new IntWrapper(0), 
                decompressed.length);
        return decompressed;
    }

}
