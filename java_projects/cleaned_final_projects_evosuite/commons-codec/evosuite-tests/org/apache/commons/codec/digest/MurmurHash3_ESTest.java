
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
import org.apache.commons.codec.digest.MurmurHash3;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class MurmurHash3_ESTest extends MurmurHash3_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      byte[] byteArray1 = new byte[8];
      byteArray1[5] = (byte)3;
      murmurHash3_IncrementalHash32x86_0.add(byteArray1, (byte)3, (byte)3);
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)3, (byte)3);
      assertEquals(70885486, murmurHash3_IncrementalHash32x86_0.end());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte)1;
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, (byte)1);
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, (byte)1);
      // Undeclared exception!
      try { 
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)0, 416);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 2 out of bounds for length 2
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte)1;
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, (byte)1);
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, (byte)1);
      int int0 = murmurHash3_IncrementalHash32x86_0.end();
      assertEquals(1107827355, int0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      byte[] byteArray0 = new byte[9];
      byteArray0[2] = (byte)58;
      int int0 = murmurHash3_IncrementalHash32x86_0.finalise(3, 3, byteArray0, (byte) (-89));
      assertEquals(127983477, int0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      byte[] byteArray0 = new byte[3];
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)0, (byte)0);
      assertEquals(0, murmurHash3_IncrementalHash32x86_0.end());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[6] = (byte)12;
      long long0 = MurmurHash3.hash643(byteArray0);
      assertEquals(5685171064728034281L, long0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      byteArray0[3] = (byte) (-24);
      long long0 = MurmurHash3.hash643(byteArray0);
      assertEquals((-596032900876998572L), long0);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      byte[] byteArray0 = new byte[16];
      long long0 = MurmurHash3.hash643(byteArray0);
      assertEquals((-4879355010014097355L), long0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      long long0 = MurmurHash3.hash642((short) (-6359));
      assertEquals(4148648213518644761L, long0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      long long0 = MurmurHash3.hash642((short)1);
      assertEquals((-3032679231428807052L), long0);
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      long long0 = MurmurHash3.hash640(2862933555777941757L);
      assertEquals(7977142960040688617L, long0);
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[5] = (byte)1;
      int int0 = MurmurHash3.hash32x860(byteArray0);
      assertEquals(1920566328, int0);
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[6] = (byte)7;
      int int0 = MurmurHash3.hash32x860(byteArray0);
      assertEquals(499142092, int0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[4] = (byte) (-3);
      byteArray0[5] = (byte)81;
      int int0 = MurmurHash3.hash324(byteArray0);
      assertEquals(1011453179, int0);
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[5] = (byte) (-1);
      byteArray0[6] = (byte)51;
      int int0 = MurmurHash3.hash324(byteArray0);
      assertEquals(1626078053, int0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, (byte)1);
      // Undeclared exception!
      try { 
        murmurHash3_IncrementalHash32x86_0.add(byteArray0, (byte)1, 223);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      long long0 = MurmurHash3.hash645(byteArray0, 0, (byte)0, (-2390));
      assertEquals(1593541470847758467L, long0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      long long0 = MurmurHash3.hash644(byteArray0, (byte)12, 0);
      assertEquals(8404154273843829576L, long0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      long long0 = MurmurHash3.hash641(3157);
      assertEquals((-6634736834468170140L), long0);
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      int int0 = MurmurHash3.hash32x861((byte[]) null, (-569), 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      int int0 = MurmurHash3.hash32x861(byteArray0, (byte)111, (byte)0, (-1613));
      assertEquals(583805940, int0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      int int0 = MurmurHash3.hash32x860(byteArray0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      int int0 = MurmurHash3.hash328(byteArray0, (byte)11, 0, (-655));
      assertEquals(1603053134, int0);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      int int0 = MurmurHash3.hash328(byteArray0, 32, 0, 908);
      assertEquals((-1301097675), int0);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      int int0 = MurmurHash3.hash327(byteArray0, 0, 0);
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      byteArray0[1] = (byte)16;
      int int0 = MurmurHash3.hash327(byteArray0, 2, (-1));
      assertEquals(2064155002, int0);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      byteArray0[0] = (byte)1;
      int int0 = MurmurHash3.hash327(byteArray0, 1, 0);
      assertEquals((-463810133), int0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      int int0 = MurmurHash3.hash326(byteArray0, 1);
      assertEquals(500407381, int0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      int int0 = MurmurHash3.hash326(byteArray0, 6);
      assertEquals((-380548134), int0);
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      int int0 = MurmurHash3.hash325("");
      assertEquals((-965378730), int0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[4] = (byte) (-3);
      int int0 = MurmurHash3.hash324(byteArray0);
      assertEquals((-1763601783), int0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      int int0 = MurmurHash3.hash323(1861685801266829510L, (-3390));
      assertEquals((-777887350), int0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      int int0 = MurmurHash3.hash322(23);
      assertEquals(1561548038, int0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      int int0 = MurmurHash3.hash321(104729L, (byte)12, (byte) (-35));
      assertEquals(428332708, int0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      int int0 = MurmurHash3.hash320(1L, 1L);
      assertEquals(1037298354, int0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      long[] longArray0 = MurmurHash3.hash128x641(byteArray0, 0, 0, (byte)1);
      assertArrayEquals(new long[] {5048724184180415669L, 5864299874987029891L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      long[] longArray0 = MurmurHash3.hash1282(byteArray0, 0, 0, 0);
      assertArrayEquals(new long[] {0L, 0L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      // Undeclared exception!
      try { 
        MurmurHash3.hash644(byteArray0, 4684, 4684);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 4684 out of bounds for length 10
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash643((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash32x860((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        MurmurHash3.hash327(byteArray0, (short) (-1), 24);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 9
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash325((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash324((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash128x641((byte[]) null, 7, (-83), (-83));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash128x640((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      // Undeclared exception!
      try { 
        MurmurHash3.hash1282(byteArray0, (-40), (-40), (-40));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -81 out of bounds for length 8
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash1280((byte[]) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      long long0 = MurmurHash3.hash645(byteArray0, (byte)0, (byte)0, (byte)0);
      assertEquals(0L, long0);
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, (byte)21, (-3390), (-777887350));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3370 out of bounds for length 1
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      long long0 = MurmurHash3.hash645(byteArray0, (byte)0, 1, 371);
      assertEquals((-6112031723299314685L), long0);
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, (byte) (-12), (-332), (byte) (-12));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -345 out of bounds for length 4
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test51()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, (byte)0, (-291), 2658);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -292 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test52()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, (byte)16, (-2048144789), 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2048144774 out of bounds for length 5
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test53()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, (byte)0, (short) (-2), 13);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test54()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash645((byte[]) null, 7, 7, 7);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test55()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        MurmurHash3.hash32x861(byteArray0, (-1067), 1, (byte) (-59));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1067 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test56()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash3.hash32x861(byteArray0, (byte)0, (-1162), (byte)0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -1163 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test57()  throws Throwable  {
      byte[] byteArray0 = new byte[14];
      int int0 = MurmurHash3.hash32x861(byteArray0, 51, (byte)0, (short) (-1));
      assertEquals((-2114883783), int0);
  }

  @Test(timeout = 4000)
  public void test58()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      // Undeclared exception!
      try { 
        MurmurHash3.hash32x861(byteArray0, (byte)0, (byte) (-1), 920);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -2 out of bounds for length 3
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test59()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash32x861((byte[]) null, (-982), 56, 56);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test60()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      int int0 = MurmurHash3.hash328(byteArray0, 0, (-332), (-332));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test61()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      // Undeclared exception!
      try { 
        MurmurHash3.hash328(byteArray0, 4, (-3410), (-1));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -3407 out of bounds for length 5
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test62()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash3.hash328(byteArray0, (byte)81, 1, 1);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 81 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test63()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      // Undeclared exception!
      try { 
        MurmurHash3.hash328(byteArray0, 877, (byte)78, (-2120));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 877 out of bounds for length 9
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test64()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash328((byte[]) null, (-154936693), (-154936693), (-154936693));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test65()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash327((byte[]) null, (byte)1, (short) (-1));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test66()  throws Throwable  {
      int int0 = MurmurHash3.hash321((-589L), (-1867L), 2422);
      assertEquals((-287202861), int0);
  }

  @Test(timeout = 4000)
  public void test67()  throws Throwable  {
      byte[] byteArray0 = new byte[11];
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      int int0 = murmurHash3_IncrementalHash32x86_0.finalise(1, 1, byteArray0, 366678052);
      assertEquals(0, murmurHash3_IncrementalHash32x86_0.end());
      assertEquals(1384765200, int0);
  }

  @Test(timeout = 4000)
  public void test68()  throws Throwable  {
      byte[] byteArray0 = new byte[15];
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, 4, 4);
      assertEquals(593689054, murmurHash3_IncrementalHash32x86_0.end());
  }

  @Test(timeout = 4000)
  public void test69()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      murmurHash3_IncrementalHash32x86_0.add(byteArray0, (-111685489), (-111685489));
      assertEquals(9, byteArray0.length);
  }

  @Test(timeout = 4000)
  public void test70()  throws Throwable  {
      byte[] byteArray0 = new byte[15];
      long[] longArray0 = MurmurHash3.hash128x640(byteArray0);
      assertArrayEquals(new long[] {7845573677149415537L, 1826583217152429490L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test71()  throws Throwable  {
      long[] longArray0 = MurmurHash3.hash1281("HM#t'ZNV2*!g/O");
      assertArrayEquals(new long[] {8024476854106698359L, (-8822075722905644794L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test72()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      // Undeclared exception!
      try { 
        MurmurHash3.hash128x641(byteArray0, (-19), (-19), (-19));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index -39 out of bounds for length 0
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test73()  throws Throwable  {
      long[] longArray0 = MurmurHash3.hash1281("{T5Eq=bC0uG");
      assertArrayEquals(new long[] {(-5529662467487770005L), (-1451557616180753302L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test74()  throws Throwable  {
      long[] longArray0 = MurmurHash3.hash1281("org.apache.commons.codec.digest.MurmurHash3");
      assertArrayEquals(new long[] {7857037817036204021L, 6968258762365418411L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test75()  throws Throwable  {
      byte[] byteArray0 = new byte[10];
      long[] longArray0 = MurmurHash3.hash1280(byteArray0);
      assertArrayEquals(new long[] {7063875085384484892L, (-6037316431886049400L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test76()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      long[] longArray0 = MurmurHash3.hash1280(byteArray0);
      assertArrayEquals(new long[] {(-2613151768389018909L), 2529546424875844979L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test77()  throws Throwable  {
      byte[] byteArray0 = new byte[6];
      long[] longArray0 = MurmurHash3.hash1280(byteArray0);
      assertArrayEquals(new long[] {8735115895426159728L, 5193896931062123826L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test78()  throws Throwable  {
      long[] longArray0 = MurmurHash3.hash1281("KZ;oW");
      assertArrayEquals(new long[] {(-374753840059279731L), 2265938371139162254L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test79()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      long[] longArray0 = MurmurHash3.hash128x640(byteArray0);
      assertArrayEquals(new long[] {8779008611884021576L, 789792335023450397L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test80()  throws Throwable  {
      long[] longArray0 = MurmurHash3.hash1281("VH");
      assertArrayEquals(new long[] {1621193727033521071L, 8283586221036498362L}, longArray0);
  }

  @Test(timeout = 4000)
  public void test81()  throws Throwable  {
      byte[] byteArray0 = new byte[11];
      long long0 = MurmurHash3.hash644(byteArray0, (-1), (-920));
      assertEquals((-290380851590073214L), long0);
  }

  @Test(timeout = 4000)
  public void test82()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      int int0 = MurmurHash3.hash32x860(byteArray0);
      assertEquals(1669671676, int0);
  }

  @Test(timeout = 4000)
  public void test83()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      int int0 = MurmurHash3.hash32x860(byteArray0);
      assertEquals((-720425247), int0);
  }

  @Test(timeout = 4000)
  public void test84()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash326((byte[]) null, (short) (-2707));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test85()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      murmurHash3_IncrementalHash32x86_0.start(1109);
      assertEquals(1161923513, murmurHash3_IncrementalHash32x86_0.end());
  }

  @Test(timeout = 4000)
  public void test86()  throws Throwable  {
      MurmurHash3.IncrementalHash32x86 murmurHash3_IncrementalHash32x86_0 = new MurmurHash3.IncrementalHash32x86();
      int int0 = murmurHash3_IncrementalHash32x86_0.end();
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test87()  throws Throwable  {
      byte[] byteArray0 = new byte[11];
      // Undeclared exception!
      try { 
        MurmurHash3.hash645(byteArray0, 366678052, 366678052, 366678052);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 366678052 out of bounds for length 11
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test88()  throws Throwable  {
      long long0 = MurmurHash3.hash640(0L);
      assertEquals((-8620514229188030809L), long0);
  }

  @Test(timeout = 4000)
  public void test89()  throws Throwable  {
      int int0 = MurmurHash3.hash322(2046551812);
      assertEquals((-1093777662), int0);
  }

  @Test(timeout = 4000)
  public void test90()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      long[] longArray0 = MurmurHash3.hash1280(byteArray0);
      assertArrayEquals(new long[] {4237109858264490658L, (-3654202066835248170L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test91()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash1282((byte[]) null, (-862048943), (-862048943), (-862048943));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test92()  throws Throwable  {
      long long0 = MurmurHash3.hash641((byte) (-89));
      assertEquals(1877368944204863702L, long0);
  }

  @Test(timeout = 4000)
  public void test93()  throws Throwable  {
      int int0 = MurmurHash3.hash320((-1794L), (-1794L));
      assertEquals((-154936693), int0);
  }

  @Test(timeout = 4000)
  public void test94()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash1281((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test95()  throws Throwable  {
      byte[] byteArray0 = new byte[9];
      long[] longArray0 = MurmurHash3.hash128x640(byteArray0);
      assertArrayEquals(new long[] {8297479994805284640L, (-1010425036434519540L)}, longArray0);
  }

  @Test(timeout = 4000)
  public void test96()  throws Throwable  {
      int int0 = MurmurHash3.hash325("^=Ci");
      assertEquals(269472428, int0);
  }

  @Test(timeout = 4000)
  public void test97()  throws Throwable  {
      int int0 = MurmurHash3.hash323(1331L, 2046551812);
      assertEquals(758345217, int0);
  }

  @Test(timeout = 4000)
  public void test98()  throws Throwable  {
      // Undeclared exception!
      try { 
        MurmurHash3.hash644((byte[]) null, (short)1671, (-3090));
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }

  @Test(timeout = 4000)
  public void test99()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      // Undeclared exception!
      try { 
        MurmurHash3.hash326(byteArray0, 630838780);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 7 out of bounds for length 7
         //
         verifyException("org.apache.commons.codec.digest.MurmurHash3", e);
      }
  }
}
