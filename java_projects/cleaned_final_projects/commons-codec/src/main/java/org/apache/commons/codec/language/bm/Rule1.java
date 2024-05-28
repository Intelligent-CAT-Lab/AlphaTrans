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

package org.apache.commons.codec.language.bm;

public class Rule1 extends Rule {
    private final String pat;
    private final String lCon;
    private final String rCon;
    private final PhonemeExpr ph;
    private final int myLine;
    private final String loc;

    public Rule1(String pat, String lCon, String rCon, PhonemeExpr ph, int cLine, String location) {
        super(pat, lCon, rCon, ph);
        this.pat = pat;
        this.lCon = lCon;
        this.rCon = rCon;
        this.ph = ph;
        this.myLine = cLine;
        this.loc = location;
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder();
        sb.append("Rule");
        sb.append("{line=").append(myLine);
        sb.append(", loc='").append(loc).append('\'');
        sb.append(", pat='").append(pat).append('\'');
        sb.append(", lcon='").append(lCon).append('\'');
        sb.append(", rcon='").append(rCon).append('\'');
        sb.append('}');
        return sb.toString();
    }
}
