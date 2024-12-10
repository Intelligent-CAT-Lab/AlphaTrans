/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.validator.routines;

import static org.junit.Assert.*;

import org.apache.commons.validator.ResultPair;
import org.junit.Before;
import org.junit.Test;

import java.net.URI;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;

/**
 * Performs Validation Test for url validations.
 *
 * @version $Revision$
 */
public class UrlValidatorTest {

    private final boolean printStatus = false;
    private final boolean printIndex =
            false; // print index that indicates current scheme,host,port,path, query test were

    @Before
    public void setUp() {
        for (int index = 0; index < testPartsIndex.length - 1; index++) {
            testPartsIndex[index] = 0;
        }
    }

    

    

    /**
     * Create set of tests by taking the testUrlXXX arrays and running through all possible
     * permutations of their combinations.
     *
     * @param testObjects Used to create a url.
     */
    public void testIsValid1(Object[] testObjects, long options) {
        UrlValidator urlVal = UrlValidator.UrlValidator1(null, null, options);
        assertTrue(urlVal.isValid("http://www.google.com"));
        assertTrue(urlVal.isValid("http://www.google.com/"));
        int statusPerLine = 60;
        int printed = 0;
        if (printIndex) {
            statusPerLine = 6;
        }
        do {
            StringBuilder testBuffer = new StringBuilder();
            boolean expected = true;
            for (int testPartsIndexIndex = 0;
                    testPartsIndexIndex < testPartsIndex.length;
                    ++testPartsIndexIndex) {
                int index = testPartsIndex[testPartsIndexIndex];
                ResultPair[] part = (ResultPair[]) testObjects[testPartsIndexIndex];
                testBuffer.append(part[index].item);
                expected &= part[index].valid;
            }
            String url = testBuffer.toString();
            boolean result = urlVal.isValid(url);
            assertEquals(url, expected, result);
            if (printStatus) {
                if (printIndex) {
                    System.out.print(testPartsIndextoString());
                } else {
                    if (result == expected) {
                        System.out.print('.');
                    } else {
                        System.out.print('X');
                    }
                }
                printed++;
                if (printed == statusPerLine) {
                    System.out.println();
                    printed = 0;
                }
            }
        } while (incrementTestPartsIndex(testPartsIndex, testObjects));
        if (printStatus) {
            System.out.println();
        }
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    static boolean incrementTestPartsIndex(int[] testPartsIndex, Object[] testParts) {
        boolean carry = true; // add 1 to lowest order part.
        boolean maxIndex = true;
        for (int testPartsIndexIndex = testPartsIndex.length - 1;
                testPartsIndexIndex >= 0;
                --testPartsIndexIndex) {
            int index = testPartsIndex[testPartsIndexIndex];
            ResultPair[] part = (ResultPair[]) testParts[testPartsIndexIndex];
            maxIndex &= (index == (part.length - 1));
            if (carry) {
                if (index < part.length - 1) {
                    index++;
                    testPartsIndex[testPartsIndexIndex] = index;
                    carry = false;
                } else {
                    testPartsIndex[testPartsIndexIndex] = 0;
                    carry = true;
                }
            }
        }

        return (!maxIndex);
    }

    private String testPartsIndextoString() {
        StringBuilder carryMsg = new StringBuilder("{");
        for (int testPartsIndexIndex = 0;
                testPartsIndexIndex < testPartsIndex.length;
                ++testPartsIndexIndex) {
            carryMsg.append(testPartsIndex[testPartsIndexIndex]);
            if (testPartsIndexIndex < testPartsIndex.length - 1) {
                carryMsg.append(',');
            } else {
                carryMsg.append('}');
            }
        }
        return carryMsg.toString();
    }

    

    

    

    

    

    

    

    

    

    

    

    

    /**
     * The data given below approximates the 4 parts of a URL <scheme>://<authority><path>?<query>
     * except that the port number is broken out of authority to increase the number of
     * permutations. A complete URL is composed of a scheme+authority+port+path+query, all of which
     * must be individually valid for the entire URL to be considered valid.
     */
    ResultPair[] testUrlScheme = {
        new ResultPair("http://", true),
        new ResultPair("ftp://", true),
        new ResultPair("h3t://", true),
        new ResultPair("3ht://", false),
        new ResultPair("http:/", false),
        new ResultPair("http:", false),
        new ResultPair("http/", false),
        new ResultPair("://", false)
    };

    ResultPair[] testUrlAuthority = {
        new ResultPair("www.google.com", true),
        new ResultPair("www.google.com.", true),
        new ResultPair("go.com", true),
        new ResultPair("go.au", true),
        new ResultPair("0.0.0.0", true),
        new ResultPair("255.255.255.255", true),
        new ResultPair("256.256.256.256", false),
        new ResultPair("255.com", true),
        new ResultPair("1.2.3.4.5", false),
        new ResultPair("1.2.3.4.", false),
        new ResultPair("1.2.3", false),
        new ResultPair(".1.2.3.4", false),
        new ResultPair("go.a", false),
        new ResultPair("go.a1a", false),
        new ResultPair("go.cc", true),
        new ResultPair("go.1aa", false),
        new ResultPair("aaa.", false),
        new ResultPair(".aaa", false),
        new ResultPair("aaa", false),
        new ResultPair("", false)
    };
    ResultPair[] testUrlPort = {
        new ResultPair(":80", true),
        new ResultPair(":65535", true), // max possible
        new ResultPair(":65536", false), // max possible +1
        new ResultPair(":0", true),
        new ResultPair("", true),
        new ResultPair(":-1", false),
        new ResultPair(":65636", false),
        new ResultPair(":999999999999999999", false),
        new ResultPair(":65a", false)
    };
    ResultPair[] testPath = {
        new ResultPair("/test1", true),
        new ResultPair("/t123", true),
        new ResultPair("/$23", true),
        new ResultPair("/..", false),
        new ResultPair("/../", false),
        new ResultPair("/test1/", true),
        new ResultPair("", true),
        new ResultPair("/test1/file", true),
        new ResultPair("/..//file", false),
        new ResultPair("/test1//file", false)
    };
    ResultPair[] testUrlPathOptions = {
        new ResultPair("/test1", true),
        new ResultPair("/t123", true),
        new ResultPair("/$23", true),
        new ResultPair("/..", false),
        new ResultPair("/../", false),
        new ResultPair("/test1/", true),
        new ResultPair("/#", false),
        new ResultPair("", true),
        new ResultPair("/test1/file", true),
        new ResultPair("/t123/file", true),
        new ResultPair("/$23/file", true),
        new ResultPair("/../file", false),
        new ResultPair("/..//file", false),
        new ResultPair("/test1//file", true),
        new ResultPair("/#/file", false)
    };

    ResultPair[] testUrlQuery = {
        new ResultPair("?action=view", true),
        new ResultPair("?action=edit&mode=up", true),
        new ResultPair("", true)
    };

    Object[] testUrlParts = {testUrlScheme, testUrlAuthority, testUrlPort, testPath, testUrlQuery};
    Object[] testUrlPartsOptions = {
        testUrlScheme, testUrlAuthority, testUrlPort, testUrlPathOptions, testUrlQuery
    };
    int[] testPartsIndex = {0, 0, 0, 0, 0};

    private final String[] schemes = {
        "http",
        "gopher",
        "g0-To+.",
        "not_valid" // TODO this will need to be dropped if the ctor validates schemes
    };

    ResultPair[] testScheme = {
        new ResultPair("http", true),
        new ResultPair("ftp", false),
        new ResultPair("httpd", false),
        new ResultPair("gopher", true),
        new ResultPair("g0-to+.", true),
        new ResultPair("not_valid", false), // underscore not allowed
        new ResultPair("HtTp", true),
        new ResultPair("telnet", false)
    };

    /**
     * Validator for checking URL parsing
     *
     * @param args - URLs to validate
     */
    public static void main(String[] args) {
        UrlValidator uv = UrlValidator.UrlValidator6();
        for (String arg : args) {
            try {
                URI uri = new URI(arg);
                uri = uri.normalize();
                System.out.println(uri.toString());
                System.out.printf("URI scheme: %s%n", uri.getScheme());
                System.out.printf("URI scheme specific part: %s%n", uri.getSchemeSpecificPart());
                System.out.printf(
                        "URI raw scheme specific part: %s%n", uri.getRawSchemeSpecificPart());
                System.out.printf("URI auth: %s%n", uri.getAuthority());
                System.out.printf("URI raw auth: %s%n", uri.getRawAuthority());
                System.out.printf("URI userInfo: %s%n", uri.getUserInfo());
                System.out.printf("URI raw userInfo: %s%n", uri.getRawUserInfo());
                System.out.printf("URI host: %s%n", uri.getHost());
                System.out.printf("URI port: %s%n", uri.getPort());
                System.out.printf("URI path: %s%n", uri.getPath());
                System.out.printf("URI raw path: %s%n", uri.getRawPath());
                System.out.printf("URI query: %s%n", uri.getQuery());
                System.out.printf("URI raw query: %s%n", uri.getRawQuery());
                System.out.printf("URI fragment: %s%n", uri.getFragment());
                System.out.printf("URI raw fragment: %s%n", uri.getRawFragment());
            } catch (URISyntaxException e) {
                System.out.println(e.getMessage());
            }
            System.out.printf("isValid: %s%n", uv.isValid(arg));
        }
    }

    @Test
    public void testIsValid0_test0_decomposed()  {
        testIsValid1(testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES);
    }

    @Test
    public void testIsValid0_test1_decomposed()  {
        testIsValid1(testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES);
        setUp();
    }

    @Test
    public void testIsValid0_test2_decomposed()  {
        testIsValid1(testUrlParts, UrlValidator.ALLOW_ALL_SCHEMES);
        setUp();
        long options =
                UrlValidator.ALLOW_2_SLASHES
                        + UrlValidator.ALLOW_ALL_SCHEMES
                        + UrlValidator.NO_FRAGMENTS;
        testIsValid1(testUrlPartsOptions, options);
    }

    @Test
    public void testIsValidScheme_test0_decomposed()  {
        if (printStatus) {
            System.out.print("\n testIsValidScheme() ");
        }
        UrlValidator urlVal = UrlValidator.UrlValidator3(schemes, 0);
    }

    @Test
    public void testIsValidScheme_test1_decomposed()  {
        if (printStatus) {
            System.out.print("\n testIsValidScheme() ");
        }
        UrlValidator urlVal = UrlValidator.UrlValidator3(schemes, 0);
        for (int sIndex = 0; sIndex < testScheme.length; sIndex++) {
            ResultPair testPair = testScheme[sIndex];
            boolean result = urlVal.isValidScheme(testPair.item);
            assertEquals(testPair.item, testPair.valid, result);
            if (printStatus) {
                if (result == testPair.valid) {
                    System.out.print('.');
                } else {
                    System.out.print('X');
                }
            }
        }
    }

    @Test
    public void testIsValidScheme_test2_decomposed()  {
        if (printStatus) {
            System.out.print("\n testIsValidScheme() ");
        }
        UrlValidator urlVal = UrlValidator.UrlValidator3(schemes, 0);
        for (int sIndex = 0; sIndex < testScheme.length; sIndex++) {
            ResultPair testPair = testScheme[sIndex];
            boolean result = urlVal.isValidScheme(testPair.item);
            assertEquals(testPair.item, testPair.valid, result);
            if (printStatus) {
                if (result == testPair.valid) {
                    System.out.print('.');
                } else {
                    System.out.print('X');
                }
            }
        }
        if (printStatus) {
            System.out.println();
        }
    }

    @Test
    public void testValidator202_test0_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
    }

    @Test
    public void testValidator202_test1_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
        assertTrue(
                urlValidator.isValid(
                        "http://l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.l.org"));
    }

    @Test
    public void testValidator204_test0_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
    }

    @Test
    public void testValidator204_test1_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
        assertTrue(
                urlValidator.isValid(
                        "http://tech.yahoo.com/rc/desktops/102;_ylt=Ao8yevQHlZ4On0O3ZJGXLEQFLZA5"));
    }

    @Test
    public void testValidator218_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES);
    }

    @Test
    public void testValidator218_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES);
        assertTrue(
                "parentheses should be valid in URLs",
                validator.isValid("http://somewhere.com/pathxyz/file(1).html"));
    }

    @Test
    public void testValidator235_test0_decomposed()  {
        String version = System.getProperty("java.version");
    }

    @Test
    public void testValidator235_test1_decomposed()  {
        String version = System.getProperty("java.version");
        if (version.compareTo("1.6") < 0) {
            System.out.println("Cannot run Unicode IDN tests");
            return; // Cannot run the test
        }
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator235_test2_decomposed()  {
        String version = System.getProperty("java.version");
        if (version.compareTo("1.6") < 0) {
            System.out.println("Cannot run Unicode IDN tests");
            return; // Cannot run the test
        }
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(
                "xn--d1abbgf6aiiy.xn--p1ai should validate",
                validator.isValid("http://xn--d1abbgf6aiiy.xn--p1ai"));
        assertTrue("президент.рф should validate", validator.isValid("http://президент.рф"));
        assertTrue(
                "www.b\u00fccher.ch should validate",
                validator.isValid("http://www.b\u00fccher.ch"));
        assertFalse("www.\uFFFD.ch FFFD should fail", validator.isValid("http://www.\uFFFD.ch"));
        assertTrue(
                "www.b\u00fccher.ch should validate",
                validator.isValid("ftp://www.b\u00fccher.ch"));
        assertFalse("www.\uFFFD.ch FFFD should fail", validator.isValid("ftp://www.\uFFFD.ch"));
    }

    @Test
    public void testValidator248_test0_decomposed()  {
        RegexValidator regex =
                RegexValidator.RegexValidator1(new String[] {"localhost", ".*\\.my-testing"});
    }

    @Test
    public void testValidator248_test1_decomposed()  {
        RegexValidator regex =
                RegexValidator.RegexValidator1(new String[] {"localhost", ".*\\.my-testing"});
        UrlValidator validator = UrlValidator.UrlValidator2(regex, 0);
    }

    @Test
    public void testValidator248_test2_decomposed()  {
        RegexValidator regex =
                RegexValidator.RegexValidator1(new String[] {"localhost", ".*\\.my-testing"});
        UrlValidator validator = UrlValidator.UrlValidator2(regex, 0);
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertTrue(
                "first.my-testing should validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertTrue(
                "sup3r.my-testing should validate",
                validator.isValid("http://sup3r.my-testing/test/index.html"));
        assertFalse(
                "broke.my-test should not validate",
                validator.isValid("http://broke.my-test/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
    }

    @Test
    public void testValidator248_test3_decomposed()  {
        RegexValidator regex =
                RegexValidator.RegexValidator1(new String[] {"localhost", ".*\\.my-testing"});
        UrlValidator validator = UrlValidator.UrlValidator2(regex, 0);
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertTrue(
                "first.my-testing should validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertTrue(
                "sup3r.my-testing should validate",
                validator.isValid("http://sup3r.my-testing/test/index.html"));
        assertFalse(
                "broke.my-test should not validate",
                validator.isValid("http://broke.my-test/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
    }

    @Test
    public void testValidator248_test4_decomposed()  {
        RegexValidator regex =
                RegexValidator.RegexValidator1(new String[] {"localhost", ".*\\.my-testing"});
        UrlValidator validator = UrlValidator.UrlValidator2(regex, 0);
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertTrue(
                "first.my-testing should validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertTrue(
                "sup3r.my-testing should validate",
                validator.isValid("http://sup3r.my-testing/test/index.html"));
        assertFalse(
                "broke.my-test should not validate",
                validator.isValid("http://broke.my-test/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
        validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertTrue(
                "machinename URL should validate",
                validator.isValid("http://machinename/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
    }

    @Test
    public void testValidator288_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
    }

    @Test
    public void testValidator288_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
        assertTrue("hostname should validate", validator.isValid("http://hostname"));
        assertTrue(
                "hostname with path should validate",
                validator.isValid("http://hostname/test/index.html"));
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertFalse(
                "first.my-testing should not validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertFalse(
                "broke.hostname should not validate",
                validator.isValid("http://broke.hostname/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
    }

    @Test
    public void testValidator288_test2_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
        assertTrue("hostname should validate", validator.isValid("http://hostname"));
        assertTrue(
                "hostname with path should validate",
                validator.isValid("http://hostname/test/index.html"));
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertFalse(
                "first.my-testing should not validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertFalse(
                "broke.hostname should not validate",
                validator.isValid("http://broke.hostname/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
        validator = UrlValidator.UrlValidator4(0);
    }

    @Test
    public void testValidator288_test3_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_LOCAL_URLS);
        assertTrue("hostname should validate", validator.isValid("http://hostname"));
        assertTrue(
                "hostname with path should validate",
                validator.isValid("http://hostname/test/index.html"));
        assertTrue(
                "localhost URL should validate",
                validator.isValid("http://localhost/test/index.html"));
        assertFalse(
                "first.my-testing should not validate",
                validator.isValid("http://first.my-testing/test/index.html"));
        assertFalse(
                "broke.hostname should not validate",
                validator.isValid("http://broke.hostname/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
        validator = UrlValidator.UrlValidator4(0);
        assertFalse("hostname should no longer validate", validator.isValid("http://hostname"));
        assertFalse(
                "localhost URL should no longer validate",
                validator.isValid("http://localhost/test/index.html"));
        assertTrue(
                "www.apache.org should still validate",
                validator.isValid("http://www.apache.org/test/index.html"));
    }

    @Test
    public void testValidator276_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator276_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(
                "http://apache.org/ should be allowed by default",
                validator.isValid("http://www.apache.org/test/index.html"));
        assertFalse(
                "file:///c:/ shouldn't be allowed by default",
                validator.isValid("file:///C:/some.file"));
        assertFalse(
                "file:///c:\\ shouldn't be allowed by default",
                validator.isValid("file:///C:\\some.file"));
        assertFalse(
                "file:///etc/ shouldn't be allowed by default",
                validator.isValid("file:///etc/hosts"));
        assertFalse(
                "file://localhost/etc/ shouldn't be allowed by default",
                validator.isValid("file://localhost/etc/hosts"));
        assertFalse(
                "file://localhost/c:/ shouldn't be allowed by default",
                validator.isValid("file://localhost/c:/some.file"));
    }

    @Test
    public void testValidator276_test2_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(
                "http://apache.org/ should be allowed by default",
                validator.isValid("http://www.apache.org/test/index.html"));
        assertFalse(
                "file:///c:/ shouldn't be allowed by default",
                validator.isValid("file:///C:/some.file"));
        assertFalse(
                "file:///c:\\ shouldn't be allowed by default",
                validator.isValid("file:///C:\\some.file"));
        assertFalse(
                "file:///etc/ shouldn't be allowed by default",
                validator.isValid("file:///etc/hosts"));
        assertFalse(
                "file://localhost/etc/ shouldn't be allowed by default",
                validator.isValid("file://localhost/etc/hosts"));
        assertFalse(
                "file://localhost/c:/ shouldn't be allowed by default",
                validator.isValid("file://localhost/c:/some.file"));
        validator =
                UrlValidator.UrlValidator3(
                        new String[] {"http", "file"}, UrlValidator.ALLOW_LOCAL_URLS);
    }

    @Test
    public void testValidator276_test3_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(
                "http://apache.org/ should be allowed by default",
                validator.isValid("http://www.apache.org/test/index.html"));
        assertFalse(
                "file:///c:/ shouldn't be allowed by default",
                validator.isValid("file:///C:/some.file"));
        assertFalse(
                "file:///c:\\ shouldn't be allowed by default",
                validator.isValid("file:///C:\\some.file"));
        assertFalse(
                "file:///etc/ shouldn't be allowed by default",
                validator.isValid("file:///etc/hosts"));
        assertFalse(
                "file://localhost/etc/ shouldn't be allowed by default",
                validator.isValid("file://localhost/etc/hosts"));
        assertFalse(
                "file://localhost/c:/ shouldn't be allowed by default",
                validator.isValid("file://localhost/c:/some.file"));
        validator =
                UrlValidator.UrlValidator3(
                        new String[] {"http", "file"}, UrlValidator.ALLOW_LOCAL_URLS);
        assertTrue(
                "http://apache.org/ should be allowed by default",
                validator.isValid("http://www.apache.org/test/index.html"));
        assertTrue("file:///c:/ should now be allowed", validator.isValid("file:///C:/some.file"));
        assertFalse(
                "file:///c:\\ should not be allowed", // Only allow forward slashes
                validator.isValid("file:///C:\\some.file"));
        assertTrue("file:///etc/ should now be allowed", validator.isValid("file:///etc/hosts"));
        assertTrue(
                "file://localhost/etc/ should now be allowed",
                validator.isValid("file://localhost/etc/hosts"));
        assertTrue(
                "file://localhost/c:/ should now be allowed",
                validator.isValid("file://localhost/c:/some.file"));
        assertFalse(
                "file://c:/ shouldn't ever be allowed, needs file:///c:/",
                validator.isValid("file://C:/some.file"));
        assertFalse(
                "file://c:\\ shouldn't ever be allowed, needs file:///c:/",
                validator.isValid("file://C:\\some.file"));
    }

    @Test
    public void testValidator391OK_test0_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
    }

    @Test
    public void testValidator391OK_test1_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
        assertTrue(urlValidator.isValid("file:///C:/path/to/dir/"));
    }

    @Test
    public void testValidator391FAILS_test0_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
    }

    @Test
    public void testValidator391FAILS_test1_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
        assertTrue(urlValidator.isValid("file:/C:/path/to/dir/"));
    }

    @Test
    public void testValidator309_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator309_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://sample.ondemand.com/"));
        assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"));
        assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"));
    }

    @Test
    public void testValidator309_test2_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://sample.ondemand.com/"));
        assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"));
        assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"));
        urlValidator = UrlValidator.UrlValidator5(new String[] {"HTTP", "HTTPS"});
    }

    @Test
    public void testValidator309_test3_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://sample.ondemand.com/"));
        assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"));
        assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"));
        urlValidator = UrlValidator.UrlValidator5(new String[] {"HTTP", "HTTPS"});
        assertTrue(urlValidator.isValid("http://sample.ondemand.com/"));
        assertTrue(urlValidator.isValid("hTtP://sample.ondemand.CoM/"));
        assertTrue(urlValidator.isValid("httpS://SAMPLE.ONEMAND.COM/"));
    }

    @Test
    public void testValidator339_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator339_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://www.cnn.com/WORLD/?hpt=sitenav"));
        assertTrue(urlValidator.isValid("http://www.cnn.com./WORLD/?hpt=sitenav"));
        assertFalse(urlValidator.isValid("http://www.cnn.com../"));
        assertFalse(urlValidator.isValid("http://www.cnn.invalid/"));
        assertFalse(
                urlValidator.isValid(
                        "http://www.cnn.invalid./"));
    }

    @Test
    public void testValidator339IDN_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator339IDN_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://президент.рф/WORLD/?hpt=sitenav"));
        assertTrue(urlValidator.isValid("http://президент.рф./WORLD/?hpt=sitenav"));
        assertFalse(urlValidator.isValid("http://президент.рф..../"));
        assertFalse(urlValidator.isValid("http://президент.рф.../"));
        assertFalse(urlValidator.isValid("http://президент.рф../"));
    }

    @Test
    public void testValidator342_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator342_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://example.rocks/"));
        assertTrue(urlValidator.isValid("http://example.rocks"));
    }

    @Test
    public void testValidator411_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator411_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://example.rocks:/"));
        assertTrue(urlValidator.isValid("http://example.rocks:0/"));
        assertTrue(urlValidator.isValid("http://example.rocks:65535/"));
        assertFalse(urlValidator.isValid("http://example.rocks:65536/"));
        assertFalse(urlValidator.isValid("http://example.rocks:100000/"));
    }

    @Test
    public void testValidator464_test0_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
    }

    @Test
    public void testValidator464_test1_decomposed()  {
        String[] schemes = {"file"};
        UrlValidator urlValidator = UrlValidator.UrlValidator5(schemes);
        String fileNAK = "file://bad ^ domain.com/label/test";
        assertFalse(fileNAK, urlValidator.isValid(fileNAK));
    }

    @Test
    public void testValidator452_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator452_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://[::FFFF:129.144.52.38]:80/index.html"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testValidator473_1_test0_decomposed()  {
        new UrlValidator(new String[] {}, null, 0L, null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testValidator473_2_test0_decomposed()  {
        List<DomainValidator.Item> items = new ArrayList<>();
        new UrlValidator(new String[] {}, null, 0L, DomainValidator.getInstance2(true, items));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testValidator473_3_test0_decomposed()  {
        List<DomainValidator.Item> items = new ArrayList<>();
        new UrlValidator(
                new String[] {},
                null,
                UrlValidator.ALLOW_LOCAL_URLS,
                DomainValidator.getInstance2(false, items));
    }

    @Test
    public void testValidateUrl_test0_decomposed()  {
        assertTrue(true);
    }

    @Test
    public void testValidator290_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator290_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(validator.isValid("http://xn--h1acbxfam.idn.icann.org/"));
        assertTrue(validator.isValid("http://test.xn--lgbbat1ad8j"));
        assertTrue(validator.isValid("http://test.xn--fiqs8s"));
        assertTrue(validator.isValid("http://test.xn--fiqz9s"));
        assertTrue(validator.isValid("http://test.xn--wgbh1c"));
        assertTrue(validator.isValid("http://test.xn--j6w193g"));
        assertTrue(validator.isValid("http://test.xn--h2brj9c"));
        assertTrue(validator.isValid("http://test.xn--mgbbh1a71e"));
        assertTrue(validator.isValid("http://test.xn--fpcrj9c3d"));
        assertTrue(validator.isValid("http://test.xn--gecrj9c"));
        assertTrue(validator.isValid("http://test.xn--s9brj9c"));
        assertTrue(validator.isValid("http://test.xn--xkc2dl3a5ee0h"));
        assertTrue(validator.isValid("http://test.xn--45brj9c"));
        assertTrue(validator.isValid("http://test.xn--mgba3a4f16a"));
        assertTrue(validator.isValid("http://test.xn--mgbayh7gpa"));
        assertTrue(validator.isValid("http://test.xn--mgbc0a9azcg"));
        assertTrue(validator.isValid("http://test.xn--ygbi2ammx"));
        assertTrue(validator.isValid("http://test.xn--wgbl6a"));
        assertTrue(validator.isValid("http://test.xn--p1ai"));
        assertTrue(validator.isValid("http://test.xn--mgberp4a5d4ar"));
        assertTrue(validator.isValid("http://test.xn--90a3ac"));
        assertTrue(validator.isValid("http://test.xn--yfro4i67o"));
        assertTrue(validator.isValid("http://test.xn--clchc0ea0b2g2a9gcd"));
        assertTrue(validator.isValid("http://test.xn--3e0b707e"));
        assertTrue(validator.isValid("http://test.xn--fzc2c9e2c"));
        assertTrue(validator.isValid("http://test.xn--xkc2al3hye2a"));
        assertTrue(validator.isValid("http://test.xn--ogbpf8fl"));
        assertTrue(validator.isValid("http://test.xn--kprw13d"));
        assertTrue(validator.isValid("http://test.xn--kpry57d"));
        assertTrue(validator.isValid("http://test.xn--o3cw4h"));
        assertTrue(validator.isValid("http://test.xn--pgbs0dh"));
        assertTrue(validator.isValid("http://test.xn--mgbaam7a8h"));
    }

    @Test
    public void testValidator361_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator361_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(validator.isValid("http://hello.tokyo/"));
    }

    @Test
    public void testValidator363_test0_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator363_test1_decomposed()  {
        UrlValidator urlValidator = UrlValidator.UrlValidator6();
        assertTrue(urlValidator.isValid("http://www.example.org/a/b/hello..world"));
        assertTrue(urlValidator.isValid("http://www.example.org/a/hello..world"));
        assertTrue(urlValidator.isValid("http://www.example.org/hello.world/"));
        assertTrue(urlValidator.isValid("http://www.example.org/hello..world/"));
        assertTrue(urlValidator.isValid("http://www.example.org/hello.world"));
        assertTrue(urlValidator.isValid("http://www.example.org/hello..world"));
        assertTrue(urlValidator.isValid("http://www.example.org/..world"));
        assertTrue(urlValidator.isValid("http://www.example.org/.../world"));
        assertFalse(urlValidator.isValid("http://www.example.org/../world"));
        assertFalse(urlValidator.isValid("http://www.example.org/.."));
        assertFalse(urlValidator.isValid("http://www.example.org/../"));
        assertFalse(urlValidator.isValid("http://www.example.org/./.."));
        assertFalse(urlValidator.isValid("http://www.example.org/././.."));
        assertTrue(urlValidator.isValid("http://www.example.org/..."));
        assertTrue(urlValidator.isValid("http://www.example.org/.../"));
        assertTrue(urlValidator.isValid("http://www.example.org/.../.."));
    }

    @Test
    public void testValidator375_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator375_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        String url = "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html";
        assertTrue("IPv6 address URL should validate: " + url, validator.isValid(url));
    }

    @Test
    public void testValidator375_test2_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        String url = "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html";
        assertTrue("IPv6 address URL should validate: " + url, validator.isValid(url));
        url = "http://[::1]:80/index.html";
        assertTrue("IPv6 address URL should validate: " + url, validator.isValid(url));
    }

    @Test
    public void testValidator375_test3_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        String url = "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html";
        assertTrue("IPv6 address URL should validate: " + url, validator.isValid(url));
        url = "http://[::1]:80/index.html";
        assertTrue("IPv6 address URL should validate: " + url, validator.isValid(url));
        url = "http://FEDC:BA98:7654:3210:FEDC:BA98:7654:3210:80/index.html";
        assertFalse("IPv6 address without [] should not validate: " + url, validator.isValid(url));
    }

    @Test
    public void testValidator353_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator353_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(validator.isValid("http://www.apache.org:80/path"));
        assertTrue(validator.isValid("http://user:pass@www.apache.org:80/path"));
        assertTrue(validator.isValid("http://user:@www.apache.org:80/path"));
        assertTrue(validator.isValid("http://user@www.apache.org:80/path"));
        assertTrue(validator.isValid("http://us%00er:-._~!$&'()*+,;=@www.apache.org:80/path"));
        assertFalse(validator.isValid("http://:pass@www.apache.org:80/path"));
        assertFalse(validator.isValid("http://:@www.apache.org:80/path"));
        assertFalse(validator.isValid("http://user:pa:ss@www.apache.org/path"));
        assertFalse(validator.isValid("http://user:pa@ss@www.apache.org/path"));
    }

    @Test
    public void testValidator382_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator382_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(
                validator.isValid(
                        "ftp://username:password@example.com:8042/over/there/index.dtb?type=animal&name=narwhal#nose"));
    }

    @Test
    public void testValidator380_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator380_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertTrue(validator.isValid("http://www.apache.org:80/path"));
        assertTrue(validator.isValid("http://www.apache.org:8/path"));
        assertTrue(validator.isValid("http://www.apache.org:/path"));
    }

    @Test
    public void testValidator420_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator420_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertFalse(validator.isValid("http://example.com/serach?address=Main Avenue"));
        assertTrue(validator.isValid("http://example.com/serach?address=Main%20Avenue"));
        assertTrue(validator.isValid("http://example.com/serach?address=Main+Avenue"));
    }

    @Test
    public void testValidator467_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES);
    }

    @Test
    public void testValidator467_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator4(UrlValidator.ALLOW_2_SLASHES);
        assertTrue(validator.isValid("https://example.com/some_path/path/"));
        assertTrue(validator.isValid("https://example.com//somepath/path/"));
        assertTrue(validator.isValid("https://example.com//some_path/path/"));
        assertTrue(validator.isValid("http://example.com//_test"));
    }

    @Test
    public void testValidator283_test0_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
    }

    @Test
    public void testValidator283_test1_decomposed()  {
        UrlValidator validator = UrlValidator.UrlValidator6();
        assertFalse(
                validator.isValid(
                        "http://finance.yahoo.com/news/Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%fr"));
        assertTrue(
                validator.isValid(
                        "http://finance.yahoo.com/news/Owners-54B-NY-housing-apf-2493139299.html?x=0&ap=%22"));
    }

    @Test
    public void testFragments_test0_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
    }

    @Test
    public void testFragments_test1_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
        assertFalse(urlValidator.isValid("http://apache.org/a/b/c#frag"));
    }

    @Test
    public void testFragments_test2_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
        assertFalse(urlValidator.isValid("http://apache.org/a/b/c#frag"));
        urlValidator = UrlValidator.UrlValidator5(schemes);
    }

    @Test
    public void testFragments_test3_decomposed()  {
        String[] schemes = {"http", "https"};
        UrlValidator urlValidator = UrlValidator.UrlValidator3(schemes, UrlValidator.NO_FRAGMENTS);
        assertFalse(urlValidator.isValid("http://apache.org/a/b/c#frag"));
        urlValidator = UrlValidator.UrlValidator5(schemes);
        assertTrue(urlValidator.isValid("http://apache.org/a/b/c#frag"));
    }
}