

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



package org.apache.commons.fileupload;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.shaded.org.mockito.Mockito.*;
import static org.evosuite.runtime.EvoAssertions.*;
import java.util.HashMap;
import java.util.Map;
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.FileItemFactory;
import org.apache.commons.fileupload.FileItemHeaders;
import org.apache.commons.fileupload.FileUpload;
import org.apache.commons.fileupload.FileUploadBase;
import org.apache.commons.fileupload.FileUploadException;
import org.apache.commons.fileupload.ProgressListener;
import org.apache.commons.fileupload.RequestContext;
import org.apache.commons.fileupload.util.FileItemHeadersImpl;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.evosuite.runtime.ViolatedAssumptionAnswer;
import org.evosuite.runtime.mock.java.io.MockIOException;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true) 
public class FileUploadBase_ESTest extends FileUploadBase_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test00()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(561, (FileItemFactory) null);
      fileUpload0.setFileItemFactory((FileItemFactory) null);
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test01()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload((-42), fileItemFactory0);
      assertEquals((-1L), fileUpload0.getSizeMax());
      
      fileUpload0.setSizeMax(0L);
      fileUpload0.getSizeMax();
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test02()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(1843, (FileItemFactory) null);
      fileUpload0.setSizeMax(1843);
      long long0 = fileUpload0.getSizeMax();
      assertEquals(1843L, long0);
  }

  @Test(timeout = 4000)
  public void test03()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      fileUpload0.getHeader(hashMap0, "");
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test04()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload((-1449), fileItemFactory0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      
      fileUpload0.setFileSizeMax(1L);
      long long0 = fileUpload0.getFileSizeMax();
      assertEquals(1L, long0);
  }

  @Test(timeout = 4000)
  public void test05()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(1843, (FileItemFactory) null);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      String string0 = fileUpload0.getFileName0(hashMap0);
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test06()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(2485, (FileItemFactory) null);
      fileUpload0.getFileItemFactory();
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test07()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(1, fileItemFactory0);
      fileUpload0.getFileItemFactory();
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test08()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(561, (FileItemFactory) null);
      fileUpload0.setFileCountMax(561);
      long long0 = fileUpload0.getFileCountMax();
      assertEquals(561L, long0);
  }

  @Test(timeout = 4000)
  public void test09()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-454), (FileItemFactory) null);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      String string0 = fileUpload0.getFieldName2(hashMap0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test10()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      FileItemFactory fileItemFactory1 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      doReturn((FileItem) null).when(fileItemFactory1).createItem(anyString() , anyString() , anyBoolean() , anyString());
      fileUpload0.setFileItemFactory(fileItemFactory1);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      fileUpload0.createItem(hashMap0, false);
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
  }

  @Test(timeout = 4000)
  public void test11()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-492), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.parseHeaders((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test12()  throws Throwable  {
      // Undeclared exception!
      try { 
        FileUploadBase.isMultipartContent((RequestContext) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test13()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(2147483645, (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getParsedHeaders((String) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test14()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-492), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getParsedHeaders("#)u)U");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Expected headers to be terminated by an empty line.
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test15()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-333288148), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getHeader((Map<String, String>) null, "multipart/");
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test16()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(0, (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getFileName1((FileItemHeaders) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test17()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-492), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getFileName0((Map<String, String>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test18()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(2147483645, (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getFieldName2((Map<String, String>) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test19()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(23, (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.getFieldName0((FileItemHeaders) null);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test20()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-1472806860), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.parseHeaders(" \rY");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Expected headers to be terminated by an empty line.
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test21()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-209235087), (FileItemFactory) null);
      // Undeclared exception!
      try { 
        fileUpload0.parseHeaders("\r");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Expected headers to be terminated by an empty line.
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test22()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(1617, fileItemFactory0);
      // Undeclared exception!
      try { 
        fileUpload0.parseHeaders(" \r\n");
        fail("Expecting exception: IllegalStateException");
      
      } catch(IllegalStateException e) {
         //
         // Expected headers to be terminated by an empty line.
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test23()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(1843, (FileItemFactory) null);
      FileItemHeadersImpl fileItemHeadersImpl0 = new FileItemHeadersImpl();
      fileItemHeadersImpl0.addHeader("Content-disposition", "form-dataform-data");
      String string0 = fileUpload0.getFieldName0(fileItemHeadersImpl0);
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test24()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-1459597726), (FileItemFactory) null);
      FileItemHeadersImpl fileItemHeadersImpl0 = new FileItemHeadersImpl();
      fileItemHeadersImpl0.addHeader("Content-disposition", "multipart/form-data");
      String string0 = fileUpload0.getFieldName0(fileItemHeadersImpl0);
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test25()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload(41, (FileItemFactory) null);
      FileItemHeadersImpl fileItemHeadersImpl0 = new FileItemHeadersImpl();
      fileItemHeadersImpl0.addHeader("Content-disposition", "attachment");
      String string0 = fileUpload0.getFileName1(fileItemHeadersImpl0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
  }

  @Test(timeout = 4000)
  public void test26()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload((-1459597726), fileItemFactory0);
      FileItemHeadersImpl fileItemHeadersImpl0 = new FileItemHeadersImpl();
      fileItemHeadersImpl0.addHeader("Content-disposition", "form-data");
      String string0 = fileUpload0.getFileName1(fileItemHeadersImpl0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test27()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-1459597726), (FileItemFactory) null);
      FileItemHeadersImpl fileItemHeadersImpl0 = new FileItemHeadersImpl();
      fileItemHeadersImpl0.addHeader("Content-disposition", "Content-disposition");
      String string0 = fileUpload0.getFileName1(fileItemHeadersImpl0);
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test28()  throws Throwable  {
      FileUpload fileUpload0 = new FileUpload((-492), (FileItemFactory) null);
      fileUpload0.getBoundary("Content-disposition");
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test29()  throws Throwable  {
      RequestContext requestContext0 = mock(RequestContext.class, new ViolatedAssumptionAnswer());
      doReturn("multipart/ce^nz.b.ce").when(requestContext0).getContentType();
      boolean boolean0 = FileUploadBase.isMultipartContent(requestContext0);
      assertTrue(boolean0);
  }

  @Test(timeout = 4000)
  public void test30()  throws Throwable  {
      RequestContext requestContext0 = mock(RequestContext.class, new ViolatedAssumptionAnswer());
      doReturn((String) null).when(requestContext0).getContentType();
      boolean boolean0 = FileUploadBase.isMultipartContent(requestContext0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test31()  throws Throwable  {
      RequestContext requestContext0 = mock(RequestContext.class, new ViolatedAssumptionAnswer());
      doReturn("Invalid RFC 2047 encoded-word: ").when(requestContext0).getContentType();
      boolean boolean0 = FileUploadBase.isMultipartContent(requestContext0);
      assertFalse(boolean0);
  }

  @Test(timeout = 4000)
  public void test32()  throws Throwable  {
      FileUploadBase.FileUploadIOException fileUploadBase_FileUploadIOException0 = new FileUploadBase.FileUploadIOException((FileUploadException) null);
      Throwable throwable0 = fileUploadBase_FileUploadIOException0.getCause();
      assertNull(throwable0);
  }

  @Test(timeout = 4000)
  public void test33()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("", 2091L, (-1184L));
      long long0 = fileUploadBase_FileSizeLimitExceededException0.getActualSize();
      assertEquals(2091L, long0);
  }

  @Test(timeout = 4000)
  public void test34()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("org.apache.commons.fileupload.FileUploadBase$IOFileUploadException", (-1449), (-1449));
      long long0 = fileUploadBase_FileSizeLimitExceededException0.getPermittedSize();
      assertEquals((-1449L), long0);
  }

  @Test(timeout = 4000)
  public void test35()  throws Throwable  {
      MockIOException mockIOException0 = new MockIOException();
      FileUploadBase.IOFileUploadException fileUploadBase_IOFileUploadException0 = new FileUploadBase.IOFileUploadException("", mockIOException0);
      Throwable throwable0 = fileUploadBase_IOFileUploadException0.getCause();
      assertSame(throwable0, mockIOException0);
  }

  @Test(timeout = 4000)
  public void test36()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("org.apache.commons.fileupload.FileUploadBase$IOFileUploadException", (-1449), (-1449));
      String string0 = fileUploadBase_FileSizeLimitExceededException0.getFieldName();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test37()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("Content-disposition", 0L, 0L);
      fileUploadBase_FileSizeLimitExceededException0.setFieldName("Content-length");
      assertNull(fileUploadBase_FileSizeLimitExceededException0.getFileName());
  }

  @Test(timeout = 4000)
  public void test38()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("))%~uYXw", 2538L, (-2824L));
      fileUploadBase_FileSizeLimitExceededException0.setFileName("-");
      assertEquals("-", fileUploadBase_FileSizeLimitExceededException0.getFileName());
  }

  @Test(timeout = 4000)
  public void test39()  throws Throwable  {
      FileUploadBase.FileSizeLimitExceededException fileUploadBase_FileSizeLimitExceededException0 = new FileUploadBase.FileSizeLimitExceededException("Content-type", (-1L), 0L);
      String string0 = fileUploadBase_FileSizeLimitExceededException0.getFileName();
      assertNull(string0);
  }

  @Test(timeout = 4000)
  public void test40()  throws Throwable  {
      FileUploadBase.SizeLimitExceededException fileUploadBase_SizeLimitExceededException0 = new FileUploadBase.SizeLimitExceededException("BJ||BA-)4]mQ+K5w", 1442L, 0L);
      FileUploadBase.InvalidContentTypeException fileUploadBase_InvalidContentTypeException0 = new FileUploadBase.InvalidContentTypeException((String) null, fileUploadBase_SizeLimitExceededException0);
  }

  @Test(timeout = 4000)
  public void test41()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      fileUpload0.getProgressListener();
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
  }

  @Test(timeout = 4000)
  public void test42()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(2, fileItemFactory0);
      fileUpload0.setHeaderEncoding("'T&");
      String string0 = fileUpload0.getHeaderEncoding();
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals("'T&", string0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test43()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload((-1449), fileItemFactory0);
      long long0 = fileUpload0.getSizeMax();
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), long0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
  }

  @Test(timeout = 4000)
  public void test44()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      
      fileUpload0.setFileCountMax(0);
      fileUpload0.getFileCountMax();
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test45()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(2, fileItemFactory0);
      fileUpload0.setProgressListener((ProgressListener) null);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test46()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      FileItemHeadersImpl fileItemHeadersImpl0 = fileUpload0.newFileItemHeaders();
      String string0 = fileUpload0.getFieldName0(fileItemHeadersImpl0);
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileSizeMax());
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test47()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      String string0 = fileUpload0.getHeaderEncoding();
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertNull(string0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }

  @Test(timeout = 4000)
  public void test48()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      HashMap<String, String> hashMap0 = new HashMap<String, String>();
      // Undeclared exception!
      try { 
        fileUpload0.createItem(hashMap0, false);
        fail("Expecting exception: NullPointerException");
      
      } catch(NullPointerException e) {
         //
         // no message in exception (getMessage() returned null)
         //
         verifyException("org.apache.commons.fileupload.FileUploadBase", e);
      }
  }

  @Test(timeout = 4000)
  public void test49()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      long long0 = fileUpload0.getFileSizeMax();
      assertEquals((-1L), long0);
      assertEquals((-1L), fileUpload0.getFileCountMax());
      assertEquals((-1L), fileUpload0.getSizeMax());
  }

  @Test(timeout = 4000)
  public void test50()  throws Throwable  {
      FileItemFactory fileItemFactory0 = mock(FileItemFactory.class, new ViolatedAssumptionAnswer());
      FileUpload fileUpload0 = new FileUpload(0, fileItemFactory0);
      long long0 = fileUpload0.getFileCountMax();
      assertEquals((-1L), long0);
      assertEquals((-1L), fileUpload0.getSizeMax());
      assertEquals((-1L), fileUpload0.getFileSizeMax());
  }
}
