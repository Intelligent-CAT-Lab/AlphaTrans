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
import org.junit.Test;

import junit.framework.TestCase;

import org.apache.commons.validator.routines.DomainValidator.ArrayType;

import java.io.BufferedReader;
import java.io.Closeable;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.net.HttpURLConnection;
import java.net.IDN;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Locale;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Tests for the DomainValidator.
 *
 * @version $Revision$
 */
public class DomainValidatorTest extends TestCase {

    private DomainValidator validator;

    @Override
    public void setUp() {
        validator = DomainValidator.getInstance0();
    }

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    public static void main(String a[]) throws Exception {
        boolean OK = true;
        for (String list :
                new String[] {
                    "INFRASTRUCTURE_TLDS", "COUNTRY_CODE_TLDS", "GENERIC_TLDS", "LOCAL_TLDS"
                }) {
            OK &= isSortedLowerCase0(list);
        }
        if (!OK) {
            System.out.println("Fix arrays before retrying; cannot continue");
            return;
        }
        Set<String> ianaTlds = new HashSet<String>(); // keep for comparison with array contents
        DomainValidator dv = DomainValidator.getInstance0();
        File txtFile = new File("target/tlds-alpha-by-domain.txt");
        long timestamp =
                download(txtFile, "https://data.iana.org/TLD/tlds-alpha-by-domain.txt", 0L);
        final File htmlFile = new File("target/tlds-alpha-by-domain.html");
        download(htmlFile, "https://www.iana.org/domains/root/db", timestamp);

        BufferedReader br = new BufferedReader(new FileReader(txtFile));
        String line;
        final String header;
        line = br.readLine(); // header
        if (line.startsWith("# Version ")) {
            header = line.substring(2);
        } else {
            br.close();
            throw new IOException("File does not have expected Version header");
        }
        final boolean generateUnicodeTlds = false; // Change this to generate Unicode TLDs as well

        Map<String, String[]> htmlInfo = getHtmlInfo(htmlFile);
        Map<String, String> missingTLD =
                new TreeMap<String, String>(); // stores entry and comments as String[]
        Map<String, String> missingCC = new TreeMap<String, String>();
        while ((line = br.readLine()) != null) {
            if (!line.startsWith("#")) {
                final String unicodeTld; // only different from asciiTld if that was punycode
                final String asciiTld = line.toLowerCase(Locale.ENGLISH);
                if (line.startsWith("XN--")) {
                    unicodeTld = IDN.toUnicode(line);
                } else {
                    unicodeTld = asciiTld;
                }
                if (!dv.isValidTld(asciiTld)) {
                    String[] info = htmlInfo.get(asciiTld);
                    if (info != null) {
                        String type = info[0];
                        String comment = info[1];
                        if ("country-code".equals(type)) { // Which list to use?
                            missingCC.put(asciiTld, unicodeTld + " " + comment);
                            if (generateUnicodeTlds) {
                                missingCC.put(unicodeTld, asciiTld + " " + comment);
                            }
                        } else {
                            missingTLD.put(asciiTld, unicodeTld + " " + comment);
                            if (generateUnicodeTlds) {
                                missingTLD.put(unicodeTld, asciiTld + " " + comment);
                            }
                        }
                    } else {
                        System.err.println("Expected to find HTML info for " + asciiTld);
                    }
                }
                ianaTlds.add(asciiTld);
                if (generateUnicodeTlds) {
                    if (!unicodeTld.equals(asciiTld)) {
                        ianaTlds.add(unicodeTld);
                    }
                }
            }
        }
        br.close();
        for (String key : (new TreeMap<String, String[]>(htmlInfo)).keySet()) {
            if (!ianaTlds.contains(key)) {
                if (isNotInRootZone(key)) {
                    System.out.println("INFO: HTML entry not yet in root zone: " + key);
                } else {
                    System.err.println("WARN: Expected to find text entry for html: " + key);
                }
            }
        }
        if (!missingTLD.isEmpty()) {
            printMap(header, missingTLD, "TLD");
        }
        if (!missingCC.isEmpty()) {
            printMap(header, missingCC, "CC");
        }
        isInIanaList0("INFRASTRUCTURE_TLDS", ianaTlds);
        isInIanaList0("COUNTRY_CODE_TLDS", ianaTlds);
        isInIanaList0("GENERIC_TLDS", ianaTlds);
        System.out.println("Finished checks");
    }

    private static void printMap(final String header, Map<String, String> map, String string) {
        System.out.println("Entries missing from " + string + " List\n");
        if (header != null) {
            System.out.println("        // Taken from " + header);
        }
        Iterator<Map.Entry<String, String>> it = map.entrySet().iterator();
        while (it.hasNext()) {
            Map.Entry<String, String> me = it.next();
            System.out.println("        \"" + me.getKey() + "\", // " + me.getValue());
        }
        System.out.println("\nDone");
    }

    private static Map<String, String[]> getHtmlInfo(final File f) throws IOException {
        final Map<String, String[]> info = new HashMap<String, String[]>();

        final Pattern domain = Pattern.compile(".*<a href=\"/domains/root/db/([^.]+)\\.html");
        final Pattern type = Pattern.compile("\\s+<td>([^<]+)</td>");
        final Pattern comment = Pattern.compile("\\s+<td>([^<]+)</td>");

        final BufferedReader br = new BufferedReader(new FileReader(f));
        String line;
        while ((line = br.readLine()) != null) {
            Matcher m = domain.matcher(line);
            if (m.lookingAt()) {
                String dom = m.group(1);
                String typ = "??";
                String com = "??";
                line = br.readLine();
                while (line.matches("^\\s*$")) { // extra blank lines introduced
                    line = br.readLine();
                }
                Matcher t = type.matcher(line);
                if (t.lookingAt()) {
                    typ = t.group(1);
                    line = br.readLine();
                    if (line.matches("\\s+<!--.*")) {
                        while (!line.matches(".*-->.*")) {
                            line = br.readLine();
                        }
                        line = br.readLine();
                    }
                    while (!line.matches(".*</td>.*")) {
                        line += " " + br.readLine();
                    }
                    Matcher n = comment.matcher(line);
                    if (n.lookingAt()) {
                        com = n.group(1);
                    }
                    if (com.contains("Not assigned")
                            || com.contains("Retired")
                            || typ.equals("test")) {
                    } else {
                        info.put(dom.toLowerCase(Locale.ENGLISH), new String[] {typ, com});
                    }
                } else {
                    System.err.println("Unexpected type: " + line);
                }
            }
        }
        br.close();
        return info;
    }

    /*
     * Download a file if it is more recent than our cached copy.
     * Unfortunately the server does not seem to honour If-Modified-Since for the
     * Html page, so we check if it is newer than the txt file and skip download if so
     */
    private static long download(File f, String tldurl, long timestamp) throws IOException {
        final int HOUR = 60 * 60 * 1000; // an hour in ms
        final long modTime;
        if (f.canRead()) {
            modTime = f.lastModified();
            if (modTime > System.currentTimeMillis() - HOUR) {
                System.out.println("Skipping download - found recent " + f);
                return modTime;
            }
        } else {
            modTime = 0;
        }
        HttpURLConnection hc = (HttpURLConnection) new URL(tldurl).openConnection();
        if (modTime > 0) {
            SimpleDateFormat sdf =
                    new SimpleDateFormat(
                            "EEE, dd MMM yyyy HH:mm:ss z"); // Sun, 06 Nov 1994 08:49:37 GMT
            String since = sdf.format(new Date(modTime));
            hc.addRequestProperty("If-Modified-Since", since);
            System.out.println("Found " + f + " with date " + since);
        }
        if (hc.getResponseCode() == 304) {
            System.out.println("Already have most recent " + tldurl);
        } else {
            System.out.println("Downloading " + tldurl);
            byte buff[] = new byte[1024];
            InputStream is = hc.getInputStream();

            FileOutputStream fos = new FileOutputStream(f);
            int len;
            while ((len = is.read(buff)) != -1) {
                fos.write(buff, 0, len);
            }
            fos.close();
            is.close();
            System.out.println("Done");
        }
        return f.lastModified();
    }

    /**
     * Check whether the domain is in the root zone currently. Reads the URL
     * http://www.iana.org/domains/root/db/*domain*.html (using a local disk cache) and checks for
     * the string "This domain is not present in the root zone at this time."
     *
     * @param domain the domain to check
     * @return true if the string is found
     */
    private static boolean isNotInRootZone(String domain) {
        String tldurl = "http://www.iana.org/domains/root/db/" + domain + ".html";
        File rootCheck = new File("target", "tld_" + domain + ".html");
        BufferedReader in = null;
        try {
            download(rootCheck, tldurl, 0L);
            in = new BufferedReader(new FileReader(rootCheck));
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                if (inputLine.contains(
                        "This domain is not present in the root zone at this time.")) {
                    return true;
                }
            }
            in.close();
        } catch (IOException e) {
        } finally {
            closeQuietly(in);
        }
        return false;
    }

    private static void closeQuietly(Closeable in) {
        if (in != null) {
            try {
                in.close();
            } catch (IOException e) {
            }
        }
    }

    private static boolean isInIanaList0(String arrayName, Set<String> ianaTlds) throws Exception {
        Field f = DomainValidator.class.getDeclaredField(arrayName);
        final boolean isPrivate = Modifier.isPrivate(f.getModifiers());
        if (isPrivate) {
            f.setAccessible(true);
        }
        String[] array = (String[]) f.get(null);
        try {
            return isInIanaList1(arrayName, array, ianaTlds);
        } finally {
            if (isPrivate) {
                f.setAccessible(false);
            }
        }
    }

    private static boolean isInIanaList1(String name, String[] array, Set<String> ianaTlds) {
        for (int i = 0; i < array.length; i++) {
            if (!ianaTlds.contains(array[i])) {
                System.out.println(name + " contains unexpected value: " + array[i]);
            }
        }
        return true;
    }

    private static boolean isSortedLowerCase0(String arrayName) throws Exception {
        Field f = DomainValidator.class.getDeclaredField(arrayName);
        final boolean isPrivate = Modifier.isPrivate(f.getModifiers());
        if (isPrivate) {
            f.setAccessible(true);
        }
        String[] array = (String[]) f.get(null);
        try {
            return isSortedLowerCase1(arrayName, array);
        } finally {
            if (isPrivate) {
                f.setAccessible(false);
            }
        }
    }

    private static boolean isLowerCase(String string) {
        return string.equals(string.toLowerCase(Locale.ENGLISH));
    }

    private static boolean isSortedLowerCase1(String name, String[] array) {
        boolean sorted = true;
        boolean strictlySorted = true;
        final int length = array.length;
        boolean lowerCase = isLowerCase(array[length - 1]); // Check the last entry
        for (int i = 0; i < length - 1; i++) { // compare all but last entry with next
            final String entry = array[i];
            final String nextEntry = array[i + 1];
            final int cmp = entry.compareTo(nextEntry);
            if (cmp > 0) { // out of order
                System.out.println(
                        "Out of order entry: " + entry + " < " + nextEntry + " in " + name);
                sorted = false;
            } else if (cmp == 0) {
                strictlySorted = false;
                System.out.println("Duplicated entry: " + entry + " in " + name);
            }
            if (!isLowerCase(entry)) {
                System.out.println("Non lowerCase entry: " + entry + " in " + name);
                lowerCase = false;
            }
        }
        return sorted && strictlySorted && lowerCase;
    }

    @Test
    public void testValidDomains_test0_decomposed()  {
        assertTrue("apache.org should validate", validator.isValid("apache.org"));
        assertTrue("www.google.com should validate", validator.isValid("www.google.com"));
        assertTrue("test-domain.com should validate", validator.isValid("test-domain.com"));
        assertTrue("test---domain.com should validate", validator.isValid("test---domain.com"));
        assertTrue("test-d-o-m-ain.com should validate", validator.isValid("test-d-o-m-ain.com"));
        assertTrue("two-letter domain label should validate", validator.isValid("as.uk"));
        assertTrue("case-insensitive ApAchE.Org should validate", validator.isValid("ApAchE.Org"));
        assertTrue("single-character domain label should validate", validator.isValid("z.com"));
        assertTrue(
                "i.have.an-example.domain.name should validate",
                validator.isValid("i.have.an-example.domain.name"));
    }

    @Test
    public void testInvalidDomains_test0_decomposed()  {
        assertFalse("bare TLD .org shouldn't validate", validator.isValid(".org"));
        assertFalse(
                "domain name with spaces shouldn't validate", validator.isValid(" apache.org "));
        assertFalse(
                "domain name containing spaces shouldn't validate",
                validator.isValid("apa che.org"));
        assertFalse(
                "domain name starting with dash shouldn't validate",
                validator.isValid("-testdomain.name"));
        assertFalse(
                "domain name ending with dash shouldn't validate",
                validator.isValid("testdomain-.name"));
        assertFalse(
                "domain name starting with multiple dashes shouldn't validate",
                validator.isValid("---c.com"));
        assertFalse(
                "domain name ending with multiple dashes shouldn't validate",
                validator.isValid("c--.com"));
        assertFalse(
                "domain name with invalid TLD shouldn't validate", validator.isValid("apache.rog"));
        assertFalse("URL shouldn't validate", validator.isValid("http://www.apache.org"));
        assertFalse("Empty string shouldn't validate as domain name", validator.isValid(" "));
        assertFalse("Null shouldn't validate as domain name", validator.isValid(null));
    }

    @Test
    public void testTopLevelDomains_test0_decomposed()  {
        assertTrue(".arpa should validate as iTLD", validator.isValidInfrastructureTld(".arpa"));
        assertFalse(".com shouldn't validate as iTLD", validator.isValidInfrastructureTld(".com"));
    }

    @Test
    public void testTopLevelDomains_test1_decomposed()  {
        assertTrue(".arpa should validate as iTLD", validator.isValidInfrastructureTld(".arpa"));
        assertFalse(".com shouldn't validate as iTLD", validator.isValidInfrastructureTld(".com"));
        assertTrue(".name should validate as gTLD", validator.isValidGenericTld(".name"));
        assertFalse(".us shouldn't validate as gTLD", validator.isValidGenericTld(".us"));
    }

    @Test
    public void testTopLevelDomains_test2_decomposed()  {
        assertTrue(".arpa should validate as iTLD", validator.isValidInfrastructureTld(".arpa"));
        assertFalse(".com shouldn't validate as iTLD", validator.isValidInfrastructureTld(".com"));
        assertTrue(".name should validate as gTLD", validator.isValidGenericTld(".name"));
        assertFalse(".us shouldn't validate as gTLD", validator.isValidGenericTld(".us"));
        assertTrue(".uk should validate as ccTLD", validator.isValidCountryCodeTld(".uk"));
        assertFalse(".org shouldn't validate as ccTLD", validator.isValidCountryCodeTld(".org"));
    }

    @Test
    public void testTopLevelDomains_test3_decomposed()  {
        assertTrue(".arpa should validate as iTLD", validator.isValidInfrastructureTld(".arpa"));
        assertFalse(".com shouldn't validate as iTLD", validator.isValidInfrastructureTld(".com"));
        assertTrue(".name should validate as gTLD", validator.isValidGenericTld(".name"));
        assertFalse(".us shouldn't validate as gTLD", validator.isValidGenericTld(".us"));
        assertTrue(".uk should validate as ccTLD", validator.isValidCountryCodeTld(".uk"));
        assertFalse(".org shouldn't validate as ccTLD", validator.isValidCountryCodeTld(".org"));
        assertTrue(".COM should validate as TLD", validator.isValidTld(".COM"));
        assertTrue(".BiZ should validate as TLD", validator.isValidTld(".BiZ"));
    }

    @Test
    public void testTopLevelDomains_test4_decomposed()  {
        assertTrue(".arpa should validate as iTLD", validator.isValidInfrastructureTld(".arpa"));
        assertFalse(".com shouldn't validate as iTLD", validator.isValidInfrastructureTld(".com"));
        assertTrue(".name should validate as gTLD", validator.isValidGenericTld(".name"));
        assertFalse(".us shouldn't validate as gTLD", validator.isValidGenericTld(".us"));
        assertTrue(".uk should validate as ccTLD", validator.isValidCountryCodeTld(".uk"));
        assertFalse(".org shouldn't validate as ccTLD", validator.isValidCountryCodeTld(".org"));
        assertTrue(".COM should validate as TLD", validator.isValidTld(".COM"));
        assertTrue(".BiZ should validate as TLD", validator.isValidTld(".BiZ"));
        assertFalse(
                "invalid TLD shouldn't validate",
                validator.isValid(".nope"));
        assertFalse("empty string shouldn't validate as TLD", validator.isValid(""));
        assertFalse("null shouldn't validate as TLD", validator.isValid(null));
    }

    @Test
    public void testAllowLocal_test0_decomposed()  {
        DomainValidator noLocal = DomainValidator.getInstance1(false);
        DomainValidator allowLocal = DomainValidator.getInstance1(true);
    }

    @Test
    public void testAllowLocal_test1_decomposed()  {
        DomainValidator noLocal = DomainValidator.getInstance1(false);
        DomainValidator allowLocal = DomainValidator.getInstance1(true);
        assertEquals(noLocal, validator);
        assertFalse(
                "localhost.localdomain should validate", noLocal.isValid("localhost.localdomain"));
    }

    @Test
    public void testAllowLocal_test2_decomposed()  {
        DomainValidator noLocal = DomainValidator.getInstance1(false);
        DomainValidator allowLocal = DomainValidator.getInstance1(true);
        assertEquals(noLocal, validator);
        assertFalse(
                "localhost.localdomain should validate", noLocal.isValid("localhost.localdomain"));
        assertFalse("localhost should validate", noLocal.isValid("localhost"));
        assertTrue(
                "localhost.localdomain should validate",
                allowLocal.isValid("localhost.localdomain"));
        assertTrue("localhost should validate", allowLocal.isValid("localhost"));
        assertTrue("hostname should validate", allowLocal.isValid("hostname"));
        assertTrue("machinename should validate", allowLocal.isValid("machinename"));
        assertTrue("apache.org should validate", allowLocal.isValid("apache.org"));
        assertFalse(
                "domain name with spaces shouldn't validate", allowLocal.isValid(" apache.org "));
    }

    @Test
    public void testIDN_test0_decomposed()  {
        assertTrue(
                "b\u00fccher.ch in IDN should validate", validator.isValid("www.xn--bcher-kva.ch"));
    }

    @Test
    public void testIDNJava6OrLater_test0_decomposed()  {
        String version = System.getProperty("java.version");
    }

    @Test
    public void testIDNJava6OrLater_test1_decomposed()  {
        String version = System.getProperty("java.version");
        if (version.compareTo("1.6") < 0) {
            System.out.println("Cannot run Unicode IDN tests");
            return; // Cannot run the test
        }
        assertTrue("b\u00fccher.ch should validate", validator.isValid("www.b\u00fccher.ch"));
    }

    @Test
    public void testIDNJava6OrLater_test2_decomposed()  {
        String version = System.getProperty("java.version");
        if (version.compareTo("1.6") < 0) {
            System.out.println("Cannot run Unicode IDN tests");
            return; // Cannot run the test
        }
        assertTrue("b\u00fccher.ch should validate", validator.isValid("www.b\u00fccher.ch"));
        assertTrue(
                "xn--d1abbgf6aiiy.xn--p1ai should validate",
                validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"));
        assertTrue("президент.рф should validate", validator.isValid("президент.рф"));
        assertFalse("www.\uFFFD.ch FFFD should fail", validator.isValid("www.\uFFFD.ch"));
    }

    @Test
    public void testRFC2396domainlabel_test0_decomposed()  {
        assertTrue("a.ch should validate", validator.isValid("a.ch"));
        assertTrue("9.ch should validate", validator.isValid("9.ch"));
        assertTrue("az.ch should validate", validator.isValid("az.ch"));
        assertTrue("09.ch should validate", validator.isValid("09.ch"));
        assertTrue("9-1.ch should validate", validator.isValid("9-1.ch"));
        assertFalse("91-.ch should not validate", validator.isValid("91-.ch"));
        assertFalse("-.ch should not validate", validator.isValid("-.ch"));
    }

    @Test
    public void testRFC2396toplabel_test0_decomposed()  {
        assertTrue("a.c (alpha) should validate", validator.isValidDomainSyntax("a.c"));
        assertTrue("a.cc (alpha alpha) should validate", validator.isValidDomainSyntax("a.cc"));
        assertTrue("a.c9 (alpha alphanum) should validate", validator.isValidDomainSyntax("a.c9"));
        assertTrue(
                "a.c-9 (alpha - alphanum) should validate", validator.isValidDomainSyntax("a.c-9"));
        assertTrue("a.c-z (alpha - alpha) should validate", validator.isValidDomainSyntax("a.c-z"));
        assertFalse("a.9c (alphanum alpha) should fail", validator.isValidDomainSyntax("a.9c"));
        assertFalse("a.c- (alpha -) should fail", validator.isValidDomainSyntax("a.c-"));
        assertFalse("a.- (-) should fail", validator.isValidDomainSyntax("a.-"));
        assertFalse("a.-9 (- alphanum) should fail", validator.isValidDomainSyntax("a.-9"));
    }

    @Test
    public void testDomainNoDots_test0_decomposed()  {
        assertTrue("a (alpha) should validate", validator.isValidDomainSyntax("a"));
        assertTrue("9 (alphanum) should validate", validator.isValidDomainSyntax("9"));
        assertTrue("c-z (alpha - alpha) should validate", validator.isValidDomainSyntax("c-z"));
        assertFalse("c- (alpha -) should fail", validator.isValidDomainSyntax("c-"));
        assertFalse("-c (- alpha) should fail", validator.isValidDomainSyntax("-c"));
        assertFalse("- (-) should fail", validator.isValidDomainSyntax("-"));
    }

    @Test
    public void testValidator297_test0_decomposed()  {
        assertTrue(
                "xn--d1abbgf6aiiy.xn--p1ai should validate",
                validator.isValid("xn--d1abbgf6aiiy.xn--p1ai"));
    }

    @Test
    public void testValidator306_test0_decomposed()  {
        final String longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A";
        assertEquals(63, longString.length());
    }

    @Test
    public void testValidator306_test1_decomposed()  {
        final String longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A";
        assertEquals(63, longString.length());
        assertTrue(
                "63 chars label should validate",
                validator.isValidDomainSyntax(longString + ".com"));
        assertFalse(
                "64 chars label should fail", validator.isValidDomainSyntax(longString + "x.com"));
        assertTrue(
                "63 chars TLD should validate",
                validator.isValidDomainSyntax("test." + longString));
        assertFalse(
                "64 chars TLD should fail", validator.isValidDomainSyntax("test.x" + longString));
    }

    @Test
    public void testValidator306_test2_decomposed()  {
        final String longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A";
        assertEquals(63, longString.length());
        assertTrue(
                "63 chars label should validate",
                validator.isValidDomainSyntax(longString + ".com"));
        assertFalse(
                "64 chars label should fail", validator.isValidDomainSyntax(longString + "x.com"));
        assertTrue(
                "63 chars TLD should validate",
                validator.isValidDomainSyntax("test." + longString));
        assertFalse(
                "64 chars TLD should fail", validator.isValidDomainSyntax("test.x" + longString));
        final String longDomain =
                longString
                        + "."
                        + longString
                        + "."
                        + longString
                        + "."
                        + longString.substring(0, 61);
        assertEquals(253, longDomain.length());
    }

    @Test
    public void testValidator306_test3_decomposed()  {
        final String longString = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz0123456789A";
        assertEquals(63, longString.length());
        assertTrue(
                "63 chars label should validate",
                validator.isValidDomainSyntax(longString + ".com"));
        assertFalse(
                "64 chars label should fail", validator.isValidDomainSyntax(longString + "x.com"));
        assertTrue(
                "63 chars TLD should validate",
                validator.isValidDomainSyntax("test." + longString));
        assertFalse(
                "64 chars TLD should fail", validator.isValidDomainSyntax("test.x" + longString));
        final String longDomain =
                longString
                        + "."
                        + longString
                        + "."
                        + longString
                        + "."
                        + longString.substring(0, 61);
        assertEquals(253, longDomain.length());
        assertTrue("253 chars domain should validate", validator.isValidDomainSyntax(longDomain));
        assertFalse(
                "254 chars domain should fail", validator.isValidDomainSyntax(longDomain + "x"));
    }

    @Test
    public void testUnicodeToASCII_test0_decomposed()  {
        String[] asciidots = {
            "", ",", ".", // fails IDN.toASCII, but should pass wrapped version
            "a.", // ditto
            "a.b", "a..b", "a...b", ".a", "..a",
        };
        for (String s : asciidots) {
            assertEquals(s, DomainValidator.unicodeToASCII(s));
        }
    }

    @Test
    public void testUnicodeToASCII_test1_decomposed()  {
        String[] asciidots = {
            "", ",", ".", // fails IDN.toASCII, but should pass wrapped version
            "a.", // ditto
            "a.b", "a..b", "a...b", ".a", "..a",
        };
        for (String s : asciidots) {
            assertEquals(s, DomainValidator.unicodeToASCII(s));
        }
        final String otherDots[][] = {
            {
                "b\u3002", "b.",
            },
            {
                "b\uFF0E", "b.",
            },
            {
                "b\uFF61", "b.",
            },
            {
                "\u3002", ".",
            },
            {
                "\uFF0E", ".",
            },
            {
                "\uFF61", ".",
            },
        };
        for (String s[] : otherDots) {
            assertEquals(s[1], DomainValidator.unicodeToASCII(s[0]));
        }
    }

    @Test
    public void testIsIDNtoASCIIBroken_test0_decomposed()  {
        System.out.println(">>DomainValidatorTest.testIsIDNtoASCIIBroken()");
        final String input = ".";
        final boolean ok = input.equals(IDN.toASCII(input));
    }

    @Test
    public void testIsIDNtoASCIIBroken_test1_decomposed()  {
        System.out.println(">>DomainValidatorTest.testIsIDNtoASCIIBroken()");
        final String input = ".";
        final boolean ok = input.equals(IDN.toASCII(input));
        System.out.println("IDN.toASCII is " + (ok ? "OK" : "BROKEN"));
        String props[] = {
            "java.version", //    Java Runtime Environment version
            "java.vendor", // Java Runtime Environment vendor
            "java.vm.specification.version", //   Java Virtual Machine specification version
            "java.vm.specification.vendor", //    Java Virtual Machine specification vendor
            "java.vm.specification.name", //  Java Virtual Machine specification name
            "java.vm.version", // Java Virtual Machine implementation version
            "java.vm.vendor", //  Java Virtual Machine implementation vendor
            "java.vm.name", //    Java Virtual Machine implementation name
            "java.specification.version", //  Java Runtime Environment specification version
            "java.specification.vendor", //   Java Runtime Environment specification vendor
            "java.specification.name", // Java Runtime Environment specification name
            "java.class.version", //  Java class format version number
        };
        for (String t : props) {
            System.out.println(t + "=" + System.getProperty(t));
        }
    }

    @Test
    public void testIsIDNtoASCIIBroken_test2_decomposed()  {
        System.out.println(">>DomainValidatorTest.testIsIDNtoASCIIBroken()");
        final String input = ".";
        final boolean ok = input.equals(IDN.toASCII(input));
        System.out.println("IDN.toASCII is " + (ok ? "OK" : "BROKEN"));
        String props[] = {
            "java.version", //    Java Runtime Environment version
            "java.vendor", // Java Runtime Environment vendor
            "java.vm.specification.version", //   Java Virtual Machine specification version
            "java.vm.specification.vendor", //    Java Virtual Machine specification vendor
            "java.vm.specification.name", //  Java Virtual Machine specification name
            "java.vm.version", // Java Virtual Machine implementation version
            "java.vm.vendor", //  Java Virtual Machine implementation vendor
            "java.vm.name", //    Java Virtual Machine implementation name
            "java.specification.version", //  Java Runtime Environment specification version
            "java.specification.vendor", //   Java Runtime Environment specification vendor
            "java.specification.name", // Java Runtime Environment specification name
            "java.class.version", //  Java class format version number
        };
        for (String t : props) {
            System.out.println(t + "=" + System.getProperty(t));
        }
        System.out.println("<<DomainValidatorTest.testIsIDNtoASCIIBroken()");
        assertTrue(true);
    }

    @Test
    public void test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test0_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("INFRASTRUCTURE_TLDS");
    }

    @Test
    public void test_INFRASTRUCTURE_TLDS_sortedAndLowerCase_test1_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("INFRASTRUCTURE_TLDS");
        assertTrue(sorted);
    }

    @Test
    public void test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test0_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("COUNTRY_CODE_TLDS");
    }

    @Test
    public void test_COUNTRY_CODE_TLDS_sortedAndLowerCase_test1_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("COUNTRY_CODE_TLDS");
        assertTrue(sorted);
    }

    @Test
    public void test_GENERIC_TLDS_sortedAndLowerCase_test0_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("GENERIC_TLDS");
    }

    @Test
    public void test_GENERIC_TLDS_sortedAndLowerCase_test1_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("GENERIC_TLDS");
        assertTrue(sorted);
    }

    @Test
    public void test_LOCAL_TLDS_sortedAndLowerCase_test0_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("LOCAL_TLDS");
    }

    @Test
    public void test_LOCAL_TLDS_sortedAndLowerCase_test1_decomposed() throws Exception {
        final boolean sorted = isSortedLowerCase0("LOCAL_TLDS");
        assertTrue(sorted);
    }

    @Test
    public void testEnumIsPublic_test0_decomposed()  {
        assertTrue(Modifier.isPublic(DomainValidator.ArrayType.class.getModifiers()));
    }

    @Test
    public void testGetArray_test0_decomposed()  {
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_MINUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_PLUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.GENERIC_MINUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.GENERIC_PLUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.LOCAL_MINUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.LOCAL_PLUS));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.COUNTRY_CODE_RO));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.GENERIC_RO));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.INFRASTRUCTURE_RO));
        assertNotNull(DomainValidator.getTLDEntries(ArrayType.LOCAL_RO));
    }
}