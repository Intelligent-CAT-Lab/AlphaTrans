
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


package org.apache.commons.codec.digest;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.codec.digest.MurmurHash2;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MurmurHash2_ESTest extends MurmurHash2_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash643("", (-538903421), 1047936355);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash323("", 0, 1717);
        fail("Expecting exception: StringIndexOutOfBoundsException");
      
      } catch(StringIndexOutOfBoundsException e) {
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      long long0 = MurmurHash2.hash643(")oXS'jH", 1, 1);
      assertEquals(3710105625432625567L, long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      byteArray0[0] = (byte)101;
      long long0 = MurmurHash2.hash641(byteArray0, (byte)1);
      assertEquals(8982822323587011191L, long0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      long long0 = MurmurHash2.hash641(byteArray0, 0);
      assertEquals((-7207201254813729732L), long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      byteArray0[0] = (byte)1;
      long long0 = MurmurHash2.hash640(byteArray0, (byte)6, (byte)1);
      assertEquals((-3785491983369535334L), long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      int int0 = MurmurHash2.hash323("org.apache.commons.codec.digest.MurmurHash2", 0, 0);
      assertEquals(275646681, int0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      int int0 = MurmurHash2.hash323("org.apache.commons.codec.digest.MurmurHash2", 7, 7);
      assertEquals((-1313868537), int0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      int int0 = MurmurHash2.hash322(" 3Ux");
      assertEquals(40297033, int0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[0] = (byte) (-108);
      int int0 = MurmurHash2.hash321(byteArray0, (byte)1);
      assertEquals((-40725216), int0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      int int0 = MurmurHash2.hash320(byteArray0, 0, (byte)54);
      assertEquals(1581775328, int0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      int int0 = MurmurHash2.hash320(byteArray0, 0, 16);
      assertEquals((-1121983635), int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash643((String) null, (-94), (-94));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash642((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash641((byte[]) null, 974);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash322((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash321((byte[]) null, 807);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        MurmurHash2.hash321(byteArray0, 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-1), (-4173));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 2
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-1869), (-1869));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1870 out of bounds for length 10
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-64011636), (-64011636));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -64011637 out of bounds for length 1
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-2555), (byte)16);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2556 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-294), (byte) (-78));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -295 out of bounds for length 4
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      long long0 = MurmurHash2.hash640(byteArray0, (byte)6, (byte)1);
      assertEquals(6496968449332415600L, long0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      byte[] byteArray0 = new byte[14];
      // Undeclared exception!
      try { 
        MurmurHash2.hash640(byteArray0, (-1887), (-1887));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1888 out of bounds for length 14
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash640((byte[]) null, 940, 940);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        MurmurHash2.hash320(byteArray0, (-2965), 2173);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2966 out of bounds for length 2
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash320((byte[]) null, 1, 1);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      // Undeclared exception!
      try { 
        MurmurHash2.hash320(byteArray0, (-2950), 2173);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2951 out of bounds for length 2
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        MurmurHash2.hash320(byteArray0, 296, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4 out of bounds for length 4
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      int int0 = MurmurHash2.hash320(byteArray0, 0, (byte)0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        MurmurHash2.hash641(byteArray0, 1809);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 0 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      long long0 = MurmurHash2.hash640((byte[]) null, 0, 0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      long long0 = MurmurHash2.hash642("eAt.phv3h;#}3m6");
      assertEquals(3195875775987614497L, long0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      long long0 = MurmurHash2.hash642(".Z,V8%");
      assertEquals((-7614162413214632062L), long0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      long long0 = MurmurHash2.hash642("Hnv]qBeD/!$\"zp Vv7");
      assertEquals((-3105253281641488939L), long0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      int int0 = MurmurHash2.hash321(byteArray0, (-1756908916));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      int int0 = MurmurHash2.hash322("Hnv]qBeD/!$\"zp Vv7");
      assertEquals((-1416464607), int0);
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      int int0 = MurmurHash2.hash321(byteArray0, (byte)1);
      assertEquals(375494588, int0);
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      long long0 = MurmurHash2.hash643("org.apache.commons.codec.digest.MurmurHash2", 4, 4);
      assertEquals((-3131028227372647069L), long0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash2.hash323((String) null, (-180), (-180));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash2", e);
      }
  }
}
