

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



package org.apache.commons.fileupload.disk;

import org.junit.Test;
import static org.junit.Assert.*;
import java.io.File;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.mock.java.io.MockFile;
import org.evosuite.runtime.testdata.EvoSuiteFile;
import org.evosuite.runtime.testdata.FileSystemHandling;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class DiskFileItemFactory_ESTest extends DiskFileItemFactory_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      File file0 = MockFile.createTempFile("org.apache.commons.fileupload.disk.DiskFileItemFactory", "");
      DiskFileItemFactory diskFileItemFactory0 = new DiskFileItemFactory(0, file0);
      int int0 = diskFileItemFactory0.getSizeThreshold();
      assertEquals(0, int0);
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      diskFileItemFactory0.setSizeThreshold((-4440));
      int int0 = diskFileItemFactory0.getSizeThreshold();
      assertEquals((-4440), int0);
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      MockFile mockFile0 = new MockFile(")aqdqM(2!m~WBA4-*??");
      EvoSuiteFile evoSuiteFile0 = new EvoSuiteFile(")aqdqM(2!m~WBA4-*??");
      FileSystemHandling.appendStringToFile(evoSuiteFile0, ")aqdqM(2!m~WBA4-*??");
      diskFileItemFactory0.setRepository(mockFile0);
      diskFileItemFactory0.getRepository();
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      MockFile mockFile0 = new MockFile("zdIj.-=r", "zdIj.-=r");
      MockFile.createTempFile("110(K?GwA9HJ=`", "zdIj.-=r", (File) mockFile0);
      diskFileItemFactory0.setRepository(mockFile0);
      diskFileItemFactory0.getRepository();
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      MockFile mockFile0 = new MockFile(")aqdqM(2!m~WBA4-*??");
      diskFileItemFactory0.setRepository(mockFile0);
      diskFileItemFactory0.getRepository();
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
      
      diskFileItemFactory0.setDefaultCharset((String) null);
      diskFileItemFactory0.getDefaultCharset();
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      File file0 = MockFile.createTempFile(".!=Dl3r#Cg;NOCnjY", "7X");
      DiskFileItemFactory diskFileItemFactory0 = new DiskFileItemFactory(2163, file0);
      diskFileItemFactory0.getRepository();
      assertEquals(2163, diskFileItemFactory0.getSizeThreshold());
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      diskFileItemFactory0.getRepository();
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
      
      diskFileItemFactory0.setDefaultCharset("");
      diskFileItemFactory0.getDefaultCharset();
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      String string0 = diskFileItemFactory0.getDefaultCharset();
      assertEquals("ISO-8859-1", string0);
      assertEquals(10240, diskFileItemFactory0.getSizeThreshold());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      DiskFileItemFactory diskFileItemFactory0 = DiskFileItemFactory.DiskFileItemFactory1();
      int int0 = diskFileItemFactory0.getSizeThreshold();
      assertEquals("ISO-8859-1", diskFileItemFactory0.getDefaultCharset());
      assertEquals(10240, int0);
  }
}
