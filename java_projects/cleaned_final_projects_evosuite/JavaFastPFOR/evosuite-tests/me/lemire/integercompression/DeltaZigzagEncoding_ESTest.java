
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

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import me.lemire.integercompression.DeltaZigzagEncoding;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DeltaZigzagEncoding_ESTest extends DeltaZigzagEncoding_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(500);
      // Undeclared exception!
      try { 
        deltaZigzagEncoding_Decoder0.decodeArray1((int[]) null, 500, 500);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Decoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(772);
      int[] intArray0 = new int[8];
      intArray0[7] = 3363;
      int[] intArray1 = deltaZigzagEncoding_Decoder0.decodeArray2(intArray0);
      assertArrayEquals(new int[] {772, 772, 772, 772, 772, 772, 772, (-910)}, intArray1);
      assertEquals(8, intArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder((-606));
      int int0 = deltaZigzagEncoding_Decoder0.decodeInt((-606));
      assertEquals(2147482739, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(822);
      int[] intArray0 = new int[4];
      int[] intArray1 = deltaZigzagEncoding_Encoder0.encodeArray1(intArray0, (-1), (-488), intArray0);
      assertSame(intArray1, intArray0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(772);
      deltaZigzagEncoding_Decoder0.setContextValue((-2523));
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(772);
      int int0 = deltaZigzagEncoding_Encoder0.encodeInt(533);
      assertEquals(477, int0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int[] intArray0 = new int[8];
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(772);
      int[] intArray1 = deltaZigzagEncoding_Encoder0.encodeArray0(intArray0, (-833), (-628), intArray0, 0);
      assertSame(intArray0, intArray1);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(772);
      int[] intArray0 = new int[8];
      int[] intArray1 = deltaZigzagEncoding_Decoder0.decodeArray1(intArray0, (-980), 0);
      assertEquals(0, intArray1.length);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(1);
      int[] intArray0 = new int[9];
      int[] intArray1 = deltaZigzagEncoding_Decoder0.decodeArray0(intArray0, 1498, (-1608), intArray0, 875);
      assertSame(intArray0, intArray1);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DeltaZigzagEncoding deltaZigzagEncoding0 = new DeltaZigzagEncoding();
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DeltaZigzagEncoding.Context deltaZigzagEncoding_Context0 = new DeltaZigzagEncoding.Context((-1));
      int int0 = deltaZigzagEncoding_Context0.getContextValue();
      assertEquals((-1), int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      DeltaZigzagEncoding.Decoder deltaZigzagEncoding_Decoder0 = new DeltaZigzagEncoding.Decoder(772);
      int[] intArray0 = new int[8];
      int[] intArray1 = deltaZigzagEncoding_Decoder0.decodeArray2(intArray0);
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(772);
      int[] intArray2 = deltaZigzagEncoding_Encoder0.encodeArray1(intArray1, (-1), (-1), intArray0);
      assertArrayEquals(new int[] {772, 772, 772, 772, 772, 772, 772, 772}, intArray1);
      assertSame(intArray2, intArray0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      int[] intArray0 = new int[9];
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(23);
      // Undeclared exception!
      try { 
        deltaZigzagEncoding_Encoder0.encodeArray2(intArray0, 2095, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2095 out of bounds for length 9
         //
         verifyException("me.lemire.integercompression.DeltaZigzagEncoding$Encoder", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      int[] intArray0 = new int[9];
      DeltaZigzagEncoding.Encoder deltaZigzagEncoding_Encoder0 = new DeltaZigzagEncoding.Encoder(1);
      int[] intArray1 = deltaZigzagEncoding_Encoder0.encodeArray3(intArray0);
      assertArrayEquals(new int[] {1, 0, 0, 0, 0, 0, 0, 0, 0}, intArray1);
  }
}
