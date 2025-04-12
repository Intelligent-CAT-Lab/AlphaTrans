
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


package org.apache.commons.codec.net;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import org.apache.commons.codec.net.PercentCodec;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class PercentCodec_ESTest extends PercentCodec_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      byteArray0[0] = (byte)67;
      PercentCodec percentCodec0 = new PercentCodec(0, true, byteArray0);
      byte[] byteArray1 = percentCodec0.decode0(byteArray0);
      assertArrayEquals(new byte[] {(byte)67}, byteArray1);
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[0] = (byte) (-40);
      PercentCodec percentCodec0 = new PercentCodec(537, false, byteArray0);
      byte[] byteArray1 = percentCodec0.encode(byteArray0);
      byte[] byteArray2 = percentCodec0.decode(byteArray1);
      assertArrayEquals(new byte[] {(byte) (-40), (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray2);
      assertEquals(9, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = new byte[7];
      byteArray1[1] = (byte)89;
      byte[] byteArray2 = percentCodec0.encode(byteArray1);
      assertSame(byteArray2, byteArray1);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      byteArray0[0] = (byte)17;
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      PercentCodec percentCodec0 = new PercentCodec(0, false, (byte[]) null);
      byte[] byteArray0 = percentCodec0.encode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec(361, true, byteArray0);
      byte[] byteArray1 = percentCodec0.encode(byteArray0);
      assertSame(byteArray1, byteArray0);
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec((-547), false, byteArray0);
      byte[] byteArray1 = percentCodec0.decode0(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      PercentCodec percentCodec0 = new PercentCodec(0, false, (byte[]) null);
      byte[] byteArray0 = percentCodec0.decode((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec((-1636), false, byteArray0);
      byte[] byteArray1 = percentCodec0.decode(byteArray0);
      assertEquals(0, byteArray1.length);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      byte[] byteArray0 = new byte[2];
      byteArray0[1] = (byte)37;
      PercentCodec percentCodec0 = new PercentCodec(1067, true, byteArray0);
      try { 
        percentCodec0.decode0(byteArray0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid percent decoding: 
         //
         verifyException("org.apache.commons.codec.net.PercentCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec((-547), false, byteArray0);
      byte[] byteArray1 = new byte[2];
      byteArray1[0] = (byte)37;
      try { 
        percentCodec0.decode(byteArray1);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Invalid URL encoding: not a valid digit (radix 16): 0
         //
         verifyException("org.apache.commons.codec.net.Utils", e);
      }
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      byte[] byteArray0 = new byte[4];
      byteArray0[0] = (byte) (-3);
      PercentCodec percentCodec0 = null;
      try {
        percentCodec0 = new PercentCodec(0, true, byteArray0);
        fail("Expecting exception: IndexOutOfBoundsException");
      
      } catch(IndexOutOfBoundsException e) {
         //
         // bitIndex < 0: -3
         //
         verifyException("java.util.BitSet", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      byte[] byteArray0 = new byte[8];
      PercentCodec percentCodec0 = new PercentCodec(3404, true, byteArray0);
      Object object0 = percentCodec0.decode1((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      byte[] byteArray0 = new byte[18];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, false, byteArray0);
      try { 
        percentCodec0.decode1(percentCodec0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type org.apache.commons.codec.net.PercentCodec cannot be Percent decoded
         //
         verifyException("org.apache.commons.codec.net.PercentCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec(0, false, byteArray0);
      Object object0 = percentCodec0.encode1((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      Object object0 = new Object();
      try { 
        percentCodec0.encode1(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be Percent encoded
         //
         verifyException("org.apache.commons.codec.net.PercentCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      byte[] byteArray0 = new byte[0];
      PercentCodec percentCodec0 = new PercentCodec(2611, true, byteArray0);
      byte[] byteArray1 = percentCodec0.encode0(byteArray0);
      assertSame(byteArray1, byteArray0);
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      Object object0 = new Object();
      try { 
        percentCodec0.decode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be Percent decoded
         //
         verifyException("org.apache.commons.codec.net.PercentCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      byte[] byteArray0 = new byte[1];
      PercentCodec percentCodec0 = new PercentCodec(0, true, byteArray0);
      Object object0 = new Object();
      try { 
        percentCodec0.encode(object0);
        fail("Expecting exception: Exception");
      
      } catch(Exception e) {
         //
         // Objects of type java.lang.Object cannot be Percent encoded
         //
         verifyException("org.apache.commons.codec.net.PercentCodec", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      byte[] byteArray0 = new byte[3];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = new byte[3];
      byteArray1[2] = (byte)43;
      byte[] byteArray2 = percentCodec0.decode0(byteArray1);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)32}, byteArray2);
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = percentCodec0.encode0(byteArray0);
      byte[] byteArray2 = percentCodec0.decode(byteArray1);
      assertEquals(21, byteArray1.length);
      assertEquals(7, byteArray2.length);
      assertArrayEquals(new byte[] {(byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0, (byte)0}, byteArray2);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      PercentCodec percentCodec0 = new PercentCodec(1301, true, (byte[]) null);
      byte[] byteArray0 = percentCodec0.decode0((byte[]) null);
      assertNull(byteArray0);
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = percentCodec0.encode0(byteArray0);
      byte[] byteArray2 = percentCodec0.encode0(byteArray1);
      assertEquals(35, byteArray2.length);
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = new byte[7];
      byteArray1[3] = (byte)14;
      byte[] byteArray2 = percentCodec0.encode0(byteArray1);
      assertEquals(19, byteArray2.length);
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, true, byteArray0);
      byte[] byteArray1 = new byte[7];
      byteArray1[0] = (byte)32;
      byte[] byteArray2 = percentCodec0.encode0(byteArray1);
      assertEquals(19, byteArray2.length);
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      byte[] byteArray0 = new byte[5];
      PercentCodec percentCodec0 = new PercentCodec((byte)0, false, byteArray0);
      byte[] byteArray1 = percentCodec0.encode0((byte[]) null);
      assertNull(byteArray1);
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      PercentCodec percentCodec0 = new PercentCodec(0, true, (byte[]) null);
      byte[] byteArray0 = new byte[10];
      byte[] byteArray1 = percentCodec0.encode0(byteArray0);
      assertSame(byteArray1, byteArray0);
      assertNotNull(byteArray1);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec(1293, true, byteArray0);
      Object object0 = percentCodec0.decode((Object) null);
      assertNull(object0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      byte[] byteArray0 = new byte[7];
      PercentCodec percentCodec0 = new PercentCodec(1293, true, byteArray0);
      Object object0 = percentCodec0.encode((Object) null);
      assertNull(object0);
  }
}
