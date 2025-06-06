



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





package org.apache.commons.csv;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.io.PipedReader;
import java.io.StringReader;
import java.nio.charset.Charset;
import java.nio.file.Path;
import java.util.HashMap;
import java.util.List;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class CSVRecord_ESTest extends CSVRecord_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("', recordNumber=", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.isSet0(2);
      assertFalse(boolean0);
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVParser cSVParser0 = new CSVParser(pipedReader0, cSVFormat0, 2, (-2998L));
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, (String[]) null, "", (-2998L), 2);
      cSVRecord0.values();
      assertEquals(2L, cSVRecord0.getCharacterPosition());
      assertEquals((-2998L), cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4("Default", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      cSVRecord0.toList();
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertEquals(1L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      PipedReader pipedReader0 = new PipedReader();
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVParser cSVParser0 = new CSVParser(pipedReader0, cSVFormat0, 2, (-2998L));
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, (String[]) null, "", (-2998L), 2);
      cSVRecord0.size();
      assertEquals((-2998L), cSVRecord0.getRecordNumber());
      assertEquals(2L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("The comment start marker character cannot be a line break", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      cSVRecord0.putIn(hashMap0);
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_CSV;
      StringReader stringReader0 = new StringReader("'(j,S=d65E5LngZpK");
      CSVParser cSVParser0 = cSVFormat0.parse(stringReader0);
      String[] stringArray0 = new String[1];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, "'(j,S=d65E5LngZpK", 0L, 0L);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      hashMap0.put("dzxj9RRU33YH](zd8k", "'(j,S=d65E5LngZpK");
      HashMap<String, String> hashMap1 = cSVRecord0.putIn(hashMap0);
      assertEquals(1, hashMap1.size());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("", cSVFormat0);
      String[] stringArray0 = new String[2];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, "Index for header '%s' is %d but CSVRecord only has %d values!", 2027L, 2027L);
      cSVRecord0.iterator();
      assertEquals(2027L, cSVRecord0.getCharacterPosition());
      assertEquals(2027L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      long long0 = cSVRecord0.getRecordNumber();
      assertEquals(1L, long0);
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      StringReader stringReader0 = new StringReader("cs,t/kCu");
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVParser cSVParser0 = new CSVParser(stringReader0, cSVFormat0, 1L, (-2748L));
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      long long0 = cSVRecord0.getRecordNumber();
      assertEquals(1L, cSVRecord0.getCharacterPosition());
      assertEquals((-2748L), long0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      String[] stringArray0 = new String[4];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "Index for header '%s' is %d but CSVRecord only has %d values!", 2027L, 2027L);
      cSVRecord0.getParser();
      assertEquals(2027L, cSVRecord0.getCharacterPosition());
      assertEquals(2027L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("", cSVFormat0);
      String[] stringArray0 = new String[5];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, (String) null, (-822L), 0L);
      cSVRecord0.getParser();
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertEquals((-822L), cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      String[] stringArray0 = new String[9];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "$VALUES", (-448L), (-448L));
      cSVRecord0.getComment();
      assertEquals((-448L), cSVRecord0.getRecordNumber());
      assertEquals((-448L), cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4("", cSVFormat0);
      String[] stringArray0 = new String[2];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, "Index for header '%s' is %d but CSVRecord only has %d values!", 2027L, 2027L);
      long long0 = cSVRecord0.getCharacterPosition();
      assertEquals(2027L, cSVRecord0.getRecordNumber());
      assertEquals(2027L, long0);
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      String[] stringArray0 = new String[5];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "W2T^[eSjIU8K@~kn", (-2665L), (-2665L));
      long long0 = cSVRecord0.getCharacterPosition();
      assertEquals((-2665L), long0);
      assertEquals((-2665L), cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_CSV;
      StringReader stringReader0 = new StringReader("'(j,S=d65E5LngZpK");
      CSVParser cSVParser0 = cSVFormat0.parse(stringReader0);
      String[] stringArray0 = new String[1];
      stringArray0[0] = "'(j,S=d65E5LngZpK";
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, "'(j,S=d65E5LngZpK", 0L, 0L);
      String string0 = cSVRecord0.get1(0);
      assertEquals("'(j,S=d65E5LngZpK", string0);
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      String[] stringArray0 = new String[2];
      stringArray0[0] = "";
      stringArray0[1] = "";
      Path path0 = Path.of("", stringArray0);
      Charset charset0 = Charset.defaultCharset();
      CSVFormat cSVFormat0 = CSVFormat.MONGODB_TSV;
      CSVParser cSVParser0 = CSVParser.parse2(path0, charset0, cSVFormat0);
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, "", (-1L), (-1L));
      cSVRecord0.get1(0);
      assertEquals((-1L), cSVRecord0.getRecordNumber());
      assertEquals((-1L), cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      StringReader stringReader0 = new StringReader("cs,t/kCu");
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVParser cSVParser0 = new CSVParser(stringReader0, cSVFormat0, 1658L, 1658L);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      cSVRecord0.putIn((HashMap<String, String>) null);
      assertEquals(1658L, cSVRecord0.getRecordNumber());
      assertEquals(1658L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("\"6^", cSVFormat0);
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, (String[]) null, "", 0L, 0L);
      boolean boolean0 = cSVRecord0.isMapped("");
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      String[] stringArray0 = new String[9];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "$VALUES", (-448L), (-448L));
      cSVRecord0.stream();
      assertEquals((-448L), cSVRecord0.getCharacterPosition());
      assertEquals((-448L), cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, (String[]) null, "", 0L, 0L);
      List<String> list0 = cSVRecord0.toList();
      assertEquals(0, list0.size());
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.isSet0(0);
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("The comment start marker character cannot be a line break", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.isSet0(2);
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertFalse(boolean0);
      assertEquals(1, cSVRecord0.size());
      assertEquals(1L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("f-", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.isSet0((-1265));
      assertFalse(boolean0);
      assertEquals(1, cSVRecord0.size());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertEquals(1L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("The comment start marker character cannot be a line break", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.isConsistent();
      assertTrue(boolean0);
      assertEquals(1, cSVRecord0.size());
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      String[] stringArray0 = new String[13];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "", (-460L), (-460L));
      boolean boolean0 = cSVRecord0.hasComment();
      assertTrue(boolean0);
      assertEquals((-460L), cSVRecord0.getRecordNumber());
      assertEquals((-460L), cSVRecord0.getCharacterPosition());
      assertEquals(13, cSVRecord0.size());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      StringReader stringReader0 = new StringReader("cs,t/kCu");
      CSVFormat.Builder cSVFormat_Builder0 = CSVFormat.Builder.create0();
      CSVFormat cSVFormat0 = cSVFormat_Builder0.build();
      CSVParser cSVParser0 = new CSVParser(stringReader0, cSVFormat0, 1658L, 1658L);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      boolean boolean0 = cSVRecord0.hasComment();
      assertFalse(boolean0);
      assertEquals(1658L, cSVRecord0.getCharacterPosition());
      assertEquals(1658L, cSVRecord0.getRecordNumber());
      assertEquals(2, cSVRecord0.size());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      String[] stringArray0 = new String[9];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "$VALUES", 0L, 0L);
      boolean boolean0 = cSVRecord0.isSet1("$VALUES");
      assertEquals(9, cSVRecord0.size());
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      String[] stringArray0 = new String[4];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, ") invalid char between encapsulated token and delimiter", 0L, 0L);
      // Undeclared exception!
      try { 
        cSVRecord0.get2(")1&DZC?O)FpC");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // No header mapping was specified, the record values can't be accessed by name
         //
         verifyException("org.apache.commons.csv.CSVRecord", e);
      }
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("\"6^", cSVFormat0);
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, (String[]) null, "", 1083L, 1083L);
      cSVRecord0.getComment();
      assertEquals(1083L, cSVRecord0.getCharacterPosition());
      assertEquals(1083L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.DEFAULT;
      CSVParser cSVParser0 = CSVParser.parse4("The comment start marker character cannot be a line break", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      int int0 = cSVRecord0.size();
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(1, int0);
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      String[] stringArray0 = new String[4];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, ") invalid char between encapsulated token and delimiter", 0L, 0L);
      cSVRecord0.getRecordNumber();
      assertEquals(4, cSVRecord0.size());
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.RFC4180;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      cSVRecord0.getParser();
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
      assertEquals(1, cSVRecord0.size());
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      String[] stringArray0 = new String[5];
      CSVRecord cSVRecord0 = new CSVRecord((CSVParser) null, stringArray0, "W2T^[eSjIU8K@~kn", (-2665L), (-2665L));
      String[] stringArray1 = cSVRecord0.values();
      assertEquals(5, stringArray1.length);
      assertEquals((-2665L), cSVRecord0.getCharacterPosition());
      assertEquals((-2665L), cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      // Undeclared exception!
      try { 
        cSVRecord0.get1(102);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // Index 102 out of bounds for length 1
         //
         verifyException("org.apache.commons.csv.CSVRecord", e);
      }
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      String string0 = cSVRecord0.toString();
      assertEquals("CSVRecord [comment='null', recordNumber=1, values=[) invalid char between encapsulated token and delimiter]]", string0);
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.MYSQL;
      CSVParser cSVParser0 = CSVParser.parse4(") invalid char between encapsulated token and delimiter", cSVFormat0);
      String[] stringArray0 = new String[4];
      CSVRecord cSVRecord0 = new CSVRecord(cSVParser0, stringArray0, ") invalid char between encapsulated token and delimiter", 0L, 0L);
      cSVRecord0.toMap();
      assertEquals(4, cSVRecord0.size());
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("format", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      long long0 = cSVRecord0.getCharacterPosition();
      assertEquals(0L, long0);
      assertEquals(1, cSVRecord0.size());
      assertEquals(1L, cSVRecord0.getRecordNumber());
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      CSVFormat cSVFormat0 = CSVFormat.POSTGRESQL_TEXT;
      CSVParser cSVParser0 = CSVParser.parse4("format", cSVFormat0);
      CSVRecord cSVRecord0 = cSVParser0.nextRecord();
      cSVRecord0.getComment();
      assertEquals(1, cSVRecord0.size());
      assertEquals(1L, cSVRecord0.getRecordNumber());
      assertEquals(0L, cSVRecord0.getCharacterPosition());
  }
}
